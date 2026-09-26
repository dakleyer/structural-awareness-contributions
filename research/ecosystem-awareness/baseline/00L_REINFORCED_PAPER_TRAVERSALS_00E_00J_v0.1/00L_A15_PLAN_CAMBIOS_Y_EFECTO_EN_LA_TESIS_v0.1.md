# Plan de cambios y efecto en la tesis del artículo

26 de septiembre de 2026 · Propuesta para aplicación conjunta

## 1 Qué significan las correcciones

**Los hallazgos no refutan la tesis central del artículo ni obligan a sustituir nuestra propuesta arquitectónica. Sí reducen el alcance de algunas afirmaciones de demostración y validación. No sería preciso describir todo como correcciones menores.**

La tesis central sostiene que una identidad válida, una autorización local y un registro completo pueden coexistir con una decisión conjunta injustificada cuando cambian la evidencia, la autoridad, las dependencias o el contexto. Las correcciones no muestran que esa posibilidad desaparezca. Los escenarios y requisitos siguen siendo una forma de identificar qué debe conservar una decisión y cuándo debe recualificarse. Eso no equivale a demostrar que una implementación concreta lo consigue siempre.

La propuesta EA sigue siendo una hipótesis de implementación y un marco de referencia. La auditoría no establece su superioridad frente a una buena implementación convencional. Tampoco la refuta: esa comparación independiente, bajo cambios de contexto y recursos equiparables, sigue pendiente.

| Capa de la tesis | Efecto de la auditoría | Consecuencia para el artículo |
|---|---|---|
| Problema central y método de requisitos | No se ha encontrado aquí una refutación del problema. | Mantener la tesis y los seis casos construidos. |
| Código e instrumentación | Había fallos reales, algunos relevantes para autorización y conservación de evidencia. | Explicar las correcciones y citar las nuevas pruebas. |
| Demostración formal | A22 tiene un puente semántico pendiente; A23 conserva resultados parciales. | Acotar qué está demostrado y qué sigue abierto. |
| Diferencial de EA | Los pares con lógica compartida no lo miden. | Mantenerlo como hipótesis comparativa falsable. |
| Marco de referencia de la Parte II | No se ha demostrado que requiera cambiar sus capas o responsabilidades. | Actualizar referencias de evidencia sin rediseñar la arquitectura. |

**La distinción decisiva:** si nuestra tesis es que hace falta preservar la justificación de las decisiones y hacer comprobables los requisitos, se mantiene como propuesta apoyada por los casos y los argumentos acotados. Si se interpreta como que ya demostramos suficiencia general de los seis principios, eficacia en productos o superioridad de EA, esa interpretación debe retirarse. La edición actual ya descarta varias de esas lecturas excesivas.

## 2 Base y regla de conservación

Artículo revisado para este plan: *When_the_Controls_Work_but_the_System_Fails_Parts_I_II.docx*, versión 2, 20 páginas. Repositorio comprobado: `96b46436dc45e1bee1879bd05242c16ff4801061`; correcciones de código: `3cf10a670093fd8f71b32371440266914f5d2ca3`.

La Parte I está congelada. El plan propone una **nota de actualización de evidencia fuera de la Parte I**, después de la Parte II, con referencias a las secciones afectadas. No se sustituirán ni resumirán párrafos de la parte congelada. Las correcciones en línea que se identifiquen quedarán preparadas para una edición posterior expresamente abierta a revisión.

<!-- PAGEBREAK -->

## 3 Lo que ya está corregido

Estas tareas ya se aplicaron en GitHub. No deben volver a presentarse como trabajo pendiente ni como resultados de productos.

| Grupo corregido | Qué significa en términos prácticos |
|---|---|
| Traspasos y trazas de fallo | La información se contrasta con una copia previa; un candidato que falla deja evidencia. También se conserva un diagnóstico si su salida no admite serialización. |
| Métricas y recursos | Se cuentan los campos realmente conservados y se validan tipos, límites y pasos simbólicos. No se mide latencia o consumo real de tokens. |
| Campañas y vigencia | Una segunda campaña no oculta las obligaciones de la primera. Se comprueba la autoridad de cada acción, su ámbito y su vigencia al actuar. |
| Peers y entradas | Se comprueban procedencia, marco autorizado, evidencia cualificada y campos materiales presentes. Dos ausencias no acreditan vigencia. |
| Evaluación emparejada | Cada brazo se puntúa frente al resultado esperado. El acuerdo entre brazos se registra, pero no sirve por sí mismo como oráculo. |
| Fin de búsqueda | Tres evidencias con capacidad seis terminan el stream; no demuestran agotamiento de seis pasos. |
| Integridad de documentos | Se detectan etiquetas de escenario incorrectas y cobertura vacía. Sigue siendo control estructural, no prueba de completitud semántica. |

