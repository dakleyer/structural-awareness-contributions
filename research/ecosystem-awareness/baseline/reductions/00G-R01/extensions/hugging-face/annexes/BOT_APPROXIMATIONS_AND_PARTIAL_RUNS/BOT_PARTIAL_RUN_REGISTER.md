# BOT-PARTIAL-RUN — registro de todas las generaciones conservadas

**12 de octubre de 2026, cinco generaciones de una misma exploración escrita/evaluada por GPT-6.** Nada de esta lista es una reproducción de los agentes históricos ni un conjunto de evaluaciones independientes por modelos diferentes.

| Alias inequívoco | Fuentes originales preservadas | Hallazgo/limitación |
|---|---|---|
| **BOT-PARTIAL-RUN v0.2** | [Código](../../review-2026-10-11/traversals/first-channel-counterfactual-v0.2/run.py) · [Datos/informe](../../review-2026-10-11/traversals/first-channel-counterfactual-v0.2/results.json) | 16 × 5 = 80 locales; 10 grafos. Primera aproximación: error por confundir verdad del propietario UNKNOWN con infracción establecida. |
| **BOT-PARTIAL-RUN v0.3** | [Código](../../review-2026-10-11/traversals/first-channel-counterfactual-v0.3/run.py) · [Datos/informe](../../review-2026-10-11/traversals/first-channel-counterfactual-v0.3/README.md) | 18 × 7 = 126 locales; 10 grafos. Corrige ese error y añade comparador fuerte; nativo fuerte y nativo fuerte+EA obtienen 2/2 efectos indebidos estipulados. |
| **BOT-PARTIAL-RUN v0.4** | [Código](../../review-2026-10-11/traversals/first-channel-counterfactual-v0.4/run.py) · [Datos/informe](../../review-2026-10-11/traversals/first-channel-counterfactual-v0.4/README.md) | 26 × 7 = 182 locales; 63 grafos. R1/R2/R3, órdenes alternativos, human escalation y señalización; nativo adaptativo y EA comparten disparador y empatan por diseño. |
| **BOT-PARTIAL-RUN v0.5** | [Código](../../review-2026-10-11/traversals/first-channel-counterfactual-v0.5/run.py) · [Datos/informe](../../review-2026-10-11/traversals/first-channel-counterfactual-v0.5/README.md) | 28 × 9 = 252 locales. Configuración del detector cambia/UNKNOWN; EA y monitor convencional comparten diagnóstico, paridad 7/7 no es comparación algorítmica separada. |
| **BOT-PARTIAL-RUN v0.6** | [Código](../../review-2026-10-11/traversals/first-channel-counterfactual-v0.6/run.py) · [Datos/informe](../../review-2026-10-11/traversals/first-channel-counterfactual-v0.6/README.md) | 30 × 10 = 300 locales. Algoritmos separados pero un mismo bot autor/evaluador: EA meta-local 8, nativo fuerte assurance 7, fail-safe 1 con 2 acciones legítimas retenidas. |

**Línea de corrección, no revisión retrospectiva de resultados:**

- **v0.2→v0.3:** se corrigió la confusión entre permiso `UNKNOWN` y prohibición probada mediante un evaluador que distingue verdad del propietario y creencia del agente.
- **v0.4:** añadió R1/R2/R3, variantes de orden, human escalation y EHD condicionado. Su paridad entre detector adaptativo y EA no discrimina algoritmos porque comparten un disparador.
- **v0.5:** incorporó parámetros y clasificaciones del detector en estado `UNKNOWN`; los dos sistemas compartían la primitiva para diagnosticar el problema, limitando la conclusión 7/7.
- **v0.6:** separa los mecanismos, pero **no autores ni oráculos**. EA meta-local (8 efectos denegados) no domina nativo fuerte con assurance (7). Fail-safe (1) sacrifica dos operaciones legítimas; no hay prueba T4 basada en latencia/coste real.

La [v0.6](../../review-2026-10-11/traversals/first-channel-counterfactual-v0.6/README.md) es la aproximación técnica más reciente, **no un resultado científico más autorizado** que v0.2–v0.5 ni un motivo para eliminar sus fallos. El [bot auto-run reproducible](BOT_AUTORUN.md) verifica que los scripts produzcan sus propios archivos al ejecutarse sin cambiar los originales.

### Casos que siguen abiertos

Autoconocimiento de EA exige observación fiable de la propia clasificación: un monitor sin iniciar, invalidado silenciosamente o incapaz de observar el cambio no se salva emitiendo `UNKNOWN`. La emisión de EHD, si existe, debe estar autorizada para cada receptor/finalidad/contenido. Las dudas correlacionadas no se convierten por repetición en corroboración independiente. Los controles convencionales capaces de realizar el mismo diagnóstico reciben todo el crédito.

[Volver al anexo](README.md).
