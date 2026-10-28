# Economic envelope K-01 — reusable comparative execution across ACC social and agentic sources

**28 October 2026 · source-owned research extension · Python standard library.**

This package turns the K-01 cost sensitivity into a configurable **economic comparison service**, while calling the **existing model's own policy, producer, receiver and referee**. It changes no theory, A/B/C/D class, physical mechanism, objective, permission, frozen UC21 case, or original result.

## 1. The precise comparison

Source of the finding: [incremental scientific audit #58, K-01](https://github.com/dakleyer/structural-awareness-contributions/pull/58). Source of the finite social model: [#44](https://github.com/dakleyer/structural-awareness-contributions/pull/44). Source of the six agentic policies: [#57](https://github.com/dakleyer/structural-awareness-contributions/pull/57).

For the original #44 one-question cost assumptions,

\[
C_B(L)=0.25L+0.75,\qquad C_{directed}=3,\qquad
C_B(L)=C_{directed}\iff L=9.
\]

The original balanced tree has \(L=\log_2(n)+2\) along the tested powers-of-two sizes. Thus n=16: B 2.25 < directed 3; n=64: B 2.75 < 3; n=128: tie; n=256: directed 3 < B 3.25. **These are consequences of the declared prices, not a universal scaling theorem.**

To avoid a favorable cost assumption masquerading as an architectural law, the comparator accepts two *independent* affine schedules
\(C_B(L)=b_0+b_1L\), \(C_T(L)=t_0+t_1L\). It computes the exact crossover, including no-crossing and all-tie regimes, without changing the study's source code. For path-priced conventional peers, the caller computes the corresponding target price at each path length and passes it through the original `Costs.target_observation` parameter.

## 2. Source-native architecture

| Component | Stable API | Owned meaning |
|---|---|---|
| [Exact comparison kernel](economic_envelope.py) | `ComparisonFrame`, `CostLedger`, `ArmObservation`, `compare_case`, `run_cases`, `summary`, `affine_cost_crossing` | Exact pricing and ranking for one question; no simulation or execution permission |
| [Original source adapters](economic_envelope_adapters.py) | `intrinsic_observations`, `agentic_observations`, restricted price-override functions | Source model supplies its own policies, evidence, physical A, outcome, costs and permissions |
| [Experiment runner](economic_envelope_runner.py) | `execute(manifest, corpus_root, model=...)`; CLI | Traverse a user-defined grid, call original modules, pin source SHA256 and report results |
| [Scenario manifest](ECONOMIC_SWEEP_MANIFEST.json) | Editable JSON matrix | n, resource headroom, source access, source prices and agentic case-cost regimes |
| [Adversarial controls](test_economic_envelope.py) | Python `unittest` | Preserve one-question identity, native accounting, source A, rights, ties, loss cases and original arm decisions |

Any third party can call `compare_case` with `ArmObservation` records obtained from their *own* model. They need not implement ACC. A comparison is accepted only when all arms share exactly the same source model, case, **receiving question**, scope, metric, unit, horizon, baseline A and public contract fingerprint. It rejects mixed evidence kinds, non-finite/boolean prices, negative/duplicated cost charges, inconsistent native totals and duplicate arms. UNKNOWN gross is not turned into zero. Ties remain ties.

Each arm has a **source-authoritative gross outcome**, an itemized *instrument-cost* ledger, and a checked native net. When the original source records a penalty for a false promise, that penalty is preserved; the kernel never replaces it with an invented value function. A cross-case report counts winners **by model**; it never sums different objectives into a global utility.

## 3. Social source #44 — multiple actual exercises

The adapter invokes `upstream_B`, `policy` for A_ONLY, B_QUALIFIED, TARGETED_EXPLORATION_OF_A and FULL_EXPAND_A, and `receiver_decision` for the source's already-existing public planner. It calls the real `deliver` through the native scoring functions; it does not reproduce the physics in this package.

The default manifest spans:

- 7 leaf counts: 4, 8, 16, 32, 64, 128, 256.
- 3 root-capacity regimes: unconstrained, 1 unit headroom, saturated.
- 2 access regimes: source available, target source inaccessible.
- 4 declared prices: original, cheap conventional peer, peer charged per path, high B acquisition.

That is **168 distinct question/cost combinations** (5 source-native arms each) in the delivered manifest. External manifests can also set `capacity_patterns` to `selected`, `all`, `none`, `alternating` or an explicit list of source leaf indices, and set `planner_budget` per price regime. These controls feed the **original** world factory and public receiver; they do not change either algorithm. It retains cases where B wins, a conventional comparator wins, conservative A wins, no qualification exists, or the receiver rejects costly B. It does **not** add jointly valid \(B_q\) certificates: [K-02 source guard #65](https://github.com/dakleyer/structural-awareness-contributions/pull/65) still applies, and joint resource scheduling stays with the separate DG3 source-owned producer/reservation work in audit #58.

## 4. Agentic source #57 — its full 30-case campaign

The agentic adapter executes `run_case` on each original scenario and reads **all six native policy arms**, including Q_REVIEW_ONLY, Q_META_PROTOCOL, CONVENTIONAL_EQUIVALENT_Q, CONVENTIONAL_DIRECTED and FULL_A_IF_AVAILABLE. The source decides under its original mission, resource budget, rights, consent, Q validity, technical options, costs and uncertainty; our accounting reads its **post-hoc referee output** afterward.

Configurable regimes vary **only** `Q.cost`, `directed.cost`, `directed.equivalent_Q_cost` and `full_A.cost`; the adapter rejects attempted changes to private productivity, mission, rights or resources. The default grid exercises the unchanged 30-case registry under source-native, cheap-directed, expensive-Q and equal-Q-peer regimes (Q-only variants skip cases where no Q exists). All six policy decisions and their gross/net values remain the source's own.

Physical resource overhead is **already inside the native output**: subtracting it again as a monetary cost would double count. The ledger therefore charges only the native `instrument_cost`; its sum and the calculated net are reconciled with source fields. This lets cost-only sensitivity be separated from the substantive ability to **discover, authorize and execute** a new mission-improving transfer.

A Q-based and an information-equivalent conventional peer with the same price are expected to tie whenever the source gives them identical decisions. Such a tie is *preserved*, not silently rebranded as unique agentic superiority.

## 5. Integration with the 13:00 work and corpus ownership

- **PR #60 — SA F1/D1 and exact qualified gain:** `assess_finite_adequacy` decides finite structural sufficiency; `compare_gain` evaluates qualified, metric-matched intervals. This package does neither. It prices and compares **already source-produced policy effects**, one question at a time. For an implementation with interval evidence, the source qualifies it through the #60 contract before adopting an economic gain claim.
- **PR #58 — DG1–DG4:** decision-memory refinement, temporal sufficiency, shared-resource reservations and risk coordination are distinct mechanisms. This accounting module can receive their policy outputs; it does not replicate their algorithms or assume an unverified joint B.
- **PR #62 — FRA and heterogeneous objective envelopes:** economics is always reported **by participant/question/metric**, without merging competitive objectives or declaring an optimum across the ecosystem. Discovered architecture candidates and legitimate selection/authority keep separate owners.
- **DDS / UC21 / 00D:** the new rows are internal sensitivity controls, not new normative UC21 scenarios, new DDS Stage B/C proof, or new canonical benchmark arms.

The implementation lives in a dependent PR against **#57's open research branch**, so both source engines are present for its CI. It does not edit #57's code, fixtures or reference results; #44's original source, #60 and #65 are unchanged.

## 6. Run and extend

From the repository root:

```bash
python -B -m unittest discover -s research/ecosystem-awareness/baseline/01I-artifacts/acc-auxiliary-model-v0.1/studies/intrinsic-abcd-economics-v0.1 -p test_economic_envelope.py -v

python -B research/ecosystem-awareness/baseline/01I-artifacts/acc-auxiliary-model-v0.1/studies/intrinsic-abcd-economics-v0.1/economic_envelope_runner.py --corpus-root . --model both

python -B research/ecosystem-awareness/baseline/01I-artifacts/acc-auxiliary-model-v0.1/studies/intrinsic-abcd-economics-v0.1/economic_envelope_runner.py --corpus-root . --manifest YOUR_MATRIX.json --details
```

The JSON output includes the matrix hash, original source SHA256s, K-01 crossing, counts of ties and strict winners by model, and optionally the full per-arm ledgers. An external application can supply a different source adapter via `run_cases(scenarios, adapter)`, preserving the same source/evidence/cost contract.

**Review focus:** verify the claim remains situated, source policies run without oracle-assisted choice, all six agentic arms retain their original mission/resource envelope, and the original 00M/00N/ACC/EP boundaries are unchanged.
