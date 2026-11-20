# ACC — Architectural fidelity review of recent experiments

**1 November 2026 · source-first corrective review · NOT a canonical change**

The source model is an **open, nonfungible set K of dimensions**, not a growing list of arbitrary independent variables or a universal net-utility function. The source anchors are [S1-P0205–P0223](../../model/01_NOTAS_COMPLETAS.md#s1-p0205), [S1-P0254–P0280](../../model/01_NOTAS_COMPLETAS.md#s1-p0254), [ACC MODEL](../../MODEL.md) and [economic core](../../ECONOMIC_MODEL_TECHNICAL_CORE_v0.1.md).

## 1. What belongs to the model

- **Dimensions**: separately justified measures, with defined units, actors, direction, evidence, and status. E, R, C and V are source examples, **not a closed list**; older source notation D/A for distribution/attribution must not be confused with epistemic A/B/C/D.
- **Parameter**: a coefficient inside an optional generator of example data. Merely naming a private return, investment, synergy or burden does not create four foundational dimensions.
- **C is coordination**: coordination effort/cost is a C measurement, **not automatically subtracted from R**, E or V. R may itself be an actor-specific declared utility measure only if its constituents are justified in that unit; avoid counting an expenditure twice.
- **Unknown**: when E cannot be evaluated because outputs are unlike, or V recognition/credit has not been independently measured, keep UNKNOWN. Never set it to zero.
- **Comparison**: partial dominance across justified, known K. R improving and C worsening is INCOMPARABLE without an explicit, accepted conversion/tradeoff. Legal/functional rights, consent and physical capability are independent typed gates; dimensions do not automatically have sovereign veto power.
- **Evidence boundary**: an illustrative payoff model or generated sensor is not a live agent measurement or a validated source fact.

## 2. What was wrong in H-01, and the correction

H-01 used four payoff-generator coefficients (return, investment, pairwise synergy, coordination burden) and automatically deducted the coordination burden from individual gain. The prior 114 admitted / 66 rejected and 24 supposedly remediable strict-trap cases are valid **only for that extra synthetic scalar-conversion assumption**. They are **not ACC-dimensional architectural conclusions**.

The new [open-dimensional comparison contract](dimensional_contract.py) and [H-01 source adapter](strategic_choice.py) retain the original simple game as a toy generator but use **only known R and C as separately assessed coordinates**. E, V and other relevant dimensions remain unknown. The previous joined payoff-cost decision is retained solely under the explicit marker LEGACY_ASSUMED_C_TO_R_CONVERSION_DIAGNOSTIC_ONLY.

Across the 180 original H-01 toy combinations, the source-preserving **R/C-only** comparison gives:

| Known R/C comparison | Cells | Meaning |
|---|---:|---|
| Monotone on known K | **46** | R improves; C does not worsen (zero new coordination burden) |
| Incomparable on known K | **92** | R improves, while C becomes worse: **tradeoff, not automatic success or failure** |
| No monotone improvement in K | **38** | One or more known dimensions worsen without a compensating independent improvement |
| Equivalent in K | **4** | No known R/C change |
| **Total** | **180** | All synthetic, not population rates |

Only **13 of 39** toy strict strategic traps appear monotone in the R/C projection, **26 are R/C tradeoffs**, and **none** proves the open model as a whole because E/V and possible further dimensions remain uncharacterized. The original PR42 feasibility witness is unchanged.

## 3. Source-backed triage across recent PRs

| PR | Finding | Action required |
|---|---|---|
| **#57** | Agentic source subtracts instrument cost from physical mission output, and sometimes uses that difference to decide whether to act. | **Block architecture-level net superiority claims** until an explicit, source-valid cost conversion is provided. Keep physical outputs and information costs separate; unconverted comparison is a partial order. |
| **#66** | Economic envelope uses net=gross−cost and ranks by max net even where the adapter declares output and cost in different units. | **Highest-priority shared-framework correction**: fail closed on incommensurable net ranking, expose independent dimensions and source decisions; do not infer an economic winner without legitimate conversion. |
| **#54** | Additional cases contain source-stipulated net utility and minimum-price outcomes; their benefit premise is not independently measured. | Keep as conditional toy identities. Map costs and outcomes to separate source dimensions before broader claim. |
| **#68** | The source social laboratory already declares dimensions and constraints explicitly. | Structurally useful. Retain source cases; prohibit any welfare B−F toy from becoming a universal objective or observed suffering. |
| **#69** | Staged source-native dimensions and actor payoff comparisons are distinct. | Generally faithful as conditional execution. Recheck any combined welfare toy or implicit fee conversion before cross-model extrapolation. |
| **#70/#72** | Errors, missed actions, information cost and Pareto front are separately published. | Valid **instrument evaluation metrics**, but not automatically ACC economic E/R/C/V. Require explicit mapping if used as economic dimensions. |
| **#73/#75** | Audit sensor quality and label leakage are epistemic diagnostics, not actor economics. | Preserve as bounded testing infrastructure; do not interpret information bits or synthetic costs as new economic dimensions. |
| **#76** | Overgenerated private payoff coefficients and scalar C deduction. | Dimensional projection implemented; old scalar analysis quarantined. Simplify its publication claims and maintain the full source example. |

This is a **code-backed scope triage, not independent certification**. In particular **#57 and #66 still need direct source-owner changes** before their net rankings can legitimately describe the nonfungible ACC architecture. No controlled source, frozen reference, or unrelated PR has been rewritten in this audit.

## 4. Minimal reusable contract

**S0 / S1 → open dimensions K (id, unit, direction, evidence, value or UNKNOWN) → nonfungible partial comparison → separate feasibility/authority/consent → result with provenance.**

Generators for rational-choice games, data-quality errors or costs are **optional adapters**, not permanent model dimensions. Their variables stay inside the adapter. A newly justified dimension extends K; a missing or incomparable one does not become a fabricated scalar or an invented invisible obstacle. The source itself says to add dimensions only on justified evidence, and to preserve UNKNOWN when a blocking mechanism is not established.

**Acceptance for future work:** R improves while C worsens => INCOMPARABLE; no cost automatically deducted from another dimension; unknown E/V stay unknown; new dimension can be added without rewiring a toy payoff generator; source output/rights and provenance remain separate. A green toy CI alone does not certify architectural fidelity.