**Evidencia publicada:** las 379 regresiones anteriores pasan sin cambiar sus aserciones; también pasan 77 comprobaciones adicionales. Sobre el código anterior, esas mismas 77 comprobaciones producen 65 fallos y 12 pases. Algunos fallos constatan contratos o APIs nuevos: no son 65 defectos independientes. Los cinco workflows del commit de correcciones terminaron correctamente.

A14 conserva el mapa de las 20 observaciones: 18 comportamientos corregidos y dos cuestiones formales con aclaración de alcance, todavía abiertas. A11 y el run original Stage-0 permanecen como evidencia histórica; las salidas corregidas tienen referencias propias.

## 4 Cambios que se pueden aplicar juntos ahora

**P01 — Actualización editorial.** Añadir la nota propuesta en §7 de este plan al final del artículo; incorporar enlaces al registro A12, auditoría A13, correcciones 00L-A14, pruebas y commit. Actualizar en la Parte II únicamente el enlace y la frase que remite a la instrumentación ejecutada. Mantener el resto del texto.

**P02 — Coherencia documental.** Comprobar README, mapa de pruebas y notas canónicas para que distingan resultados históricos de actuales. Añadir solo los enlaces o precisiones que falten: los seis originales y los README ya enlazan las correcciones. Utilizar nombres completos como **00K-A14** y **00L-A14**, porque son documentos distintos.

**P03 — Cierre de entrega.** Añadir a A12 una entrada con archivos afectados, fuente del artículo, identificadores de versión, pruebas, cambios propuestos frente a aplicados y pendientes. Publicar el conjunto documental en un único commit y una única nueva versión del Word, después de verificar su conservación.

Este bloque no necesita esperar a que A22/A23 queden resueltos. Su función es describir con precisión el conocimiento disponible.

<!-- PAGEBREAK -->

## 5 Plan para cerrar las cuestiones formales

### F01 Completar o acotar el puente de A22

**Dónde:** 00K-A20, 00K-A22 y `fixtures/00K-FORMAL/full-cube`.

**Problema:** las 64 firmas y el argumento de conteo se reproducen en el modelo simplificado. El programa no comprueba todavía que cada construcción corresponda a un modelo de toda la teoría de coherencia B1–B11 de A20. Faltan, entre otras relaciones, el conflicto derivado de registros, el proceso de indagación y la autoridad sin amplificación.

**Trabajo propuesto:**

1. Fijar la correspondencia entre los objetos de A20 y los campos del programa, indicando qué se conserva y qué se abstrae.
2. Derivar el conflicto material de registros actuales usados por la decisión, representar el proceso de búsqueda y su presupuesto o función de descenso, y representar el grant con su límite de no amplificación.
3. Comprobar B1–B11 mediante condiciones separadas de los predicados P1–P6. Para cada firma, verificar primero la coherencia del modelo y después calcular su firma; no usar la firma deseada para declarar válida la coherencia.
4. Conservar testigos, contraejemplos y mutaciones que violen cada condición. Explicar por qué la traducción del texto a esas condiciones es fiel.

**Criterio de cierre:** un puente explícito que preserve las propiedades utilizadas y testigos coherentes para las 64 firmas. Si no se consigue, se conserva el resultado del modelo simplificado y se limita la afirmación sobre el sustrato completo. No se modifica una definición para recuperar artificialmente el número 64. El límite de seis bits sigue siendo válido para 64 estados distinguibles; su aplicación al sustrato completo depende del puente.

### F02 Revisar la fidelidad semántica de A23

**Dónde:** 00K-A23, `requirement-sufficiency`, su mapa de cláusulas y Requirements-vNext.

