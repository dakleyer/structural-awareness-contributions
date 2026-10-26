# FLORES — integración auditada del suplemento técnico P0–P3, 13 octubre 2026

**Objeto:** verificar e integrar el [componente técnico RECEIVER-P0-P3](technical/TECHNICAL_INDEX.md) en **la misma campaña** [DDS-A-FLORES-POP-EA-01](CAMPAIGN.md), contrastándolo con el [giro de enfoque 12–13 octubre](APPROACH_DRIFT_2026-10-12_13.md) y el [ensayo UC17-08 de mínima intervención](PRIMARY_TRIAL_PROTOCOL_DRAFT_v0.1.md).

**Estado de esta revisión:** `MAINTAINER_SIDE_DOCUMENTARY_AND_CODE_INSPECTION`, no auditoría externa independiente, no ejecución nativa de Flores, no nuevo Stage ni resultado Stage A.  
**Corte fuente:** GitHub commit `c6858fd2110fe7debd93b20dc4fdfa5b6302f8ea`, añadido el 13 octubre.  
**Regla:** preservar fuentes científicas previas, no fusionar dos protocolos que prueban propiedades distintas, no aceptar un test del propio autor como prueba del sistema.

## 1. Qué apareció realmente en el mismo expediente

Se creó un suplemento técnico **dentro** de `flores-population-ea/technical/`, con [índice](technical/TECHNICAL_INDEX.md), [registro de componente](technical/TECHNICAL_COMPONENT_RECORD.json), [protocolo P0–P3](technical/PROTOCOL_P0_P3.md), [puente EHD 04/05A](technical/EHD_04_05A_MAPPING.md), [13 puertas G00–G12](technical/ACCEPTANCE_AND_B2.md), [residual ledger de nueve preguntas](technical/RESIDUAL_LEDGER.md), [auditorías y defectos](technical/AUDIT_RECONCILIATION.md), [fuentes/pins y 20 cuerpos de comentarios hasheados](technical/SOURCES_AND_PINS.md), [historia SHA-256](technical/HISTORY_AND_REPRODUCTION.md), [matriz CSV](technical/STAGE_A_GATE_TRACE.csv), [código de ejemplo](technical/code/qualifier.py), [receipts sintéticos](technical/code/mock_receipts.json) y [tests propios](technical/code/test_qualifier.py). Existe además un [borrador de solicitud externa no enviado](technical/SUBMISSION_BRIEF_EN.md).

**No es una segunda campaña** ni se debe adscribir como trabajo de Justin Flores: el nombre de componente local `DDS-A-FLORES-POP-EA-01/RECEIVER-P0-P3` conserva su independencia de la ejecución fuente y el mismo Stage A propuesto. La identidad propietaria de la campaña y el índice DDS original siguen siendo únicos.

## 2. Reconciliación de **dos variantes prospectivas**, no de dos resultados

| Dimensión | **FLO-F0..F4** — derivación mínima UC17-08 | **RECEIVER-P0→P3** — suplemento corregido |
|---|---|---|
| Entrada prioritaria | Registro source-native UC17-08 `attested absence`; futuro output poblacional solo si se publica | Futura evidencia ciega `flags` y post-unblind `seal/key`, representada por **mock receipts** hoy |
| Perturbación | Un adaptador **downstream** transforma indebidamente `attested absence → permit` en F2 | Un evaluador **downstream** retira una asociación de prueba material (perfil/referencia/rol/alcance) en P2 |
| Fundamento que pierde apoyo | Fidelidad de traducción y suficiencia de una afirmación consumidora específica, no corrección del detector | Justificación de `Q_KEY_RELATIVE_COMPARABILITY` (solo al comparar con clave authored); original key truth sigue `NOT_ESTABLISHED` |
| Recuperación | Restituir mapeo y probar recuperación solo de afectado F3 | Restituir asociación fuente válida P3 con historial y claims no afectados intactos |
| Control positivo / negativo | F1 clean; F4 indistinguibilidad si fuente/mapeo no accesible | P1 legítimo, decoración no material, reconstrucción alternativa, falso sello, UNKNOWN y barrera de acceso |
| Techo científico | Cambio de **semántica receptora**, no dinámico R3 de independencia | Cambio **sintético de base demostrativa en receptor**, B→UNKNOWN cuando proceda, NO EA-C automático, no evento real de los jueces |
| Comparador | B2 fuerte tipo/provenance/permission/versión | B2 fuerte con **el mismo grafo de dependencias** y coste total |
| Estado | Draft prioritario propuesto por el titular tras pivot, no congelado | Subperfil técnico activo corregido y mock instrumentado, **no ejecutado con Flores** |

