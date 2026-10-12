# Anexo — aproximaciones de bots, pruebas parciales y discusiones

**12 de octubre de 2026 · índice auxiliar de la extensión Hugging Face / R01.** No se han desplazado, eliminado, renombrado ni modificado los originales. Este es el **punto único nuevo de entrada** a las pruebas exploratorias desde el README de Hugging Face. Un nombre de catálogo `BOT-APPROX` identifica una *aproximación*, no un resultado validado.

El caso científico original sigue en [R01 → Hugging Face](../../README.md). Los documentos con requisitos, evidencia histórica y la especificación de DDS mantienen autoría, versiones y procedimientos distintos de los registros de bots.

## Qué puede leerse, y cómo

[BOT-APPROX — revisiones documentales, identidad de los bots y críticas de autor no verificado](BOT_APPROX_REVIEW_REGISTER.md) · [BOT-PARTIAL-RUN — versiones v0.2–v0.6 y sus falsaciones/correcciones](BOT_PARTIAL_RUN_REGISTER.md) · [BOT-AUTORUN — repetición automática reproducible, no peer review](BOT_AUTORUN.md) · [BOT-REVIEW-QUEUE — trabajos para un futuro evaluador humano o bot realmente independiente](BOT_INDEPENDENT_REVIEW_QUEUE.md) · [Catálogo íntegro de archivos originales y hashes Git de referencia](BOT_BLOB_MANIFEST.json).

### Recorridos ya efectuados por el mismo bot

| Nombre de catálogo | Casos estipulados | Estado de la inferencia |
|---|---|---|
| [BOT-PARTIAL-RUN v0.2](../../review-2026-10-11/traversals/first-channel-counterfactual-v0.2/run.py) | 16 × 5 = 80 locales; 10 grafos | Primera aproximación: error por confundir verdad del propietario UNKNOWN con infracción establecida. |
| [BOT-PARTIAL-RUN v0.3](../../review-2026-10-11/traversals/first-channel-counterfactual-v0.3/README.md) | 18 × 7 = 126 locales; 10 grafos | Corrige ese error y añade comparador fuerte; nativo fuerte y nativo fuerte+EA obtienen 2/2 efectos indebidos estipulados. |
| [BOT-PARTIAL-RUN v0.4](../../review-2026-10-11/traversals/first-channel-counterfactual-v0.4/README.md) | 26 × 7 = 182 locales; 63 grafos | R1/R2/R3, órdenes alternativos, human escalation y señalización; nativo adaptativo y EA comparten disparador y empatan por diseño. |
| [BOT-PARTIAL-RUN v0.5](../../review-2026-10-11/traversals/first-channel-counterfactual-v0.5/README.md) | 28 × 9 = 252 locales | Configuración del detector cambia/UNKNOWN; EA y monitor convencional comparten diagnóstico, paridad 7/7 no es comparación algorítmica separada. |
| [BOT-PARTIAL-RUN v0.6](../../review-2026-10-11/traversals/first-channel-counterfactual-v0.6/README.md) | 30 × 10 = 300 locales | Algoritmos separados pero un mismo bot autor/evaluador: EA meta-local 8, nativo fuerte assurance 7, fail-safe 1 con 2 acciones legítimas retenidas. |

**Conclusión admisible hasta hoy:** en v0.6 un mecanismo EA de autocalificación puede representar `QUALIFICATION_NOT_ESTABLISHED` cuando una fuente apropiada permite saber que su propia clasificación ha perdido fundamento. **No se demuestra inmunidad** frente a un observador parado, un cambio invisible o una mala política. El comparador convencional fuerte del mismo conjunto obtiene 7 efectos adversos frente a 8 del EA meta-local; el fail-safe deja más trabajo legítimo sin realizar. Son conteos de un *modelo determinista ideado por ChatGPT GPT-6*, no tasas de fallo de Hugging Face ni Stage A/B/C acreditados.

### Estudios anteriores relacionados, sin renombrarlos «bot review»

La [matriz de estudios anteriores](../../review-2026-10-11/EVIDENCE_MATRIX.md) conserva los ensayos HF C3/oráculo, EA v0.1/v0.2, el nativo 8/8 frente a EA 7/8, cached-lineage, Casbin, estudios probabilísticos/sociales, 00K, R01 y los contraejemplos. **No se suman sus denominadores**, ni estos ensayos originales cambian de estatus por vincularlos aquí.

### Ceguera, preservación e independencia

[Stage A v0.3, material ciego congelado](../../review-2026-10-11/blind/START_HERE.md): un revisor no expuesto debe leer solo su paquete, **no este anexo** hasta sellar sus conclusiones. Las críticas de 8 octubre no tienen auditor original autenticado; no atribuimos un nombre/modelo sin evidencia. Los ensayos v0.2–v0.6 son **una única línea de trabajo asistida por GPT-6**, aunque se cambien los algoritmos; no cinco auditorías independientes.

Los archivos originales siguen exactamente en `review-2026-10-11/` y sus `traversals/`, así como los resultados anteriores enlazados desde la extensión. La capa de presentación cambia, no su trazabilidad, sus resultados negativos o el contrato S1–S14/T1–T4. El resultado del CI es solo *reproducción técnica de código escrito y evaluado por el mismo bot*.

[VNext del README original — revisión y modificación de navegación](../../README_VNext.md).
