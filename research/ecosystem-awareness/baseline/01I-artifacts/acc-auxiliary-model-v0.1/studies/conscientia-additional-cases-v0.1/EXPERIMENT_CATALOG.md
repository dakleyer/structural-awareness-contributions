# EXPERIMENT_CATALOG — catálogo histórico de 46 ejemplos sintéticos ejecutables

**Estatus: EJEMPLOS / FIXTURES SINTÉTICOS, NO EXPERIMENTOS EMPÍRICOS.** Se conserva el nombre histórico del archivo para no romper enlaces. Ninguna cifra pertenece a una empresa, familia, ciudad, persona o agente productivo real. La familia KL supone distribuciones uniformes sobre soportes finitos; consultar las condiciones de evidencia en [README.md](README.md).

| ID | Fuente | Pregunta del caso (etiqueta ilustrativa) | Resultado reproducido |
|---|---|---|---|
| `BAN-01-LOCAL-VS-WASTE` | CE1 | Ban 01 Local Vs Waste | `WEAK_PARETO_RESOURCE_SERVICE_GAIN` |
| `BAN-02-TRANSPORT-NO-FREE-LUNCH` | CE1 | Ban 02 Transport No Free Lunch | `TRADEOFF_NOT_PARETO_CERTIFIED` |
| `BAN-03-LEGITIMATE-DONATION` | CE1 | Ban 03 Legitimate Donation | `WEAK_PARETO_RESOURCE_SERVICE_GAIN` |
| `BAN-04-WITHHELD-CONSENT` | CE1 | Ban 04 Withheld Consent | `RIGHTS_BLOCKED` |
| `BAN-05-NO-COORDINATION-CAPACITY` | CE1 | Ban 05 No Coordination Capacity | `COORDINATION_BLOCKED` |
| `ROBIN-01-SMALL-GAIN-LARGE-SHARE` | CE1 | Robin 01 Small Gain Large Share | `RELATIVE_CREDIT_FEASIBLE` (credit_shortfall=0) |
| `ROBIN-02-RELATIVE-CREDIT-HARD-CONSTRAINT` | CE1 | Robin 02 Relative Credit Hard Constraint | `RELATIVE_CREDIT_IMPOSSIBLE` (credit_shortfall=1.0) |
| `ROBIN-03-CREDIT-FEASIBLE` | CE1 | Robin 03 Credit Feasible | `RELATIVE_CREDIT_FEASIBLE` (credit_shortfall=0) |
| `MIN-01-COORDINATION-REORG` | CE1 | Min 01 Coordination Reorg | `WEAK_PARETO_RESOURCE_SERVICE_GAIN` |
| `MIN-02-SAME-REORG-OVER-CAPACITY` | CE1 | Min 02 Same Reorg Over Capacity | `COORDINATION_BLOCKED` |
| `MIN-03-RIGHTS-BLOCK-REORG` | CE4 | Min 03 Rights Block Reorg | `RIGHTS_BLOCKED` |
| `UTIL-01-APPLES-MARKET-THRESHOLD` | CE11 | Util 01 Apples Market Threshold | `LOCAL_MONOTONE_STOP_BELOW_BETTER_STATE` |
| `EFF-01-TWO-HORIZONS-OPTIMUM` | CE1 | Eff 01 Two Horizons Optimum | `GAPS_ESTABLISHED_IN_TOY` |
| `EFF-02-UNATTAINABLE-IDEAL` | CE4 | Eff 02 Unattainable Ideal | `OPTIMUM_NOT_ESTABLISHED` |
| `WELFARE-01-DOUBLE-BANANA` | CE1 | Welfare 01 Double Banana | `HYPOTHETICAL_NET_NEGATIVE` (net_welfare_toy=-2.0) |
| `WELFARE-02-LESS-DISCOMFORT` | CE1 | Welfare 02 Less Discomfort | `HYPOTHETICAL_NET_NONNEGATIVE` (net_welfare_toy=2.0) |
| `WELFARE-03-DONT-EQUATE-TO-SUFFERING` | CE2 | Welfare 03 Dont Equate To Suffering | `SUBJECTIVE_NOT_MEASURED` |
| `HID-01-HUMAN-ROLE-TRANSITION` | CE10 | Hid 01 Human Role Transition | `HUMAN_INPUT_DIFF_NOT_OBSERVED_HID` (ACW_delta=20) |
| `HID-02-NO-SAME-SERVICE` | CE10 | Hid 02 No Same Service | `MATCHED_REFERENCE_MISSING` |
| `HID-03-NEO-NOT-DEBT` | CE10 | Hid 03 Neo Not Debt | `HUMAN_INPUT_DIFF_NOT_OBSERVED_HID` (ACW_delta=0) |
| `ENTROPY-01-MULTI-PREIMAGE` | CE6 | Entropy 01 Multi Preimage | `FINITE_SHANNON_ONLY` (conditional_answer_bits=1.0) |
| `ENTROPY-02-QUESTION-SUFFICES` | CE11 | Entropy 02 Question Suffices | `FINITE_SHANNON_ONLY` (conditional_answer_bits=0.0) |
| `ENTROPY-03-SKEWED-PRIOR` | CE6 | Entropy 03 Skewed Prior | `FINITE_SHANNON_ONLY` (conditional_answer_bits=0.19439186) |
| `ENTROPY-04-OPEN-D-NO-PRIOR` | CE7 | Entropy 04 Open D No Prior | `PRIOR_NOT_IDENTIFIED` |
| `KL-01-CORRECT-REVERSE` | CE7 | Kl 01 Correct Reverse | `FINITE_SUPPORT_DIRECTION_CORRECTED` (coverage_delta_bits=1.0) |
| `KL-02-NO-SUPPORT-MISMATCH` | CE7 | Kl 02 No Support Mismatch | `FINITE_SUPPORT_DIRECTION_CORRECTED` (coverage_delta_bits=0.0) |
| `ATTR-01-LISTED-BUT-NO-DEPENDENCY` | CE8 | Attr 01 Listed But No Dependency | `DEPENDENCY_ATTRIBUTION_DIVERGENCE` |
| `ATTR-02-UNLISTED-REAL-DEPENDENCY` | CE8 | Attr 02 Unlisted Real Dependency | `DEPENDENCY_ATTRIBUTION_DIVERGENCE` |
| `ATTR-03-METRIC-ERRATUM-BLOCKED` | CE8 | Attr 03 Metric Erratum Blocked | `MEASUREMENT_EDITION_CONFLICT_BLOCKED` |
| `MISSION-01-ONE-SOURCE-REPLICATED` | CE3 | Mission 01 One Source Replicated | `UNSUPPORTED_MISSION_CHANGE` |
| `MISSION-02-AUTHORIZED-NEW-MISSION` | CE3 | Mission 02 Authorized New Mission | `SUPPORTED_AND_AUTHORIZED_CHANGE` |
| `MISSION-03-UNQUALIFIED-UNKNOWN` | CE3 | Mission 03 Unqualified Unknown | `MISSION_BASIS_NOT_ESTABLISHED` |
| `QUAL-01-B-SOURCE-BEATS-FULL` | CE11 | Qual 01 B Source Beats Full | `COST_COMPARISON_IF_BENEFIT_REALIZED` (best_mode=SOURCE_B) |
| `QUAL-02-CONVENTIONAL-BEATS-B` | CE11 | Qual 02 Conventional Beats B | `COST_COMPARISON_IF_BENEFIT_REALIZED` (best_mode=TARGETED_CONVENTIONAL) |
| `QUAL-03-Q-NOT-VALID` | CE11 | Qual 03 Q Not Valid | `COST_COMPARISON_IF_BENEFIT_REALIZED` (best_mode=TARGETED_CONVENTIONAL) |
| `QUAL-04-NO-GAIN-NEEDED` | CE11 | Qual 04 No Gain Needed | `COST_COMPARISON_IF_BENEFIT_REALIZED` (best_mode=A_ONLY) |
| `CLOSURE-01-LOWER-BOUND-SUFFICES` | CE11 | Closure 01 Lower Bound Suffices | `PREDICATE_SUPPORTED_IN_FRAME` |
| `CLOSURE-02-CROSSES-THRESHOLD` | CE11 | Closure 02 Crosses Threshold | `PREDICATE_UNDETERMINED` |
| `CLOSURE-03-NO-REGULARITY` | CE11 | Closure 03 No Regularity | `REGULARITY_NOT_ESTABLISHED` |
| `CAPACITY-01-ORANGE-COLLUSION-NOT-INFERRED` | CE1 | Capacity 01 Orange Collusion Not Inferred | `EVIDENCE_INSUFFICIENT_FOR_CLAIM` |
| `CAPACITY-02-EDU-STRUCTURAL-OPPORTUNITY` | CE4 | Capacity 02 Edu Structural Opportunity | `EVIDENCE_INSUFFICIENT_FOR_CLAIM` |
| `CAPACITY-03-CAPABILITY-RETAINED` | CE4 | Capacity 03 Capability Retained | `EVIDENCE_INSUFFICIENT_FOR_CLAIM` |
| `ACC-01-DENSE-GAP-40` | CE1 | Acc 01 Dense Gap 40 | `CONDITIONAL_COUNTERFACTUAL_GAP_NOT_HID` (ratio_percent=39.0) |
| `ACC-02-SPARSE-GAP-40` | CE1 | Acc 02 Sparse Gap 40 | `CONDITIONAL_COUNTERFACTUAL_GAP_NOT_HID` (ratio_percent=1.95) |
| `ACC-03-NO-GAP` | CE1 | Acc 03 No Gap | `CONDITIONAL_COUNTERFACTUAL_GAP_NOT_HID` (ratio_percent=0.0) |
| `ACC-04-RECOVERED-SYNERGY` | CE1 | Acc 04 Recovered Synergy | `CONDITIONAL_COUNTERFACTUAL_GAP_NOT_HID` (ratio_percent=32.63598326) |

