# When a Declared Collective-Choice Operator Is Correct but Its Operating Frame Is Not Yet Qualified

**Theme #18 — external scientific discussion packet (candidate v0.1, 27 October 2026).**
**Author-side research concept:** Iván Abril Palma / The Integral Management Society. AI-assisted research synthesis. **NOT POSTED to FG-TIDA, not reviewed/accepted by Theme #18 members, not an ITU-T work item, and not empirical validation.** This is a compact *review invitation*, not an implementation requirement.

## The proposal in one paragraph

FG-TIDA Theme #18 already asks how a multi-objective agentic system declares and measures its collective-choice operator and regime, including which objectives/"voters" participate, what modes exist and which transitions are permitted. This proposal adds a distinct, testable external-evaluation object: **continued decision-frame adequacy**. Even when the declared operator is correctly implemented and action-level conformance passes, the system may lack evidence that the mode's observation context, feasible actions, objective measurements or admissible candidate set still support **this consequential choice at the relevant time**. Regime Awareness (RA) can provide **qualified, representation-relative evidence of environmental departure**; Ecosystem Awareness (EA) can qualify its relevance, provenance, unresolved distinctions and legitimate next inquiry. A new operational representation may also be required **without a positively detected environmental change**. Neither RA nor EA declares a replacement operator, grants authority or executes a transition.

