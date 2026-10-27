# CONS-EX — Campaña reproducible de los Google Docs de Conscientia Ecosystemica

**26 octubre 2026 · Estado: 46 CASOS SINTÉTICOS EJECUTADOS + 88 BARRIDOS DE SENSIBILIDAD; 65 CONTROLES UNITARIOS LOCALES.**

**Clasificación de evidencia (F-06).** Los 46 son *ejemplos trabajados y fixtures sintéticos ejecutables*: comprueban las reglas y sus condiciones límite bajo entradas estipuladas; los 88 barridos prueban sensibilidad respecto de parámetros fijados. Las 65 pruebas son controles de regresión, **no 65 experimentos empíricos ni validaciones independientes**. La familia `kl` usa expresamente soportes finitos y **distribuciones uniformes**: `log2(m/n)` no se generaliza a distribuciones arbitrarias. La familia `closure` sí ejercita una inferencia matemática condicionada por regularidad Lipschitz, sin validar esa regularidad en el mundo. El resto puede ser útil como explicación, documentación de restricciones o contraejemplo, sin atribuir a los datos sintéticos fuerza probatoria externa.

El registro incluye **12 Google Docs concretos**. Los **46 casos** se vinculan directamente a **9** de ellos (CE1, CE2, CE3, CE4, CE6, CE7, CE8, CE10 y CE11); CE5, CE9 y CE12 se conservan como contexto documental, sin atribuirles un caso ejecutado propio. Cada caso declara su fuente en [EXPERIMENT_CATALOG.md](EXPERIMENT_CATALOG.md) y en el manifiesto fijado por hash [CASES.json](CASES.json). Los resultados de referencia están en [REFERENCE_RESULTS.json](REFERENCE_RESULTS.json) y [REFERENCE_SWEEPS.json](REFERENCE_SWEEPS.json). Cada afirmación tiene su nivel de evidencia; no hay campañas reales con participantes, proveedores o productos.

El paquete anterior [RAV-EX/01 — 20 casos «La generación de las rotondas»](../risk-aversion-persistence-v0.1/experiments-from-escritos-v0.1/README.md) **ya existe en main** y permanece intacto. Este paquete añade casos nuevos centrados en la contribución Conscientia (algunas preguntas comparten temática, pero no se presentan como réplicas independientes). Entre ambos hay 66 **filas registradas de ensayo**, no 66 resultados empíricos independientes.

## Qué investiga, en grupos con falsadores adversos

| Familia | Casos | Predicción/resultado acotado | Condición que invalida la lectura favorable |
|---|---:|---|---|
| Plátanos y coordinación | 5 | Reparto local puede reducir recursos y ampliar servicio | Transporte adicional, falta de consentimiento, coordinación saturada |
| Crédito/Viernes–Robinson | 3 | Beneficio absoluto y crédito relativo son distintos | Exigencias conjuntas 7+4 sobre 10 son inviables; 7+3 sí |
| Ministerios, instituciones | 3 | Reorganización puede liberar recursos | Sin coordinación o autorización, alternativa no ejecutable |
| Manzanas y utilidad no monótona | 1 | Un mínimo local no equivale a máximo global | Perfil de utilidad/discreción es supuesto finito |
| Eficiencia en dos horizontes | 2 | Brecha puede pasar de 20 a 45 con más output | Contrafactual no factible no establece deuda |
| Disconfort y contabilidad humana | 6 | W=B−F puede cambiar de signo, inputs GIC/NEO/ACW separables | F no observada, referente no comparable, NEO no equivale a HID |
| Shannon, preimágenes y KL | 6 | Ambigüedad de pregunta vs origen; dirección correcta de KL | Sin prior o con exterior abierto no calcular H(D) |
| Attribution Gap | 3 | Inventario y dependencia efectiva pueden divergir | Fórmula E entre ediciones del instrumento sin errata: **BLOCKED** |
| Cambio de misión | 3 | Fuentes repetidas no son independientes; cambio legítimo permitido | Falta de autoridad o procedencia; R0–R2 UC21 NO ejecutado |
| Q/B frente a ampliación A | 4 | B puede tener menor coste, pero peer convencional también gana | Q falsa/irrelevante/cara; beneficio contrafactual no demostrado |
| Cierre parcial e indeterminación | 7 | Una pregunta puede decidirse sin clausurar el residual | Sin regularidad o sin evidencia individual no inferir un hecho |
| Redes de dependencia | 4 | G/P puede subir condicionalmente con densidad | Red estrella, g=0, óptimo no ejecutable, costes ocultos |

