# ACC — Source-anchored narrative acceptance experiments (v0.1)

**Research-only, 29 October 2026.** Author's examples are acceptance cases, not decoration, training observations, a political economy simulation of the real world or a DDS/UC21 product test. This is a *standalone finite test layer* over their declared assumptions, separate from `00M` epistemic A/B/C/D, `00N`, the agentic engine #57 and the pricing envelope #66. License and attribution: repository root controls apply, with original conceptual authorship of Iván Abril Palma / The Integral Management Society.

## Why this layer exists

The existing campaign (`conscientia-campaign-v0.1/campaign.py`) retains microexamples but largely as fixed arithmetic/metadata. #66 runs 168 source-social policy-price combinations and 118 agentic-price combinations; #67 computes the physical response for one source-native question. Those pass *their* tests but do not establish preservation of the narrative examples' transitions and dimensions.

This implementation makes the author's examples runnable **without** converting all examples into a monetary objective. Each source-anchored fixture declares states, oriented axes with **separate units**, *per-actor* payoffs if the source/explicit toy assumption supports them, conservation constraints, budgeted resources, consent/authority/safety/coordination/evidence guards, and a graph of possible transitions. `UNKNOWN` is not zero, `FAIL` or permission; an attractive end state is not thereby accessible. The breadth-first reachability engine checks cumulative resource use and separates unilateral steps from an atomic joint transition. Stage-by-stage partial orders expose a pre-existing but newly material axis without creating it or automatically creating an agent/veto.

**Three different layers are kept independent:**

1. **Final-state physical-model constraint check:** declared conservation, capacity and coupling rules. A pass is conditional on the *declared toy representation*, not external feasibility evidence.
2. **Legitimacy/decision:** consent, authority, coordination, safety, evidence, and other source-named gates; `UNKNOWN` remains unresolved.
3. **Evaluation:** dimension-wise oriented change and (when explicitly supplied) payoffs by actor; these cannot override failed gates. `W=B−F` is checked only for stipulated finite toy numbers and never inferred from production or published as observed psychological experience.

## Source-to-fixture-to-test acceptance ledger

| Original source ID | Preserved question | Expected result of `run_case` | Regression |
|---|---|---|---|
| EX-BAN-02 | Additional transport to someone in need | Distribution ↑, transport efficiency ↓; genuine trade-off | `test_banana_extra_transport_genuine_tradeoff` |
| EX-BAN-01 | 14,000 km then waste vs use in production region | E/R dominates; adding actual coordination effort changes result to trade-off; authorization unresolved | `test_banana_origin_activates_coordination_without_creating_it` |
| EX-BAN-03 | Caritas/DANA hypothetical donor, pre-existing route | K2 and K3 dominance; hypothetical relative recognition K4 trade-off; refused consent prevents route; legitimate alternative can be declared | `test_dana_original_credit_is_not_an_institutional_accusation` |
| EX-BAN-04 | **Exact S0/S1/S2**: 0 / 2 with 1 wasted / 2 both used | Physical conservation; **B1=5, F1=7, W1=−2** as stipulated toy only; real route unresolved | `test_two_bananas_original_arithmetic_and_physical_conservation` |
| EX-ROBIN-01 | Friday gets 1 coconut+fish, Robinson 999+999 | Both direct gains positive under toy proxy, relative-gain objection still possible | `test_robinson_1_999_source_counts_and_relative_refusal` |
| EX-MIN-01 | Two ministries; illustrative 700 applications → 2 | Technical axis positive; full service, rights, livelihoods and authority unverified | `test_ministries_efficiency_does_not_establish_pareto_or_legality` |
| EX-APPLE-01 | Nonmonotone utility, local peak vs distant alternative | 3→4 loses utility; unilateral path fails; atomic financed move can reach q8 in positive control | `test_apples_nonmonotone_but_pareto_finals_possible` |
| EX-LINEAR-01 | Binary coupling x1=x2; (0,0)→(1,1) | Both final states feasible; no unilateral feasible intermediate | `test_binary_joint_without_unilateral_intermediate` |
| EX-CREDIT-01 | Credit 7+4 and budget 10 | End state is physically/accountingly invalid, even if selected axes improve | `test_credit_7_plus_4_is_physically_invalid_not_just_unpopular` |
| EX-SOLIDAR-01 | Dependence vs freely chosen solidarity | No unobserved consent invented; consent-granted positive-control route remains possible | `test_solidarity_requires_actual_consent_and_no_universal_welfare` |
| EX-ORANGE-01 | Discarded oranges, conjectures about price | Recoverable quantity, collusion, lived distress: **NOT_ESTABLISHED** | `test_oranges_and_student_are_not_numeric_discoveries` |
| EX-HUMAN-01 | Lycée, university place and unused capability | Capability quantity, individual choice and distress **not measured** | `test_oranges_and_student_are_not_numeric_discoveries` |
| EX-SUPER-01 | Internal output X−200 | X=1000 toy yields 800, repair route unverified | `test_X_minus_200_does_not_invent_repair_authority` |
| EX-BUSINESS-01 | Marketing +60, Operations +40, Systems −30 | Gross 70; transfer 35 and **invented** cost allocation (6,4,5) gives 55 net; board authority still UNKNOWN | `test_marketing_offer_accounting_70_to_55_and_authority` |

Source anchors are stored per case. `EX-BAN-02`'s Africa detail is an **author clarification**, not an historical assertion of a measured shipment. The DANA/Caritas scenario concerns an explicitly hypothetical donor perception and attributes no practice or bad faith to the real organization. The `R` component of EX-ROBIN-01 and its payoffs are **positive toy proxies**, not equivalences between food items and real human utility. In EX-BUSINESS-01 the 15-unit cost split is an *added experimental assumption*, not the source author's measured allocation. Conditionality and counterfactual assumptions are not presented as data.

## Run

Requires Python 3.12+ standard library. From this directory:

```bash
python -B build_fixtures.py
python -B engine.py --manifest cases.json --output results.json
python -B -m unittest discover -s . -p 'test_*.py' -v
```

`cases.json` is deterministically generated from the maintained source-anchored `build_fixtures.py` and supports editing/adding cases externally with no changes to `engine.py`. `results.json` contains the per-case state-invariant checks, each edge's material and institutional gates, reached states and paths with and without atomic joint steps, stage-by-stage oriented coordinate deltas, and explicit status for any stipulated toy welfare quantity. Do not treat produced files as independent evidence. The CI reruns generation and all controls.

## Reuse / controls / review limits

A third party can supply an independently declared JSON scenario with arbitrary new axis IDs, units, stages, states, balances, roles and gates. No original case name is hard-coded in the engine. The adversarial tests exercise a new **water-use** problem, exact rational units, genuinely cumulative resource budgets, malformed or false gate statuses, a new dimension with missing measurement, source identity, physical conservation, and failed consent despite large material benefit.

**Not proven:** independent validation of any historical observation, field behavior, an actual safe or legal shipment, measured F or HID, a social Pareto optimum, C/D exhaustive coverage, agentic decision correctness, a new technology's competitive advantage, or execution of UC21 DDS Stage C. This is not a merger of #66, #67, #57 or #60; those modules retain native physical policies and post-hoc referees. The new narrative suite is an independent acceptance layer to be reviewed before introducing adapters. No changes to frozen case registries, owner canons or source text.
