#!/usr/bin/env node
/**
 * Atlas Phase 2 — optional MSCA view v0.1 structural/provenance validator.
 * It NEVER validates MSCA sufficiency, legitimate ownership or historical truth.
 * Usage: node scripts/validate-msca-view-v01.mjs [msca-fixture.json] [atlas-fixture.json]
 */
import { readFileSync } from 'node:fs';
import { dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const here = dirname(fileURLToPath(import.meta.url));
const viewPath = process.argv[2] ? resolve(process.argv[2]) : resolve(here, '../examples/msca-view-v01.json');
const atlasPath = process.argv[3] ? resolve(process.argv[3]) : resolve(here, '../examples/language-v02-pilot.json');
const fixture = JSON.parse(readFileSync(viewPath, 'utf8'));
const atlas = JSON.parse(readFileSync(atlasPath, 'utf8'));
const dictionary = JSON.parse(readFileSync(resolve(here, '../TAG_DICTIONARY_v0.1.json'), 'utf8'));
const stateKinds = new Set(['POPULATED', 'UNKNOWN', 'UNPOPULATED']);
const assessmentKinds = new Set(['UNASSESSED', 'SUPPORTED', 'FAILED', 'UNRESOLVED']);
const authKinds = new Set(['NOT_ESTABLISHED', 'REQUESTED', 'AUTHORIZED', 'DENIED', 'EXPIRED', 'NOT_APPLICABLE']);
const abcKinds = new Set(['A', 'B', 'C', 'D']);
const jfKinds = new Set(['JF.F1', 'JF.F2', 'JF.F3', 'JF.F4']);
const core = ['S', 'E', 'C', 'P', 'M'];
const itemMap = new Map((atlas.items || []).map(x => [x.id, x]));
const nodeMap = new Map((atlas.nodes || []).map(x => [x.id, x]));
const clusterMap = new Map((atlas.conceptual_clusters || []).map(x => [x.id, x]));
const themeMap = new Map((atlas.themes || []).map(x => [x.id, x]));
const walkMap = new Map((atlas.walks || []).map(x => [x.id, x]));
const allTagKeys = new Set();
const tagMap = new Map((dictionary.etiquetas || []).map(x => [x.key, x]));

function inspect(candidate) {
  const errors = [];
  const check = (ok, message) => { if (!ok) errors.push(message); };
  const seen = new Set();
  check(candidate.meta?.version === '0.1-experimental', 'Versión del adaptador incorrecta');
  check(candidate.meta?.source_fixture === 'language-v02-pilot.json', 'Fixture base incorrecto');
  check(candidate.meta?.dictionary_version === atlas.meta?.dictionary_version, 'Diccionario Atlas incongruente');
  check(candidate.meta?.dictionary_version === dictionary.dictionary_version, 'Versión del diccionario cargado incongruente');
  check(Array.isArray(candidate.views) && candidate.views.length > 0, 'Faltan vistas');

  for (const view of candidate.views || []) {
    const id = view.view_id || '<sin-id>';
    check(typeof view.view_id === 'string' && !!view.view_id, `Vista sin identificador ${id}`);
    check(!seen.has(id), `Vista duplicada ${id}`);
    seen.add(id);
    check(view.adapter_version === candidate.meta?.version, `Versión no consistente ${id}`);
    check(typeof view.description === 'string' && view.description.length > 25, `Descripción insuficiente ${id}`);
    check(view.scope?.activity && view.scope?.decision && view.scope?.process_boundary && view.scope?.as_of, `Falta actividad, pregunta, límite o fecha ${id}`);
    const map = view.source_map || {};
    for (const [field, lookup, mustHave] of [
      ['cluster_refs', clusterMap, true],
      ['theme_refs', themeMap, false],
      ['node_refs', nodeMap, true],
      ['walk_refs', walkMap, true],
      ['item_refs', itemMap, true]
    ]) {
      check(Array.isArray(map[field]), `Falta lista ${field} en ${id}`);
      if (mustHave) check((map[field] || []).length > 0, `No hay anclas ${field} en ${id}`);
      for (const ref of map[field] || []) check(lookup.has(ref), `Referencia ${field} inexistente ${ref} en ${id}`);
    }

    for (const ref of map.item_refs || []) {
      const i = itemMap.get(ref);
      check(!!i?.hook?.uri && !!i?.hook?.locator && !!i?.hook?.observed_at, `Hook irrecuperable ${ref} en ${id}`);
    }
    for (const observation of map.observations || []) {
      const w = walkMap.get(observation.walk_ref);
      const actual = w?.steps?.[observation.step_index];
      check((map.walk_refs || []).includes(observation.walk_ref) && !!actual, `Observación sin paso citado en ${id}`);
      if (actual) {
        check(actual.abcd === observation.atlas_abcd && abcKinds.has(observation.atlas_abcd), `ABCD no coincide con recorrido en ${id}`);
        check((observation.atlas_jf || []).every(f => jfKinds.has(f) && actual.jf_roles?.includes(f)), `JF no coincide con recorrido en ${id}`);
      }
      check(typeof observation.msca_implication === 'string' && observation.msca_implication.length > 15, `Falta interpretación de observación en ${id}`);
    }

    const binding = view.objective_binding || {};
    check(['BOUND', 'UNBOUND'].includes(binding.binding_status), `Binding status inválido en ${id}`);
    check(['UNKNOWN', 'VERIFIED'].includes(binding.owner_status), `Estado del titular inválido en ${id}`);
    if (binding.binding_status === 'BOUND') {
      check(binding.owner_status === 'VERIFIED' && !!binding.owner_ref && !!binding.envelope_ref, `Objetivo ligado sin propietario legítimo documentado en ${id}`);
    } else {
      check(binding.owner_status === 'UNKNOWN' && binding.owner_ref === null && binding.envelope_ref === null, `UNBOUND con titular/envelope supuesto en ${id}`);
    }

    check(view.msca && typeof view.msca === 'object', `Falta S/E/C/P/M en ${id}`);
    check(JSON.stringify(Object.keys(view.msca || {}).sort()) === JSON.stringify([...core].sort()), `Núcleo alterado o incompleto en ${id}`);
    for (const slot of core) {
      const field = view.msca?.[slot] || {};
      check(stateKinds.has(field.state), `${id}.${slot}: estado inválido`);
      check(Array.isArray(field.item_refs), `${id}.${slot}: faltan item_refs`);
      for (const ref of field.item_refs || []) {
        check(itemMap.has(ref), `${id}.${slot}: item_ref inexistente ${ref}`);
        check((map.item_refs || []).includes(ref), `${id}.${slot}: item_ref no trazado al mapa ${ref}`);
      }
      if (field.state === 'POPULATED') {
        check(field.value !== null && field.value !== undefined && !!field.qualification, `${id}.${slot}: POPULATED exige valor y calificación`);
        check((field.item_refs || []).length > 0, `${id}.${slot}: POPULATED sin ancla de evidencia`);
      } else {
        check(field.value === null, `${id}.${slot}: UNKNOWN/UNPOPULATED no debe simular valor establecido`);
        check(typeof field.reason === 'string' && !!field.reason, `${id}.${slot}: estado incompleto sin razón`);
      }
    }

    check(assessmentKinds.has(view.assessment?.state), `${id}: assessment state inválido`);
    check(Array.isArray(view.assessment?.configuration_refs), `${id}: lista de configuraciones ausente`);
    check(typeof view.assessment?.rationale === 'string' && !!view.assessment.rationale, `${id}: evaluación sin explicación`);
    check(Array.isArray(view.candidate_configurations), `${id}: candidatos ausentes`);
    if (view.assessment?.state === 'SUPPORTED') {
      check(binding.binding_status === 'BOUND', `${id}: SUPPORTED sin titular/objetivo ligados`);
      check(view.msca?.S?.state === 'POPULATED' && view.msca?.E?.state === 'POPULATED', `${id}: SUPPORTED sin S/E establecidos`);
      check((view.assessment.configuration_refs || []).length > 0, `${id}: SUPPORTED sin configuración evaluada`);
      check((view.candidate_configurations || []).some(x => x.assessment === 'SUPPORTED' && x.evidence_item_refs?.length), `${id}: SUPPORTED sin prueba de candidato`);
    }
    if (binding.binding_status === 'UNBOUND') {
      check(view.assessment?.state !== 'SUPPORTED', `${id}: evaluación SUPPORTED de S no legitimado`);
      check(view.msca?.S?.state === 'UNKNOWN', `${id}: S establecido sin owner/envelope`);
    }
    if (view.assessment?.state === 'UNASSESSED') check(view.assessment.configuration_refs?.length === 0, `${id}: UNASSESSED no debe aparentar configuración probada`);
    check(view.qualified_position_msca === null || (typeof view.qualified_position_msca === 'object' && !Array.isArray(view.qualified_position_msca)), `${id}: posición MSCA mal definida`);
    const gate = view.authority_boundary || {};
    for (const name of ['authorization_state', 'execution_state', 'effect_state']) check(authKinds.has(gate[name]), `${id}: puerta operativa ${name} inválida`);
    check(!(gate.authorization_state === 'NOT_ESTABLISHED' && gate.execution_state === 'AUTHORIZED'), `${id}: ejecución incorrectamente marcada autorizada`);
    check(Array.isArray(view.etiquetas), `${id}: falta lista de etiquetas`);
    for (const e of view.etiquetas || []) {
      check(e?.key && typeof e.key === 'string', `${id}: etiqueta sin clave`);
      allTagKeys.add(e.key);
      const definition = tagMap.get(e.key);
      check(!!definition && definition.kind === 'flexible_tag' && definition.applies_to.includes('analysis_profile'), `${id}: etiqueta fuera del diccionario o ámbito: ${e.key}`);
      if (definition?.value_type === 'object') check(e.value && typeof e.value === 'object' && !Array.isArray(e.value), `${id}: valor de etiqueta no es objeto: ${e.key}`);
      if (definition?.state !== 'active') check(e.dictionary_state === 'candidate_local_only', `${id}: etiqueta candidata promovida silenciosamente: ${e.key}`);
      check(typeof e.basis === 'string' && e.basis.length > 3, `${id}: etiqueta sin justificación: ${e.key}`);
      for (const ref of e.item_refs || []) check((map.item_refs || []).includes(ref), `${id}: etiqueta sin trazabilidad al ítem ${ref}`);
    }
    check(Array.isArray(view.candidate_questions), `${id}: faltan preguntas de minería`);
    for (const d of view.dependencies || []) {
      check(core.includes(d.field), `${id}: dependencia con campo desconocido ${d.field}`);
      check(itemMap.has(d.item_ref) && (map.item_refs || []).includes(d.item_ref), `${id}: hook de dependencia inexistente`);
      check(d.on_change === 'requalify_dependent_claims', `${id}: dependencia sin revalidación`);
    }
    // This adapter must not become a place for global ABCD or automatic JF→MSCA scoring.
    check(!('abcd' in view) && !('jf_role' in view) && !('JF' in view.msca), `${id}: conflación de recorrido y MSCA`);
  }

  // Required teaching case: same cluster, distinct objective-bound control questions.
  if (seen.has('MSCA-JUBAP-CHANGE-001') && seen.has('MSCA-JUBAP-HUMAN-002')) {
    const business = candidate.views.find(x => x.view_id === 'MSCA-JUBAP-CHANGE-001');
    const human = candidate.views.find(x => x.view_id === 'MSCA-JUBAP-HUMAN-002');
    check(business.scope.activity !== human.scope.activity, 'Dos problemas de control fusionados por actividad');
    check(business.source_map.cluster_refs.includes('CL-JUBAP') && human.source_map.cluster_refs.includes('CL-JUBAP'), 'Falta clúster compartido de prueba');
  }
  return errors;
}

const errors = inspect(fixture);
if (!errors.length) {
  const invalid = structuredClone(fixture);
  invalid.views[0].assessment.state = 'SUPPORTED';
  const diagnostic = inspect(invalid);
  if (!diagnostic.some(e => e.includes('SUPPORTED sin titular/objetivo ligados') || e.includes('evaluación SUPPORTED de S no legitimado'))) errors.push('Autoprueba negativa: no se detectó A→SUPPORTED ilícito');

  const wrongPath = structuredClone(fixture);
  wrongPath.views[1].source_map.observations[0].atlas_abcd = 'A';
  if (!inspect(wrongPath).some(e => e.includes('ABCD no coincide'))) errors.push('Autoprueba negativa: no se detectó trasvase falso de recorrido');

  const falseOwner = structuredClone(fixture);
  falseOwner.views[0].objective_binding.binding_status = 'BOUND';
  if (!inspect(falseOwner).some(e => e.includes('Objetivo ligado sin propietario'))) errors.push('Autoprueba negativa: no se detectó titular inexistente');
}

if (errors.length) {
  console.error(`ATLAS MSCA View v0.1 — ${errors.length} error(es) estructurales`);
  for (const error of errors) console.error(`  ✗ ${error}`);
  process.exitCode = 1;
} else {
  console.log('ATLAS MSCA View v0.1 — validación estructural correcta');
  console.log(`${fixture.views.length} vistas objetivo-independientes, ${itemMap.size} ítems del Atlas vinculables`);
  console.log(`Diccionario ${dictionary.dictionary_version}; ${allTagKeys.size} etiquetas usadas como candidatas locales.`);
  console.log('Autopruebas negativas: SUPPORTED sin S, ABCD alterado y titular ficticio rechazados.');
  console.log('No valida legitimidad, suficiencia, causalidad ni eficacia de un método.');
}
