# ACC — Modelo auxiliar

**Papel:** conjunto de artefactos opcionales de investigación alojado en la línea del [Agentic Citizenship Contract](../../01I_AGENTIC_CITIZENSHIP_CONTRACT_HUMAN_GOVERNED_PARTICIPATION_PROFILE_v0.1.md). **Estado:** modelo de trabajo deliberadamente acotado con un primer piloto determinista ejecutado; la evaluación científica e integración posteriores permanecen abiertas. Autoría de las ideas: Iván Abril Palma / The Integral Management Society; organización documental asistida por Codex.

**Nombre del artefacto:** ACC — Modelo auxiliar. «Conscientia» identifica únicamente los documentos de origen.

Este paquete reúne el modelo de sistemas y sociedad desarrollado en esas fuentes: oportunidades de mejora, condiciones de aceptación, coordinación, atribución, costes de transición, capacidades humanas, bienestar e incertidumbre. Incluye la exposición, los ejemplos, los modelos formales y las hipótesis de los documentos de trabajo, con su procedencia y sus límites.

**Su alojamiento en ACC permite encontrarlo y estudiarlo dentro de esa línea. Es un artefacto para utilización e integración posteriores. No ocupa todo ACC, no redefine su alcance y no especifica cómo incorporar ACC en un agente, su arquitectura interna o su protocolo de ejecución.** Tampoco convierte los supuestos económicos o éticos de un ensayo en obligaciones generales de ciudadanía agéntica.

## Pregunta principal

¿Cómo convertir mejoras posibles en acuerdos y transiciones realizables, y cuándo una mayor producción puede coexistir con más oportunidad perdida, coste de reajuste o carga humana? El recorrido parte de eficiencia y distribución, abre coordinación/atribución y n dimensiones, distingue acuerdo inmediato de negociación y examina sus efectos temporales. [Núcleo del modelo](MODEL.md#núcleo-económico-del-modelo).

Las perspectivas humanas, epistémicas e institucionales se integran en esa pregunta. [Revisión por perspectivas y pasadas](REVIEW_AND_COVERAGE.md) permite comprobar qué aporta cada una y localizar sus pasajes completos.

## Cómo leerlo

| Lectura | Para qué sirve |
|---|---|
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

Existe ahora un [piloto económico determinista](studies/economic-pilot-v0.1/STUDY_PROTOCOL.md), con [recorrido manual](studies/economic-pilot-v0.1/MANUAL_TRAVERSAL.md), código y [resultados](studies/economic-pilot-v0.1/results/RESULTS.md). Ejecuta una especificación pequeña: los procedimientos principales empatan y los límites conservan sus FAIL. No es una integración operativa de ACC ni un cierre DDS. Las cifras sintéticas históricas conservan su procedencia y siguen sin autenticarse; la [recreación analítica nueva](studies/synthetic-recreation-v0.1/README.md) se identifica por separado.

## Relación con el corpus

ACC conserva sus condiciones de participación y gobierno. EA conserva ABCD y cualificación; MSCA, suficiencia de control; los mecanismos de identidad/autoridad, sus mandatos; y el ejecutor, la acción. El modelo puede informar futuras decisiones o contrastes de esos consumidores sin transferir sus competencias. [Límites y decisiones posteriores](ACC_BOUNDARY.md).

Los ejemplos humanos, institucionales, empresariales y de infraestructuras forman parte del objeto del modelo. Su primer estudio puede realizarse sin agentes de IA. Las cuatro pasadas de revisión de este paquete son relecturas de Codex, asistente de IA; no una revisión humana independiente ni un cierre científico. La elección de un soporte informático, de una ubicación posterior o de un perfil contractual concreto corresponde a trabajo futuro.

## Qué cambió tras las auditorías

Se restauran premisas de compensación, acuerdo y autoridad; se explicitan las cautelas de bienestar y ejemplos hipotéticos; se corrigen rangos y se prepara una trazabilidad conceptual. [La disposición de las 24 acciones](review/AUDIT_ACTIONS.md) distingue lo aplicado y lo pendiente. El [mapa de conceptos](review/CONCEPT_MAP.md) y las [notas de fuentes](review/SOURCE_NOTES.md) permiten seguir las condiciones y sus diferencias históricas.

Para reproducir el piloto basta Python 3.12 o posterior y su biblioteca estándar. Las instrucciones están en su protocolo. La coincidencia de un ejecutable con tablas manuales no certifica toda la teoría ni mide bienestar humano. El alojamiento y uso posterior en ACC conservan los límites declarados al comienzo de esta página.