**What is already theirs:** [Theme #18 and its collective-choice proposal](https://github.com/FG-TIDA/themes/issues/18), [Arnaud's regime/mode example](https://github.com/FG-TIDA/themes/issues/18#issuecomment-5492408009), [X.dmst design-time relationship](https://github.com/FG-TIDA/themes/issues/18#issuecomment-6247541576), [#18/#6 pinned-conformance distinction](https://github.com/FG-TIDA/themes/issues/18#issuecomment-6255006005), [#16 oversight qualification](https://github.com/FG-TIDA/themes/issues/18#issuecomment-6301230176). We **do not** claim discovery of operator/regime separation, voter-version mismatch, choice-rule impossibility or population drift.

## Two independently falsifiable claims

**H18-A (change of observable regime).** Under a declared observation map Ψ, a properly selected and qualified history H, a structural descriptor I and explicit threshold/delay scope, there can be a material deviation from the recent observable regime while the operator, voter set and declaration version remain unchanged. RA's reported departure is an **input to** review; it does not prove a hidden cause, identify safety-criticality beyond Ψ, or prescribe the correct new mode. A properly qualified neutral signal does not certify the mission-level frame. **Falsifiers:** ordinary noise, invalid/stale H or B, equivalent strong conventional monitoring, no decision-relevant change, unusable detection delay or net-negative intervention.

**H18-B (change of decision-sufficient representation).** A previously correct interface may cease to support a newly admissible operation, decision question or candidate class even with *no* observed operator drift and *no* positive RA departure. In the finite declared model \((X,o,r,\Sigma)\), exact deterministic quotient adequacy requires:

\[
\ker(o)\subseteq\ker(r),\qquad
o(x)=o(y)\Rightarrow o(f(x))=o(f(y))
\quad(\forall f\in\Sigma).
\]

A four-state counterexample establishes failure after adding an operation \(f\): \(o(x)=x\bmod2\), old transition \(s(x)=x+1\bmod4\), new \(f=[1,1,0,3]\), and \(o(0)=o(2)\) but \(o(f(0))\ne o(f(2))\). **This is known quotient/congruence mathematics** in a declared finite model, not a novel impossibility theorem or a real-world inference. A sound conventional set-valued abstraction may still give an adequate lawful decision, so exact quotient failure is **not itself a mandatory HOLD**.

In a further small instance, additional source Q should be chosen *conditional on what o already distinguishes*: \(X=\{0,1,2,3\}\), \(o(x)=\lfloor x/2\rfloor\), \(r(x)=x\), \(Q(x)=x\bmod2\). Q alone does not suffice, but (o,Q) does: the two remaining same-o/conflicting-r pairs are separated at one declared incremental Q cost. Source eligibility, rights and cost remain independent prerequisites.

## Illustrative multi-objective examples with precise nonclaims

**Example 1 — fixed operator, changed operating context (synthetic).** Predeclare the operator as a hard safety veto followed by a cardinal \(service-cost\) score, with a stable voter set and reference version. Initially both failover and stop are marked safe: failover has service 5, cost 1 and score 4; stop scores 0. A qualified *toy* capacity departure (10 to 7, threshold 2) provides a **review trigger only**. **Independent** new safety evidence then finds failover unsafe: the **same operator** selects stop. Without that independent safety evidence, RA's negative direction does **not** establish which option is safe. The [finite fixture and executable check](./09_THEME18_FINITE_FIXTURE_CASES_v0.1.json) reproduce only these assumptions and arithmetic, not an actual RA detector or 6G system.

**Example 2 — admission and actual opportunity are different (synthetic; anchored to a distinct PR).** A source-preserving [agentic ACC extension on PR #57](https://github.com/dakleyer/structural-awareness-contributions/pull/57) has **two physical resource providers** and **four separate abstract observers**. Four independently identified local admission rejections about **one actually captured event** characterize a shared admission complement; the corresponding event is not yet evidence of a better feasible candidate. A separate, bounded, source-qualified positive claim and actual **post-exchange candidate arrival** are required before proposing a change. In its three staged synthetic reference outcomes, current mission output is **10**, remains **10** when only a blocked near-opportunity is known, and becomes **11.5** under a new gate with a valid candidate, authorized transfer and a separately assumed source-to-AG01 correspondence. The **13.5** technical optimum is *offline-referee knowledge*. The original PR57 Q_META_PROTOCOL did **not** include the new arrival gate: this is a **new overlay**. A conventional peer given identical Q, permissions and event may tie. The [new PR60 candidate-admission checks](./test_theme18_candidate_admission.py) validate only the logical boundaries, **not** the PR57 production model or its underlying economics.

**Example 3 — retaining an unresolved event and changing interpretation at runtime.** [SA-O2/O4/O5](https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/structural-awareness/SA_OPERATIONAL_RESIDUAL_AND_ONLINE_CONTEXT_PLASTICITY_v0.1.md) establishes restricted conditions in which a pre-admission captured-but-unresolved event may be reinterpreted upon receiving a valid new certificate, whereas a permanently dropped event cannot be recovered from the reduced output. It also identifies a finite class where a sound, scoped and properly costed proof guard can replace repeated evaluation work **without changing the substantive verdict**, even if it adds zero target-state Shannon information. [Finite controls](./test_theme18_online_context.py) test these boundaries. Neither fact entails an externally detectable physical regime change or exclusive advantage over an equally equipped conventional controller.

## A possible transport-neutral evidence record

**Candidate semantics only, not #18's agreed API:**

| Field cluster | Minimum bounded content |
|---|---|
| Declared choice reference | Decision ID; declarer and standing reference; operator, voter inventory, mode, choice regime, authorized transition conditions, version, validity and policy scope |
| Observable RA report | Ψ/context/baseline/threshold/delay and freshness; qualified deviation **or explicit unavailable/UNKNOWN**; source exclusions; no unqualified "neutral" |
| EA receiving qualification | Decision-specific adequacy statement; defined receiving question; existing A; B sources with rights; C/D or UNKNOWN qualification; source independence; evidence, test witnesses, expiry, budget and deadline |
| Candidate-domain qualifier (when material) | Admitted choice domain; explicit local admission predicates; actually received new candidate and first capture source/time; separate positive quality evidence; new interpretation/version and permission gates |
| External handling | Distinct #5 authority and #6 act-time verdict; #16 oversight if needed; #21 population evidence where scoped; actual execution receipt and separate observed effect |

**Status vocabulary proposed only for research:** REFERENCE_UNDECLARED / STALE; RA_QUALIFIED_DEPARTURE / RA_QUALIFIED_COMPATIBLE / RA_UNKNOWN; FRAME_ADEQUATE_IN_SCOPE / REQUALIFY / UNDERDETERMINED; CANDIDATE_NOT_RECEIVED / CANDIDATE_REQUIRES_EVIDENCE / CANDIDATE_ELIGIBLE_FOR_CONTROL_REVIEW; CONTROL_NOT_EVALUATED_HERE. No single scalar or status conflates these.

## Suggested two-stage external evaluation

**Stage A (available now, source auditable):** review this note and supporting documents, replay [Theme 18's ten finite source predictions](./09_THEME18_FINITE_FIXTURE_CASES_v0.1.json), [source-to-contract reconciliation](./11_THEME18_20261027_CORPUS_RECONCILIATION_AND_ADMISSION_CONTRACT_v0.1.md), [candidate tests](./test_theme18_candidate_admission.py), and [online-context tests](./test_theme18_online_context.py); independently challenge the math, source trace and scope. These toy tests are not a substitute for independent empirical evidence.

**Stage B (NOT executed):** obtain an actual authored Theme #18 representative choice reference; build separate RA observable report, EA receiving sufficiency check and #6/#5 control adapter with independent source verification. Freeze **prospectively** the mission/rights/information opportunities and competent conventional equivalent access, full preparation and reconfiguration costs, noise, latency, attacker and source independence, and legitimate positive-change paths. Evaluate both correctly permitted continuation and unwarranted false HOLD; ties and stronger conventional performance are valid negative results. **No hand-selected post-failure optimum or zero-cost retrospectively configured peer**, but equally no intentionally deprived baseline.

**Submission boundary:** No publication to [Theme #18](https://github.com/FG-TIDA/themes/issues/18) has been made by this research PR. The scope, wording, permission to share, source rights and any external handoff require a separate explicit author decision. The status of this note is **for review**, not an ITU-T technical specification.
