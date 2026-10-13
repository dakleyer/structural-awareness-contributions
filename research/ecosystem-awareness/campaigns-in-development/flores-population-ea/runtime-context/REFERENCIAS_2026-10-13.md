> Registro de preparación incorporado al expediente GitHub existente el 13 octubre 2026. Las menciones a «local» describen su preparación anterior. Rige [la orientación R2/freeze/R3](PRINCIPIO_R2_FREEZE_R3_2026-10-13.md); los checks siguen siendo sintéticos y no un ensayo nativo. Volver a [CAMPAIGN](../CAMPAIGN.md) o [CONTINUATION](../CONTINUATION.md).

# Referencias para el estudio temporal de Flores

Fecha de consulta: 13 octubre 2026. 18 entradas: 11 trabajos/especificaciones externos y 7 anchors del problema y corpus. Solo fuentes primarias; el nivel de consulta identifica texto completo, pasajes focales o abstract. No equivalen a 18 reproducciones.

## R01 One or Two Things We Know about Concept Drift

Fabian Hinder, Valerie Vaquet, Barbara Hammer. 2023. [Fuente primaria](https://arxiv.org/abs/2310.15826).

**Consulta:** Abstract y metadatos primarios.

**Aplicación:** Taxonomía de drift y separación entre detección, localización y explicación. Orienta la elección de un canal observable y la comparación de métodos.

**Límite:** No se reproduce el benchmark del artículo ni se aplica su taxonomía automáticamente a una retirada de justificación.

## R02 Adversarial Attacks for Drift Detection

Fabian Hinder, Valerie Vaquet, Barbara Hammer. 2025. [Fuente primaria](https://arxiv.org/html/2411.16591v2).

**Consulta:** Texto primario §§2–3 y formulación de adversarios.

**Aplicación:** Muestra construcciones de cambios que evaden ciertos métodos de detección por selección de datos/métrica. Exige probar qué observa un detector concreto.

**Límite:** No demuestra invisibilidad frente a cualquier fuente externa ni superioridad EA. Sus distribuciones/ventanas difieren de este toy context witness.

## R03 Symbolic Runtime Verification for Monitoring under Uncertainties and Assumptions

Hannes Kallwies, Martin Leucker, César Sánchez. 2022. [Fuente primaria](https://arxiv.org/html/2207.05678v1).

**Consulta:** Texto primario accesible; abstract y secciones de formulación consultadas.

**Aplicación:** Competidor metodológico de monitoring con observación parcial y supuestos explícitos. Obliga a tratar el caso como restricción de inferencia en vez de etiqueta de fallo.

**Límite:** No ejecutamos su implementación ni trasladamos sus garantías a nuestro código. El acceso a HTML v3 falló; se usa v1 explícita.

## R04 Detecting and Correcting for Label Shift with Black Box Predictors

Zachary Lipton, Yu-Xiang Wang, Alexander Smola. 2018. [Fuente primaria](https://proceedings.mlr.press/v80/lipton18a.html).

**Consulta:** Abstract editorial primario y problem setup recuperado por búsqueda primaria.

**Aplicación:** Contraejemplo a una prohibición genérica de detectar shift sin labels: existen soluciones condicionadas a invariancias e invertibilidad. Mantener esos supuestos visibles.

**Límite:** Label shift no es automáticamente el context drift buscado. No importar p(x|y) invariante o confusion matrix invertible sin demostrarlo.

## R05 Failing Loudly An Empirical Study of Methods for Detecting Dataset Shift

Stephan Rabanser, Stephan Günnemann, Zachary C. Lipton. 2019. [Fuente primaria](https://papers.neurips.cc/paper_files/paper/2019/hash/846c260d715e5b854ffad5f70a516c88-Abstract.html).

**Consulta:** Abstract de proceedings y texto inicial del artículo consultados.

**Aplicación:** Referencia de detectores estadísticos fuertes que deben recibir crédito dentro de sus observaciones. Facilita distinguir tests de shift de tests de fundamento.

**Límite:** No reproducción oficial ni evidencia de eficacia en los seis jueces de Flores. No asignar a EA funciones de two-sample testing como novedad.

## R06 An Assumption Based TMS

Johan de Kleer. 1986. [Fuente primaria](https://dekleer.org/Publications/An%20Assumption-Based%20TMS.pdf).

**Consulta:** PDF original del autor, introducción y definición de contextos.

**Aplicación:** Precedente directo de conservar derivaciones por conjuntos de supuestos y reutilizar solo lo que sigue justificado. B2 puede usar esas técnicas.

**Límite:** No ejecución del ATMS original ni prueba de equivalencia de todos los perfiles EA. El código local solo hace joins y enumeración finita.

## R07 Defeaters and Eliminative Argumentation in Assurance 2.0

Robin Bloomfield, Kate Netkachova, John Rushby. 2024. [Fuente primaria](https://arxiv.org/html/2405.15800v1).

**Consulta:** Texto primario accesible y enfoque de defeaters consultado.

**Aplicación:** Estructura la autocrítica y el registro de razones que derrotan una derivación. Obliga a separar argumento, evidence y objeciones.

**Límite:** No convierte nuestro diseño en certificación ni hace independientes sus auditores. No utilizamos un cálculo de confianza de Assurance 2.0.

## R08 Using Models at Runtime to Address Assurance for Self Adaptive Systems

Betty H. C. Cheng y coautores. 2014. [Fuente primaria](https://arxiv.org/abs/1505.00903).

**Consulta:** Abstract y metadatos originales; arXiv 2015 del capítulo 2014.

**Aplicación:** La assurance puede necesitar mantenerse durante ejecución cuando entorno/sistema cambian. Sitúa la contribución como composición contextual, no idea nueva de runtime monitoring.

**Límite:** Consulta de resumen, no revisión completa de sus 36 páginas ni reproducción de casos.

## R09 How Do We Certify for the Unexpected

John Rushby. 2008. [Fuente primaria](https://www.sri.com/publication/information-computer-science-pubs/how-do-we-certify-for-the-unexpected/).

**Consulta:** Página y abstract primarios de SRI.

**Aplicación:** Precedente de trasladar parte de verification/assurance a runtime con claims/evidence/argument explícitos.

**Límite:** No base para afirmar certificación ni trasladar garantías aeronáuticas a esta propuesta.

## R10 PROV DM The PROV Data Model

W3C; editores Luc Moreau y Paolo Missier. 2013. [Fuente primaria](https://www.w3.org/TR/prov-dm/).

**Consulta:** Recomendación primaria; componentes y §5.1.8 invalidation.

**Aplicación:** Relations de provenance y temporalidad para construir el peer convencional. Invalidation diferencia persistencia de un objeto y disponibilidad para uso.

**Límite:** PROV modela provenance; no autentica factualidad ni por sí sola decide suficiencia de Q.

## R11 Remote ATtestation procedureS RATS Architecture RFC 9334

IETF. 2023. [Fuente primaria](https://www.rfc-editor.org/rfc/rfc9334.html).

**Consulta:** Arquitectura primaria; §10 freshness.

**Aplicación:** Evidence/attestation freshness y posible cambio después de evaluación. Exige valorar tiempo y consumo de result dentro de una política.

**Límite:** No implementamos RATS ni criptografía. La carrera temporal reconocida no prueba que todo relying party falle ni que EA la resuelva.

## R12 Planted Judge Demonstration Specification v1.0

Justin Philip Flores / Himalogic; fixture CTGT. 2026. [Fuente primaria](https://github.com/Himalogic/FG-TIDA-analysis/blob/07ac94fb100975bfff2e8ab0c644bd02ec87e537/planted-judge/README.md).

**Consulta:** README completo y expected.py completo leídos; copias locales derivadas.

**Aplicación:** Baseline exacto, propietario, límites, semántica y controles que se preservan.

**Límite:** Código expected no es resultado; original fixture ZIP no abierto/rehasheado y scripts nativos aún no disponibles en la carpeta consultada.

## R13 Observation Architecture and Identifiability

Olena Pavlenko. 2026. [Fuente primaria](https://github.com/FG-TIDA/themes/issues/21#issuecomment-5532364422).

**Consulta:** Comentario primario completo releído en esta conversación.

**Aplicación:** Orden de afirmación, arquitectura, identificación e incertidumbre; sustenta retornar al paso 3 ante cambio en paso 2.

**Límite:** Comentario mutable; no un artículo formal ni autorización de un ensayo. No identificar sus pasos con DDS stages.

## R14 Flores Boundary for Receiving Feedback

Justin Philip Flores. 2026. [Fuente primaria](https://github.com/FG-TIDA/themes/issues/21#issuecomment-5903046577).

**Consulta:** Comentario primario completo leído en esta conversación.

**Aplicación:** Insufficiency y named gap permitidos como propuesta de interface; no dirigir medición con desired answer/purpose/budget.

**Límite:** No aceptación de esta extensión temporal ni acuerdo de colaboración/coautoría.

## R15 DDS Stage A Challenge Trajectory Profile

IMSV / Tegrity.AI corpus. 2026. [Fuente primaria](https://github.com/dakleyer/structural-awareness-contributions/blob/fc90cdc78e8c593ddb848f988962e27b00f00c93/research/ecosystem-awareness/DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1.md).

**Consulta:** Texto actual recuperado; apartados de scope/admission/evidence consultados.

**Aplicación:** Objeto specification bajo Challenge y falsadores; no elevar preflight a arquitectura/producto.

**Límite:** Canonical working profile no es independent acceptance del nuevo estudio.

## R16 Canonical Requirements S1 to S14 and Conditions T1 to T4

IMSV / Tegrity.AI corpus. 2026. [Fuente primaria](https://github.com/dakleyer/structural-awareness-contributions/blob/fc90cdc78e8c593ddb848f988962e27b00f00c93/research/ecosystem-awareness/baseline/00_CANONICAL_REQUIREMENTS_CHALLENGES_SUFFICIENCY_HYPOTHESES_KPIS.md).

**Consulta:** Definiciones originales de requisitos seleccionados y T1–T4 leídas.

**Aplicación:** Mapping de obligaciones observability, indeterminacy, provenance, scope, authority y burden.

**Límite:** No crear nuevos IDs ni dar PASS a requisitos completos por un fixture parcial.

## R17 Canonical Architecture Benchmark and Reference Scenario Evidence 00D

IMSV / Tegrity.AI corpus. 2026. [Fuente primaria](https://github.com/dakleyer/structural-awareness-contributions/blob/fc90cdc78e8c593ddb848f988962e27b00f00c93/research/ecosystem-awareness/baseline/00D_CANONICAL_ARCHITECTURE_BENCHMARK_AND_REFERENCE_SCENARIO_EVIDENCE_v0.2.md).

**Consulta:** Contrato B2/B3 y fairness consultados; copia completa derivada.

**Aplicación:** B2 fuerte con igual evidence/resources y crédito pleno de equivalencia convencional.

**Límite:** No resultados comparativos del nuevo estudio ni universal gap de productos.

## R18 A B C D and Mathematical Plausibility 00M v0.8

IMSV / Tegrity.AI corpus. 2026. [Fuente primaria](https://github.com/dakleyer/structural-awareness-contributions/blob/fc90cdc78e8c593ddb848f988962e27b00f00c93/research/ecosystem-awareness/baseline/00M_ABCD_AND_MATHEMATICAL_PLAUSIBILITY_v0.8_RESEARCH_NOTE.md).

**Consulta:** Semántica y UNKNOWN leídos; copia derivada completa.

**Aplicación:** Separar pérdida de justificación de clasificación automática C o D; especificar proceso/aspecto.

**Límite:** Plausibilidad conceptual no prueba engineering feasibility o eficacia.

## Selección de competidores

Los competidores más próximos son monitor simbólico con supuestos, truth maintenance/ATMS, y un relying party convencional con provenance/freshness. Two-sample drift detection es una referencia estadística útil cuando cambia el canal observado. No se presenta un simple detector de votes como un peer completo de la especificación contextual.

## Derechos y reproducción

Las citas son breves y las anotaciones son síntesis propias. Los originales permanecen en los sitios de sus autores. No se distribuyen PDFs ajenos ni se atribuye permiso de código/datos por el acceso al abstract. Las copias de source-snapshots son textos de los repositorios del problema y no garantizan identidad binaria de attachments CTGT o ZIP históricos. Antes de reproducción oficial revisar versión, licencia, datos y comandos del autor.