**Problema:** el guard descarta ciertos atajos en cada cláusula. No establece por sí solo que el conjunto de cláusulas sea una traducción fiel y no circular del canon. La equivalencia final con un principio puede ser legítima si está derivada correctamente; no debe prohibirse solo por ser equivalencia.

**Trabajo propuesto:**

1. Mantener el certificado actual y trazar cada cláusula desde el texto canónico hasta el estado, la transición y la obligación observable que representa.
2. Para **P3**, distinguir actuar sobre una premisa material no resuelta de ejecutar una respuesta autorizada a esa incertidumbre.
3. Para **P5**, distinguir detectar o registrar un cambio de hacer efectiva la revalidación, cancelación o autorización correspondiente antes de actuar. Comprobar si la ruta canónica ya exige ese efecto.
4. Para **P6**, distinguir evidencia correlacionada correctamente cualificada de su promoción indebida a corroboración independiente.
5. Comprobar alcanzabilidad de los contraejemplos y fidelidad de P1/P2/P4, sin tratar sus proyecciones finitas como equivalencia completa con el canon.

**Criterio de cierre:** clasificar cada caso como error de traducción, estado no alcanzable bajo una condición canónica justificada, obligación de implementación no representada o carencia real del canon. Solo esta última justificaría una propuesta de cambio de requisitos. No adoptar S15/T5/H7 ni eliminar contraejemplos para obtener un resultado verde. La revisión semántica separada debe quedar identificada; otra ejecución del mismo modelo no equivale a revisión externa independiente.

<!-- PAGEBREAK -->

## 6 Mapa de cambios del artículo

Las ubicaciones siguientes corresponden a la versión 2 revisada. Las páginas orientan; las frases y los títulos son los anclajes estables. Mientras siga congelada la Parte I, las precisiones se incorporarán en la nota final, identificando su sección original.

| ID y ubicación | Cambio concreto | Efecto sobre la tesis |
|---|---|---|
| E01 Parte I §2, p 4, “R2/V11 tests the latter” | Identificar R2/V11 como diseño pendiente de ejecución; conservar sus condiciones de comparación. | Precisa el estado de evidencia. |
| E02 Parte I §6, pp 9–10, “The 00L verifier requires equality” | Identificar esa igualdad como condición histórica. El runner corregido puntúa cada brazo frente al oráculo y conserva desacuerdos. | Corrige la metodología descrita. |
| E03 Parte I §6, 00E, p 8 | Añadir que el stream termina antes de consumir la capacidad declarada; no inferir ahorro o agotamiento de recursos. | Retira una interpretación puntual no medida. |
| E04 Parte I §6, 00H, p 9; §8, p 13 | Enlazar controles de campañas mixtas, scope y vigencia. Mantener la independencia de Branch I como hecho estipulado. | Refuerza el fixture; no garantiza todas las extensiones. |
| E05 Parte I §7, p 11, “The full-cube result realizes all 64” | Precisar que corresponde al modelo simplificado; el puente a B1–B11 sigue pendiente. | Limita una afirmación formal importante. |
| E06 Parte I §§4 y 7, pp 6–7 y 11–12 | Conservar P1/P2/P4 como resultados parciales. Añadir el alcance por cláusula del guard y la revisión de P3/P5/P6. | Mantiene abierta la suficiencia general. |
| E07 Parte I §9, p 14, “Stage-0 execution update” | Separar el run histórico del posterior con detector, métricas y trazas corregidos. No convertir el segundo en ejecución prospectivamente prerregistrada. | Corrige qué instrumentación quedó comprobada. |
| E08 Parte I §10 y apéndice, pp 15–18 | Extender el índice a A13/00L-A14 y separar 379 regresiones de 77 comprobaciones nuevas. Conservar citas históricas. | Actualiza trazabilidad y cuentas. |
| E09 Parte II, p 20, “Some of this is already runnable” | Añadir un enlace a 00L-A14 y a la nota final. Mantener que compartir lógica no prueba paridad entre arquitecturas. | No modifica las capas ni las responsabilidades. |

**Ya correctamente acotado en el artículo:** los casos son construidos; los productos no están ejecutados; los comparadores comparten lógica; A23 no cierra las seis implicaciones; A25/A26 requieren una garantía base independiente para transferir una garantía. No hace falta reescribir esas explicaciones ni añadir advertencias repetidas.

