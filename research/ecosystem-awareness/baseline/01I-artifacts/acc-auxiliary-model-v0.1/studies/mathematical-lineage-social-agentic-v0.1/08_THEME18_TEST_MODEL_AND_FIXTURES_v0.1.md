# 08 — Theme #18: preregisterable test model, multi-objective examples and falsifiers

**v0.1 · 27 October 2026 · Stage A test-design instrument, not a test-results report.** Companion to [07 — issue-to-interface analysis](./07_THEME18_COLLECTIVE_CHOICE_REGIME_ADEQUACY_INTERFACE_v0.1.md), [02 — finite formal core](./02_FORMAL_CORE_AND_PROOFS.md), [05 — independent validation](./05_INDEPENDENT_VALIDATION_PROTOCOL.md) and [PR #57 agentic-reduction scenarios](https://github.com/dakleyer/structural-awareness-contributions/pull/57). **No joint Theme #18/RA/EA system or cross-theme tests have been run under this annex.** Fixture records are [09](./09_THEME18_FINITE_FIXTURE_CASES_v0.1.json); their `expected` fields are **declared predictions** rather than measured outputs.

## 1. What would make Regime Awareness *necessary* for a particular #18 decision?

Distinguish three propositions that test programmes often blur:

- **Change exists:** external or model/contract conditions materially differ (`\rho_t\ne\rho_{t-1}` under a declared equivalence). It may be invisible to the available instrumentation.
- **Change matters:** two otherwise observationally equivalent states under existing `o` require different admissible decisions/qualifications for a *predeclared* target `r`, or a previously qualified transition model ceases to be adequate.
- **Additional regime-relevant information is necessary:** there is no common allowed decision for the current evidence fiber and neither existing qualified `o` nor another existing lawful source resolves it before the decision deadline.

Only under **predeclared scope and qualified assumptions** can the third property justify requiring an extra capability. It does not prove that an implementation branded "Regime Awareness" is the unique or cheapest solution: a capable conventional controller with the same qualified observation can implement the same function.

A *RA signal can be decision-useful without being mandatory*: it may shorten detection delay, support earlier requalification, improve an authorized choice, or avoid wasted queries. Conversely, there is **no positive RA claim** when the physical change is unobservable under `\Psi`, or when there is no validated context/baseline. Preserve UNKNOWN.

## 2. Formal testing objects and independent ground truth

Freeze a test case before scoring, with these independently authored fields:

| Object | Owner | Minimum specification |
|---|---|---|
| `\mathcal D_{18}` | Reference designer / legitimate policy authority | Authored version, objective/voter set, operator, choice-axiom regime, mode, admissible alternatives, normalization and constraints, transition triggers, source/expiry and grant standing |
| `X,\Sigma,o,r` | Independent fixture author | Qualified finite world states and eligible operations; presently available observations; decision question `r`, not inferred from result |
| `\Psi,I,H,B,\tau,\ell` | RA candidate designer under referee audit | Observable map, contextual sufficiency criterion, recent baseline, thresholds/sign semantics, missed-change class, detection delay and invalidity handling |
| `Q_j,\kappa_j` | Independent sources / rights assessor | Discriminating source facts, evidence provenance, version, freshness, access/license/rights, cost and independence; not the referee's secret state |
| `C,V,C_{\rm total}` | Existing operational owner | Resource/mission constraint, governance-feasible alternatives, utility/partial order, action permissions, cost and useful horizon; no hidden free transition |
| `W_t` / source-world truth | **Offline referee only** | Actual generated environment, mode/operation change and authorized feasible outcomes for post-decision scoring, never a runtime API |
| `H_0,H_1,...` | Evaluation team | Frozen policy arms, identical observational rights, source feeds, admissible queries and real cost ledger |

Decompose outputs into: **(a)** exact observation/regime finding, **(b)** reference/version finding, **(c)** choice operator and winner/cycle, **(d)** interface/decision sufficiency, **(e)** admissible evidentiary next steps, **(f)** conformance/authority received separately, **(g)** measured outcome. No field may silently stand in for another.

## 3. Arm design: no intentionally crippled conventional alternative

| Arm | Available capabilities | Main measurement |
|---|---|---|
| **R0 — current declared reference, competent conventional** | #18 reference; required #5/#6 checks; best conventional context/monitoring and evidence sources **actually available** under the same rights; action abstention when necessary | Adequacy/error and costs of current best practice |
| **R1 — RA observation qualification added** | R0 + **independently validated** `\Psi/H/I/B/\tau/\ell` report and valid UNKNOWN when context fails; does not add evidence the competing monitor was prevented from seeing | Marginal effect of qualified departure evidence |
| **R2 — RA + EA decision requalification** | R1 + source/decision-scope composition and conditional residual-based targeted inquiry; no policy authority | Marginal effect of scoped adequacy and query selection |
| **R3 — strong equivalent conventional peer** | All R2 evidence, certificates and permissions, using conventional formal monitors, abstract interpretation, constraint solver and targeted observation, with measured costs | **Primary differentiation falsifier**: expected tie when equivalent |
| **R4 — offline full-information referee** | True generated world, optimal eligible action, future outcome **for scoring only**, not a deployable comparator | Actual false assurances, unnecessary HOLD and bounded regret |

Run R0/R1/R2/R3 on **the same declared mission, candidate set, raw measurement/evidence eligibility, access rights and budget**. If RA/EA changes the *available information* under R1/R2, document that new source and its acquisition cost explicitly; provide an equivalent eligible conventional route in R3. Do not compare a new source to a baseline prohibited from using the same source. R4 must not leak answers into `Q_j` or normal operation.

If the practical question is only whether qualified signals help rather than architectural differentiation, compare **source absent vs source present** separately and clearly label it an *information-access effect*, not superiority over a competent peer with the same information.

## 4. Main example families — exact contrast, no fabricated empirical result

### T18-RA-01 — Environmental departure; operator remains fixed

**Source inspiration:** Arnaud's 6G normal/degrade/critical-stop discussion, [#18 comment](https://github.com/FG-TIDA/themes/issues/18#issuecomment-5492408009). Construct a *new independent toy*, not a reconstruction of an ITU system. Freeze operator as a **lexicographic safety veto followed by a cardinal objective score**, voter set V and declaration version v1. In normal context, both feasible candidates meet the hard veto. Exogenous validated "capacity degraded" is a *qualified RA observable departure*; a critical-service flag may be missing or obtained only by a separately permitted source Q.

- **Necessary observation:** choose matched worlds with identical past choice outputs and current operator ID, but different service-criticality / system-capacity conditions that change admissible fallback decisions. Publish the sensing limits; do not assert RA sees the criticality if `\Psi` cannot.
- **Expected:** a qualified departure causes EA to question the *normal-mode assumptions*; a separate authorized, versioned policy decides degrade vs safe stop **after criticality evidence**. #6 checks actual act-time action against the updated pinned reference. An RA alert is never the transition permit.
- **Negative:** noise below a valid threshold; the operator changes legitimately with a valid version and no physical departure; same new condition but all still-allowed decisions coincide, so no extra Q is required.

### T18-RA-02 — Reproducible four-state interface insufficiency

**Source:** PR #60 [02 `2 D1](./02_FORMAL_CORE_AND_PROOFS.md). Model `X=\{0,1,2,3\}`, `o(x)=x\bmod2`, old operation `s(x)=x+1\bmod4` and new operation `f=[1,1,0,3]` indexed by x. Initial fixed target `r=o`.

- Before the signature change, `o` is sufficient for `r` and respects `s`.
- After admitting f, `o(0)=o(2)` but `o(f(0))=1` and `o(f(2))=0`; the previously exact deterministic observational quotient fails.
- **Expected:** `EXACT_OPERATIONAL_QUOTIENT_INADEQUATE` with witness (0,2), **not** "operator drift" or a claim that RA identified a hidden physical change. A competent set-valued monitor can produce successor set `\{0,1\}`; evaluate whether that is sufficient for the receiving decision rather than forcing HALT.
- **Negative:** retain only `s`; add a new f that preserves parity; provide a completely discriminating authorized source; or choose a receiving question with the same lawful disposition in both states.

### T18-RA-03 — Supplementary Q must be conditional on already available A

**Audited correction source:** [PR #59 finding D26-F08](https://github.com/dakleyer/structural-awareness-contributions/pull/59). Use `X=\{0,1,2,3\}`, already available `o(x)=\lfloor x/2\rfloor`, independently defined `r(x)=x` and eligible unit-cost `Q(x)=x\bmod2`.

- Given **Q alone**, states 0 and 2 remain identical, so `r` does **not** factor through Q.
- Given **(o,Q)**, all four states are distinguished exactly. Only two already-o-equal, r-conflicting pairs require separation: (0,1) and (2,3).
- **Expected:** conditional `U_{r\mid o}` coverage succeeds with incremental Q-cost 1, given valid rights/source; Q-only set-cover must not mistakenly report "not obtainable". Q is not automatically epistemic-B until independently source-qualified.
- **Negative:** Q depends only on o; Q expired/ineligible; `r` already factors through o (zero marginal information value).

This test is a **known corrective obligation**, not an already-applied repair to [02 D3](./02_FORMAL_CORE_AND_PROOFS.md) or [03 P3](./03_METAPROTOCOL_ALGORITHMS_AND_COST.md).

### T18-RA-04 — Same present A, different capacities; ACC/AG01 and AG11

**Source:** [PR #57](https://github.com/dakleyer/structural-awareness-contributions/pull/57), AG01/AG11. Initial resources A=6 and B=4, present service=10; marginal productivity of B differs between states yet both present the same functional output. A **source-labelled, partially scoped** Q can specify a lower bound for a bounded transfer. **Q is not authenticated by the current synthetic planner**.

- **Qualified positive fixture AG01:** a 2-unit authorized transfer is calculated to produce service 11.5; the offline technical optimum 13.5 is *not* attainable solely from Q for decision rights and contract boundaries. The conventional peer with equivalent Q follows the same branch and can tie.
- **False Q fixture AG11:** an apparently valid-labelled bound can lead to output 8.875, worse than current service 10. Expected external-evaluation finding: **source-authentication/independent verification gap**, not proof an actual RA detector would have prevented it.
- **Decision use:** a change to the collective-choice objective/weights, utility constraints or feasible actions could make Q material. Freeze the choice rule and source evidence separately to identify *what actually changed*.
- **Controls:** absent consent (AG07), undeclared metamorphosis (AG05), material D (AG09), cheap directed inspection, same-Q strong conventional peer. No free resources or authority created.

### T18-RA-05 — Objective/voter set change, operator unchanged

**Source:** Arnaud [X.dmst proposal](https://github.com/FG-TIDA/themes/issues/18#issuecomment-6247541576), Cyril's [stale-reference fixture plan](https://github.com/FG-TIDA/themes/issues/18#issuecomment-6255006005). Freeze a two-alternative scoring calculation with two voters (security/privacy) and a fixed aggregator. Remove privacy while retaining the same operator code.

- **Version increments**: #6 can identify a pinned-reference mismatch at action time; no RA environmental alarm required for this detection.
- **No version increment**: a single action record may not expose the voter-set change; test independent #21 population data/instrumentation and remain unresolved where identifiability fails.
- **Expected:** distinguish `STALE_REFERENCE` / `UNOBSERVABLE_VOTER_CHANGE` from `OPERATOR_DRIFT` and `ENVIRONMENTAL_REGIME_DEPARTURE`.

### T18-RA-06 — Condorcet cycle is not regime departure

**Source:** [Arnaud's runtime cycle clarification](https://github.com/FG-TIDA/themes/issues/18#issuecomment-6173025205). Voters: (a>b>c), (b>c>a), (c>a>b). Condorcet majority relation cycles a>b, b>c, c>a. The relevant conflict emerges from **the declared choice rule and profile**.

- **Expected:** `CYCLE_NO_UNIQUE_WINNER` as #18 mechanism result; #6 escalation/indeterminate handling per **pinned policy**, not automatically `P_{\mathrm{RA}}=+1`. Human intervention requires an applicable standing/oversight route; the detector does not invent it.
- **Negative:** an explicitly declared lawful cycle-resolution rule; a noncyclic profile; a cycle discovered without any evidence of physical regime change.

### T18-RA-07 — RA context invalid, not neutral

**Source:** [EA–RA 01C](../../../../01C_EA_REGIME_AWARENESS_INTERFACE_ANNEX_v0.2.md) and [01D](../../../../01D_EA_MSCA_RA_OPERATION_COMPOSITION_PROFILE_v0.1.md). Hold a numerical score at the baseline but expire `\Psi`, its source contract, or its contextual boundary. Do not allow an out-of-date neutral report to be reused.

- **Expected:** `RA_UNKNOWN_UNSUPPORTED_CONTEXT`; no `P_{\mathrm{RA}}=0`. EA preserves relevant residual, identifies qualified next inquiry or abstains; **an independent action that did not rely on RA may still be admissible**.
- **Negative:** fresh, qualified signal with no departure reports `P_{\mathrm{RA}}=0` but does **not** prove whole-ecosystem normality.

### T18-RA-08 — Observational aliasing: mode, operator or sensor

**Source:** [Pam's three-way identifiability problem](https://github.com/FG-TIDA/themes/issues/18#issuecomment-5494021998), [Theme #18 hostile trace](https://github.com/FG-TIDA/themes/issues/18#issuecomment-5498414499). Construct at least two distinct (mode, operator, observation-channel) triples that yield exactly the same finite choice trace but different held-out results. If the probe travels through the same corrupted channel, it need not resolve them.

- **Expected:** compatible explanation set with explicit evidence coverage and UNKNOWN cause; identification only after **eligible, independent distinguishing** evidence actually separates hypotheses.
- **Negative:** pretending additional copies of the same trace are independent source evidence; claiming operator drift when the true difference was an authorized mode switch.

### T18-RA-09 — Local pass, population signal, ecosystem-frame question

**Source:** [Theme #21](https://github.com/FG-TIDA/themes/issues/21), RA [R10 population example](./02_FORMAL_CORE_AND_PROOFS.md) and [#16](https://github.com/FG-TIDA/themes/issues/18#issuecomment-6301230176). A succession of locally conformant agents can coexist with a material, changing population/participant set, or correlated evaluator failure.

- **Expected:** #21 supplies explicitly scoped population evidence (with dependence and identifiability limits). RA tests only the chosen observable structural change, EA assesses materiality for a mission. #16 may receive an exceptional requalification request. No global authority is inferred.
- **Negative:** local pass does not imply global-frame adequacy; conversely a population metric change alone does not authorize shutting down all agents.

### T18-RA-10 — Sufficient existing observation; no extra Regime Awareness required

Use arbitrarily complex hidden interiors but choose `r=h\circ o` and all admitted transitions congruent on `o`. Strong incumbent already carries necessary version/authority and context data.

- **Expected:** `ADEQUATE_FOR_DECLARED_DECISION` or an equivalently justified conventional result; **no mandatory Q**, no claim of unique RA value and no avoidable escalations.
- **Negative:** if our candidate always flags a regime problem or forces queries, the design fails specificity/economy.

## 5. Required prospective measurements

1. **Reference integrity:** authenticated/versioned reference resolution, falsely accepted stale voter set, illegal mode change, missing declarer/standing; none silently treated as operator drift.
2. **RA detection:** defined event class; false alert, missed change, detection delay, sign stability, scope loss, baseline drift, representation/context invalidation and out-of-window latency; source-independent measurements.
3. **Decision adequacy:** decision-specific false CERTIFIED, excessive HOLD, justified CONTINUE, legitimate positive mode transitions, uncovered fibers/witnesses and independently scored outcomes.
4. **Information and cost:** extra source Q eligibility and authenticity, baseline A costs vs incremental Q costs, proof verification, computation, source licenses, communication, human review, transition/rollback and deadline misses.
5. **Control/authority:** unauthorized transitions/action dispatch must be zero in a passing safety profile; #6/standing verdicts checked separately and pinned to exact action/time.
6. **Strong-peer delta:** R2 vs R3 net value, decision regret and effect under matched access; report ties and losses equally, with exact model qualification or uncertainty bounds, never broad "agentic win" percentages.

**No globally fixed numeric success threshold:** each deployment fixes admissible false positive/negative costs, non-inferiority and execution delay **before tests**. A mathematical witness is not an empirical sensor-validation result.

## 6. Evaluator's gate and stop rules

**Stage A (present PR):** publish source-faithful interface analysis, candidate payload, formal fixtures, oracle/assumption separation, false-certification tests and unresolved research items. The JSON file is a frozen proposal for tests, not observed data.

**Stage B0:** reconcile PR #59's conditional-Q correction *in* 02/03 and underlying callers; independently freeze #18 reference fixtures, world generator, witness alternatives and a competent same-source conventional baseline. Resolve #58's equivalence-by-code and PR #60 attribution/rights review. Ensure no #18 team accepted/provided a field spec unless a real comment or artifact says so.

**Stage B1:** implement reference scorer, RA observable detector/context validator, EA qualifier, Q selection, strong peer and #6 **adapter** as separate components; execute true matched tests with complete traces. The named program **must not** fabricate an action permit.

**Stage B2:** independently generated out-of-sample objectives, exogenous mode triggers, noisy sensor and hostile channels, delayed/false Q, competing grants, new voters and dynamic populations; actual latency, source review cost and release policy.

**Rejection gates:** false actuation, source/authority fabrication, known incorrect exact-factorization result, stale neutral reported as valid, original/derived theorem misattribution, unknown real-world state claimed measured from a finite toy, or systematic inability to distinguish decision relevance from ordinary noise. "No added advantage over strong R3" is an **acceptable negative scientific result**, not a reason to suppress evidence.

**Potential external FG-TIDA artifact only after owner approval:** 3–5-page technical note with the interface contract, one exact four-state witness, one independent multiobjective environment-change case, full negative controls, and links to publicly reviewed proofs/fixtures. Do **not** attach the entire internal mathematical lineage or present this Stage A as an accepted standard.