#!/usr/bin/env node
/**
 * Atlas Phase 2 v0.2: structural checks only. No assertion of semantic truth.
 * Usage: node scripts/validate-language-v02.mjs [fixture.json|- (stdin)] [dictionary.json]
 */
import { readFileSync } from 'node:fs';
import { dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const here = dirname(fileURLToPath(import.meta.url));
const fixtureFile = process.argv[2] === '-' ? null : process.argv[2] ? resolve(process.argv[2]) : resolve(here, '../examples/language-v02-pilot.json');
const dictionaryFile = process.argv[3] ? resolve(process.argv[3]) : resolve(here, '../TAG_DICTIONARY_v0.1.json');
const corpus = JSON.parse(readFileSync(fixtureFile ?? 0, 'utf8'));
const dictionary = JSON.parse(readFileSync(dictionaryFile, 'utf8'));
const errors = [];
const assert = (ok, msg) => { if (!ok) errors.push(msg); };

function identifiers(records, kind) {
  const all = new Set();
  for (const r of records || []) {
    assert(typeof r.id === 'string' && r.id.length > 0, `${kind} sin ID`);
    assert(!all.has(r.id), `${kind} ID repetido: ${r.id}`);
    all.add(r.id);
  }
  return all;
}

function checkType(value, type) {
  if (type === 'array' || type.startsWith('array:')) return Array.isArray(value);
  if (type === 'object') return value !== null && typeof value === 'object' && !Array.isArray(value);
  if (type === 'number') return typeof value === 'number' && Number.isFinite(value);
  if (type === 'boolean') return typeof value === 'boolean';
  if (type.startsWith('enum:')) return typeof value === 'string';
  return typeof value === type;
}

const tagKeys = new Set();
const tagMap = new Map();
for (const t of dictionary.etiquetas || []) {
  assert(typeof t.key === 'string' && /^[a-z]+:[a-z_]+$/.test(t.key), `Clave de etiqueta inválida: ${t.key}`);
  assert(!tagKeys.has(t.key), `Etiqueta repetida ${t.key}`);
  tagKeys.add(t.key); tagMap.set(t.key, t);
  assert(t.translations?.es && t.translations?.en, `Traducción incompleta: ${t.key}`);
  assert(t.definition && Array.isArray(t.applies_to) && t.applies_to.length > 0, `Entrada incompleta: ${t.key}`);
  assert(['reserved_field', 'flexible_tag'].includes(t.kind), `Clase de etiqueta inválida: ${t.key}`);
  assert(t.kind !== 'reserved_field' || t.json_path, `Campo reservado sin ruta: ${t.key}`);
}
assert(dictionary.dictionary_version === corpus.meta?.dictionary_version, 'Versión de diccionario distinta de la del fixture');
assert(dictionary.normalization_policy?.load_first === true, 'Debe cargarse el diccionario primero');
assert(dictionary.normalization_policy?.permit_new_labels === true, 'Las etiquetas no pueden declararse cerradas');
assert(dictionary.normalization_policy?.prefer_reuse === true, 'No consta regla de reutilización');
assert(JSON.stringify(corpus.meta?.classification_order) === JSON.stringify(['ABCD', 'JF']), 'Orden ABCD→JF no declarado');
const ABCD = new Set(['A', 'B', 'C', 'D']);
const JF = new Set(['JF.F1', 'JF.F2', 'JF.F3', 'JF.F4']);
const terminalKinds = new Set(dictionary.controlled_vocabularies?.TERMINAL || []);
assert(terminalKinds.has('D') && terminalKinds.has('CUT_NO_RELEVANCE'), 'Faltan clases de parada diferenciadas');

const itemIDs = identifiers(corpus.items, 'Ítem');
const nodeIDs = identifiers(corpus.nodes, 'Nodo');
const edgeIDs = identifiers(corpus.edges, 'Arista');
const walkIDs = identifiers(corpus.walks, 'Recorrido');
identifiers(corpus.conceptual_clusters, 'Clúster');
const themeIDs = identifiers(corpus.themes, 'Tema');
const edgeMap = new Map((corpus.edges || []).map(e => [e.id, e]));
const proposalKeys = new Set((corpus.proposed_dictionary_changes || []).map(x => x.proposed_key));

function checkItemRefs(refs, context, required = false) {
  assert(Array.isArray(refs), `${context}: item_refs no es una lista`);
  if (required) assert(refs?.length > 0, `${context}: faltan anclas de ítem`);
  for (const r of refs || []) {
    const id = typeof r === 'string' ? r : r?.item_id;
    assert(itemIDs.has(id), `${context}: ítem desconocido ${id}`);
    if (typeof r === 'object') assert(!!r.role, `${context}: vínculo ítem-nodo sin función probatoria`);
  }
}

function checkLabels(obj, kind) {
  assert(Array.isArray(obj.etiquetas), `${kind} ${obj.id}: faltan etiquetas []`);
  for (const e of obj.etiquetas || []) {
    const def = tagMap.get(e.key);
    if (!def) {
      assert(e.key?.startsWith('proposed:') && proposalKeys.has(e.key), `${kind} ${obj.id}: etiqueta inexistente sin propuesta ${e.key}`);
      assert(e.proposal_status === 'local_only' || e.basis, `${kind} ${obj.id}: propuesta sin estado`);
    } else {
      assert(def.kind === 'flexible_tag', `${kind} ${obj.id}: campo reservado duplicado en etiquetas ${e.key}`);
      assert(def.applies_to.includes(kind), `${kind} ${obj.id}: etiqueta ${e.key} fuera de ámbito`);
      assert(def.state !== 'deprecated', `${kind} ${obj.id}: etiqueta deprecada ${e.key}`);
      assert(checkType(e.value, def.value_type), `${kind} ${obj.id}: tipo inválido ${e.key}`);
    }
    assert(typeof e.basis === 'string' && !!e.basis, `${kind} ${obj.id}: etiqueta sin base interpretativa`);
    checkItemRefs(e.item_refs || [], `Etiqueta ${e.key}`);
  }
}

for (const i of corpus.items || []) {
  assert(i.description && i.kind && i.version && i.evidence_status, `Ítem incompleto: ${i.id}`);
  if (i.evidence_status !== 'pending_anchor') {
    assert(typeof i.hook?.uri === 'string' && typeof i.hook?.locator === 'string' && !!(i.hook?.revision || i.hook?.observed_at), `Hook insuficiente: ${i.id}`);
    if (i.hook?.uri === 'examples/language-v02-pilot.json') {
      const pointer = i.hook.locator?.split('/').slice(1) || [];
      let val = corpus;
      for (const segment of pointer) val = val?.[segment];
      assert(val !== undefined, `Hook local no resuelve el JSON Pointer: ${i.id}`);
    }
  }
  checkLabels(i, 'item');
}

for (const n of corpus.nodes || []) {
  assert(n.label && n.description && n.version && n.evidence_status, `Ficha de nodo incompleta: ${n.id}`);
  checkItemRefs(n.item_refs, `Nodo ${n.id}`, true);
  checkLabels(n, 'node');
  assert(!('abcd' in n) && !('jf_roles' in n), `Nodo tiene calificación global: ${n.id}`);
}

for (const e of corpus.edges || []) {
  assert(nodeIDs.has(e.source) && nodeIDs.has(e.target), `Arista sin extremos válidos ${e.id}`);
  assert(e.predicate && e.reason && e.version && e.evidence_status, `Arista sin predicado, justificación o versión: ${e.id}`);
  assert(['directed', 'symmetric', 'inverse_available'].includes(e.semantic_direction), `Arista sin tipo de dirección válido ${e.id}`);
  assert(e.semantic_direction !== 'inverse_available' || e.inverse_predicate, `Arista sin predicado inverso ${e.id}`);
  assert(!('abcd' in e) && !('jf_roles' in e) && !('status' in e), `Arista de nivel 1 no puede tener ABCD/JF global: ${e.id}`);
  checkItemRefs(e.item_refs, `Arista ${e.id}`, true);
  checkLabels(e, 'edge');
}

let walkToD = 0, repeatedC = 0, collateralC = 0;
const qualifications = new Map();
for (const w of corpus.walks || []) {
  const p = w.position;
  assert(p && nodeIDs.has(p.origin) && p.activity && p.question && p.scope && p.capability && p.as_of, `Posicionamiento incompleto ${w.id}`);
  assert(JSON.stringify(w.classification_order) === JSON.stringify(['ABCD', 'JF']), `Recorrido sin orden ABCD→JF ${w.id}`);
  assert(w.dictionary_version === dictionary.dictionary_version, `Recorrido con diccionario distinto ${w.id}`);
  assert(terminalKinds.has(w.terminal_kind), `Terminal desconocido: ${w.id}`);
  assert(Array.isArray(w.steps) && w.steps.length, `Recorrido sin pasos: ${w.id}`);
  let cursor = p.origin;
  const seen = new Set([cursor]);
  let previous;
  for (let j = 0; j < (w.steps || []).length; j++) {
    const s = w.steps[j], edge = edgeMap.get(s.edge_id);
    assert(!!edge, `${w.id}: arista no encontrada ${s.edge_id}`);
    assert(ABCD.has(s.abcd), `${w.id}: ABCD inválido ${s.abcd}`);
    assert(typeof s.abcd_reason === 'string' && s.abcd_reason.length > 10, `${w.id}: falta razón epistemológica`);
    assert(['forward', 'reverse'].includes(s.direction), `${w.id}: dirección de flecha inválida`);
    assert(s.from === cursor, `${w.id}: discontinuidad desde ${cursor} al paso ${j}`);
    assert(nodeIDs.has(s.to), `${w.id}: destino inexistente ${s.to}`);
    assert(!seen.has(s.to), `${w.id}: ciclo sin control en ${s.to}`);
    if (edge) {
      const from = s.direction === 'forward' ? edge.source : edge.target;
      const to = s.direction === 'forward' ? edge.target : edge.source;
      assert(from === s.from && to === s.to, `${w.id}: dirección no corresponde a la arista ${edge.id}`);
      assert(s.direction !== 'reverse' || edge.semantic_direction !== 'directed', `${w.id}: inversión semántica no autorizada en ${edge.id}`);
      const key = `${edge.id}:${p.origin}`;
      const statuses = qualifications.get(key) || new Set();
      statuses.add(s.abcd);
      qualifications.set(key, statuses);
    }
    if (s.abcd === 'D') assert(j === w.steps.length - 1, `${w.id}: continúa después de D`);
    if (previous === 'C' && s.abcd === 'C') repeatedC++;
    if (s.abcd === 'C' && s.jf_roles?.includes('JF.F4')) collateralC++;
    previous = s.abcd;
    assert(['assessed', 'not_assessed', 'not_applicable'].includes(s.jf_applicability), `${w.id}: falta estado JF`);
    assert(Array.isArray(s.jf_roles), `${w.id}: faltan roles JF []`);
    for (const role of s.jf_roles || []) assert(JF.has(role), `${w.id}: factor F de espacio de nombres incorrecto ${role}`);
    assert(s.jf_applicability === 'assessed' || s.jf_roles?.length === 0, `${w.id}: roles declarados sin evaluar JF`);
    if (s.jf_roles?.length) assert(!!s.jf_reason, `${w.id}: factor JF sin razón`);
    checkItemRefs(s.item_refs, `${w.id} paso ${j}`, true);
    seen.add(s.to); cursor = s.to;
  }
  if (w.terminal_kind === 'D') {
    walkToD++;
    assert(w.steps.at(-1).abcd === 'D' && w.complete_to_D === true, `${w.id}: cierre D inconsistente`);
  } else assert(w.steps.at(-1).abcd !== 'D' && w.complete_to_D === false, `${w.id}: cierre parcial inconsistente`);
}

for (const c of corpus.conceptual_clusters || []) {
  checkLabels(c, 'cluster');
  assert(c.description && c.version && c.review_status, `Clúster incompleto ${c.id}`);
  for (const id of c.core_node_ids || []) assert(nodeIDs.has(id), `Clúster ${c.id}: core inexistente ${id}`);
  for (const id of c.position_refs || []) assert(walkIDs.has(id), `Clúster ${c.id}: posición inexistente ${id}`);
  for (const id of c.boundary_walk_refs || []) assert(walkIDs.has(id), `Clúster ${c.id}: frontera inexistente ${id}`);
  checkItemRefs(c.item_refs, `Clúster ${c.id}`, true);
}
// Theme definitions describe only the matter. Node memberships are a separate
// public minimal projection; detailed judge reasons must never be encoded here.
const allowedThemeKeys = new Set(['id', 'title', 'description', 'scope', 'etiquetas', 'version', 'review_status', 'aliases', 'translations']);
for (const t of corpus.themes || []) {
  checkLabels(t, 'theme');
  assert(t.description && t.title && t.version && t.review_status, `Tema incompleto ${t.id}`);
  for (const field of Object.keys(t)) assert(allowedThemeKeys.has(field), `Tema ${t.id}: campo de relaciones/interpretación prohibido ${field}`);
  if ('scope' in t) assert(typeof t.scope === 'string', `Tema ${t.id}: scope semántico inválido`);
}
const projection = corpus.theme_projection;
assert(!!projection && typeof projection === 'object', 'Falta manifiesto independiente de proyección temática');
assert(typeof projection?.version === 'string' && typeof projection?.graph_snapshot === 'string' && typeof projection?.scope === 'string', 'La proyección temática debe declarar versión, grafo de origen y alcance');
assert(Array.isArray(projection?.classified_node_ids), 'La proyección temática debe declarar nodos clasificados');
const classifiedNodeIDs = new Set(projection?.classified_node_ids || []);
assert(classifiedNodeIDs.size === (projection?.classified_node_ids || []).length, 'Nodos clasificados repetidos en proyección temática');
for (const id of classifiedNodeIDs) assert(nodeIDs.has(id), `Proyección temática: nodo clasificado desconocido ${id}`);
const membershipKeys = new Set();
const themeWeightTotals = new Map();
const associationFields = ['node_id', 'theme_id', 'weight'];
for (const a of corpus.theme_assignments || []) {
  assert(Object.keys(a).sort().join(',') === associationFields.slice().sort().join(','), `Asociación nodo–tema pública con campos distintos de node_id, theme_id, weight: ${JSON.stringify(a)}`);
  assert(nodeIDs.has(a.node_id), `Asociación temática: nodo desconocido ${a.node_id}`);
  assert(themeIDs.has(a.theme_id), `Asociación temática: tema desconocido ${a.theme_id}`);
  assert(classifiedNodeIDs.has(a.node_id), `Asociación temática parcial/no declarada del nodo ${a.node_id}`);
  assert(typeof a.weight === 'number' && Number.isFinite(a.weight) && a.weight > 0 && a.weight <= 1, `Asociación temática: peso inválido ${a.node_id}/${a.theme_id}: ${a.weight}`);
  const key = `${a.node_id}\u0000${a.theme_id}`;
  assert(!membershipKeys.has(key), `Asociación temática repetida ${a.node_id}/${a.theme_id}`);
  membershipKeys.add(key);
  if (typeof a.weight === 'number' && Number.isFinite(a.weight)) themeWeightTotals.set(a.node_id, (themeWeightTotals.get(a.node_id) || 0) + a.weight);
}
for (const id of classifiedNodeIDs) {
  const sum = themeWeightTotals.get(id);
  assert(sum !== undefined && Math.abs(sum - 1) <= 1e-9, `Nodo ${id}: la suma de todos los pesos temáticos debe ser exactamente 1 (actual: ${sum ?? 'sin asociaciones'})`);
}
for (const rejected of corpus.rejected_candidates || []) {
  assert(nodeIDs.has(rejected.source) && nodeIDs.has(rejected.target) && rejected.reason, 'Candidato rechazado incompleto');
  assert(!(corpus.edges || []).some(e => (e.source === rejected.source && e.target === rejected.target) || (e.source === rejected.target && e.target === rejected.source)), 'Candidato rechazado figura como arista activa');
}
assert(qualifications.get('E-J02:JFW')?.has('A') && qualifications.get('E-J02:FON')?.has('C'), 'Misma arista E-J02 no demuestra A y C por origen');
assert(walkToD >= 1, 'Falta ruta que alcanza D');
assert(repeatedC >= 1, 'Falta ruta C→C');
assert(collateralC >= 1, 'Falta demostrar que JF.F4 puede ser ABCD.C');

if (errors.length) {
  console.error(`ATLAS v0.2: ${errors.length} error(es) estructurales`);
  for (const error of errors) console.error(`  ✗ ${error}`);
  process.exitCode = 1;
} else {
  console.log('ATLAS v0.2 — validación estructural correcta');
  console.log(`Diccionario ${dictionary.dictionary_version}: ${tagKeys.size} claves (${[...tagMap.values()].filter(t => t.kind === 'flexible_tag').length} flexibles)`);
  console.log(`Ítems ${itemIDs.size}; nodos ${nodeIDs.size}; aristas nivel 1 ${edgeIDs.size}; recorridos nivel 2 ${walkIDs.size}`);
  console.log(`Rutas hasta D ${walkToD}; C→C ${repeatedC}; JF.F4 con C ${collateralC}`);
  console.log(`Proyección temática: ${classifiedNodeIDs.size} nodos clasificados; ${membershipKeys.size} asociaciones; suma de pesos por nodo = 1`);
  console.log('Arista E-J02 = A desde JUBAP, C desde Focus ON sin calificación global de arista.');
  console.log('NOTA: no verifica evidencia histórica, semántica ABCD/JF, calidad de traducciones ni economía de inferencia.');
}
