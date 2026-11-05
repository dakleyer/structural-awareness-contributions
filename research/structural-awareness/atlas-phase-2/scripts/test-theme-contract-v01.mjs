#!/usr/bin/env node
/**
 * Negative checks for the Atlas's public theme contract. Each deliberately
 * malformed fixture is passed via stdin: no persistent records are created.
 */
import { readFileSync } from 'node:fs';
import { dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import { spawnSync } from 'node:child_process';

const here = dirname(fileURLToPath(import.meta.url));
const base = JSON.parse(readFileSync(resolve(here, '../examples/language-v02-pilot.json'), 'utf8'));
const validator = resolve(here, 'validate-language-v02.mjs');
const dictionary = resolve(here, '../TAG_DICTIONARY_v0.1.json');
let failures = 0;

function inspect(doc) {
  const run = spawnSync(process.execPath, [validator, '-', dictionary], {
    input: JSON.stringify(doc), encoding: 'utf8'
  });
  return { exit: run.status, output: `${run.stderr}\n${run.stdout}` };
}

const good = inspect(base);
if (good.exit !== 0) {
  console.error('✗ El piloto de referencia no valida:', good.output);
  process.exit(1);
}

const cases = [
  ['suma inferior a 1', c => { c.theme_assignments[1].weight = 0.1; }, 'la suma de todos los pesos'],
  ['suma superior a 1', c => { c.theme_assignments[1].weight = 0.9; }, 'la suma de todos los pesos'],
  ['campo interpretativo en asociación pública', c => { c.theme_assignments[0].reason = 'contrato prohibido'; }, 'campos distintos'],
  ['rol principal en asociación pública', c => { c.theme_assignments[0].role = 'primary'; }, 'campos distintos'],
  ['explicación de agrupación en ficha de tema', c => { c.themes[0].why_together = 'contrato prohibido'; }, 'campo de relaciones/interpretación prohibido'],
  ['comparación entre temas en ficha', c => { c.themes[0].distinction_from = ['TH-DIAGNOSTIC']; }, 'campo de relaciones/interpretación prohibido'],
  ['referencia a clúster en ficha de tema', c => { c.themes[0].cluster_refs = ['CL-JUBAP']; }, 'campo de relaciones/interpretación prohibido'],
  ['duplicación nodo–tema', c => { c.theme_assignments.push({...c.theme_assignments[1]}); }, 'Asociación temática repetida'],
  ['tema inexistente', c => { c.theme_assignments[0].theme_id = 'TH-UNKNOWN'; }, 'tema desconocido'],
  ['peso cero', c => { c.theme_assignments[1].weight = 0; }, 'peso inválido'],
  ['nodo declarado clasificado sin sus asignaciones', c => { c.theme_assignments = c.theme_assignments.filter(a => a.node_id !== 'FON'); }, 'la suma de todos los pesos'],
  ['asignación de nodo fuera de la proyección', c => { c.theme_assignments.push({node_id: 'KOT', theme_id: 'TH-TRANSFORMATION', weight: 1}); }, 'parcial/no declarada'],
  ['clave temática retirada', c => { c.themes[0].etiquetas.push({key:'theme:distinction', value:'contrato prohibido', basis:'editorial', item_refs:[]}); }, 'etiqueta deprecada']
];

for (const [name, change, expected] of cases) {
  const sample = structuredClone(base);
  change(sample);
  const result = inspect(sample);
  if (result.exit === 0 || !result.output.includes(expected)) {
    failures++;
    console.error(`✗ ${name}: no fue rechazado como se esperaba\n${result.output}`);
  }
}

if (failures) process.exitCode = 1;
else console.log(`Contrato temático: piloto válido y ${cases.length} casos negativos rechazados correctamente; ficha pública descriptiva, ternas mínimas y suma por nodo = 1.`);
