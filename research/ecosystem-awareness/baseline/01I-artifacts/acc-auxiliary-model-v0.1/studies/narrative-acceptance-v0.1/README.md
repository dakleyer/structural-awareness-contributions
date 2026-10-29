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

## Native-source concordance (independent replay)

Run `python -B source_replay.py --output source-concordance.json` after generating `cases.json`. This **imports and calls the original source functions** in the adjacent Conscientia campaign and bounded-traps modules, without rewriting or monkey-patching their simulation, reference output or source registries.

Eight scenarios have a directly overlapping source-native microcalculation, constraint or evidence gate: two-bananas, DANA consent, credit, apples, binary coupling, ministries, oranges and lycée. Six remain **source-anchored newly operationalized fixtures with no identical source-native executable** (BAN-01/02, ROBIN, SOLIDAR, SUPER, BUSINESS). The joint jump in APPLE is deliberately an **added positive control**: `market_jump()` in the source expressly says `direct_jump_assumed_available=False`. The concordance flags this difference rather than claiming exact source execution. Repeating the source's finite arithmetic is a consistency regression, **not an independent empirical replication**.


## G-03 continuation — operation-generated examples, not just stored destinations (29 Oct 2026)

The original `engine.py` is kept intact as an **acceptance/referee layer**. It tests declared states, their dimensional differences, source-named gates and reachability. Those declared destination states are not outputs generated by an action. Therefore this PR now adds a separate **source-anchored finite mechanism layer** rather than claiming the original acceptance grid is a fully generative experiment.