## Protocolo reproducible

Usar Python ≥3.10 **sin dependencias externas**, desde esta carpeta del repositorio:

```bash
python -B campaign.py > /tmp/conscientia_experiments.json
python -B sensitivity.py > /tmp/conscientia_sensitivity.json
python -B -m unittest discover -s . -p 'test_*.py' -v
python -B -c "import json; from pathlib import Path; assert json.loads(Path('REFERENCE_RESULTS.json').read_text())==json.loads(Path('/tmp/conscientia_experiments.json').read_text()); assert json.loads(Path('REFERENCE_SWEEPS.json').read_text())==json.loads(Path('/tmp/conscientia_sensitivity.json').read_text())"
```

El artefacto de salida incluye `input_sha256`, `case_count`, clase de evidencia y resultados por caso, además de barras y controles nulos. Las **88 variaciones** proceden de cuatro rejillas congeladas de topología/interacciones, Q frente a peer, crédito y regularidad; no hay selección posterior de perfiles vencedores. No se ha medido la entropía de un D abierto ni comparado proveedores.

## Lo que estos resultados NO demuestran

- No son investigación experimental sobre personas, ni verifican un caso francés, donación de Cáritas, institución, empresa o precio real de naranjas. Las escenas son ejemplos propuestos por el autor.
- No prueban que Ecosystem Awareness tenga una ventaja económica universal, ni que B/C/D pueda reducirse a un conjunto cerrado; son **posibilidades y contraejemplos** bajo premisas declaradas.
- No son resultados de UC21 nativo, DDS Stage C ni 01K HID medido. El programa de refutación separado se conserva en [puente 00M-ACC-UC21](../00m-acc-uc21-bridge-v0.1/README.md).
- No establecen causalidad social por haber reproducido una ecuación. [DOI/artículos de disciplinas anteriores](../scoped-closure-metacognition-v0.1/CROSS_PR_RESEARCH_NOVELTY_SYNTHESIS_2026-10-26.md) son antecedentes, no validación de los números aquí elegidos.

## Estado de las pruebas de campo y requisitos de datos

| Propuesta de campo (NO ejecutada) | Instrumento/autoridad que falta | Resultado que debe conservarse abierto |
|---|---|---|
| D02 Attribution Gap E | Resolver desacuerdo entre versión PDF y HTML de la medida y reproducibilidad interevaluador | `MEASUREMENT_EDITION_CONFLICT_BLOCKED` |
| D17 Cost of Clarity, captura–recaptura | Población, independencia/identificación de fuentes y muestras auténticas | PREPARADO / NO ESTIMADO |
| D20/HID mediación humana | Consentimientos, registros reales GIC/NEO/ACW/UNKNOWN, contrafactual de mismo servicio | SIN MEDICIÓN HID |
| Desarrollo humano y sufrimiento | Preferencia individual, opción factible, medición psicológica validada | NO MEDIDO; dignidad no monetizable |
| UC21 S1–S6 | Instrumento, ejecutor de producto real, gates originales, observador independiente, R1 corregido/δ R2 preregistrado | NO PASS/FAIL Nativo |

## Mapa hacia la reducción agéntica

No se presupone que un agente «sufre». Un futuro módulo de reducción deberá representar **frustración funcional de misión**, oportunidades de reasignación por límites B/C/D, coste de coordinación/metamorfosis y meta-protocolo autorizado. Los comportamientos de solidaridad, apagado o cambio de rol que ya estaban en una función agente NO se venderán como capacidades metafísicas nuevas; el diferencial sólo existe si Q permite elegir una transición antes no justificada y viable.