**A19, A20, A21, A24, A25 y A26:** revisar las referencias que dependan de una afirmación más fuerte de A22/A23. Mantener la trazabilidad y los resultados que no dependan de ella. No declarar toda la cadena invalidada, ni concluir que toda la cadena queda confirmada porque las pruebas de regresión pasan.

<!-- PAGEBREAK -->

## 7 Texto propuesto para la nota de actualización

El siguiente texto se añadiría **fuera de la Parte I congelada**. Su ubicación propuesta es después de la Parte II. Los anclajes remiten a las secciones originales y permiten leerlas sin confundir los resultados históricos con el estado actual.

### Evidence update following the adversarial audit

The argument in Part I remains that locally valid controls may fail to preserve the justification of a combined decision after material change. The subsequent audit corrected the supporting test implementations and narrowed several claims about what their results establish. These changes do not establish product effectiveness, universal sufficiency or an EA-specific comparative advantage.

For Sections 6 and 9, the correction commit preserves the original 379 symbolic regression assertions and adds 77 separate correction checks. All pass. Handoff checks now compare received information with a pre-adapter snapshot; failed candidates, runtime errors and invalid trace values retain diagnostic records. Residual preservation is counted by field, and symbolic costs are checked against event steps and declared limits. Mixed-campaign authority, action-time validity, peer scope and input validation have also been corrected. These are bounded implementation and instrumentation results.

The 00L equality condition described in Section 6 belongs to the historical verifier. The corrected replay scores each arm against the declared expected disposition and retains disagreements. The short negative 00E stream ends after three evidence steps with capacity six; it therefore does not demonstrate resource exhaustion or an efficiency advantage. Shared-logic peers remain regression controls rather than independent architectural comparators.

For Section 7, A22 realizes 64 signatures in its simplified executable model. The counting argument remains valid for 64 distinguishable signatures; applying that result to the full A20 background theory requires the still-open semantic bridge. A23 retains finite-projection implications for P1/P2/P4 and countermodels under semantic review for P3/P5/P6. Its clause-local guard does not by itself establish the source fidelity or non-circularity of the complete bundle. Those countermodels do not automatically establish defects in the canonical requirements.

R2/V11 in Section 2 remains a proposed drift test, with execution pending. The corrected Stage-0 replay is a post-audit instrumentation revision, distinct from the historical preregistered execution. A12, A13 and 00L-A14 identify the versions, corrections, traces and remaining obligations. Independently implemented matched candidates are still needed to test the proposed EA benefit under regime change and comparable decision burden.