## Las doce fuentes exactas

| ID | Documento real (Google Docs) | ¿Qué permite afirmar? |
|---|---|---|
| CE1 | [Abrir origen](https://docs.google.com/document/d/1QUzDHPp-yjrgCsjpXq7HLVMldNUO4iOFZ-4W2t4mHuI/edit) | Notas extensas Conscientia Ecosystemica / Magnifica Humanitas (secciones 10A–10E, plátanos, IQ-01–06, HID y dinámica). |
| CE10 | [Abrir origen](https://docs.google.com/document/d/1vwTSpSK_f4ePjg3ayRwI3fDkB9fqzYpWA4BiYL8n7qk/edit) | What Goes Unpriced Is Paid in Human Intelligence — separación carga, capacidad, coste y causalidad. |
| CE11 | [Abrir origen](https://docs.google.com/document/d/1qpBDFBZa7nGKlTD2D5poYuStCf0oJcAogBtUuzEjD90/edit) | Documento de trabajo sobre composición abierta/modelo social multiagente v0.6, Parts I–VII. |
| CE12 | [Abrir origen](https://docs.google.com/document/d/1rJTg__x4xKYRQbo63hFH3V-BNtkxsgnCUwgQ-oUCPck/edit) | Conscientia Ecosystematis para Magnifica Humanitas — correspondencia económica/social (oficio y rol humano). |
| CE2 | [Abrir origen](https://docs.google.com/document/d/1aKYkPlmuaiNv51QtW51q30fiNDdXrZ-1LQOJ2EGKhrg/edit) | De la dependencia sufrida a la solidaridad elegida, v3 (tres aportaciones, UC21, desarrollo y solidaridad). |
| CE3 | [Abrir origen](https://docs.google.com/document/d/1YRehP7BuSOR9qBhFs3OOrYrPjH3TDvoL4hPJ9eFV-TY/edit) | Conscientia Ecosystematis — Saber lo que no sabemos (FH-C, FH-E, Cyber Napoleon, ABCD, UC21 S1–S6). |
| CE4 | [Abrir origen](https://docs.google.com/document/d/1QHzTPaEGY0OCgUr-ObswadFGgrh7JP8XIxX-t36tj1M/edit) | Preservación de capacidades: clausura arquitectónica; educación, ministerios, oficios, derechos. |
| CE5 | [Abrir origen](https://docs.google.com/document/d/1ZBCAoni5TUVxGkbFGeTY0uRSBaS14vWYK3hhHDXlmww/edit) | A/B/C/D y hormigas metamórficas (documento histórico iterativo; usar semántica 00M para B/C/D). |
| CE6 | [Abrir origen](https://docs.google.com/document/d/19VwS524d9Kx3RVXbZjSdUn5yi9gRYAF-H66Mut540EU/edit) | Distorsión Entrópica — Laboratorio (propuesta δ y KL; fórmula original revisada críticamente). |
| CE7 | [Abrir origen](https://docs.google.com/document/d/1lBdXV47NjRY9pIbQlfYsdCcwGjSz_3k85P7m47Zw9J8/edit) | Auditoría matemática: dirección KL, testigos finitos, límites Landauer/PEF. |
| CE8 | [Abrir origen](https://docs.google.com/document/d/1wgFHAKE9sZFWrgvCIe4HUcK5cO3tuSidC2q24BVEFKU/edit) | Measuring the Attribution Gap v2 — revisión de instrumentos; edición de fórmula E bloqueada. |
| CE9 | [Abrir origen](https://docs.google.com/document/d/1sMuoAcfAqq8uQeeR98NBkr8-NChS2mZBQ1DmKSdAMuA/edit) | Optimization, Coherence, and the Frame — optimización/atribución vs coherencia de misión. |

## Interpretación obligatoria

- Cuando dice «óptimo», la alternativa está *estipulada como factible dentro del experimento*, no verificada socialmente. Si no es factible se devuelve `OPTIMUM_NOT_ESTABLISHED`.
- `HUMAN_INPUT_DIFF_NOT_OBSERVED_HID` declara solo magnitudes sintéticas; el humano observado, sufrimiento subjetivo y 01K HID real permanecen sin medir.
- La discrepancia de preimágenes y KL exige universo y distribuciones finitas caracterizadas; no estima entropía del exterior B/C/D.
- `MISSION-01`/`02` usan reglas instrumentales declaradas de cualificación; no ejecutan ni puntúan el UC21 nativo.
- Cada resultado con fuente CE1–CE12 es una **ilustración cuantificada** asociada a un mecanismo, no una extracción empírica del texto ni una cita experimental anterior.
- Los hechos y cifras que figuran explícitamente como hipotéticos en los Docs no se declaran observados por esta campaña.

