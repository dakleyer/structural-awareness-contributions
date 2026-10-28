# Anexo de la auditoría incremental — ayudas visuales, propuestas y referencias

> **¿Primera vez aquí?** Empiece por la [guía de lectura](GUIA_DE_LECTURA.md): estado vigente de todos los registros, ideas clave en lenguaje llano, mapa de rondas y glosario (ronda 14).

**Documento principal:** [Auditoría científica incremental](../INCREMENTAL_SCIENTIFIC_AUDIT_2026-10-26.md).
**Propósito:** que cada hallazgo deje algo utilizable en el PR auditado: una figura, una referencia que citar, una prueba que añadir o una formulación más precisa. Nada de este anexo cambia código, resultados ni canon.
**Reproducción:** todas las cifras de este anexo salen de [`audit_companion.py`](audit_companion.py) (biblioteca estándar, sin importar los estudios auditados). `python -B audit_companion.py --write` regenera [`COMPANION_RESULTS.json`](COMPANION_RESULTS.json) y las figuras de [`figures/`](figures/).

## Índice

1. [Mapa de hallazgos](#1-mapa-de-hallazgos)
2. [Figuras y vistas en tabla](#2-figuras-y-vistas-en-tabla)
3. [Propuestas ejecutables por hallazgo](#3-propuestas-ejecutables-por-hallazgo)
4. [Enriquecimiento por PR](#4-enriquecimiento-por-pr)
5. [Referencias](#5-referencias)
6. [Glosario provisional](#6-glosario-provisional)

---

## 1. Mapa de hallazgos

Cada PR auditado, con sus hallazgos y severidad. Las flechas discontinuas marcan hallazgos transversales: el mismo supuesto o el mismo patrón en varios PRs.

```mermaid
flowchart LR
  subgraph S["Modelo social"]
    P42["#42 Trampas acotadas"]
    P43["#43 Composición anidada"]
  end
  subgraph E["Campañas"]
    P48["#48/#49 Campaña 60×5"]
    P54["#54 46 casos + 88 barridos"]
  end
  subgraph R["Reducción agéntica"]
    P57["#57 Metaprotocolo 30×6 + 160"]
  end
  NOTE["Nota de revisión externa"]

  P42 --> H01["H-01 Alta: trampa de factibilidad, no subóptimo racional"]
  P42 --> H05["H-05 Media: utilidades estipuladas"]
  P43 --> H03["H-03 Alta: la pérdida es censura, no anidamiento"]
  P43 --> H04["H-04 Media: 'sufrimiento' = brecha de contribución"]
  P43 --> H06["H-06 Verificado: cotas de información correctas"]
  P48 --> G01["G-01 Alta: comparadores estipulados"]
  P48 --> G02["G-02 Media: auditoría booleana"]
  P48 --> G03["G-03 Media: microexperimentos literales"]
  P54 --> F06["F-06 Alta: casos trabajados, no experimentos"]
  P57 --> F01["F-01 Alta: metaprotocolo = convencional en código"]
  P57 --> F02["F-02 Alta: H5 es la única vía y no compara arquitecturas"]
  P57 --> F03["F-03 Media: recuentos del barrido = rejilla"]
  P45["#45 Cierre local"] --> I01["I-01 Alta: intervalo vacío aceptado como apoyo"]
  NOTE --> N06["N-06 Alta: encuadre de #54 y #57"]

  H02["H-02 Alta: brecha g·E supuesta"]
  P42 -.-> H02
  P48 -.-> H02
  P54 -.-> H02
  G03 -.-> F06
  F01 -.-> N06
  F06 -.-> N06
```

Ciclo de vida de un hallazgo en este registro:

```mermaid
stateDiagram-v2
  [*] --> ABIERTO
  ABIERTO --> RESPONDIDO: el autor responde o corrige
  RESPONDIDO --> CERRADO: la corrección se verifica en un commit fijado
  RESPONDIDO --> RECHAZADO: el autor justifica que no aplica
  RESPONDIDO --> ABIERTO: la respuesta no lo resuelve
  ABIERTO --> VERIFICADO: el hallazgo confirma algo correcto
  CERRADO --> [*]
  RECHAZADO --> [*]
  VERIFICADO --> [*]
```

## 2. Figuras y vistas en tabla

### F-01 · Dónde se separan, y dónde no, los brazos de #57

```mermaid
flowchart TD
  IN["Caso público A + Q"] --> D{"Brazo"}
  D -->|A_ONLY| K["Mantener A, coste 0"]
  D -->|Q_META_PROTOCOL| QC["coste = Q.cost"]
  D -->|CONVENTIONAL_EQUIVALENT_Q| EC["coste = equivalent_Q_cost"]
  D -->|CONVENTIONAL_DIRECTED| DC["coste = directed.cost; tasa = medida"]
  QC --> NG["near_gain con Q.lower_rate"]
  EC --> NG
  DC --> NG2["near_gain con tasa medida"]
  NG --> G["Compuertas: liberación, consentimiento, autoridad, protocolo conjunto"]
  NG2 --> G
  G --> T{"near > coste"}
  T -->|sí| X["Transferir"]
  T -->|no| K2["No transferir, coste pagado"]
```

`Q_META_PROTOCOL` y `CONVENTIONAL_EQUIVALENT_Q` sólo difieren en la caja de coste. Con el precio por defecto (0,3 en ambos) producen el mismo resultado en todos los casos.

### F-03 · Barrido de 160 celdas de #57

![Ganador por celda en la mitad del barrido con tasa real 2,0](figures/F03_sweep_winners.svg)

Vista en tabla (ganador exclusivo por mitad del barrido):

| Mitad del barrido | A | Q + metaprotocolo | Convencional dirigido | Empate |
|---|---:|---:|---:|---:|
| Tasa real 0,6 (80 celdas; ninguna transferencia mejora) | 80 | 0 | 0 | 0 |
| Tasa real 2,0 (80 celdas) | 27 | 14 | 39 | 0 |
| Total publicado | 107 | 14 | 39 | 0 |
| Tasa 2,0 con el brazo equivalente al mismo precio que Q | 27 | 0 | 39 | 14 |

### F-04 · Caso AG01 completo

| Brazo | Valor neto |
|---|---:|
| A_ONLY | 10,0 |
| Q_META_PROTOCOL | 11,2 |
| CONVENTIONAL_EQUIVALENT_Q | 11,2 |
| CONVENTIONAL_DIRECTED | **12,3** (producción 13,5 = óptimo técnico) |

### G-01 · Estructura del registro de 60 casos de #48/#49

| Propiedad | Valor |
|---|---:|
| Casos adjudicables | 48 |
| Casos en que el veredicto del peer convencional es igual a la verdad | 48 |
| Casos con A completo disponible | 32 |
| De ellos, veredicto igual a la verdad | 32 |
| Casos FALSE_Q | 12 |
| De ellos, con `independent_audit = true` | 4 |
| Tablas de utilidad distintas | 1 |
| Precios del peer / de Q | 0,5–1,6 / 1,0–2,2 |

### H-02 · La brecha supuesta frente a n

![Brecha supuesta como proporción de la producción frente a n](figures/H02_network_gap.svg)

| n | Densa | Estrella |
|---:|---:|---:|
| 5 | 4 % | 1,6 % |
| 10 | 9 % | 1,8 % |
| 20 | 19 % | 1,9 % |
| 40 | 39 % | 1,95 % |
| 101 | 100 % | 1,98 % |
| 102 | 101 % | 1,98 % |

### H-03 · Censura frente a anidamiento (n = 4, 16 estados ocultos)

```mermaid
flowchart BT
  L1["Rama 1: cap 8 o 10"] -->|"min(petición, cap)"| M1["Suma parcial"]
  L2["Rama 2: cap 8 o 10"] -->|"min(petición, cap)"| M1
  L3["Rama 3: cap 8 o 10"] -->|"min(petición, cap)"| M2["Suma parcial"]
  L4["Rama 4: cap 8 o 10"] -->|"min(petición, cap)"| M2
  M1 --> TOP["Receptor: sólo la suma total"]
  M2 --> TOP
```

| Observación | Informes por rama distinguibles | Sumas anidadas distinguibles |
|---|---:|---:|
| Petición 8 (censurada, como en #43) | 1 | 1 |
| Petición 10 (sin censura) | 16 | 5 |

Sólo la segunda fila aísla la pérdida atribuible a la composición: log₂16 − log₂5 ≈ 1,68 bits para n = 4.

## 3. Propuestas ejecutables por hallazgo

Bocetos mínimos, en el estilo de los estudios existentes (biblioteca estándar, deterministas). Son propuestas para que el autor las adopte o rechace; no se han añadido a ningún estudio.

### H-01 — Forma de juego para «subóptimo racional»

```python
# Caza del ciervo: la desviación unilateral es FACTIBLE pero no rentable.
PAY = {(1, 1): (5, 5), (0, 0): (4, 4), (1, 0): (0, 4), (0, 1): (4, 0)}

def is_nash(a, b):
    return PAY[(a, b)][0] >= PAY[(1 - a, b)][0] and PAY[(a, b)][1] >= PAY[(a, 1 - b)][1]

assert is_nash(0, 0) and is_nash(1, 1)          # dos equilibrios
assert PAY[(1, 1)] > PAY[(0, 0)]                # (1,1) Pareto-superior
assert (4 - 0) ** 2 > (5 - 4) ** 2              # (0,0) domina en riesgo (Harsanyi y Selten)
```

Con esto, (0,0) es un subóptimo *racional* en sentido técnico, y la dominancia en riesgo ofrece el puente natural hacia la aversión al riesgo de #46.

### F-01 / F-02 — Coste de reconfiguración por arquitectura

```python
# Hoy: overhead común a todos los brazos (physical_response).
# Propuesta: el diferencial agéntico, si existe, es exactamente esta diferencia.
OVERHEAD_BY_ARM = {"Q_META_PROTOCOL": h_agentic, "CONVENTIONAL_EQUIVALENT_Q": h_conventional}
# Ventaja en producción para la misma transferencia k: (h_conventional - h_agentic) * true_rate
```

Así el modelo hace explícito que la hipótesis agéntica es una afirmación sobre `h_conventional − h_agentic`, que debe medirse fuera del modelo (H5).

### G-01 — Veredicto derivado de la información de cada comparador

```python
# Hoy: peer["verdict"] escrito igual a la verdad en cada caso.
# Propuesta: el veredicto sale de la señal que el comparador observa, con error explícito.
def peer_verdict(signal_quality: float, truth: str, rng) -> str:
    return truth if rng.random() < signal_quality else ("ALLOW" if truth == "BLOCK" else "BLOCK")
# Barrer signal_quality para Q, peer y A completo con la MISMA semilla y la MISMA información.
```

### H-02 — Brecha derivada de un mecanismo

```python
# Hoy: gap = g * E (supuesto). Propuesta: ganancia y coste por enlace.
def realized_gap(n, topology, gain_per_link, coord_cost_per_link, b=10):
    E = n * (n - 1) // 2 if topology == "dense" else n - 1
    net = max(0.0, gain_per_link - coord_cost_per_link) * E
    return net / (b * n)   # la brecha se cierra si coord_cost_per_link >= gain_per_link
```

### H-03 — Prueba que separe censura y anidamiento

Añadir a `test_nested_model.py` una aserción del tipo de la tabla H-03: con petición 10, los informes por rama distinguen 2ⁿ estados y la suma anidada n + 1. Si el título de #43 se mantiene, esta es la prueba que lo sostiene.

### F-06 / G-03 — Convención de nombres

| Si el resultado… | Llamarlo |
|---|---|
| se sigue aritméticamente de entradas estipuladas | caso trabajado / fixture de especificación |
| comprueba que el código reproduce su propio JSON | prueba de regresión |
| puede fallar por razones que el autor del caso no fija | experimento sintético |
| compara con observaciones independientes | evidencia empírica (DDS Stage C) |

## 4. Enriquecimiento por PR

| PR | Figura o tabla que añadir | Prueba que añadir | Formulación que ajustar | Referencias que citar |
|---|---|---|---|---|
| #42 | Forma normal 2×2 con equilibrios marcados | `is_nash` y dominancia en riesgo (H-01) | «trampa de factibilidad» o «equilibrio Pareto-inferior», según el caso | Cooper y John 1988; Skyrms 2004; Arthur 1989 |
| #43 | Diagrama censura frente a anidamiento | Separación de la sección 3, H-03 | «no identificabilidad bajo observación censurada»; «brecha de desarrollo estructural» | Nahmias 1994; Hayek 1945; Simon 1962; Kushilevitz y Nisan 1997 |
| #45 | — | Contraejemplo de intersección vacía como prueba de regresión (I-01) | Rechazo estricto de `lo > hi`; tolerancia relativa si se mantiene | Shubert 1972 |
| #48/#49 | Tabla G-01 junto a la matriz 60×5 | Comparadores con calidad de señal barrida | «comprobación de la función de puntuación» | Howard 1966; Sargent 2013; Grimm et al. 2020 |
| #54 | Tabla de convención de nombres | — | «46 casos trabajados»; supuesto de uniformidad en `kl` | Cover y Thomas 2006; Shubert 1972 (cotas de Lipschitz en `closure`) |
| #57 | Figura F-03 y tabla F-04 | Brazo equivalente en el barrido; `h` por brazo | «prueba de reducción en v0.1» | Smith 1980; Bernstein et al. 2002; Howard 1966 |
| Transversal | Figura H-02 | Una única definición de brecha compartida | Declarar que #42, #49 y #54 comparten supuesto | Manski 2003 (identificación parcial) |

## 5. Referencias

Referencias para situar cada resultado en la literatura existente. Las marcadas con † se han comprobado contra una fuente bibliográfica en esta ronda; el resto son obras de referencia estándar.

| Referencia | Para qué sirve aquí | Hallazgos |
|---|---|---|
| Cooper, R. y John, A. (1988). Coordinating coordination failures in Keynesian models. *Quarterly Journal of Economics*, 103(3), 441–463.† | Equilibrios Pareto-inferiores por complementariedades estratégicas | H-01 |
| Skyrms, B. (2004). *The Stag Hunt and the Evolution of Social Structure*. Cambridge University Press. | Caza del ciervo como modelo canónico de cooperación arriesgada | H-01, #46 |
| Harsanyi, J. C. y Selten, R. (1988). *A General Theory of Equilibrium Selection in Games*. MIT Press. | Dominancia en riesgo frente a dominancia en pagos | H-01, #46 |
| Arthur, W. B. (1989). Competing technologies, increasing returns, and lock-in by historical events. *The Economic Journal*, 99(394), 116–131. | Bloqueo por dependencia de trayectoria | H-01, H-05 |
| Hayek, F. A. (1945). The use of knowledge in society. *American Economic Review*, 35(4), 519–530. | Conocimiento disperso y señales agregadas | H-03 |
| Simon, H. A. (1962). The architecture of complexity. *Proceedings of the American Philosophical Society*, 106(6), 467–482. | Sistemas jerárquicos casi descomponibles | H-03 |
| Nahmias, S. (1994). Demand estimation in lost sales inventory systems. *Naval Research Logistics*, 41(6), 739–757.† | Estimación con observaciones censuradas: el mecanismo real de #43 | H-03 |
| Kushilevitz, E. y Nisan, N. (1997). *Communication Complexity*. Cambridge University Press. | Cotas de bits de comunicación como las de H-06 | H-06 |
| Cover, T. M. y Thomas, J. A. (2006). *Elements of Information Theory* (2.ª ed.). Wiley. | Entropía, información mutua, divergencia KL | G-03, F-06 |
| Williams, P. L. y Beer, R. D. (2010). Nonnegative decomposition of multivariate information. arXiv:1004.2515.† | El XOR como caso canónico de sinergia | G-03 |
| Shubert, B. O. (1972). A sequential method seeking the global maximum of a function. *SIAM Journal on Numerical Analysis*, 9(3), 379–388.† | Cotas de Lipschitz como en `closure` | F-06 |
| Howard, R. A. (1966). Information value theory. *IEEE Transactions on Systems Science and Cybernetics*, 2(1), 22–26. | Valor de la información frente a su coste (Q, peer, A completo) | F-01, G-01 |
| Manski, C. F. (2003). *Partial Identification of Probability Distributions*. Springer. | Qué se identifica y qué no con información parcial | H-02, H-03 |
| Smith, R. G. (1980). The Contract Net Protocol. *IEEE Transactions on Computers*, C-29(12), 1104–1113. | Precedente de coordinación por contratos (ya citado en #57) | F-01 |
| Bernstein, D. S., Givan, R., Immerman, N. y Zilberstein, S. (2002). The complexity of decentralized control of Markov decision processes. *Mathematics of Operations Research*, 27(4), 819–840. | Dec-POMDP (ya citado en #57) | F-01 |
| Sargent, R. G. (2013). Verification and validation of simulation models. *Journal of Simulation*, 7(1), 12–24. | Distinción entre verificación (regresión) y validación | F-06, G-01 |
| Grimm, V. et al. (2020). The ODD protocol for describing agent-based and other simulation models: a second update. *JASSS*, 23(2), 7.† | Plantilla de descripción de modelos para la revisión externa | N-05, N-09 |

## 6. Glosario provisional

Borrador para N-08, a partir de los documentos del corpus. El autor debe confirmarlo antes de enviarlo a un revisor.

| Término | Significado en el corpus | Dónde se define |
|---|---|---|
| ACC | Agentic Citizenship Contract: perfil de participación agéntica gobernada por humanos. El «modelo auxiliar ACC» es el paquete de investigación alojado en esa línea | `01I_AGENTIC_CITIZENSHIP_CONTRACT_…`; [README del modelo auxiliar](../../README.md) |
| A / B / C / D | A: resultado de la explotación activa. B: reserva caracterizada, con base y límites de A. C: frontera de exploración aún no evaluable. D: incertidumbre residual sin vía efectiva de evaluación | `00M_ABCD_AND_MATHEMATICAL_PLAUSIBILITY_v0.8_RESEARCH_NOTE.md` |
| Q | Declaración cualificada de tipo B, acotada a una pregunta, con fuente, vigencia y cota | Estudios #48, #57 |
| 00M / 00N | Notas de investigación sobre semántica A/B/C/D y plausibilidad matemática (00M) y del mecanismo a los requisitos (00N) | `research/ecosystem-awareness/baseline/` |
| HID / 01K | Human Intelligence Debt; 01K es el perfil propietario de capacidad humana y deuda | `01K_HUMAN_INTELLIGENCE_CAPACITY_ESCALATION_AND_DEBT_PROFILE_v0.1.md` |
| DDS | Deployment Differential Study: método de evaluación con tres etapas | `DDS_CANONICAL_METHOD_INDEX_v0.1.md` |
| Stage A / B / C | A: descubrimiento de especificación. B: verificación de arquitectura. C: validación de implementación frente a ejecución y efectos observados de forma independiente | `DDS_CANONICAL_METHOD_INDEX_v0.1.md` |
| UC-21 | Caso de uso 21 del grupo FG-TIDA de la UIT, familia de desafíos sobre suficiencia de la base de decisión en composición, traspaso y cambio | Issue oficial UC-21 y DDS |
| EA | Ecosystem Awareness, la línea de investigación del corpus | `research/ecosystem-awareness/` |
| FH-C / FH-E | Hipótesis del argumento autónomo del modelo auxiliar | `model/02_ARGUMENTO_AUTONOMO.md` |


## 7. Corpus reconciliation and promotion readiness (27 October 2026)

**Contributor:** Codex, AI-assisted review requested by Iván. Use PR58 for discussion and this receiving view; use the existing owning VNext for the single literal source patch. PR59 transports those records, not a competing scientific approval or source queue.

### 7.1 What the reviews agree on, and what remains open

| Topic / existing finding | Receiving source review | Actionable conclusion |
|---|---|---|
| Empty numerical interval (I-01 / D26-F01) | [01I repair and regression companion](https://github.com/dakleyer/structural-awareness-contributions/blob/38fa9c83a898c7cfaa12151e9dff4812bebd9b10/research/ecosystem-awareness/baseline/01I_VNext.md) | Real source defect remains open. The complete two-file candidate is prepared; software checks pass, numerical policy/source adoption pending. |
| Equivalent comparator and selected-grid ranks (F-01/F-03) | PR59 D26-F03; this audit's existing arguments | Keep conditional fixture outcomes and ties visible. Identity of an algorithm is not observed independent efficacy. |
| Stipulated peer/audit fields and overlap (G-01/G-05) | PR59 source/data cross-check | Preserve all cases and lineage. A true-valued audit flag is not an independent audit, and repeated cells are not independent replication. |
| Finite information/partition results (H-06 and source lemmas) | Existing finite proofs and source-specific scopes | Retain valid conditional mathematics and its negative cases as such; do not turn it into observed deployment advantage. |
| Existing A omitted from supplementary-query selection (D26-F08) | 01I D26-C04/C05 against PR60 | New Theme18 fixture uses the corrected condition, while the original formal/caller passages still need synchronized repair. |
| UC21/DDS namespace/admission (D26-F09) | 01I D26-C06/C07 and receiving DDS VNext | Preserve native UC21 R0/R1/R2 and separate prospective DDS R1/R2/R3; require the actual failure/repair/passing-predecessor evidence. |
| Human evidence/decision reading (TAX26) | [Foundational owner](https://github.com/dakleyer/structural-awareness-contributions/blob/38fa9c83a898c7cfaa12151e9dff4812bebd9b10/research/ecosystem-awareness/baseline/01_FOUNDATIONAL_VNext.md#tax26-02--give-readers-one-operational-evidence-to-decision-distinction) and [interface owner](https://github.com/dakleyer/structural-awareness-contributions/blob/38fa9c83a898c7cfaa12151e9dff4812bebd9b10/research/ecosystem-awareness/baseline/04_GENERAL_FUNCTIONAL_INTERFACES_AGENTIC_SECURITY_VNEXT_REVIEW_AND_DELTA_v0.1_DRAFT.md#tax26-04--make-human-review-evidence-interpretable-at-if-s6) | Nine literal pairs revalidated; recommend 02/04 first without payload, schema or permission changes. |
| Newly added mathematics/overlays | Current main research route, PR57/60 | Preserve these additions. Their new proofs, fixtures, source editions and claims require their own review; old PR58 coverage is not inherited automatically. |

### 7.2 Bounded promotion selection

| Selection | Benefit / impact | Risk / effort | Exact readiness and dependency |
|---|---|---|---|
| **TAX26-02:** evidence → human understanding → sufficiency judgment → decision/execution/effect | High; makes the foundational reader dictionary operationally intelligible | Low / Low | Full unique old/new pair in its owner; source unchanged and candidate absent. Additive private preview reverses exactly. Select with 04. |
| **TAX26-04:** the same distinction at the human-review interface | High; improves interpretation of actual human-review evidence | Low / Low | Preserves IF-S6 payload and human decision ownership. Full pair in its owner; select with 02. |
| **Mathematical citation fragment repair** | Medium; restores a currently broken direct reader route | Low / Low | [Complete original/proposed paragraph](https://github.com/dakleyer/structural-awareness-contributions/blob/38fa9c83a898c7cfaa12151e9dff4812bebd9b10/architectural-contributions/ecosystem-positioning/README_VNext.md#navigation-candidate--current-mathematical-reading-route-27-october-2026). One extra hyphen; same intended theorem. Three-file private reader preview removes the one live fragment error; 17 historical snapshot reports remain classified. |
| **D26-C01 + regression companion** | High; rejects unsupported support from an empty interval | Medium / Low–Medium | [Complete predicate and test method](https://github.com/dakleyer/structural-awareness-contributions/blob/38fa9c83a898c7cfaa12151e9dff4812bebd9b10/research/ecosystem-awareness/baseline/01I_VNext.md). 60 original tests pass; 61 candidate tests with 18 adverse subcases pass; generated report equal. Select semantics and the two files together. |
| **D26-C04/05 and 06/07** | High for integrated correctness and traversal identity | Medium / Medium, with the row-only 07 change Low/Low but dependent | Fix source/caller and prose/matrix units in the still-open PR60; do not mark the original issue corrected because a new annex uses the right formulation. |

Other TAX26 pairs remain intact for subsequent selection; a current literal match is not by itself a decision to adopt. Per-arm cost mechanisms, source-accuracy estimates, human-welfare claims and new experiments remain research development, not quick editorial promotions.

### 7.3 Recheck the remedies as well as the diagnoses

**G-01 signal sketch:** the earlier peer_verdict(signal_quality, truth, rng) is a generative observation/noise model. It is not a runtime decision rule driven solely by the comparator's available evidence. Separate three roles: the generator may use hidden truth to emit a signal; the runtime comparator receives only permitted observations; the referee alone uses truth for scoring. A shared random seed is not automatically equal information. Noise/calibration parameters still require an independently justified design; randomizing a stipulated verdict does not establish real comparator performance.

**F-02/H-02 cost and gap sketches:** a declared per-arm h makes the hypothesis visible but does not measure it. Replacing g*E with (gain_per_link−coord_cost_per_link)*E still stipulates per-link economics; it does not identify a causal coordination mechanism from observations. Keep these as explicit finite models until the relevant mechanism, measurements and negative controls are specified.

**H-01 check refinement:** the displayed PAY values really are Pareto ordered. However, Python tuple “greater than” checks lexicographic order; it does not test Pareto dominance in general. For example (5,0)>(4,4) is lexicographically true but not Pareto superior. The next edition should use componentwise comparison. This is an improvement of a review example, not a claim that the displayed payoff fact is false.

**Current complete affected line:**

````python
assert PAY[(1, 1)] > PAY[(0, 0)]                # (1,1) Pareto-superior
````

**Proposed complete replacement:**

````python
assert all(x >= y for x, y in zip(PAY[(1, 1)], PAY[(0, 0)]))
assert any(x > y for x, y in zip(PAY[(1, 1)], PAY[(0, 0)]))  # Pareto improvement
````

**Glossary scope refinement:** Q is local notation, not a universal synonym for category B. Keep source-specific meanings and 00M qualification. The next reader edition can use this exact row; the earlier glossary is preserved above.

**Current complete row:**

````markdown
| Q | Declaración cualificada de tipo B, acotada a una pregunta, con fuente, vigencia y cota | Estudios #48, #57 |
````

**Proposed complete row:**

````markdown
| Q / Q_j | Study-local source/query notation. Q in #48/#57 is the declared scoped claim; Q_j in #60 is an eligible observation query. Its A/B/C/D role requires actor-, question- and time-specific 00M qualification; the variable name alone does not assign B. | Study definitions and canonical 00M v0.8 |
````

These two review-example refinements have Low risk and Low effort; the Q clarification has Medium reader impact, the assertion refinement Low. They do not change study programs or canonical taxonomy by being published here.

### 7.4 Execution and promotion receipts

For a named source wave: bind the actual source head and complete old passage, preserve its untouched predecessor, apply only the selected full pair, verify unchanged gaps by the inverse operation, run checks relevant to the change and read the published result back. Record the actual applied commit in the single owning VNext and clear its active pending status; retain the original audit and immutable predecessor. A draft PR, transferred proposal or successful document job is not that receipt. Do not close I-01 while its original source is unchanged; do not execute a candidate twice.

This continuation appends to the existing audit and annex. Current main additions and prior review content are preserved; no study, fixture, result or workflow is changed or executed by these review edits.

Publication revalidation: current main 2d9e4509447910a8541827edfc82c592d42e3520 retains the nine TAX26 target blobs and the interval-study source/test blobs unchanged. Its concurrent research additions/edits are inherited without modification; this continuation does not certify their scientific content.


## 8. Mathematical review and development opportunities

**Recepción de la ronda 8 · Codex, asistencia de IA a petición de Iván.** El registro de hallazgos y estados de recepción está en la [ronda 8 de la auditoría](../INCREMENTAL_SCIENTIFIC_AUDIT_2026-10-26.md#ronda-8). Esta sección desarrolla la evidencia nueva y las oportunidades; conserva literalmente todo el anexo previo. Las formulaciones siguientes son propuestas de investigación y de corrección, no cambios ya adoptados.

### 8.1 Correcciones a la lectura de auditoría

**M27-09 — generalización del control de implementación.** En PR57, Q_META_PROTOCOL y CONVENTIONAL_EQUIVALENT_Q entran por la misma rama de plan_public, líneas144–148; se cambia el precio declarado del instrumento. El test AG01 verifica salida y valor neto iguales con el mismo precio. Es una comprobación de la reproducción de ese mecanismo ya proporcionado. No mide cómo se descubre Q, cómo se selecciona una adaptación ni el coste completo de obtenerla.

La Parte I §8, en el corte 891af45a75b245082859147c0f7233cf85dd9035, distingue descubrir, seleccionar, compilar y ejecutar. También establece que quien efectúa el mismo metarazonamiento implementa funcionalmente esa arquitectura cualquiera que sea su nombre. Esta distinción forma parte del argumento y debe conservarse al interpretar F-01. No se exige que la aportación sea imposible de programar en software ordinario.

Mi frase del chat que presentó una conclusión general se retira como extrapolación del revisor. La última frase de SA-O2 §3 merece una precisión editorial local. **Fuente objetivo sin modificar:** [SA-O2](https://github.com/dakleyer/structural-awareness-contributions/blob/891af45a75b245082859147c0f7233cf85dd9035/research/structural-awareness/SA_OPERATIONAL_RESIDUAL_AND_ONLINE_CONTEXT_PLASTICITY_v0.1.md#L40).

**Antes, oración completa:**

> An ordinary controller retaining identical information ties.

**Después, oración de sustitución propuesta, no aplicada:**

> Retaining the same qualified distinctions permits the same target discrimination when a suitable decoder is effectively available. Reproducing the same decision procedure can reproduce its decisions; equal net utility additionally requires the relevant costs and conditions to match. This does not evaluate discovery, selection or adaptation effort, whose distinction from execution is stated in Part I §8.

**Efecto, riesgo y recepción:** precisión del alcance informativo, sin cambiar la prueba por fibras; impacto lector alto, esfuerzo bajo. La edición de la fuente necesita su propietario y ruta de revisión, no se aplica desde este anexo. No se borran F-01 ni sus estados históricos: se corrige la inferencia general que yo había añadido.

**M27-06 — navegación.** La política actual DC-GH-01 v1.0.3 admite materiales subordinados/opcionales y conciliación progresiva de roles. La mera ausencia de una fila individual no demuestra incumplimiento. Se conserva como tarea de identidad/navegación; mi anterior alegación genérica se retira. No se altera el registro ni se inventa el rol de los documentos.

### 8.2 Consistencia conjunta, intervalo vacío y selección suplementaria

**M27-01, contraejemplo nuevo.** Frame de ámbito scope, revisión v1, evidencia vigente, regularidad cualificada L=1. Dos registros de origen distinto declaran f(0)=0 y f(0)=2. En q=1 sus envolventes son [−1,1] y [1,3], así que la intersección local es [1,1]. La implementación devuelve LOCALLY_SUPPORTED_TRUE para f(1)≥1. Pero el conjunto de funciones que satisfacen ambas observaciones es vacío.

Esto muestra una obligación distinta de I-01: rechazar estrictamente lo>hi en el punto consultado conserva [1,1] y no detecta la incompatibilidad en x=0. El control positivo f(0)=0,f(1)=1 mantiene una función 1-Lipschitz y debe conservar su respuesta.

Para un **submodelo de coordenadas exactas**, intervalos [l_i,u_i] y una métrica d, existe una función L-Lipschitz compatible si y solo si todos los intervalos son propios y l_i≤u_j+L d(x_i,x_j) para todo i,j. Necesidad: aplicar la condición Lipschitz a cada par. Suficiencia: f(x)=max_i(l_i−L d(x_i,x)) es L-Lipschitz, f(x_j)≥l_j y las desigualdades garantizan f(x_j)≤u_j. Este es un candidato de contrato comprobable para ese submodelo.

**Límite del remedio:** el código también admite x_i inciertos. La prueba anterior no resuelve automáticamente su semántica, correlaciones ni factibilidad conjunta; hay que fijar esos cuantificadores antes de ofrecer un reemplazo general. Alternativamente, el informe puede declarar explícitamente que solo ha calculado una envolvente local, sin certificar existencia conjunta. Las fuentes siguen sin autenticación criptográfica. No se parchea la función en esta ronda.

**M27-02:** el acompañante reproduce la segunda entrada [1e-13,0] y el estado positivo, manteniendo su identidad I-01/D26-F01. El candidato de intervalo estricto sigue en 01I VNext; la nueva prueba conjunta debe añadirse a su alcance antes de afirmar que resuelve ambas cuestiones.

**M27-03, cuatro mundos.** X={0,1,2,3}; o(x)=⌊x/2⌋, r(x)=x y Q(x)=x mod2. Q sola deja sin separar (0,2) y (1,3). Tras observar o, solo quedan (0,1) y (2,3), ambos separados por Q. Para selección **suplementaria**, usar:

```text
U_(r|o) = {{x,y}: o(x)=o(y), r(x) != r(y)}
C_j^(o) = {{x,y} in U_(r|o): Q_j(x) != Q_j(y)}
```

D3 es correcto para la selección basada en Q sola; no se retira. El problema es su aplicación como complemento de una observación ya disponible. Los candidatos D26-C04/05 y sus propietarios siguen siendo la única propuesta de integración.

**M27-07:** un evento con cuatro valores (.9,.85,.8,.95), capturado antes de admisión pero sin first_capture_observer_id, puede cualificarse y producir salida11,5 con regla emitida. El hallazgo concierne la obligación de procedencia. Si esa identidad es opcional, hay que presentarla como desconocida; no inferirla ni borrar el evento para aparentar completitud.

**M27-08:** para D(n)=n(1−q^(n−1)), la fórmula q^(n−2)(1−q)((1+q)−n(1−q)) corresponde a D(n+1)−2D(n)+D(n−1). Si un consumidor define segunda diferencia como D(n)−2D(n−1)+D(n−2), debe desplazar el índice. En n=19,q=.9 la diferencia numérica es visible. Es una propuesta de coherencia de notación, no un nuevo mecanismo económico.

### 8.3 Ecuaciones y alcance de las fuentes releídas

**M27-05, R12.** Original: [TeX de 10 agosto2025](https://drive.google.com/file/d/1pAylPfeN4KkZiOzp-7UYX8peNvnlFtV2/view), 10.822 bytes, SHA256 cd17979d580d92076ff49a9e39ef7a84b4782e11810b54ffe58f3b7889615bbb. El expediente individual ya distingue el TeX anónimo, su render temporal de cinco páginas, R11 firmado y adaptación posterior a certificados. No se registra como error del expediente una distinción que ya conserva.

El ejemplo fuente 7+5(1−.4)=10 se refiere a divisiones homogéneas. Para reutilizar verificaciones reales hacen falta pesos de coste, prueba de elegibilidad y costes de renovación/coordinación. La fórmula de von Neumann en la línea133 iguala la entropía espectral a una suma de solapamientos de autovectores con Ω. Para una base ortonormal fija, esa suma con Ω fija no cambia al variar el espectro, mientras la entropía sí. Una identidad general necesitaría construir y justificar pesos/asignaciones dependientes del estado. Este contraste no refuta una asignación libre distinta para cada estado, ni la línea más estrecha de reutilización de verificación.

**M27-10, R19.** [Original](https://drive.google.com/file/d/1kjoTgijyzpQsWXUSkZesOLFr4qaPs4L2/view), §4.1, ecuación(4), página4, cotejada visualmente: Ṡ=rS−q(H−S). Para r,q,H>0, el equilibrio es S*=qH/(r+q), pero S(t)−S*=e^((r+q)t)(S(0)−S*). Es inestable; en 0 el campo es −qH y en H es rH, así que el intervalo no es invariante. Ṡ=q(H−S)−rS invierte la realimentación: entonces V=(S−S*)² tiene V̇=−2(r+q)V y el intervalo queda invariante. Ese cambio constituye un modelo propuesto distinto, cuya interpretación física debe justificarse otra vez.

**M27-11/12, ventanas.** Fuentes: [Minimal Proof](https://drive.google.com/file/d/1PpwYraPHiFoOaat_ZeP2Pw5dk-d5y1Fg/view) y [Ordered Multiscale Decoupling](https://drive.google.com/file/d/1wev5ifF7qTS8OJfna47igLwXYE0oSNfT/view), lectura focal de supuestos y proposiciones.

1. Una representación enriquecida permite reproducir las políticas anteriores y puede mejorar el **óptimo alcanzable**. Eso no demuestra que todo estimador fijo mejore al cambiar su entrada/contexto. Con muestras independientes de varianza1, diez actuales y noventa anteriores de media distinta Δ, la media actual tiene MSE=.1 y la conjunta .01+(.9Δ)². Para Δ=.1 la conjunta es mejor; para Δ=1 es peor. El sesgo no determina por sí solo el riesgo total. La Parte II actual ya usa formulaciones de políticas y condiciones de sesgo–varianza.
2. A2 permite acumular instancias anteriores **del mismo tipo**. Sea θ∈{0,1} con prior1/2. Una observación actual X y otra antigua del mismo tipo Z son independientes dado θ y cada una acierta θ con probabilidad.75. P(θ=1|X=1)=.75; P(θ=1|X=Z=1)=.9. Pueden estar separadas por un régimen de otro tipo. La ventana contigua actual no es entonces suficiente respecto de toda la historia. Para concluirlo hay que conservar la historia pertinente del mismo tipo o exigir su irrelevancia condicional.
3. La igualdad de posterior es suficiencia exacta; alcanzar riesgo por debajo de una tolerancia es adecuación práctica para una pérdida y tarea. No son definiciones intercambiables.
4. A3 ya supone estimabilidad por debajo de tolerancia. Una búsqueda finita permite elegir un mínimo si la familia factible no está vacía; no prueba por sí misma que el régimen actual ya contenga suficientes muestras ni que el anclaje encontrado sea verdadero.

**M27-14, D28.** [Fuente](https://tegrity.ai/1379-2/), Prop.3. Estados equiprobables, inacción=(0,0), acción segura=(0,1), otra acción=(−1,100). La segura satisface no-inferioridad frente a inacción. No domina a la otra en el segundo estado y su esperanza.5 es menor que49.5. Se conserva el contrato estricto de seguridad; para afirmar dominancia entre arquitecturas hace falta otro argumento sobre sus políticas, acciones y criterio.

**M27-15/16, D34.** [Fuente](https://tegrity.ai/structural-limits-of-current-ai-integrity-under-regime-change/). Una trayectoria de distribuciones puede salir de la región certificada y volver. Tampoco una tasa de llegada superior a servicio durante un intervalo implica crecimiento ilimitado. La revisión requiere validez indexada en tiempo y condiciones sobre duración, acumulado, servicio y plazos.

**M27-17/18/19, D37.** [Fuente](https://tegrity.ai/evolution-of-regime-awareness-capability/). El texto leído ya explicita P(A)P(P|A), su relación con la intersección y la severidad; esa aclaración no se trata como defecto vigente. Las configuraciones por poda/amplificación requieren una dinámica para llamarse atractores estables. Las ecuaciones afines/cuadráticas de precio requieren unidades, dominio y regla de elección de raíz. En el caso afín (b+d)x=c−a; si b+d=0 y c≠a no hay raíz, mientras que si también c=a todas las x satisfacen la igualdad.

Las fuentes web y Drive son instantáneas de lectura del27octubre; una edición posterior debe revalidar el hallazgo correspondiente. No se publican aquí sus originales completos ni se cambian sus permisos.

### 8.4 Desarrollos matemáticos propuestos

**M27-O1 — suficiencia dinámica.** En un modo fijo m, X abierto, h:X→h(X) submersión C² y F_m C¹, inputs u(t) comunes y soluciones únicas dentro del dominio: existe g_m C¹ con ẏ=g_m(y,u), y=h(x), que representa toda la dinámica observada si y solo si:

```text
h(x)=h(x')  =>  Dh(x)F_m(x,u)=Dh(x')F_m(x',u), para todo u.
```

Necesidad por regla de la cadena. Suficiencia definiendo g con cualquier representante; la condición lo hace independiente del representante y las secciones locales de la submersión aportan regularidad. Unicidad identifica las trayectorias. Este es un resultado clásico de proyección/lumping; una pregunta particular puede necesitar menos que la reducción completa.

Ejemplo: ẋ1=−a x1+κx2+u, ẋ2=−b x2, a,b>0, h=x1. Los autovalores siguen siendo −a,−b. Para κ=0 el resumen es cerrado; para κ≠0 dos estados con igual x1 y distinto x2 dan distinta derivada. Con a=b=κ=1, u=0, estados(0,±1), y±(t)=±te^(−t). A t=1, la pregunta y>.2 tiene respuestas opuestas con igual observación inicial. La historia ideal con modelo conocido puede recuperar x2=(ẏ+a y−u)/κ: el ejemplo no demuestra invisibilidad permanente.

Antecedente primario: [Li y Rabitz, exact lumping](https://doi.org/10.1016/0009-2509(89)85014-6). La posible aportación es el contrato temporal con fuentes, perspectivas, dominio y preguntas, no apropiarse del teorema clásico.

**M27-O2 — error y vigencia.** Si ẏ=g(y,u)+d(t), ||d(t)||≤ε(t), g es L-Lipschitz con L≥0 y la reducción ŷ comienza en el mismo estado, entonces:

```text
||y(t)-yhat(t)|| <= integral_0^t exp(L(t-s))*epsilon(s) ds.
```

La ecuación integral y Grönwall dan la cota; con error inicial se añade exp(Lt)||e(0)||. En el ejemplo triangular, |x2(0)|≤M da la cota exacta E(t)=|κ|M |(e^(−bt)−e^(−at))/(a−b)|, o |κ|M t e^(−at) cuando a=b. Para la pregunta y(t)≤c, ŷ(t)+E(t)≤c certifica el sí. No satisfacer esa desigualdad deja la respuesta sin certificar por este criterio.

El margen puntual puede perderse y volver. La pregunta de seguridad durante todo [0,T] exige el supremo sobre el intervalo; recuperar un margen actual no borra un cruce anterior. El modelo, la cota de perturbación, acceso y permiso para nueva evidencia son premisas independientes.

**M27-O3 — mejora individual y población cambiante.** Edad a, entradas b0 exp(γt), pérdida técnica ℓ(a)=exp(−βa), b0,γ,β>0, sin salidas ni interacciones. Las tasas γ,β tienen unidades de tiempo inverso:

```text
partial_t n + partial_a n = 0
n(t,0) = b0*exp(gamma*t); n(0,a)=0 para a>0
n(t,a) = b0*exp(gamma*(t-a)) para 0<a<t; cero para a>t
```

Por características, con solución débil en el frente a=t. Integrar la densidad y su producto con ℓ da:

```text
N(t)=b0*(exp(gamma*t)-1)/gamma
mean_loss(t)=[gamma/(gamma+beta)]*
            [1-exp(-(gamma+beta)*t)]/[1-exp(-gamma*t)]
limit_mean=gamma/(gamma+beta)>0
```

Cada identidad que entra en s tiene pérdida exp(−β(t−s))→0. La fracción de población con pérdida>θ, 0<θ<1, tiende a1−θ^(γ/β). Si γ=β, la distribución límite es uniforme: media1/2 y fracción por encima de1/4 igual a3/4. Recupera la distinción transversal de R10 del30julio, no sus pasos finitos ni las otras ediciones.

Con llegada constante, la media es (1−exp(−βt))/(βt)→0. La persistencia depende de la renovación, no se deduce de una mejora individual. El antecedente de transporte por edades está en [McKendrick, ejemplo9](https://doi.org/10.1017/S0013091500034428). No se atribuyen estos límites al artículo histórico ni a datos reales de agentes, personas o sufrimiento.

**M27-O4 — cola y balance.** Llegadas brutas λ≥0 y servicio μ≥0 en las mismas unidades de esfuerzo por tiempo, carga inicial w0≥0:

```text
Y(t)=w0+integral_0^t (lambda(s)-mu(s)) ds
w(t)=Y(t)-min(0,inf_{0<=s<=t}Y(s))
```

El regulador solo crece cuando la cola está vacía. El ejemplo λ=4,μ=2 hasta t=3 y λ=0 después llega a6 y se vacía en t=6; si la llegada4 persiste, w=2t. Una cola que se recupera puede haber incumplido un plazo. La espera w/μ requiere FIFO, capacidad constante y trabajo homogéneo, más el propio servicio de la nueva tarea.

Para un recurso conservado en una red, ẋ=Bv+s−d y 1ᵀB=0 implican d(1ᵀx)/dt=1ᵀ(s−d). Sumar tránsito por todas las aristas puede contar la misma unidad varias veces; no equivale al flujo neto que cruza el límite del origen. Tiempo, dinero, información y energía requieren balances separados.

**M27-O5 — ventana y estabilidad.** Para un menú finito de ventanas T, definir la familia factible mediante un testigo cualificado de validez del modelo, una cota E_t(T)≤ε_pregunta, coste≤presupuesto y demora≤plazo restante. Si no está vacía, un criterio de selección con desempate produce una opción; si está vacía, registra insuficiencia y las vías permitidas de adquisición de evidencia. La regla no demuestra que los testigos sean verdaderos ni un origen natural único.

Lema: s(t) absolutamente continuo, |ṡ|≤v, 0<v<∞, umbrales θon>θoff, sin saltos que eludan su cruce. Entre cambios opuestos, Δθ≤∫|ṡ|dt≤vΔt, así que Δt≥Δθ/v. No hay acumulación infinita de cambios en un horizonte finito. Acotar una señal primaria necesita constantes de composición para acotar s; los reinicios deben respetar el contrato. En discreto, con salto máximo c, la cota es ceil(Δθ/c) pasos y puede ser uno. La estabilidad de conmutación no identifica por sí misma el régimen verdadero.

### 8.5 Ejecución, reproducibilidad y transferencia

El [acompañante](math_audit_companion_2026-10-27.py) usa biblioteca estándar. Obtiene cuatro fuentes públicas en revisiones inmutables o admite una copia local con `--source-archive`; verifica el hash Git antes de ejecutar los módulos de estudio. Solo realiza cálculos finitos; no modifica los estudios. La ejecución local de esta ronda produce [32 comprobaciones satisfactorias](MATH_AUDIT_RESULTS_2026-10-27.json), incluidos contraejemplos, controles positivos, posterior .75/.9, integración diferencial y cuadratura de población. Un futuro cambio de blob requiere otra ejecución y recepción; no se asume que el resultado siga vigente.

Los desarrollos pueden aportar reglas/escenarios candidatos a DDS-PC-001/002/003/008, renovación a009/019, capacidad a011/012 y ventanas a010/013. No se declara completada Stage A (Specification Discovery), Stage B (Architecture Verification) ni Stage C (pinned Implementation/Problem Validation). Una demostración interna, una simulación finita y un efecto observado son evidencias distintas.

**Cobertura pendiente:** crítica matemática independiente, delimitación de originalidad, semántica de coordenadas inciertas en M27-01, incorporación de cambios en sus fuentes propietarias y evidencia aplicada de las oportunidades. Los resultados negativos o de corrección del propio revisor permanecen en el registro. Esta lista no se sustituye por recuentos de tests ni por una calificación global del corpus.


## 9. Corpus-wide interpretation repair

La [ronda 9](../INCREMENTAL_SCIENTIFIC_AUDIT_2026-10-26.md#ronda-9) amplía M27-09 desde una corrección del revisor hacia una reparación de lectura para cualquier autor, lector o resumidor.

La [guía transversal completa](INTERPRETATION_AND_COMPARISON_REPAIR_2026-10-27.md) contiene:
- siete dimensiones distintas de comparación y la separación entre etapas de descubrimiento, evidencia, selección, adaptación, ejecución y renovación;
- formulaciones positivas y precisas de lo demostrado, con controles contra la extrapolación y contra una defensa propagandística;
- 36 fichas antes/después sobre 24 fuentes/ediciones, verificadas contra sus unidades exactas;
- reglas de traslado a resúmenes, tablas, figuras, código/datos, matrices, índices, auditorías, VNext y ediciones protegidas;
- papeles separados para reproducción, información, ablación, incumbente independiente y referencia del evaluador;
- rutas propietarias, una primera ola sugerida y una prueba futura de comprensión para personas nuevas.

El contenido válido de F-01 permanece: el brazo con Q equivalente comparte la lógica especificada y el precio puede cambiar el neto. Se precisa qué se puede concluir de ese control y cómo se debe nombrar. El programa matemático conserva sus resultados de representación, expresividad y utilidad condicionada. La posibilidad de un resultado adverso de un incumbente competente permanece explícita y no se elimina mediante una reclasificación de nombres.

Esta propuesta sustituye como candidata editorial desarrollada la formulación breve de §8.1, que se conserva como historia. No crea una segunda VNext ni aplica las sustituciones a las fuentes. La pauta vigente de esta ronda y sus fichas son el receptor para continuar la discusión.

[Datos de fichas](INTERPRETATION_REPAIR_CANDIDATES_2026-10-27.json) · [Cobertura](INTERPRETATION_COVERAGE_2026-10-27.json) · [Índice completo](INTERPRETATION_COVERAGE_INDEX_2026-10-27.csv.gz) · [Verificador](verify_interpretation_repair_2026-10-27.py) · [Resultado interno](INTERPRETATION_REPAIR_VERIFICATION_2026-10-27.json).


## 10. Corpus refresh and open audit work — 28 October 2026

**Auditoría realizada por Codex, asistente de IA.** Relectura por mandato de Iván, con recepción en el PR compartido58. La [ronda12 del registro](../INCREMENTAL_SCIENTIFIC_AUDIT_2026-10-26.md#ronda-12--relectura-del-corpus-y-estado-real-de-la-auditoría-28-octubre-2026) contiene la matriz vigente de todos los pendientes. Esta sección desarrolla los nuevos argumentos y las unidades exactas de propuesta. No se modifican las fuentes de60/62/64 ni los34 cambios pendientes de la guía anterior.

### 10.1 Factibilidad Lipschitz: el resultado exacto es útil; el código debe certificarlo

Para coordenadas exactas x_i e intervalos [l_i,u_i], existe una selección de valores Lipschitz-compatible si y sólo si l_i-u_j ≤ L|x_i-x_j| para todos i,j. La suficiencia puede verse sin apelar a un solver: f_-(x)=max_i(l_i-L|x-x_i|) es L-Lipschitz; en cada x_j cumple f_-(x_j)≥l_j y las condiciones por pares aseguran f_-(x_j)≤u_j. La extensión construida muestra el contenido positivo del candidato64. Para coordenadas inciertas, su d_min certifica la condición para cada asignación permitida y d_max puede descartar todas; la franja no certificada conserva abstención. No se afirma una misma función universal para todas las posibles posiciones a la vez.

La aritmética flotante no realiza automáticamente esa demostración exacta. ε=2^-54 es exactamente representable. Con (0,1),(1,-ε),L=1, la diferencia exacta es1+ε>1; una resta redondeada da1 y permite TRUE. Un segundo caso, sólo f(0)=1,L=ε, tiene en x=1 la envolvente exacta [1-ε,1+ε], que cruza el umbral1; el programa la colapsa a [1,1]. No se ha usado una interpretación decimal incierta para fabricar el fallo: son números binarios exactos del propio contrato.

**Remedio completo propuesto:** (a) representar exactamente los números declarados —o incluir su incertidumbre como intervalos—; (b) calcular diferencias, distancias, productos y envolventes con racionales exactos o redondeo dirigido exterior; (c) comparar el umbral con los límites certificados, nunca con un redondeo que estrecha el intervalo; (d) si se muestran límites float, convertirlos exteriormente y no reutilizar una cifra de presentación como prueba; (e) no emitir SUPPORTED cuando la incertidumbre numérica cruza el umbral. Corregir únicamente _joint_evidence_status deja abierto el segundo caso. Los tests siguientes son criterios que el arreglo debe satisfacer y FALLAN ahora; no se publica aquí un parche de implementación no verificado.

### 10.2 Un certificado de guarda sólo se usa dentro de su dominio

Para el fixture60, la implicación probada es «x∈D y guard(x) ⇒ REJECT». El chequeo de proof_scope==DOMAIN acredita D, pero no verifica x∈D. El contraejemplo x=12 muestra que el atajo amplía silenciosamente el dominio frente a full_verdict. La reparación propuesta añade la pertenencia antes de la guarda; controles x=-2,10,12 deben conservar el rechazo por dominio y todos los x∈D conservar el veredicto. No se está evaluando un detector RA desplegado.

### 10.3 Cotas de utilidad y tiempo de uso

Una cota NaN no constituye una desigualdad probada: en Python, NaN<=0.75 es falso. Por eso la rama de rechazo no se activa. Infinito tampoco es la cota finita de la geometría declarada. Proponer una acción externa a partir de ese campo no ejecuta la acción, pero destruye el significado de «ganancia certificada». La ficha propone conservar UTILITY_NOT_ESTABLISHED cuando tipo o finitud fallan. Import y comprobación son una selección inseparable.

El helper temporal tiene una limitación distinta: sólo conoce la captura. La comprobación de vigencia al uso requiere el reloj de la decisión. La ficha ofrece esa semántica como candidata y exige actualizar todos sus llamadores y casos límite; si el propietario sólo pretendía validez histórica a captura, debe decirlo y no citar el test como validación de vigencia actual. No se inventa un tiempo real de recepción o una infracción en producción.

### 10.4 Asertividad y alcance en el material nuevo

IP37–42 prolongan la guía existente sin borrar resultados: el ahorro frente a la rejilla exhaustiva y el valor de la guarda siguen siendo afirmaciones matemáticas positivas bajo sus hipótesis. Repetir una misma función demuestra reproducción, aunque se le cambie el nombre al resultado. Compartir información tampoco selecciona por sí solo una política. El comparador independiente competente sigue siendo necesario cuando la afirmación evaluada trata del proceso completo; su resultado se incorpora con el alcance de aquella prueba, sin convertirlo en una conclusión general del programa.

### 10.5 Oportunidad de fortalecer el coste del selector (M28-O1)

CA-1 es un certificado condicional por instancia: si hay testigo útil y el coste total es menor, se logra la misma tarea binaria con menos trabajo. CA-4 añade el resultado asintótico bajo kq=o(nN) y overhead=o(nN). Ambos conservan su alcance positivo. La tarea científica que sigue es dar una condición medible de calidad/coste del selector, no suponer que la desigualdad siempre se cumple.

**Lema propuesto de selección con retorno.** En una familia finita, el procedimiento de rejilla completa cuesta D=nN probes unitarias. Un selector y su validación tienen overhead h; se revisa un conjunto de como máximo s<D pares. Con probabilidad p el conjunto contiene un testigo que se verifica correctamente. Si no, se retorna a la rejilla restante reutilizando todas las evaluaciones ya pagadas. Se mantienen tarea, autorización, calidad y costes comunes del certificado final. Entonces

\[
\mathbb E[C]\le h+p\,s+(1-p)D=h+D-p(D-s).
\]

**Demostración:** éxito cuesta como máximo h+s; sin éxito, selección más exploración de los restantes cuesta como máximo h+D. Promediar ambos casos da la cota. Ahorro suficiente frente a aquella rejilla: h<p(D-s). Si sólo se sabe p≥p_0, usar h<p_0(D-s). Los costes no unitarios y costes de autorización diferentes requieren su propio balance; no esconderlos en probes.

Ejemplo meramente construido: D=100,s=10,h=5,p=1/2 da cota60. Con p=0 cuesta105; con h=50 la cota105 tampoco mejora100. Un selector con presupuesto máximo conserva límite por instancia, y registrar los fracasos permite estimar p en pruebas posteriores sin omitir denominadores. Este p mide testigos útiles hallados por una política fijada en una distribución de tareas; no es la frecuencia de UNKNOWN ni una probabilidad inferida del exterior.

El lema compara exactamente con la rejilla completa que la fuente define. No es una cota inferior de toda búsqueda ni sustituye la comparación con políticas selectivas independientes. Su aportación práctica es dar un criterio falsable para el coste/calidad de Φ antes de afirmar ahorro total. No se presenta como resultado empírico ni se atribuye novedad al cálculo elemental de esperanza.

### 10.6 Receptor temporal del ciclo de contexto/aprendizaje (M28-O2)

M27-O1/O2/O5 adquieren un receptor claro en62 §14. Para un modelo continuo z'=F_v(z), observación y=h_v(t,z) y versión v fija entre cambios, el criterio de proyectabilidad pasa a exigir que ∂_t h_v+Dh_v F_v sea constante en cada fibra de h_v(t,·), dentro del dominio cualificado. Una desigualdad de error, margen de decisión y horizonte acota adecuación aproximada sin afirmar suficiencia exacta. Al cambiar v o redirigir la Semantic Window, la obligación se reinicia sobre la nueva pregunta/representación; conservar la historia necesaria y mapear explícitamente los certificados válidos.

Una primera maqueta matemática puede usar flujo entre cambios y un mapa de reset autorizado (z,v)→(z^+,v^+), con fecha de emisión/caducidad, error y presupuesto. Se debe demostrar qué dato cruza el reset, qué margen se pierde y si la histéresis acota la velocidad del indicador realmente usado. Una interfaz Update sin regla ejecutada no prueba aprendizaje, estabilidad ni convergencia. Este es un siguiente entregable propuesto, no otra demostración ya incorporada al corpus.

### 10.7 Unidades exactas antes/después — incorporación pendiente

Las fichas siguientes son propuestas en los receptores existentes, con preimagen completa, blob y línea comprobados. Toda selección requiere la revisión del propietario de esa fuente. Las operaciones sobre funciones distintas del mismo archivo se han contrastado conjuntamente para evitar solapamientos. No son una segunda VNext ni se ejecutan al publicar la auditoría.

#### M28-01-REG

**Propuesta; no aplicada.** [Fuente y unidad](https://github.com/dakleyer/structural-awareness-contributions/blob/0229bf9439be8459680dce4f7fe0376a9cd31306/research/ecosystem-awareness/baseline/01I-artifacts/acc-auxiliary-model-v0.1/studies/scoped-closure-metacognition-v0.1/test_metacognition.py#L122). Blob bdbac801a9cda734e53b549f0fe162556dcaf516. Receptor: PR64; fuente numérica y tests, recepción01I/PR59.

Dos regresiones semánticas: contradicción conjunta y certificado sobre límite inferior redondeado. Ambas FALLAN en el candidato actual, como exige el diagnóstico; no se anuncian como reparación ejecutada.

**ANTES — unidad literal completa**

~~~text
    def test_local_overlap_does_not_hide_global_source_conflict(self):
        points=(sample(y_min=0,y_max=0),
                sample(claim_id="p2",origin_id="s2",y_min=2,y_max=2))
        # Both projections at x=1 contain 1. No single f can obey both
        # values at x=0, even though their query-local intervals intersect.
        result=qualify(frame(),q(x=1,threshold=1),points)
        self.assertEqual(result["local_answer_status"],"EVIDENCE_OR_ASSUMPTIONS_INCONSISTENT")
        self.assertIsNone(result["conditional_answer_bounds"])

~~~

**DESPUÉS — propuesta completa**

~~~text
    def test_local_overlap_does_not_hide_global_source_conflict(self):
        points=(sample(y_min=0,y_max=0),
                sample(claim_id="p2",origin_id="s2",y_min=2,y_max=2))
        # Both projections at x=1 contain 1. No single f can obey both
        # values at x=0, even though their query-local intervals intersect.
        result=qualify(frame(),q(x=1,threshold=1),points)
        self.assertEqual(result["local_answer_status"],"EVIDENCE_OR_ASSUMPTIONS_INCONSISTENT")
        self.assertIsNone(result["conditional_answer_bounds"])


    def test_binary_rounding_does_not_hide_joint_contradiction(self):
        eps = 2.0 ** -54
        p1 = sample(claim_id="a", origin_id="a", x_min=0.0, x_max=0.0,
                    y_min=1.0, y_max=1.0)
        p2 = sample(claim_id="b", origin_id="b", x_min=1.0, x_max=1.0,
                    y_min=-eps, y_max=-eps)
        result = qualify(frame(lipschitz=1.0), q(x=0.0, threshold=1.0),
                         (p1, p2))
        self.assertEqual(result["local_answer_status"],
                         "EVIDENCE_OR_ASSUMPTIONS_INCONSISTENT")

    def test_rounded_lower_bound_is_not_a_positive_certificate(self):
        eps = 2.0 ** -54
        p1 = sample(x_min=0.0, x_max=0.0, y_min=1.0, y_max=1.0)
        result = qualify(frame(lipschitz=eps), q(x=1.0, threshold=1.0), (p1,))
        self.assertEqual(result["local_answer_status"],
                         "UNDETERMINED_FROM_AVAILABLE_EVIDENCE")
~~~

#### M28-02-FIX

**Propuesta; no aplicada.** [Fuente y unidad](https://github.com/dakleyer/structural-awareness-contributions/blob/3a846c6bb0fed6c25bf6deaa7af084a69ea242b5/research/ecosystem-awareness/baseline/01I-artifacts/acc-auxiliary-model-v0.1/studies/mathematical-lineage-social-agentic-v0.1/test_theme18_online_context.py#L53). Blob e8518ca15964b91ac925adf727ddae70d192a138. Receptor: PR60; fixture propietario, recepción01I/PR59.

La guarda sólo puede omitir la evaluación en el dominio probado. Se conserva el contrato de rechazo fuera del dominio y todas las salidas internas.

**ANTES — unidad literal completa**

~~~text
def guarded_verdict(x, *, guard_validated, proof_scope):
    """Never skip substantive decision without matching qualified proof."""
    if not guard_validated or proof_scope != DOMAIN:
        return full_verdict(x), False
    if guard(x):
        return "REJECT", True
    return full_verdict(x), False

~~~

**DESPUÉS — propuesta completa**

~~~text
def guarded_verdict(x, *, guard_validated, proof_scope):
    """Never skip substantive decision without matching qualified proof."""
    if x not in DOMAIN:
        raise ValueError("outside qualified domain")
    if not guard_validated or proof_scope != DOMAIN:
        return full_verdict(x), False
    if guard(x):
        return "REJECT", True
    return full_verdict(x), False

~~~

#### M28-03-IMPORT

**Propuesta; no aplicada.** [Fuente y unidad](https://github.com/dakleyer/structural-awareness-contributions/blob/3a846c6bb0fed6c25bf6deaa7af084a69ea242b5/research/ecosystem-awareness/baseline/01I-artifacts/acc-auxiliary-model-v0.1/studies/mathematical-lineage-social-agentic-v0.1/test_theme18_candidate_admission.py#L10). Blob 57794f4c2605443170b1f8b9f523ee53a1d6f9c5. Receptor: PR60; misma fuente del fixture.

Necesario para la comprobación explícita de finitud de la siguiente unidad; seleccionar ambas juntas.

**ANTES — unidad literal completa**

~~~text
import itertools
import unittest
~~~

**DESPUÉS — propuesta completa**

~~~text
import itertools
import math
import unittest
~~~

#### M28-03-FIX

**Propuesta; no aplicada.** [Fuente y unidad](https://github.com/dakleyer/structural-awareness-contributions/blob/3a846c6bb0fed6c25bf6deaa7af084a69ea242b5/research/ecosystem-awareness/baseline/01I-artifacts/acc-auxiliary-model-v0.1/studies/mathematical-lineage-social-agentic-v0.1/test_theme18_candidate_admission.py#L67). Blob 57794f4c2605443170b1f8b9f523ee53a1d6f9c5. Receptor: PR60; seleccionar con M28-03-IMPORT.

Sin cota finita y numérica no se ha establecido la ganancia de utilidad. La salida sigue siendo propuesta, nunca actuación. Comprobar NaN,±infinito,booleanos,None y controles0,84/0,75.

**ANTES — unidad literal completa**

~~~text
    elif not source_to_value_link_qualified or source_value_lower_bound is None:
        result["candidate_status"] = "UTILITY_NOT_ESTABLISHED"
    elif source_value_lower_bound <= CURRENT_GEOMETRY_VALUE:
~~~

**DESPUÉS — propuesta completa**

~~~text
    elif (not source_to_value_link_qualified
          or isinstance(source_value_lower_bound, bool)
          or not isinstance(source_value_lower_bound, (int, float))
          or not math.isfinite(source_value_lower_bound)):
        result["candidate_status"] = "UTILITY_NOT_ESTABLISHED"
    elif source_value_lower_bound <= CURRENT_GEOMETRY_VALUE:
~~~

#### M28-04-TIME

**Propuesta; no aplicada.** [Fuente y unidad](https://github.com/dakleyer/structural-awareness-contributions/blob/3a846c6bb0fed6c25bf6deaa7af084a69ea242b5/research/ecosystem-awareness/baseline/01I-artifacts/acc-auxiliary-model-v0.1/studies/mathematical-lineage-social-agentic-v0.1/test_theme18_online_context.py#L21). Blob e8518ca15964b91ac925adf727ddae70d192a138. Receptor: PR60; decidir primero si la propiedad del fixture es histórica o al uso.

Propuesta para vigencia al uso. Actualizar todos los callers para pasar tiempo de decisión; ejemplo t2 válido/t4 inválido con captura1,caducidad3. La igualdad en3 conserva el convenio actual y debe declararse inclusiva. No supone que exista un servicio real con este fallo.

**ANTES — unidad literal completa**

~~~text
def requalify(retained, certificate):
    """Only a qualified scope-compatible *rule* may reinterpret a retained event."""
    if retained is None:
        return "NO_REPLAY_SOURCE"
    if certificate is None:
        return "UNRESOLVED"
    if (not certificate.get("verified", False)
        or certificate.get("source_scope") != retained["scope"]
        or certificate.get("expires_before") < retained["time"]):
        return "CERTIFICATE_UNSUPPORTED"
    if certificate.get("target_event") != retained["event"]:
        return "NOT_APPLICABLE_TO_EVENT"
    return "ADMISSIBLE_FOR_NEW_REVIEW"

~~~

**DESPUÉS — propuesta completa**

~~~text
def requalify(retained, certificate, *, decision_time):
    """Only a qualified scope-compatible *rule* may reinterpret a retained event."""
    if retained is None:
        return "NO_REPLAY_SOURCE"
    if decision_time < retained["time"]:
        return "CERTIFICATE_UNSUPPORTED"
    if certificate is None:
        return "UNRESOLVED"
    if (not certificate.get("verified", False)
        or certificate.get("source_scope") != retained["scope"]
        or certificate.get("expires_before") < decision_time):
        return "CERTIFICATE_UNSUPPORTED"
    if certificate.get("target_event") != retained["event"]:
        return "NOT_APPLICABLE_TO_EVENT"
    return "ADMISSIBLE_FOR_NEW_REVIEW"

~~~

#### IP-37

**Propuesta; no aplicada.** [Fuente y unidad](https://github.com/dakleyer/structural-awareness-contributions/blob/f3f5e2078ba75443ea6e17ea2af9800f8d8ccec3/research/structural-awareness/SA_POSITIONED_RESIDUAL_REUSE_AND_LOCAL_ADAPTATION_v0.1.md#L506). Blob 977880fbd4b3a73667aacafdfb60459a075a4268. Receptor: Propietario de la nota62; no fuente canónica nueva.

Capacidad de implementar no significa igualdad de toda política o del proceso de descubrimiento. Afirmar primero el resultado de trabajo que sí se ha formulado.

**ANTES — unidad literal completa**

~~~text
A classical algorithm granted the *same* map, costs and adaptation rules can implement SEL and tie it.
~~~

**DESPUÉS — propuesta completa**

~~~text
An ordinary implementation can realize SEL: this is a constructive implementation property. Reusing the supplied SEL procedure on the same inputs reproduces its selected probes; equality of complete work additionally requires the same acquisition, selection, validation and lifecycle accounting. The positive result here is the conditional work reduction from informative paid-for selection against the declared exhaustive procedure; independent discovery and adaptation require their own process comparison.
~~~

#### IP-38

**Propuesta; no aplicada.** [Fuente y unidad](https://github.com/dakleyer/structural-awareness-contributions/blob/3a846c6bb0fed6c25bf6deaa7af084a69ea242b5/research/ecosystem-awareness/baseline/01I-artifacts/acc-auxiliary-model-v0.1/studies/mathematical-lineage-social-agentic-v0.1/11_THEME18_20261027_CORPUS_RECONCILIATION_AND_ADMISSION_CONTRACT_v0.1.md#L30). Blob b451e9d654760765af88104b943fefecd0ca285e. Receptor: PR60, recepción temática11; sincronizar lector12 y fixtures.

No reducir el ahorro probado a una conclusión global sobre una clase de arquitectura. Mantener la equivalencia del procedimiento suministrado y el coste de adquisición separado.

**ANTES — unidad literal completa**

~~~text
the same proved guard used by a conventional evaluator **ties**, not loses by architecture.
~~~

**DESPUÉS — propuesta completa**

~~~text
reusing that same proved guard and evaluator reproduces the scoped verdict and check count. The demonstrated contribution is the saving against repeated full checking under the stated inequality; a comparison of guard discovery, validation, integration and renewal requires its own complete cost account.
~~~

#### IP-39

**Propuesta; no aplicada.** [Fuente y unidad](https://github.com/dakleyer/structural-awareness-contributions/blob/3a846c6bb0fed6c25bf6deaa7af084a69ea242b5/research/ecosystem-awareness/baseline/01I-artifacts/acc-auxiliary-model-v0.1/studies/mathematical-lineage-social-agentic-v0.1/test_theme18_online_context.py#L144). Blob e8518ca15964b91ac925adf727ddae70d192a138. Receptor: PR60; mismo fixture de M28-02/M28-04.

El test llama dos veces al mismo cálculo. Su nombre debe describir ese control, no atribuir una competencia o proceso comparativo que no ejecuta. Conserva números y aserción.

**ANTES — unidad literal completa**

~~~text
    def test_competent_same_guard_conventional_peer_ties(self):
        our = ledger(10, 5)
        peer = ledger(10, 5)
        self.assertEqual(our, peer)

~~~

**DESPUÉS — propuesta completa**

~~~text
    def test_reusing_supplied_guard_reproduces_cost_ledger(self):
        # Reproduction control for this supplied ledger; no independent peer
        # acquisition, guard discovery or adaptation is executed here.
        first = ledger(10, 5)
        repeated = ledger(10, 5)
        self.assertEqual(first, repeated)
~~~

#### IP-40

**Propuesta; no aplicada.** [Fuente y unidad](https://github.com/dakleyer/structural-awareness-contributions/blob/3a846c6bb0fed6c25bf6deaa7af084a69ea242b5/research/ecosystem-awareness/baseline/01I-artifacts/acc-auxiliary-model-v0.1/studies/mathematical-lineage-social-agentic-v0.1/test_theme18_candidate_admission.py#L169). Blob 57794f4c2605443170b1f8b9f523ee53a1d6f9c5. Receptor: PR60; mismo fixture de M28-03.

El nombre peer fuerte no corresponde a una segunda implementación ni a adquisición independiente. Afirmar lo que se comprueba conserva el control sin inflar ni borrar la aportación.

**ANTES — unidad literal completa**

~~~text
    def test_strong_peer_with_same_evidence_ties(self):
        args = dict(received_after_exchange=True,
                    source_to_value_link_qualified=True,
                    source_value_lower_bound=.84, action_authorized=True,
                    decision_budget_ok=True)
        # Correct tie for identical algorithm and evidence; does not prove
        # one architecture superior (or test adaptation cost).
        self.assertEqual(assess_candidate(reports(), **args),
                         assess_candidate(reports(), **args))

~~~

**DESPUÉS — propuesta completa**

~~~text
    def test_supplied_candidate_procedure_reproduces_fixture(self):
        args = dict(received_after_exchange=True,
                    source_to_value_link_qualified=True,
                    source_value_lower_bound=.84, action_authorized=True,
                    decision_budget_ok=True)
        # Repeating the supplied function checks deterministic reproduction.
        # No independent acquisition, selection or adaptation is run here.
        self.assertEqual(assess_candidate(reports(), **args),
                         assess_candidate(reports(), **args))

~~~

#### IP-41

**Propuesta; no aplicada.** [Fuente y unidad](https://github.com/dakleyer/structural-awareness-contributions/blob/f3f5e2078ba75443ea6e17ea2af9800f8d8ccec3/research/structural-awareness/SA_POSITIONED_RESIDUAL_REUSE_AND_LOCAL_ADAPTATION_v0.1.md#L508). Blob 977880fbd4b3a73667aacafdfb60459a075a4268. Receptor: Propietario de la nota62, §13.3.

La aritmética condicional sí aporta un resultado; «nothing» borra ese alcance positivo. Separar con precisión conteo de probes, coste completo y evidencia operativa.

**ANTES — unidad literal completa**

~~~text
The comparison establishes nothing until the selection actually captures a useful witness, the input evidence was not leaked, and full costs/quality are matched.
~~~

**DESPUÉS — propuesta completa**

~~~text
The counts exhibit the proposed probe reduction, conditional on a justified selector and a useful captured witness. Establishing total-work or operational improvement further requires leakage-free selection, complete acquisition and lifecycle costs, matched quality and an actual successful certificate.
~~~

#### IP-42

**Propuesta; no aplicada.** [Fuente y unidad](https://github.com/dakleyer/structural-awareness-contributions/blob/f3f5e2078ba75443ea6e17ea2af9800f8d8ccec3/research/structural-awareness/SA_EA_EP_DDS_FOUNDATIONAL_BRIDGE_v0.1.md#L246). Blob e01385a28ae26522c9120bd9e8bdc583dc36929b. Receptor: Puente62 §7; sincronizar anexo13 sin cambiar SA-O4.

Separar la ventaja de discriminación informativa del ahorro de cómputo/procedimiento sobre la misma información. La condición abreviada no debe bloquear la interpretación positiva de SA-O4 o CA-4.

**ANTES — unidad literal completa**

~~~text
A gain attributed to meta-information is only established where the comparator demonstrably does **not** already use equivalent information, and where the additional mechanism/measurement cost is included.
~~~

**DESPUÉS — propuesta completa**

~~~text
An information-discrimination claim must identify a task-relevant distinction absent from the comparator observation. A work-allocation or inference-cost claim may instead compare different procedures on the same available information, including SA-O4 proof reuse and the linked residual-reuse annex §13 selective search; identify that procedural change and measure full acquisition, selection, verification and lifecycle costs. Keep the claimed dimension explicit, and compare actual competent implementations under the same decision contract.
~~~

#### M28-07-IMPORT

**Propuesta; no aplicada.** [Fuente y unidad](https://github.com/dakleyer/structural-awareness-contributions/blob/5046bbf4ac6dcbd6b7c2393929986868bb5d254d/research/ecosystem-awareness/baseline/01I-artifacts/acc-auxiliary-model-v0.1/review/incremental-audit-2026-10-26/math_audit_companion_2026-10-27.py#L7). Blob 1e9695cca3fa2fbcb2c850bf0d6598a366589f6d. Receptor: Acompañante8 del propio PR58; propuesta de higiene, no cambio matemático.

Dependencia estándar para caché temporal; seleccionar las cuatro unidades M28-07 juntas.

**ANTES — unidad literal completa**

~~~text
import argparse, hashlib, importlib.util, itertools, json, math, sys, urllib.request
~~~

**DESPUÉS — propuesta completa**

~~~text
import argparse, hashlib, importlib.util, itertools, json, math, sys, urllib.request
import tempfile
~~~

#### M28-07-ARGS

**Propuesta; no aplicada.** [Fuente y unidad](https://github.com/dakleyer/structural-awareness-contributions/blob/5046bbf4ac6dcbd6b7c2393929986868bb5d254d/research/ecosystem-awareness/baseline/01I-artifacts/acc-auxiliary-model-v0.1/review/incremental-audit-2026-10-26/math_audit_companion_2026-10-27.py#L26). Blob 1e9695cca3fa2fbcb2c850bf0d6598a366589f6d. Receptor: Seleccionar con IMPORT/OUTPUT/ENTRY de M28-07.

El resultado versionado deja de ser destino implícito; la caché por defecto proviene del contexto temporal del punto de entrada. --source-archive sigue leyendo las mismas fuentes fijadas.

**ANTES — unidad literal completa**

~~~text
def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--source-archive",type=Path)
    parser.add_argument("--output",type=Path,default=HERE/"MATH_AUDIT_RESULTS_2026-10-27.json")
    args=parser.parse_args()
    root=args.source_archive or HERE/".pinned-math-audit-sources"
~~~

**DESPUÉS — propuesta completa**

~~~text
def main(cache_root):
    parser=argparse.ArgumentParser()
    parser.add_argument("--source-archive",type=Path)
    parser.add_argument("--output",type=Path)
    args=parser.parse_args()
    root=args.source_archive or cache_root
~~~

#### M28-07-OUTPUT

**Propuesta; no aplicada.** [Fuente y unidad](https://github.com/dakleyer/structural-awareness-contributions/blob/5046bbf4ac6dcbd6b7c2393929986868bb5d254d/research/ecosystem-awareness/baseline/01I-artifacts/acc-auxiliary-model-v0.1/review/incremental-audit-2026-10-26/math_audit_companion_2026-10-27.py#L140). Blob 1e9695cca3fa2fbcb2c850bf0d6598a366589f6d. Receptor: Seleccionar con IMPORT/ARGS/ENTRY de M28-07.

Salida a stdout o creación exclusiva explícita. Si el destino existe, falla sin truncarlo. Se conserva el contenido de las32 comprobaciones.

**ANTES — unidad literal completa**

~~~text
    args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"passed":result["passed"],"total":result["total"],"verified_source_blobs":len(verified)},ensure_ascii=False))
~~~

**DESPUÉS — propuesta completa**

~~~text
    payload=json.dumps(result,ensure_ascii=False,indent=2)+"\n"
    if args.output:
        with args.output.open("x",encoding="utf-8",newline="\n") as stream:
            stream.write(payload)
        print(json.dumps({"passed":result["passed"],"total":result["total"],"verified_source_blobs":len(verified)},ensure_ascii=False))
    else:
        print(payload,end="")
~~~

#### M28-07-ENTRY

**Propuesta; no aplicada.** [Fuente y unidad](https://github.com/dakleyer/structural-awareness-contributions/blob/5046bbf4ac6dcbd6b7c2393929986868bb5d254d/research/ecosystem-awareness/baseline/01I-artifacts/acc-auxiliary-model-v0.1/review/incremental-audit-2026-10-26/math_audit_companion_2026-10-27.py#L142). Blob 1e9695cca3fa2fbcb2c850bf0d6598a366589f6d. Receptor: Seleccionar con las otras tres unidades M28-07.

El contexto elimina caché temporal al salir, incluso ante error. No crea una caché dentro del directorio publicado.

**ANTES — unidad literal completa**

~~~text
if __name__=="__main__":main()
~~~

**DESPUÉS — propuesta completa**

~~~text
if __name__=="__main__":
    with tempfile.TemporaryDirectory(prefix="imsv-math-audit28-") as audit_tmp:
        main(Path(audit_tmp))
~~~

### 10.8 Higiene del acompañante de ronda8 y criterio de cierre

El archivo antiguo conserva un destino por defecto y write_text sobre el JSON de referencia. La propuesta concreta es hacer --output opcional sin destino por defecto; si no se proporciona, escribir el JSON completo a stdout; si se proporciona, abrir ese destino con modo exclusivo x; usar TemporaryDirectory para descargas/caché y comprobar sus hashes. Verificar que una ejecución sin argumentos no altera ningún blob/ruta versionada y que un destino existente falla sin truncarlo. Mantener iguales las32 comprobaciones matemáticas y sus resultados. Este comportamiento ya se implementa en el acompañante23 de esta ronda, pero no se atribuye retroactivamente al antiguo.

### 10.9 Custodia, alcance de evidencia y continuación

Los pares se verifican literal e inversamente contra los heads indicados. Las nuevas regresiones numéricas son deliberadamente FALLIDAS en la fuente: describen la condición de aceptación del futuro arreglo. Las otras propuestas pequeñas tienen comprobaciones privadas de dominio, datos inválidos, vigencia y reproducción; no se modifican los snapshots. El acompañante23 permite reproducir los fallos actuales con tres blobs fijados, guarda caché temporal, salida por defecto a stdout y --output exclusivo. El resultado de red se compara con el local por contenido, no como dos experimentos.

La matriz de la ronda12 es la cola vigente. La primera acción es reparar certificados y recibir los estados ya avanzados; después escoger las fichas editoriales y continuar las líneas matemáticas y auditorías de fondo pendientes. Las34 operaciones IP anteriores y las nuevas unidades requieren su propia incorporación. Las restricciones de fuente congelada/histórica, consumidores y autoridad se conservan; no hay merge, cambio de main, nuevo protocolo de runtime, revisión humana independiente o envío FG-TIDA en esta ronda.


### 10.10 Source-owner reception after round 13 and remaining actionable units

Codex, AI-assisted review requested by Iván. This receives the concurrent rounds 12/13 rather than creating another audit round. [PR59's existing 01I owner](https://github.com/dakleyer/structural-awareness-contributions/blob/c7ba35c0c578fe65a856a8ea45eef2ea132fa187/research/ecosystem-awareness/baseline/01I_VNext.md#round12-source-reception) now records the changed source states, the complete remaining M28 technical units and impact/risk/effort. M28-06's owner-state reception is done; source promotion and remaining scientific review keep their own status.

**Numeric disposition verified in main 51fc686f:** fresh 72/72 tests, the formerly incorrect decimal-product case now rejected, the sub-ULP threshold undetermined and the legitimate positive control preserved at [1.5,1.5]. The frozen reference blob is unchanged and the generated report matches by value. This agrees with Claude's round 13 reconfirmation. D28-F01 is another witness of M28-01, not a separate defect. The old D26-C01 pending runtime card has been retired with its original anchor and a pinned complete history. Do not run the old one-line fix over the rational implementation or copy M28-01-REG into another active repair queue.

**Pending small source units:** M28-02 domain membership and the atomic M28-03 IMPORT/FIX pair remain proposed fixture corrections. The four M28-07 units are one I/O package. Their full old/new units are received in 01I under the original IDs; no new VNext or public companion is added here. D26-C04–07 are already implemented in PR60's branch, pending its review/merge, and must not be offered as unapplied to that branch. Nine TAX26 units and the localized IP-31/D28-C02 reading corrections remain source selections; D28-C01's expected-positive assertion remains a separate optional test improvement, privately rechecked at 72 tests.

**Additional plan review — M28-04-TIME:** the proposed function needs a finite/typed decision-time contract and complete caller units before execution. With capture 1, expiry 3 and an otherwise matching certificate, passing decision_time=NaN makes both comparisons false and currently yields ADMISSIBLE_FOR_NEW_REVIEW in that proposed function. This is a counterexample to the **candidate patch's input contract**, not a new allegation about deployed runtime. Select historical validity versus validity at use, provide the missing caller before/after units and expiry-boundary tests, and complete the existing proposal. Do not apply only its signature change or create a second competing plan.

The main comparison retains all prior paths/modes and frozen-reference bytes. The two working PR62 papers have valid local outgoing routes but only mutual incoming routes in the preview; a selected optional-research index entry remains their navigation dependency. Main's earlier known-case/prospective clarification and P5's successful three-cell reproduction remain incorporated. Full-process comparative evidence, depth/access experiments, remaining original-source adjudications and mathematical developments retain rounds 12/13's actual pending scopes.


## 11. Ronda 16 — recepción y propuestas acotadas

Revisión de Codex, asistida por IA. La [ronda16](../INCREMENTAL_SCIENTIFIC_AUDIT_2026-10-26.md#ronda-16) recibe los cierres numéricos y el arreglo de dominio. Los siguientes son candidatos de desarrollo, edición y herramienta, no una nueva lista de defectos del runner reparado.

### Fuentes primarias consultadas para§15

| Antecedente | Lectura efectiva en esta ronda y consecuencia |
|---|---|
| [Zhang–Ji2005, AAAI](https://cdn.aaai.org/AAAI/2005/AAAI05-195.pdf) | Lectura focal de resumen, introducción y modelo/criterio: selección de sensores con coste y sinergia en una red probabilística. Es un antecedente pertinente; no aporta directamente el contrato de transición de roles de este corpus. |
| [Williams–Beer2010, PID](https://arxiv.org/abs/1004.2515) | Resumen y ficha de autores: información redundante y sinérgica. Sirve para precisar el control XOR; no acredita eficacia de la integración§15. |
| [Bessiere et al.2013, IJCAI](https://www.ijcai.org/Abstract/13/078) | Resumen: el usuario clasifica asignaciones parciales. El proveedor de respuestas es un recurso que la comparación debe identificar y contabilizar. |
| [Lenguajes de restricciones desconocidos2023, IJCAI](https://www.ijcai.org/proceedings/2023/208) | Resumen y pasajes introductorios: aprendizaje desde soluciones/no soluciones y lenguaje inferido. No describirlo como si necesitara enumerar de antemano todos los candidatos ni como un servicio de consultas equivalente al de2013. |
| [SafeOpt2015, PMLR](https://proceedings.mlr.press/v37/sui15.html) | Resumen y ficha primaria: exploración con condiciones de regularidad y seguridad. Para adaptarlo a transiciones de arquitectura se necesita una correspondencia declarada de entradas/acciones/efectos. |
| [Rainbow ICAC2004, IEEE](https://ieeexplore.ieee.org/abstract/document/1301377) y [Computer2004, autores](https://www.cs.cmu.edu/~able/publications/computer04/) | Resúmenes y atribución confirmados; son dos ediciones relacionadas y el DOI ICAC citado es correcto. Antecedente de monitorización/adaptación con modelos de arquitectura. No se registra un supuesto error de referencia que esta consulta descarta. |

La página2024 citada en§15 no se pudo recuperar en esta ronda; tampoco se ha completado una lectura sistemática de toda la bibliografía ni de sus demostraciones. Estas lecturas focales apoyan las correspondencias de contratos y la selección de comparadores, no una conclusión de originalidad o equivalencia global. El contenido interno propietario de MSCA no se solicita ni se publica.

### Unidades antes/después

Son propuestas para sus receptores existentes. Las preimágenes son únicas, fijadas y reversibles; no se aplican al publicar esta sección. Se conservan los identificadores FA-4 y las rutas de lectura.

#### R16-P01

**Propuesta; no aplicada.** [Unidad fuente](https://github.com/dakleyer/structural-awareness-contributions/blob/a02f2d3180cd4ceb00cdc38e1224ba3cdd5f7872/research/ecosystem-awareness/baseline/01I-artifacts/acc-auxiliary-model-v0.1/review/incremental-audit-2026-10-26/reconfirm_I01_2026-10-28.py#L55). Receptor: Herramienta de reconfirmación del propio PR58; complemento de J08, no reabrir I01. Impacto Medium / riesgo Low / esfuerzo Low.

El script imprime discrepancias pero termina con éxito incluso si bad/lost son positivos. Hacer útil su código de salida si se incorpora a verificación automática. No afecta la corrección del runner ni invalida los cero errores realmente observados.

**ANTES — unidad completa**

~~~text
print("exactly decidable cases:",dec,"| code abstained or differed:",lost)
~~~

**DESPUÉS — propuesta completa**

~~~text
print("exactly decidable cases:",dec,"| code abstained or differed:",lost)
if bad or lost:
    raise SystemExit(1)
~~~

#### R16-P02

**Propuesta; no aplicada.** [Unidad fuente](https://github.com/dakleyer/structural-awareness-contributions/blob/4421ff535f9b6c3d70f34882e505af35924f234c/research/structural-awareness/SA_POSITIONED_RESIDUAL_REUSE_AND_LOCAL_ADAPTATION_v0.1.md#L795). Receptor: Nota de investigación62 §15.4; propietario actual; mantener FA-4 y métricas no fungibles. Impacto High / riesgo Medium / esfuerzo Medium.

Formalizar la cautela que §15.4 ya expresa: condicionar cada brazo a su propio éxito selecciona muestras distintas. La ilustración de la ronda conserva el mismo50% de éxito y aun así invierte el orden de costes. Es una concreción de M28-O1, no un fallo nuevo de CA-4.

**ANTES — unidad completa**

~~~text
The expected advantage is **conditional**:

\[
\mathbb{E}[C_{\rm five}\mid \text{validated, authorized gain}\geq g]
<
\mathbb{E}[C_{\rm comparator}\mid \text{same evidence, gain}\geq g],
\tag{FA-4}
\]
~~~

**DESPUÉS — propuesta completa**

~~~text
For each policy j on the same paired tasks and a predeclared horizon tau, let S_j indicate a certified authorized gain at least g, T_j the time to its first such certificate (infinity if absent), and C_j the actual cost of every attempt, including failures. Report

\[
p_j=\Pr(S_j=1),\qquad
\overline C_j=\mathbb E[C_j],\qquad
\overline T_j=\mathbb E[\min(T_j,\tau)].
\tag{FA-4}
\]

Cost conditional on S_j=1 is a secondary description of successful runs. At matched valid-witness recall, compare complete costs on all tasks; any time/cost trade-off needs its declared decision profile. A lower success-conditioned mean alone does not establish lower total cost. The existing requirement below to report misses and unconditional work remains operative.
~~~

#### R16-P03

**Propuesta; no aplicada.** [Unidad fuente](https://github.com/dakleyer/structural-awareness-contributions/blob/4421ff535f9b6c3d70f34882e505af35924f234c/research/structural-awareness/SA_POSITIONED_RESIDUAL_REUSE_AND_LOCAL_ADAPTATION_v0.1.md#L764). Receptor: Nota62 §15.3; desarrollo finito de H06/contraste PID; sin divulgar MSCA privado. Impacto High / riesgo Low / esfuerzo Medium.

Dar un control positivo y negativo ejecutable a la composición no fungible: la tasa UNKNOWN no identifica por sí sola la información conjunta. Se preservan procedencia, alcance y autorización.

**ANTES — unidad completa**

~~~text
A source may withhold, aggregate or mark a field UNKNOWN under its confidentiality/ACC rules; the receiver must not infer missing detail. These are **functional requirements on interoperability**, not the proprietary by-leaves composition algorithm or a new canonical MSCA schema. The receiving EA/EHD/Cartography route preserves reference identity and anti-correlation checks. Independent sources can improve spatial/architectural localization, like complementary sensors with different blind spots; a composed residual hotspot is an **exploration hint**, not a truth oracle. There remains an unobserved remainder at every level.
~~~

**DESPUÉS — propuesta completa**

~~~text
A source may withhold, aggregate or mark a field UNKNOWN under its confidentiality/ACC rules; the receiver must not infer missing detail. These are **functional requirements on interoperability**, not the proprietary by-leaves composition algorithm or a new canonical MSCA schema. The receiving EA/EHD/Cartography route preserves reference identity and anti-correlation checks. Independent sources can improve spatial/architectural localization, like complementary sensors with different blind spots; a composed residual hotspot is an **exploration hint**, not a truth oracle. There remains an unobserved remainder at every level.

**Classical finite composition control.** Let X0 and X1 be independent fair bits and Y=X0 XOR X1. Each single source leaves H(Y|Xi)=1 bit and is unresolved about Y on every exposure. Repeating X0 still leaves one bit; receiving the complementary X1 gives H(Y|X0,X1)=0. The local UNKNOWN rates are identical, yet duplicate and complementary composition have different target discrimination. Use this as a bounded control for mechanism3, with the same object/question/version and legitimate disclosure; add separate incompatible-scope, correlated-clone and permission-denied cases. This is a standard four-world example, not a new Shannon/PID theorem, an implementation of proprietary MSCA internals or a measured ecosystem benefit.
~~~

#### R16-P04

**Propuesta; no aplicada.** [Unidad fuente](https://github.com/dakleyer/structural-awareness-contributions/blob/4421ff535f9b6c3d70f34882e505af35924f234c/research/structural-awareness/SA_POSITIONED_RESIDUAL_REUSE_AND_LOCAL_ADAPTATION_v0.1.md#L830). Receptor: Nota62 §15.6; complemento del protocolo G01/F01; revisión sólo funcional, sin cambiar dueños. Impacto High / riesgo Low / esfuerzo Medium.

Convertir los antecedentes en comparadores implementables. QuAcq2013 pide etiquetas de asignaciones parciales; el trabajo de lenguaje desconocido2023 parte de ejemplos; SafeOpt supone regularidad. Los recursos de esos contratos deben ser explícitos y pagados.

**ANTES — unidad completa**

~~~text
- **Primary endpoints:** proportion of **independently certified, ACC-authorized ecosystem architectural gains** at fixed evaluation budget; full time/resources to **first** certified transition meeting declared shortfall improvement \(g\); ability to identify a valid gate and correctly reject hard constraints; missed high-value opportunities against an auditable bounded ground-truth fixture.
~~~

**DESPUÉS — propuesta completa**

~~~text
- **Information and query contract for each comparator:** fix the supplied examples, allowed queries and answer provider, label/oracle cost, initial feasible seed and regularity/model assumptions, permitted architecture mutations, disclosure rights and human approval time. Distinguish passive labelled-example acquisition from active partial-query learning and safe sequential optimization. Missing a legitimate oracle or adapter is a declared applicability limit; it is not a scored failure of that technology.
- **Primary endpoints:** proportion of **independently certified, ACC-authorized ecosystem architectural gains** at fixed evaluation budget; full time/resources to **first** certified transition meeting declared shortfall improvement \(g\); ability to identify a valid gate and correctly reject hard constraints; missed high-value opportunities against an auditable bounded ground-truth fixture.
~~~

#### R16-P05

**Propuesta; no aplicada.** [Unidad fuente](https://github.com/dakleyer/structural-awareness-contributions/blob/a3326843aa9822b1d7a4c774531fc51818300125/research/ecosystem-awareness/baseline/01I_VNext.md#L243). Receptor: Única01I VNext de PR59; concreción de M28-06, no nueva cola. Impacto High / riesgo Low / esfuerzo Low.

La recepción final ya cierra C01 y retira M28-02 de implementación, pero las tablas «Current» del comienzo conservan el estado candidato anterior. Un puntero vigente evita volver a aplicar o auditar como pendiente la reparación recibida.

**ANTES — unidad completa**

~~~text
## Current-source reconciliation and promotion queue — 28 October 2026
~~~

**DESPUÉS — propuesta completa**

~~~text
## Current-source reconciliation and promotion queue — 28 October 2026

**Current reading after incorporation51fc686:** D26-C01/I01/M27-01/02/M28-01 are repaired in main and technically reconfirmed. The66/68-test statements and candidate-only status below describe earlier cuts preserved as history; use the applied receipt above for the current disposition. D26-C04–07 remain implemented in branch60; M28-02 subsequently advanced there atcb72bb65, pending incorporation. Other source selections retain their own status.
~~~

#### IP-43

**Propuesta; no aplicada.** [Unidad fuente](https://github.com/dakleyer/structural-awareness-contributions/blob/a02f2d3180cd4ceb00cdc38e1224ba3cdd5f7872/research/ecosystem-awareness/baseline/01I-artifacts/acc-auxiliary-model-v0.1/review/incremental-audit-2026-10-26/GUIA_DE_LECTURA.md#L30). Receptor: Guía de lectura de PR58; misma política interpretativa, sin cambiar estados ni autoría. Impacto High / riesgo Low / esfuerzo Low.

Transportar la pauta afirmativa de IP01–42 al nuevo resumen para lectores: decir primero qué se ha demostrado y después qué pregunta compara cada control. Preservar críticas locales y estados, evitando una conclusión global abreviada.

**ANTES — unidad completa**

~~~text
- **Qué ha encontrado, en grande.**
  - Las matemáticas finitas que se han comprobado son correctas bajo sus supuestos.
  - Varias comparaciones y «experimentos» dan el resultado que ya estaba escrito en sus datos o en su código. Sirven como comprobaciones, pero no prueban una ventaja.
  - Hubo un fallo real de cálculo (I-01), que ya está corregido en la rama principal y reconfirmado.

~~~

**DESPUÉS — propuesta completa**

~~~text
- **Qué ha encontrado, en grande.**
  - Las pruebas finitas revisadas establecen resultados concretos bajo sus hipótesis: una representación puede conservar una distinción necesaria para decidir; información compatible puede sostener una conclusión local útil; una guarda probada puede ahorrar comprobaciones en su dominio y balance de costes.
  - Los fixtures también comprueban reproducción y sensibilidad bajo entradas o procedimientos suministrados. Esos resultados conservan su valor; para estudiar adquisición, selección o adaptación se necesita el proceso correspondiente y su evidencia.
  - El fallo numérico I-01 y sus ampliaciones están corregidos y reconfirmados. La guarda de dominio M28-02 ya se corrigió y reconfirmó en la rama60; su incorporación sigue pendiente.

~~~
