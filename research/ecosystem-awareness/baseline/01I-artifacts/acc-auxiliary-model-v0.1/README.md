# ACC — Modelo auxiliar

**Papel:** conjunto de artefactos opcionales de investigación alojado en la línea del [Agentic Citizenship Contract](../../01I_AGENTIC_CITIZENSHIP_CONTRACT_HUMAN_GOVERNED_PARTICIPATION_PROFILE_v0.1.md). **Estado:** modelo de trabajo deliberadamente acotado con un primer piloto determinista ejecutado; la evaluación científica e integración posteriores permanecen abiertas. Autoría de las ideas: Iván Abril Palma / The Integral Management Society; organización documental asistida por Codex.

**Nombre del artefacto:** ACC — Modelo auxiliar. «Conscientia» identifica únicamente los documentos de origen.

Este paquete reúne el modelo de sistemas y sociedad desarrollado en esas fuentes: oportunidades de mejora, condiciones de aceptación, coordinación, atribución, costes de transición, capacidades humanas, bienestar e incertidumbre. Incluye la exposición, los ejemplos, los modelos formales y las hipótesis de los documentos de trabajo, con su procedencia y sus límites.

**Su alojamiento en ACC permite encontrarlo y estudiarlo dentro de esa línea. Es un artefacto para utilización e integración posteriores. No ocupa todo ACC, no redefine su alcance y no especifica cómo incorporar ACC en un agente, su arquitectura interna o su protocolo de ejecución.** Tampoco convierte los supuestos económicos o éticos de un ensayo en obligaciones generales de ciudadanía agéntica.

## Pregunta principal