Estas dos pruebas se relacionan y pueden informar la selección de requisitos, pero **no están ejecutadas, no comparten un Run Card congelado ni se convierten automáticamente en una sola campaña experimental puntuada**. El giro del 12 no autoriza a declarar que P0–P3 corregido es inútil: se rechazó el antiguo Q-bind/B→C ilusorio, no la pregunta seria de *pérdida y recuperación de suficiencia del fundamento*. Un revisor independiente puede considerar ambos paquetes al acordar la primera ejecución. El ensayo mínimo UC17-08 conserva prioridad de diseño, no “selección formal” ni aceptación externa.

## 3. Los hallazgos científicos del componente que NO se pueden perder

1. **El escenario original de Flores no se reescribe:** seis jueces guionizados, ocho casos puntuados, `J1..J6` solo asignados una vez por run, detector blind, unblind posterior, `UC17-08` no puntuado, `UC17-09` contenido/remediación versus validación C10 y el shared blind spot UC17-02. [Protocolo externo fijado](https://github.com/Himalogic/FG-TIDA-analysis/blob/07ac94fb100975bfff2e8ab0c644bd02ec87e537/planted-judge/README.md).
2. **Q_METHOD, Q_BLIND_RECEIPT, Q_KEY_RELATIVE_COMPARABILITY, Q_KEY_OBJECTIVELY_TRUE, Q_INDEPENDENCE** no son sinónimos: un sello rechazado invalida la comparación con la clave, pero **no refuta que la clave de Cyril sea objetiva o subjetivamente verdadera**; su verdad independiente sigue no establecida sin referencia externa.
3. **EHD N07–N10 e IF-S9**: no exigir B/C/D nuevos a Flores; la fuente A original es separada de metadatos de interfaz, con versionado, dependencia y `UNKNOWN` en el consumidor. `Indeterminate` de la política origen no implica EA C/D; las etiquetas B/C/D son relativas al proceso, no campos originales obligatorios.
4. **P2 corregido:** supresión sintética local de una asociación necesaria ⇒ `NOT_ESTABLISHED` en la proposición dependiente; no es `REFUTED` por simple ausencia, ni B→C automático, ni R3 fuente real.
5. **P3:** recuperación solo con base efectivamente restituida; conservar toda la historia y afirmaciones no afectadas, permitir prueba de asociación alternativa legítima.
6. **R0/R1 residual ledger de nueve cuestiones:** distingue límites nativos conocidos, sesgo compartido sistemático, inferencia de independencia no establecida, origen authored de la clave y agujeros de cobertura; la prueba de probes 96/12 es **hipotética**, no ejecución de Flores.
7. **Reparos 13 y diferencial B2:** un verificador convencional competente puede implementar el mismo grafo y empatar o superar al caso EA. Se puntúa utilidad y costes en Stage A, no singularidad de una marca.
8. **13 gates G00–G12** son **propuestos**, no un catálogo Stage A aceptado por un auditor; los 21 checks del `qualifier.py` son consistencias sobre hechos y receipts mock, no resultados de jueces ni efectividad de EA.

## 4. Auditoría del código de ejemplo: límites y defecto adicional

Inspeccionados [qualifier.py](technical/code/qualifier.py), [test_qualifier.py](technical/code/test_qualifier.py) y [mock_receipts.json](technical/code/mock_receipts.json) (GitHub blobs `c776e122...`, `e5f07d4...`, `ea0a247...`). El checker evalúa un **grafo de requisitos explícitamente introducido por el autor**, con `SUPPORTED / REFUTED / NOT_ESTABLISHED`. Su función no lee ni valida el dato fuente de Flores, no infiere dependencias nuevas desde observaciones, no verifica firmas, no discrimina por sí sola un nuevo canal/forma de corrupción. Un B2 puede implementarlo.

**T-A01 — check de indistinguibilidad demasiado débil (ALTO):** al final de `test_qualifier.py`, la variante `x` asigna `independent_key_truth = NOT_ESTABLISHED`, **que ya tenía ese valor en `mock_receipts.json`**. Por tanto compara una copia con el mismo hecho y el mismo input: `evaluate(x,"P1")==evaluate(SPEC,"P1")` es una **igualdad trivial**, no demuestra que dos mundos ocultos materialmente diferentes pero observacionalmente indistinguibles sean manejados correctamente. **Acción:** añadir futuro control con variable de verdad exclusivamente en oracle privado, dos mundos de verdad distintos, mismo paquete visible y mismas respuestas; no cambiar silenciosamente el test histórico para convertirlo en prueba ya ejecutada.

**T-A02 — comandos de reproducción obsoletos (MEDIO):** `technical/HISTORY_AND_REPRODUCTION.md` manda ejecutar la ruta histórica `research/ecosystem-awareness/fg-tida/tests/flores-population-theme21/code/`, **que no existe en el árbol actual**. La ubicación real es `research/ecosystem-awareness/campaigns-in-development/flores-population-ea/technical/code/`. Se registran comandos correctos mediante errata/versionado, no se presupone que el lector conoce el traslado.

**T-A03 — alcance de pruebas (ALTO):** el fichero tiene **17 aserciones enumeradas, tres casos derivados de supresión de asociación y una comprobación de igualdad (17+3+1 = 21)**. La afirmación del suplemento de “21 selfchecks” es trazable al código inspeccionado, pero **no constituye ejecución independiente en esta auditoría**, ni prueba cegada, ni evaluación externa o de modelo. La validez de la lógica fuente/mock, la corrección del oráculo y el coste total permanecen abiertos.

**T-A04 — semántica condicional (MEDIO):** el checker da `REFUTED` a un **conjuntivo explícito** cuando una de sus dependencias está refutada; no permite concluir que una afirmación ajena al conjuntivo también sea falsa. El sucesor v0.3 corrige precisamente el fallo anterior que infería falsedad de `Q_KEY_OBJECTIVELY_TRUE` a partir de un sello refutado. No atribuir una comprobación del key authored a la realidad externa.

**T-A05 — receipts sintéticos (ALTO):** estados como `blind_flags_receipt: SUPPORTED` o `seal_join: SUPPORTED` son **valores mock autorales**; actualmente no acreditan publicación/validación de flags/seal reales. En una prueba admitida deben reemplazarse por observaciones nativas legitimadas y cotejarse con una fuente independiente.

**Estado final de la revisión del código:** `SOURCE_AND_TEST_LOGIC_INSPECTED / 21_ASSERTIONS_ENUMERATED / NOT_EXECUTED_BY_THIS_AUDITOR / NO_EA_OR_NATIVE_FLORES_RESULT`.

## 5. Estado real de custodia ZIP: dos observaciones distintas

La [Historia técnica](technical/HISTORY_AND_REPRODUCTION.md) registra nueve artefactos originales del 11–12 octubre y **sus SHA-256 calculados en otro entorno de trabajo el 13**. Incluye `EA_FLORES_RESIDUAL_DISCRIMINABILITY_v0_2_2026-10-12.zip` con SHA-256 `8e1d2196736e2a1ef862e37e3e4d4a30361bb5d2121ebe6f22b501715aa520c6` y `EA_POPULATION_STAGE_A_AUDIT_CORRECTED_v0_5_2026-10-12.zip` con SHA-256 `0b2a2b5f91e7b5f040ab550fae2d5c86c32b2a9910c719eafc1b6f0afdf507e0`, además de v0.1/v0.3/v0.4, precursor Markdown y textos de reentrada.

**Corrección a nuestro dossier previo:** la frase “no se encontraron los ZIP” se refería a la **sesión que creó el primer expediente** y no puede mantenerse como estado absoluto de la iniciativa. El componente técnico **afirma comprobación SHA-256 de originales que estuvieron disponibles en otro runtime**, pero **este auditor no tuvo los bytes para repetirla**. No se distribuyeron públicamente los ZIP, y no debe declararse preservación pública binaria/reproducción independiente de su contenido desde esta carpeta. Registrar los hashes y la existencia afirmada, con procedencia, es más riguroso que borrar ese avance o fingir su reproducción aquí.

En cambio sí se conservaron en el presente expediente seis **textos completos legibles** de Library (cuatro PDF como texto extraído, dos TXT), [manifiesto](history/recovered-text/RECOVERY_MANIFEST.json). Los textos extraídos tampoco reemplazan originales PDF/TXT byte idénticos. Para custodia íntegra de históricos privados será necesario un almacén autorizado fuera de la prueba ciega pública.

## 6. Reglas finales de coherencia

- **Un solo expediente DDS en desarrollo**, `DDS-A-FLORES-POP-EA-01`. El componente corregido P0–P3 y el control UC17-08 se conservan **dentro**, como propuestas de mecanismos distintos; no dos campañas Stage A ejecutadas.
- **Una sola metodología** DDS, pero **sin congelación/admisión** de la campaña concreta. Variantes, fuente nativa y ensayos sintéticos no son Stage B/C.
- **Primer estudio preferente**: perturbar la frontera fuente→receptor con un cambio bien observable, comparar B2 completo y EA bajo idénticos costos; **componente P0–P3**: mantener como candidato científico técnicamente especificado, no rechazarlo por errores de un prototipo anterior ya corregidos.
- **Ausencia de superioridad demostrada**: los checks de mock y los auditor-review notes no son resultados. Puede haber equivalencia o una especificación convencional suficientemente buena.
- **Nunca tratar la corrección interna de la campaña como autorización del participante externo**. No enviar el borrador de correo ni publicar jueces/desenlaces privados.
- **No asumir la presencia de los ZIP en este runtime solo porque otro los verificó**. Conservar el acta técnica exacta y pedir/paridad de bytes si una futura ejecución los necesita.

**Próximo punto de decisión:** revisor independiente selecciona el primer `Challenge` mínimo y adjudica requisitos/acciones con el propietario de la decisión, libera lo que pueda verse del experimento original, fija B2 y la especificación EA y hace el Run Card real. Hasta ese momento estado = `CAMPAIGN_IN_DEVELOPMENT / PIVOT_DOCUMENTED / TECHNICAL_SUBPROFILE_PRESENT / NOT_PREREGISTERED / NOT_EXECUTED`.

## 7. Consolidation decision / chronology of this audit

The [master campaign](CAMPAIGN.md), [scientific approach drift](APPROACH_DRIFT_2026-10-12_13.md), [two candidate designs](PRIMARY_TRIAL_PROTOCOL_DRAFT_v0.1.md) and [technical index](technical/TECHNICAL_INDEX.md) have now been reconciled into **one** Stage A campaign in development with **distinct** planned trials and statuses. The owner priority to run a small Flores-native receiving-mapping perturbation does not revoke the corrected technical P0–P3 subprofile. Old P0–P3 Q-bind/B→C assertions remain falsified/restricted, while bounded recipient proof-loss/recovery is still open science.

The technical source's nine archival SHA claims are attributed to the other 13 October authoring runtime; original private ZIPs and hidden evaluator oracles are not published, and the present audit did not rehash them. This is **not** external independent adjudication of either design and no Stage A verdict was issued.
