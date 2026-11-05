#!/usr/bin/env node
/** Structural validation of a non-canonical methodological fixture. This script
 * checks traceability and path mechanics; it cannot prove epistemic truth. */
import {readFileSync} from 'node:fs';
import {fileURLToPath} from 'node:url';
import {resolve, dirname} from 'node:path';

const defaultFile = resolve(dirname(fileURLToPath(import.meta.url)), '../examples/phase2-fixtures.json');
const fixtureFile = process.argv[2] ? resolve(process.argv[2]) : defaultFile;
const fixture = JSON.parse(readFileSync(fixtureFile, 'utf8'));
const ABCD = new Set(['A','B','C','D']);
const terminals = new Set(['D','END_OF_GRAPH','CUT_NO_RELEVANCE','BUDGET','CYCLE','REVIEW_PENDING']);
const errors = [];
function assert(ok, message) {if(!ok) errors.push(message);}
function unique(records, category) {
  const ids=new Set();
  for(const rec of records) {
    assert(typeof rec.id==='string' && rec.id.length>0, `${category}: ID ausente`);
    assert(!ids.has(rec.id), `${category}: ID duplicado ${rec.id}`);
    ids.add(rec.id);
  }
  return ids;
}
const itemIds=unique(fixture.items,'ítems');
const nodeIds=unique(fixture.nodes,'nodos');
const edgeIds=unique(fixture.edges,'relaciones');
unique(fixture.walks,'recorridos');
const edgeMap=new Map(fixture.edges.map(e=>[e.id,e]));

for(const item of fixture.items) {
  assert(item.hook && item.hook.uri && item.hook.locator, `Hook sin URI/localizador: ${item.id}`);
  assert(item.hook && (item.hook.revision || item.hook.observed_at), `Hook sin estado observado: ${item.id}`);
}
for(const node of fixture.nodes) {
  assert(typeof node.description==='string' && node.description.trim().length>0, `Ficha libre ausente: ${node.id}`);
  assert(Array.isArray(node.item_refs) && node.item_refs.length>0, `Nodo sin ítem ancla: ${node.id}`);
  for(const ref of node.item_refs||[]) assert(itemIds.has(ref), `Ítem no encontrado para nodo ${node.id}: ${ref}`);
}
for(const edge of fixture.edges) {
  assert(nodeIds.has(edge.source) && nodeIds.has(edge.target), `Arista sin nodos válidos: ${edge.id}`);
  assert(typeof edge.predicate==='string' && !!edge.reason, `Relación sin predicado/razón: ${edge.id}`);
  assert(!('status' in edge) && !('abcd' in edge), `A/B/C/D no puede ser global en arista: ${edge.id}`);
  for(const ref of edge.item_refs||[]) assert(itemIds.has(ref), `Ítem ausente en arista ${edge.id}: ${ref}`);
}
const gradesByPosition=new Map();
let complete=0, incomplete=0, consecutiveC=0;
let A_reach=new Map();
for(const walk of fixture.walks) {
  const p=walk.position;
  assert(p && nodeIds.has(p.origin) && p.question && p.activity && p.scope && p.capability, `Posición incompleta: ${walk.id}`);
  assert(terminals.has(walk.terminal_kind), `Terminal inválido: ${walk.id}`);
  assert(Array.isArray(walk.steps) && walk.steps.length>0, `Recorrido sin pasos: ${walk.id}`);
  let cursor=p.origin, previous=null;
  const seen=new Set([cursor]);
  const reachedA = A_reach.get(p.origin)||new Set();
  let prefixAllA=true;
  for(let i=0;i<(walk.steps||[]).length;i++) {
    const s=walk.steps[i], e=edgeMap.get(s.edge);
    assert(!!e, `${walk.id}: arista desconocida ${s.edge}`);
    assert(ABCD.has(s.status), `${walk.id}: calificación inválida ${s.status}`);
    assert(s.dir===1||s.dir===-1, `${walk.id}: dirección inválida`);
    assert(!!s.reason, `${walk.id}: razón de calificación ausente`);
    if(!e) continue;
    const from=s.dir===-1?e.target:e.source;
    const to=s.dir===-1?e.source:e.target;
    assert(from===cursor, `${walk.id}: salto discontinuo ${cursor}→${from} en ${s.edge}`);
    assert(!seen.has(to), `${walk.id}: nodo repetido / ciclo en ${to}`);
    seen.add(to);cursor=to;
    if(s.status==='D') assert(i===walk.steps.length-1, `${walk.id}: recorrido continúa después de D`);
    if(s.status==='C' && previous==='C') consecutiveC++;
    previous=s.status;
    prefixAllA=prefixAllA && s.status==='A';
    if(prefixAllA) reachedA.add(to);
    const byEdge=gradesByPosition.get(s.edge)||new Map();
    const statuses=byEdge.get(p.origin)||new Set();
    statuses.add(s.status);byEdge.set(p.origin,statuses);gradesByPosition.set(s.edge,byEdge);
  }
  A_reach.set(p.origin,reachedA);
  const last=walk.steps[walk.steps.length-1];
  if(walk.terminal_kind==='D') {
    complete++;
    assert(last?.status==='D', `${walk.id}: declara D terminal pero no acaba en D`);
  } else {
    incomplete++;
    assert(last?.status!=='D', `${walk.id}: terminó en D pero se declaró ${walk.terminal_kind}`);
  }
}
for(const bad of fixture.rejected_candidates||[]) {
  assert(nodeIds.has(bad.source) && nodeIds.has(bad.target), 'Candidato rechazado sin nodos');
  assert(!fixture.edges.some(e=>(e.source===bad.source&&e.target===bad.target)||(e.source===bad.target&&e.target===bad.source)),
    `Candidato rechazado conserva arista: ${bad.source}-${bad.target}`);
}
const themeIds=unique(fixture.themes||[], 'temas');
const primaries=new Map();
for(const theme of fixture.themes||[]) {
  assert(typeof theme.description==='string' && theme.description.length>0, `Ficha temática sin descripción: ${theme.id}`);
  for(const id of theme.primary_nodes||[]) {
    assert(nodeIds.has(id), `${theme.id}: nodo primario inexistente ${id}`);
    primaries.set(id,(primaries.get(id)||0)+1);
  }
  for(const id of theme.secondary_nodes||[]) assert(nodeIds.has(id), `${theme.id}: nodo secundario inexistente ${id}`);
}
for(const id of nodeIds) assert(primaries.get(id)===1, `Nodo sin tema primario único (peso 1): ${id}`);
for(const cluster of fixture.conceptual_clusters||[]) {
  assert(nodeIds.has(cluster.core) && nodeIds.has(cluster.position_origin), `Clúster inválido ${cluster.id}`);
}