**Referencias para enlazar en la nota:** [A12 registro acumulativo](https://github.com/dakleyer/structural-awareness-contributions/blob/96b46436dc45e1bee1879bd05242c16ff4801061/research/ecosystem-awareness/baseline/00L_REINFORCED_PAPER_TRAVERSALS_00E_00J_v0.1/00L_A12_REGISTRO_MEJORAS_ARTICULO_README_v0.1.md), [A13 auditoría](https://github.com/dakleyer/structural-awareness-contributions/blob/96b46436dc45e1bee1879bd05242c16ff4801061/research/ecosystem-awareness/baseline/00L_REINFORCED_PAPER_TRAVERSALS_00E_00J_v0.1/00L_A13_AUDITORIA_TRANSVERSAL_PRUEBAS_v0.1.md), [00L A14 correcciones](https://github.com/dakleyer/structural-awareness-contributions/blob/96b46436dc45e1bee1879bd05242c16ff4801061/research/ecosystem-awareness/baseline/00L_REINFORCED_PAPER_TRAVERSALS_00E_00J_v0.1/00L_A14_CORRECCIONES_AUDITORIA_v0.1.md) y [commit de código y pruebas](https://github.com/dakleyer/structural-awareness-contributions/commit/3cf10a670093fd8f71b32371440266914f5d2ca3).

**Frase mínima para la Parte II:** “The subsequent correction record and evidence update distinguish the historical runs from the corrected instrumentation and its remaining validation limits.” Enlazar “correction record” con 00L-A14 y “evidence update” con la nota final del artículo.

<!-- PAGEBREAK -->

## 8 Aplicación conjunta y criterio de cierre

### Orden de aplicación

1. Fijar la versión del artículo y el commit del repositorio al iniciar la edición. Si hay trabajo paralelo, conservarlo e integrar únicamente los cambios de este plan que sigan siendo necesarios.
2. Preparar en una misma revisión P01–P03 y E01–E09: nota final, enlace mínimo en Parte II y referencias documentales. No ejecutar de nuevo las 18 correcciones ya publicadas.
3. Verificar que toda la Parte I, incluidos sus vínculos y su apéndice, permanece intacta. Comparar texto y estructura del documento, no solo contar párrafos. Revisar visualmente el Word completo.
4. Comprobar enlaces y cuentas; distinguir 00K-A14 de 00L-A14, resultados locales de CI y runs históricos de corregidos. No sumar las distintas familias como ensayos independientes.
5. Publicar una nueva versión del Word y un commit documental con A12 actualizado. El artículo debe enlazar la revisión exacta que describe.
6. Trabajar F01/F02 como un bloque formal separado, manteniendo el estado abierto hasta disponer de su evidencia. Cuando esté resuelto o delimitado, trasladar el resultado real al artículo y a las dependencias, sin anticipar un cierre favorable.

### Qué debe quedar pendiente de forma explícita

La comparación con candidatos independientes; el diferencial de EA bajo deriva; la ejecución R2/V11; la eficacia y el coste a escala de producto; el puente formal A22 y la fidelidad/alcanzabilidad de A23. El texto del plan no convierte ninguno de estos puntos en resultado ejecutado.

### Cuándo cambiaría realmente nuestra tesis

Habría una revisión sustantiva si se demostrara que una obligación propuesta no es necesaria en el alcance declarado, que S1–S14 admiten una actuación que viola su finalidad aun cumpliéndose fielmente, o que las distinciones del marco no pueden observarse ni mantenerse con recursos viables. Un peer convencional que iguala o mejora a EA limitaría el diferencial de EA en ese alcance, sin eliminar por ello el problema ni el valor de requisitos neutrales.

Los hallazgos actuales todavía no establecen esas conclusiones. Sí muestran que una regresión verde puede convivir con supuestos insuficientemente comprobados. El valor de la corrección es que ahora cada afirmación tiene un alcance y una evidencia más claros para investigadores, implementadores y revisores.

## 9 Fuentes de trabajo

- [A12 y constancia de cinco workflows correctos](https://github.com/dakleyer/structural-awareness-contributions/blob/96b46436dc45e1bee1879bd05242c16ff4801061/research/ecosystem-awareness/baseline/00L_REINFORCED_PAPER_TRAVERSALS_00E_00J_v0.1/00L_A12_REGISTRO_MEJORAS_ARTICULO_README_v0.1.md).
- [A14 y matriz de hallazgos corregidos y abiertos](https://github.com/dakleyer/structural-awareness-contributions/blob/96b46436dc45e1bee1879bd05242c16ff4801061/research/ecosystem-awareness/baseline/00L_REINFORCED_PAPER_TRAVERSALS_00E_00J_v0.1/00L_A14_CORRECCIONES_AUDITORIA_v0.1.md).
- [A20 y restricciones B1–B11](https://github.com/dakleyer/structural-awareness-contributions/blob/96b46436dc45e1bee1879bd05242c16ff4801061/research/ecosystem-awareness/baseline/00K_A20_SHARED_SUBSTRATE_MATHEMATICAL_INDEPENDENCE_P1_P6_v0.1.md).
- [A22 y límite del modelo simplificado](https://github.com/dakleyer/structural-awareness-contributions/blob/96b46436dc45e1bee1879bd05242c16ff4801061/research/ecosystem-awareness/baseline/00K_A22_FULL_CUBE_BOOLEAN_DIAGNOSTIC_MINIMALITY_v0.1.md).
- [A23 y revisión de las cláusulas](https://github.com/dakleyer/structural-awareness-contributions/blob/96b46436dc45e1bee1879bd05242c16ff4801061/research/ecosystem-awareness/baseline/fixtures/00K-FORMAL/requirement-sufficiency/CLAUSE_AUDIT.md).
- Artículo *When_the_Controls_Work_but_the_System_Fails_Parts_I_II.docx*, versión 2, consultado completo. Este plan no modifica ese archivo ni las demostraciones.