- [`mechanistic_replay.py`](mechanistic_replay.py): reusable, exact-rational, strictly bounded operation runner. It calculates *new* states from transfers, production/delta, setpoints, finite payoff formulas and source-declared utility profiles; checks conservation/coupling, cumulative resource budgets, actor-local nondecrease and the existing native guard/constraint functions in `engine.py`. A physically possible **counterfactual** and a legitimately **committed** state are reported separately. UNKNOWN never authorizes execution. The mechanism does not synthesize source information or infer new dimensions from a blocked transition.
- [`MECHANISM_CASES.json`](MECHANISM_CASES.json): **all 14 original EX identities** expressed as an independent operation manifest. Source-defined destination fixtures are **not** read to produce an outcome. Actions have declared experimental parameters, and hard numerical claims remain synthetic.
- [`test_mechanistic_replay.py`](test_mechanistic_replay.py): direct tests for all 14 mechanisms, including changed production quantities, physical overdraft, non-fungible consent, source utility valley, coupled binary actions, per-actor accounting and unchanged UNKNOWN when data are absent.
- [`agentic_crosswalk.py`](agentic_crosswalk.py): optionally executes source-native [PR #57](https://github.com/dakleyer/structural-awareness-contributions/pull/57) at pinned SHA `a9894049` **without modifying its model**. Eight author examples have *structural analogues only* in five native PR57 cases; six have **no equivalent same-question executor**. It tests the original source's refusal, authority, shared D, same-A/different-future and authorized-resource-transfer boundaries. It does **not** call them a full agentic reduction of the banana, ministries, human or credit examples.

**Source ownership reconciled:** The independently developed [PR #68](https://github.com/dakleyer/structural-awareness-contributions/pull/68) already supplies the source-owned Conscientia campaign implementation: 40 finite social illustrative cases, three original PR44 runs, and all thirty PR57 agentic cases (six native arms), with finite conditional information and XOR computed from source rows. Its `campaign.py` changes and G-03 corrections remain solely in **#68**. This #69 PR does **not** replace or alter `conscientia-campaign-v0.1/campaign.py`, and does not supply another Shannon/XOR implementation. Its distinct contribution is **source-anchored action sequences** with source-native acceptance/commitment checks and rigorous boundary tests.

### Important example semantics recovered

**DANA / Cáritas and Viernes / Robinson:** a share of the *newly created* gain has no defined numerical value in a baseline where no gain yet exists. The operation runner therefore reports **NOT_ESTABLISHED** for a baseline-to-proposal comparison including that relative-share coordinate, rather than fabricating a baseline fraction of `1` or `1/2`. The hypothesis of a relative-credit objection remains tested through the independent consent and attribution condition, and any comparison between **two proposals with an actually defined new differential** is permitted. The frozen v0.1 narrative acceptance remains available for traceability; this is a stronger, separately documented experimental treatment, not a retrospective rewrite of the source.

**Marketing / Operations / Systems:** the initial narrative acceptance used a *declared additional* experimental 15-unit cost allocation and 35-unit compensation, producing 55 units. The new operation runner returns to the **original [economic-pilot protocol](../economic-pilot-v0.1/STUDY_PROTOCOL.md)**: gross (60+40-30=70), transfer **40** and real reconfiguration inputs **6+4+2=12**, yielding **58** under its expressly transferable toy numerarium. The three net participant payoffs (14,36,8) are computed from the separate inputs, and authority remains **UNKNOWN**. Both treatments are labeled with their actual assumptions; they are not silently equated.

**Two bananas:** (S_0\to S_1\to S_2) is calculated by an operation to produce two fruit and another to move one from waste to the child, conserving material. The source's (B_1=5,F_1=7,W_1=-2) is a **stipulated toy welfare illustration**, not a number derived from fruit counts or a measurement of a child/holder. The transfer (S_1\to S_2) remains blocked pending safety/authority evidence.

### Repeatable checks

```bash
python -B -m unittest discover -s . -p 'test_*.py' -v
python -B mechanistic_replay.py --manifest MECHANISM_CASES.json --output /tmp/acc_operation_results.json
# agentic source must be a local checkout of exact PR57 model/CASES.json:
python -B agentic_crosswalk.py --source-dir /tmp/acc_pr57_pinned_source --output /tmp/acc_agentic_analogue_results.json
```

The CI runs native Conscientia tests, both narrative and mechanical source checks, and pulls the **unchanged** pinned PR57 source into a temporary directory for explicit structural-analogue tests. All results are published as **synthetic trace artifacts** under the PR workflow. No original 00M/00N/EA/EP owner definition, UC21 case or source-owned policy has been changed.

**Research status:** execution of source-declared finite mechanisms, source-anchored negative tests and conditional physical transitions; not an empirical test, human welfare model, agentic equivalence of all 14 cases, or an identified general Pareto frontier in real society. The owner's original examples remain the acceptance criterion, including the right for some to remain formally unresolved.


### Independent conditional IQ-03 sensitivity (no competing source implementation)

The [finite feasibility stress-test helper](finite_feasible_gap.py) lives here in the **narrative acceptance supplement**, not in the canonical Conscientia source owned by [PR #68](https://github.com/dakleyer/structural-awareness-contributions/pull/68). It accepts a declared service question, finite capacity-limited technology alternatives, startup costs, resource intensities and eligibility/rights states. Its bounded solver chooses a least-resource combination **conditional on toy assumptions**, never claiming an externally available or authorized option.

The existing illustrative period values (100→80 input units for service 100; 110→65 for service 140) can be reproduced from stated rational intensity parameters. In [adversarial tests](test_finite_feasible_gap.py), modified costs produce no increasing gap, setup costs can eliminate the benefit, UNKNOWN eligibility preserves unresolved options, and a conventional choice can dominate. This sensitivity is supplementary to PR68's original IQ-03 example: it is **not** an alternative source of truth, a measured social economy, or a proof of growing debt.

### Ownership and integration with #66, #67 and #68

- #66: policy-only economic comparisons with the source receiver separately reported (L-04); no new social optimization theory.
- #67: source native physical response from the original producer; no access to the referee during public planning.
- #68: author-owned source campaign G-03, its forty variants and thirty native agentic cases. Its original source files and tests stay unchanged in their own PR.
- **#69:** distinct operation-sequence and counterfactual-to-commitment acceptance tests over fourteen preserved EX identities, plus source analogues and independently bounded sensitivity. It is a review aid for #68, not a replacement engine or a proof of equivalence between distinct questions.

The integration CI checks these boundaries together at explicitly pinned commits and publishes separate artifacts. No PR is automatically merged.