assert(consecutiveC>=1, 'Falta un ejemplo C→C');
const edgeJFW = gradesByPosition.get('E-J02');
assert(edgeJFW?.get('JFW')?.has('A') && edgeJFW?.get('FON')?.has('C'), 'No se verifica E-J02: A desde JUBAP, C desde Focus ON');
assert(complete>=2, 'Faltan recorridos completos hasta D');
assert(incomplete>=1, 'Falta demostrar un recorrido parcial no-D');
assert(themeIds.size>0, 'Temas no definidos');

if(errors.length) {
  console.error(`VALIDACIÓN FALLIDA (${errors.length}):`);
  for(const err of errors) console.error(`  ✗ ${err}`);
  process.exitCode=1;
} else {
  console.log('VALIDACIÓN ESTRUCTURAL CORRECTA · Atlas fase 2 (experimental)');
  console.log(`Ítems: ${itemIds.size}; nodos: ${nodeIds.size}; relaciones neutras: ${edgeIds.size}; recorridos: ${fixture.walks.length}`);
  console.log(`Recorridos hasta D: ${complete}; parciales: ${incomplete}; pares C→C: ${consecutiveC}`);
  console.log(`Misma arista E-J02: origen JUBAP = A; origen Focus ON = C`);
  console.log('Alcance A observado por origen (en rutas fixture; no centralidad global):');
  for(const [origin, ids] of A_reach) console.log(`  ${origin}: ${ids.size} nodo(s) [${[...ids].join(', ')}]`);
  console.log('NOTA: se ha validado estructura; la semántica A/B/C/D requiere revisión y evidencia humana.');
}
