#!/usr/bin/env node
/**
 * Atlas Phase 2 — checks a proposed per-agent MSCA cartographic slice.
 * Scope: structural integrity, relative walks, D stopping, source hooks and
 * selective disclosure. NOT a proof of material dependency, completeness,
 * epistemic correctness, authority, consent or MSCA sufficiency.
 * Usage: node scripts/validate-msca-cartographic-slice-v01.mjs
 */
import { readFileSync } from 'node:fs';
import { dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const here = dirname(fileURLToPath(import.meta.url));
const loc = x => resolve(here, '../examples/' + x);
const sample = JSON.parse(readFileSync(process.argv[2] ? resolve(process.argv[2]) : loc('msca-cartographic-slice-v01.json'), 'utf8'));
const atlas = JSON.parse(readFileSync(loc('language-v02-pilot.json'), 'utf8'));
const views = JSON.parse(readFileSync(loc('msca-view-v01.json'), 'utf8'));
const items = new Map(atlas.items.map(x => [x.id, x]));
const nodes = new Map(atlas.nodes.map(x => [x.id, x]));
const edges = new Map(atlas.edges.map(x => [x.id, x]));
const walks = new Map(atlas.walks.map(x => [x.id, x]));
const clusters = new Map(atlas.conceptual_clusters.map(x => [x.id, x]));
const themes = new Map(atlas.themes.map(x => [x.id, x]));
const mscaViews = new Map(views.views.map(x => [x.view_id, x]));
const ABCD = new Set(['A', 'B', 'C', 'D']);
const term = new Set(['D', 'END_OF_GRAPH', 'CUT_NO_RELEVANCE', 'BUDGET', 'CYCLE', 'REVIEW_PENDING']);

function inspect(doc) {
  const errors = [];
  const check = (ok, label) => { if (!ok) errors.push(label); };
  const ids = new Set();
  check(doc.meta?.version === '0.1-experimental', 'Versión del adaptador inválida');
  check(doc.meta?.source_atlas_fixture === 'language-v02-pilot.json', 'No se identifica el Atlas de origen');
  check(doc.meta?.source_msca_fixture === 'msca-view-v01.json', 'No se identifica la vista MSCA de origen');
  check(Array.isArray(doc.slices) && doc.slices.length > 0, 'Faltan láminas');

  for (const x of doc.slices || []) {
    const id = x.slice_id || '<sin-id>';
    check(!ids.has(id) && id !== '<sin-id>', `Lámina sin ID o duplicada: ${id}`);
    ids.add(id);
    check(x.version === doc.meta?.version, `${id}: versión distinta`);
    check(x.producer?.agent_id && x.producer?.as_of, `${id}: falta agente/fecha`);
    check(x.producer?.cart_i_ref === null && x.producer.cart_i_state === 'NOT_INSTANTIATED_IN_CANONICAL_MSCA', `${id}: Cart_i canónico fingido`);
    check(x.focal_context?.activity && x.focal_context?.decision && x.focal_context?.source_limit, `${id}: sin actividad, decisión o límite`);
    const view = mscaViews.get(x.focal_context?.focal_msca_view_ref);
    check(!!view, `${id}: MSCA vista inexistente`);
    check(x.focal_context?.objective_binding_status === view?.objective_binding?.binding_status, `${id}: binding distinto de la vista MSCA`);
    check(!x.focal_context?.objective_envelope_ref && !x.focal_context?.architectural_role_ref, `${id}: titular/rol atribuido sin prueba`);

    const select = x.selection || {};
    for (const [name, map] of [['seed_cluster_refs', clusters], ['position_refs', walks], ['seed_node_refs', nodes]]) {
      check(Array.isArray(select[name]) && select[name].length > 0, `${id}: sin ${name}`);
      for (const ref of select[name] || []) check(map.has(ref), `${id}: ${name} inexistente: ${ref}`);
    }
    check(select.reason && select.theme_percentage_policy === 'NOT_DEFINED_IN_THIS_PHASE', `${id}: tema condicionado por fórmula ficticia`);
    for (const t of select.theme_selection || []) {
      check(themes.has(t.theme_ref) && nodes.has(t.node_ref), `${id}: tema/nodo inexistente`);
      const association = themes.get(t.theme_ref)?.node_associations.find(a => a.node_id === t.node_ref);
      check(association?.weight === t.weight, `${id}: peso no coincide con la ficha temática`);
      check(t.state === 'provisional_not_global_percentage', `${id}: peso confundido con porcentaje global`);
    }

    const internal = x.internal_slice || {};
    const hookRefs = new Set((internal.item_hooks || []).map(h => h.item_ref));
    const nodeRefs = new Set(internal.node_refs || []);
    const edgeRefs = new Set(internal.conceptual_edge_refs || []);
    check(Array.isArray(internal.item_hooks), `${id}: falta lista de hooks`);
    for (const hook of internal.item_hooks || []) {
      const item = items.get(hook.item_ref);
      check(!!item, `${id}: item no existente ${hook.item_ref}`);
      check(hook.uri === item?.hook?.uri && hook.locator === item?.hook?.locator, `${id}: hook modificado ${hook.item_ref}`);
      check(hook.evidence_status === item?.evidence_status, `${id}: evidencia de item mal atribuida ${hook.item_ref}`);
    }
    for (const ref of nodeRefs) check(nodes.has(ref), `${id}: nodo no existente ${ref}`);
    for (const ref of edgeRefs) {
      const edge = edges.get(ref);
      check(!!edge && nodeRefs.has(edge?.source) && nodeRefs.has(edge?.target), `${id}: arista conceptual sin nodos extremos ${ref}`);
    }
    check(Array.isArray(internal.material_dependency_refs) && internal.material_dependency_state === 'NOT_QUALIFIED_BY_THIS_EXAMPLE', `${id}: dependencia material no calificada asumida`);
    check(internal.material_dependency_refs.every(e => !edgeRefs.has(e)), `${id}: dependencia material confundida con arista conceptual`);
    check(internal.objective_envelope_node_refs?.length === 0 && internal.objective_envelope_graph_state === 'NO_OWNER_BOUND_OBJECTIVE_NODE_ESTABLISHED', `${id}: nodo de S implícitamente legitimado`);

    let completeD = 0, partial = 0;
    check(Array.isArray(internal.walks) && internal.walks.length > 0, `${id}: faltan recorridos`);
    for (const w of internal.walks || []) {
      const source = walks.get(w.walk_ref);
      check(!!source && select.position_refs?.includes(w.walk_ref), `${id}: recorrido no seleccionado ${w.walk_ref}`);
      check(w.origin === source?.position?.origin && select.seed_node_refs?.includes(w.origin), `${id}: origen distinto de posición ${w.walk_ref}`);
      check(Array.isArray(w.path) && w.path.length === source?.steps.length, `${id}: camino parcial u omisión sin declaración ${w.walk_ref}`);
      check(term.has(w.terminal_kind) && w.terminal_kind === source?.terminal_kind, `${id}: terminal inválido ${w.walk_ref}`);
      check(w.complete_to_D === source?.complete_to_D, `${id}: cierre D distinto del Atlas ${w.walk_ref}`);
      check(typeof w.boundary_reason === 'string' && w.boundary_reason.length > 30, `${id}: sin razón del límite ${w.walk_ref}`);
      let cursor = w.origin;
      (w.path || []).forEach((step, index) => {
        const prior = source?.steps?.[index], edge = edges.get(step.edge_ref);
        check(ABCD.has(step.abcd), `${id}: ABCD inválido en ${w.walk_ref}:${index}`);
        check(step.edge_ref === prior?.edge_id && step.from === prior?.from && step.to === prior?.to, `${id}: trama distinta de la fuente ${w.walk_ref}:${index}`);
        check(step.abcd === prior?.abcd && JSON.stringify(step.jf_roles) === JSON.stringify(prior?.jf_roles), `${id}: calificación distinta del recorrido ${w.walk_ref}:${index}`);
        check(step.from === cursor && edgeRefs.has(step.edge_ref) && nodeRefs.has(step.to), `${id}: discontinuidad o arista fuera de lámina ${w.walk_ref}:${index}`);
        check(edge?.source === step.from && edge?.target === step.to && step.direction === 'forward', `${id}: dirección semántica incorrecta ${w.walk_ref}:${index}`);
        for (const item of step.item_refs || []) check(hookRefs.has(item), `${id}: paso sin hook ${w.walk_ref}:${index}`);
        if (step.abcd === 'D') check(index === w.path.length - 1, `${id}: ruta continúa más allá de D ${w.walk_ref}`);
        cursor = step.to;
      });
      if (w.complete_to_D) {
        completeD++;
        check(w.path.at(-1)?.abcd === 'D' && w.terminal_kind === 'D', `${id}: D terminal aparente`);
      } else {
        partial++;
        check(w.path.at(-1)?.abcd !== 'D' && w.terminal_kind !== 'D', `${id}: falso D en ruta parcial`);
      }
    }
    const c = internal.coverage_summary || {};
    check(c.selected_roots === select.seed_node_refs?.length && c.selected_walks === internal.walks?.length, `${id}: conteos de selección incorrectos`);
    check(c.walks_closed_to_D === completeD && c.walks_partial === partial, `${id}: conteo de cierres falso`);
    check(c.universal_coverage_claim === false && !!c.scope, `${id}: completitud universal falsa`);

    const control = x.control_projection || {};
    check(control.msca_view_ref === view?.view_id && control.assessment_state === view?.assessment?.state, `${id}: estado MSCA no coincide`);
    check(control.assessment_state === 'UNASSESSED' && control.authority_state === 'NOT_ESTABLISHED', `${id}: prueba de control o autoridad no establecida`);
    for (const f of ['S', 'E', 'C', 'P', 'M']) check(control.slot_states?.[f] === view?.msca?.[f]?.state, `${id}: estado ${f} MSCA incoherente`);

    const disc = x.disclosure_example || {};
    check(disc.state === 'PREPARED_NOT_TRANSMITTED' && !!disc.receiver_agent_id, `${id}: simulación transmitida ficticiamente`);
    check(disc.omission_qualifier === 'NOT_DECLARED', `${id}: omisión confundida con D=0`);
    check(disc.omitted_walk_count === internal.walks.length - disc.included_walk_refs.length, `${id}: cuenta de omisiones incoherente`);
    for (const w of disc.included_walk_refs || []) check(internal.walks.some(p => p.walk_ref === w), `${id}: recorrido divulgado no incluido internamente`);
    check(disc.receiver_must_not_infer?.includes('D=0'), `${id}: no se protege residual omitido`);
    check(x.receiver_analysis?.state === 'NOT_EVALUATED' && x.receiver_analysis.blindspots_found?.length === 0, `${id}: puntos ciegos atribuidos sin composición`);
    for (const dep of x.requalification_on_change || []) {
      check(hookRefs.has(dep.item_ref) && dep.effect === 'review_dependent_projection', `${id}: invalidación no anclada`);
      for (const w of dep.affected_walk_refs || []) check(internal.walks.some(p => p.walk_ref === w), `${id}: dependencia sin recorrido`);
    }
  }
  return errors;
}

const errors = inspect(sample);
if (!errors.length) {
  const badD = structuredClone(sample);
  badD.slices[0].internal_slice.walks[1].complete_to_D = true;
  if (!inspect(badD).some(e => e.includes('cierre D distinto'))) errors.push('Autoprueba: no rechaza D inventado');

  const badDisclosure = structuredClone(sample);
  badDisclosure.slices[0].disclosure_example.omission_qualifier = 'D=0';
  if (!inspect(badDisclosure).some(e => e.includes('omisión confundida'))) errors.push('Autoprueba: no rechaza D=0 por no divulgación');

  const badEdge = structuredClone(sample);
  badEdge.slices[0].internal_slice.walks[0].path[0].abcd = 'B';
  if (!inspect(badEdge).some(e => e.includes('calificación distinta'))) errors.push('Autoprueba: no rechaza cambio de ABCD');
}

if (errors.length) {
  console.error(`Atlas/MSCA slice v0.1 — ${errors.length} error(es)`);
  for (const error of errors) console.error(`  ✗ ${error}`);
  process.exitCode = 1;
} else {
  console.log('Atlas/MSCA slice v0.1 — validación estructural correcta');
  for (const x of sample.slices) console.log(`Lámina ${x.slice_id}: ${x.internal_slice.coverage_summary.walks_closed_to_D} camino(s) a D, ${x.internal_slice.coverage_summary.walks_partial} parcial(es), MSCA ${x.control_projection.assessment_state}`);
  console.log('Autopruebas negativas: D falso, D=0 por omisión y ABCD alterado rechazados.');
  console.log('NO valida calidad del tema, dependencia material, interoperabilidad real, permiso ni suficiencia de control.');
}