¿Cómo convertir mejoras posibles en acuerdos y transiciones realizables, y cuándo una mayor producción puede coexistir con más oportunidad perdida, coste de reajuste o carga humana? El recorrido parte de eficiencia y distribución, abre coordinación/atribución y n dimensiones, distingue acuerdo inmediato de negociación y examina sus efectos temporales. [Núcleo del modelo](MODEL.md#núcleo-económico-del-modelo).

Las perspectivas humanas, epistémicas e institucionales se integran en esa pregunta. [Revisión por perspectivas y pasadas](REVIEW_AND_COVERAGE.md) permite comprobar qué aporta cada una y localizar sus pasajes completos.

## Cómo leerlo

**Lectura técnica prioritaria:** [núcleo económico abierto completo](ECONOMIC_MODEL_TECHNICAL_CORE_v0.1.md) — producción, brechas, dimensiones soberanas, compensaciones, coordinación, costes de reajuste y modelos M0–M3. Su puente específico de deuda humana y aceleración se desarrolla en la [nota 01K-A02](../../01K_A02_HID_SECOND_ORDER_ECONOMIC_ACCELERATION_RESEARCH_NOTE_v0.1.md), dentro del propietario HID; ninguna de las dos piezas constituye un requisito normativo ACC.

| Lectura | Para qué sirve |
|---|---|
| [Núcleo técnico económico](ECONOMIC_MODEL_TECHNICAL_CORE_v0.1.md) | Definiciones económicas completas, restricciones, ecuaciones, cifras ilustrativas, familias rivales y falsadores |
| [01K-A02 — experimentos HID de segundo orden](../../01K_A02_HID_SECOND_ORDER_ECONOMIC_ACCELERATION_RESEARCH_NOTE_v0.1.md) | Hipótesis de aceleración, medición de deuda humana, controles y agenda experimental aún no ejecutada |
| [Auditoría de promoción del modelo social — 25 octubre](review/PROMOTION_AUDIT_2026-10-25.md) | Decisión sobre PRs y ramas, límites del experimento ABCD, pruebas, gates para promover a la rama principal sin asumir eficacia de EA |
| [Toy económico ejecutable y parametrizable](studies/parametric-economic-toy-v0.1/README.md) | Ejecutar óptimos, costes, permisos, HID directo por cada óptimo, contraste ABCD, crecimiento n→n+1, aceleración y barridos; 52 pruebas sintéticas |
| [Auditoría: HID primario por óptimo y experimento ABCD](studies/parametric-economic-toy-v0.1/HID_OPTIMUM_ABCD_AUDIT_v0.1.md) | Fórmula por resta de inputs informacionales humanos, comparabilidad, controles ABCD y aceleración sin ACW como sustituto |
| [Puentes experimentales HID · Attribution Gap · Informational Friction · obligaciones](studies/causal-bridges-v0.1/README.md) | Medir diferencias de inputs humanos frente a óptimos comparables y contrastar, con controles sintéticos, atribución, mapa/flujo y alta/extinción de obligaciones; 19 pruebas nuevas |
| [Modelo integrado](MODEL.md) | Comprender el problema, sus mecanismos, los límites y las preguntas abiertas |
| [Especificación del modelo de estudio](STUDY_SPECIFICATION.md) | Saber qué estados, variables, supuestos y observaciones deberá fijar una ejecución futura |
| [Casos y dimensiones](CASES.md) | Recorrer los ejemplos conservados y localizar su desarrollo completo |
| [Programa de evaluación DDS](DDS_EVALUATION_PLAN.md) | Pasar del modelo a preguntas contrastables; desde DDS, enlazar casos UC21/R01 cuando corresponda |
| [Fuentes y cobertura](SOURCES_AND_COVERAGE.md) | Identificar los cuatro textos fuente, su relación y los párrafos que se conservan |
| [Límites de integración con ACC](ACC_BOUNDARY.md) | Distinguir alojamiento, posible uso posterior e integración todavía no definida |
| [Estado de las afirmaciones](RESEARCH_STATUS.md) | Separar supuestos, hipótesis, resultados declarados y pruebas futuras |

## Textos completos del modelo y su contexto

1. [Notas completas y anexos](model/01_NOTAS_COMPLETAS.md): recorrido económico, bienestar, soberanía, incertidumbre, modelos matemáticos, experimentos declarados y ejemplos.
2. [Argumento autónomo](model/02_ARGUMENTO_AUTONOMO.md): FH-C/FH-E, verdad y fundamento para actuar, ABCD, mecanismo de Awareness y elección humana.
3. [Capacidades y diálogo](model/03_CAPACIDADES_Y_DIALOGO.md): capacidades efectivas, fines, correspondencias, autoridad y evaluación.
4. [Correspondencia técnica y social](model/04_CORRESPONDENCIA_TECNICA_Y_SOCIAL.md): antecedentes económicos, dinero y garantías, opcionalidad, preservación, transmisión y métodos relacionados.

Los textos completos conservan desarrollos históricos y formulaciones que requieren conciliación. [MODEL](MODEL.md) orienta su uso; una transcripción no reemplaza la definición canónica de otro documento. Los localizadores de otros archivos privados están sustituidos por una marca explícita; sus originales se mantienen en la custodia local. Esa supresión de localizadores no elimina el pasaje conceptual.

## Ruta de desarrollo

**Modelo acotado → especificación de preguntas y comparadores en DDS → preparación de casos y oráculos → arquitectura/implementación de estudio → ejecución y efectos → revisión de resultados.** Cuando una pregunta utilice UC21/R01, el adaptador queda definido en su protocolo DDS y conserva el contrato de fuente.

Existe también un [toy paramétrico ejecutable](studies/parametric-economic-toy-v0.1/README.md) con tres motores, 52 pruebas (34 previas y 18 de HID/ABCD) y un registro de resultados numéricos reproducible. Es adicional al piloto congelado, no lo reemplaza ni acredita medición humana.

El [estudio adicional de puentes HID / Attribution Gap / Informational Friction / obligaciones](studies/causal-bridges-v0.1/README.md) incorpora un protocolo reproducible de comparaciones y una matriz de cobertura/lagunas. Sus 19 pruebas verifican código sintético y no ejecutan las campañas empíricas HID2 de 01K. 

Existe ahora un [piloto económico determinista](studies/economic-pilot-v0.1/STUDY_PROTOCOL.md), con [recorrido manual](studies/economic-pilot-v0.1/MANUAL_TRAVERSAL.md), código y [resultados](studies/economic-pilot-v0.1/results/RESULTS.md). Ejecuta una especificación pequeña: los procedimientos principales empatan y los límites conservan sus FAIL. No es una integración operativa de ACC ni un cierre DDS. Las cifras sintéticas históricas conservan su procedencia y siguen sin autenticarse; la [recreación analítica nueva](studies/synthetic-recreation-v0.1/README.md) se identifica por separado.

## Relación con el corpus

ACC conserva sus condiciones de participación y gobierno. EA conserva ABCD y cualificación; MSCA, suficiencia de control; los mecanismos de identidad/autoridad, sus mandatos; y el ejecutor, la acción. El modelo puede informar futuras decisiones o contrastes de esos consumidores sin transferir sus competencias. [Límites y decisiones posteriores](ACC_BOUNDARY.md).

Los ejemplos humanos, institucionales, empresariales y de infraestructuras forman parte del objeto del modelo. Su primer estudio puede realizarse sin agentes de IA. Las cuatro pasadas de revisión de este paquete son relecturas de Codex, asistente de IA; no una revisión humana independiente ni un cierre científico. La elección de un soporte informático, de una ubicación posterior o de un perfil contractual concreto corresponde a trabajo futuro.

## Qué cambió tras las auditorías

Se restauran premisas de compensación, acuerdo y autoridad; se explicitan las cautelas de bienestar y ejemplos hipotéticos; se corrigen rangos y se prepara una trazabilidad conceptual. [La disposición de las 24 acciones](review/AUDIT_ACTIONS.md) distingue lo aplicado y lo pendiente. El [mapa de conceptos](review/CONCEPT_MAP.md) y las [notas de fuentes](review/SOURCE_NOTES.md) permiten seguir las condiciones y sus diferencias históricas.

Para reproducir el piloto basta Python 3.12 o posterior y su biblioteca estándar. Las instrucciones están en su protocolo. La coincidencia de un ejecutable con tablas manuales no certifica toda la teoría ni mide bienestar humano. El alojamiento y uso posterior en ACC conservan los límites declarados al comienzo de esta página.


### Puente experimental UC21 / DDS y revisión científica (25-10-2026)

La integración ejecutable con los seis escenarios está en el [contrato de falsabilidad](studies/parametric-economic-toy-v0.1/UC21_DDS_FALSIFIABILITY_CONTRACT.md), junto con la [matriz de efectos S1–S6](studies/parametric-economic-toy-v0.1/UC21_SIX_SCENARIO_NEGATIVE_TEST_MATRIX.md), el [adaptador Python y tests](studies/parametric-economic-toy-v0.1/README.md#integración-ejecutable-uc21--dds--acc--01k-25-10-2026) y la [autoevaluación crítica](studies/parametric-economic-toy-v0.1/EXECUTABLE_ENGINE_AUDIT_2026-10-25.md). Esta adición prepara estudios DDS sin modificar el oráculo ni los criterios UC21 congelados. Los resultados actuales siguen siendo sintéticos/documentales, no ejecución de productos reales.

### Vinculación con 00M y la falsación UC21

El [estudio de puente](studies/00m-acc-uc21-bridge-v0.1/README.md) conserva tres afirmaciones separadas: plausibilidad de 00M para declaraciones incompletas, dominancia débil de Q disponible/opcional/gratuito en el **modelo social**, y refutación adversa de predicciones por tecnología convencional o EA en el **protocolo fuente UC21/DDS**. Una defensa en un δ registrado refuta esa predicción; el existencial HR requiere cobertura más fuerte. La bibliografía y su atribución se auditan en el mismo estudio, manteniendo el estatus de investigación y los propietarios del corpus.

### Campaña Conscientia Ecosystemica — fuentes Google Docs → experimentos ejecutables (26-10-2026)

La [campaña integrada](studies/conscientia-campaign-v0.1/README.md) registra 23 fuentes —incluidos los Docs de *Conscientia Ecosystemica*, capacidades y los dosieres HID/Attribution Gap/Informational Friction/Cost of Clarity— y **60 casos sintéticos × cinco estrategias** con resultados positivos y negativos. Reejecuta los estudios anteriores PR #42–#45 y el adaptador UC21 sólo en su fixture sintético; no declara pruebas nativas, observaciones humanas ni cumplimiento de los gates de UC21. La [matriz de cobertura y pendientes](studies/conscientia-campaign-v0.1/SOURCE_COVERAGE_AND_BACKLOG.md) distingue lo implementado de lo que necesita datos/permiso. Los [resultados íntegros](studies/conscientia-campaign-v0.1/RUN_SUMMARY.md) son un corte local; GitHub CI adjunta el JSON integral regenerado.
