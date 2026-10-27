# 07 — FG-TIDA Theme #18 × Regime Awareness: multi-objective choice and continued regime adequacy

**Research annex v0.1 · Stage A · 27 October 2026 · owner review required.** This is an **informative source-to-interface study in the open PR #60**, not a submission to FG-TIDA, an approved interface, an implemented detector, a scientifically validated tool or a normative ITU-T proposal. Origin of architectural synthesis: Iván Abril Palma / The Integral Management Society; technical drafting is AI-assisted. [Evidence and test protocol](./08_THEME18_TEST_MODEL_AND_FIXTURES_v0.1.md) and [machine-readable miniature fixtures](./09_THEME18_FINITE_FIXTURE_CASES_v0.1.json).

> **Research question.** When can an agentic system remain conformant to an authored multi-objective choice reference while the observable operating regime, the admissible action domain, or the information supporting that reference has become inadequate for a particular consequential decision? What qualified, bounded evidence would justify requalification without letting a detector silently choose a new operator or mint new authority?

## 1. What Theme #18 actually owns — source-grounded, not inferred

The source is [FG-TIDA Theme #18](https://github.com/FG-TIDA/themes/issues/18), including its original research questions and subsequent public dialogue, read on 27 October 2026. This table distinguishes issue-owner discussion from our proposed interface. It does **not** claim that discussions have been formally adopted by FG-TIDA or ITU-T.

| Source / public development | What is explicitly on the table | Boundary for this annex |
|---|---|---|
| [Original #18 proposal](https://github.com/FG-TIDA/themes/issues/18) | Collective-choice analogy for conflicting objectives; testable, **unproved** mathematical-bijection hypothesis; operator catalogue, declaration and estimation of effective operator/drift, regulatory bridge; observability, adversaries and runtime costs | Do not assume Arrow applies unchanged to all cardinal constrained optimizers; do not invent another operator catalogue |
| [Arnaud on Pam's regime point](https://github.com/FG-TIDA/themes/issues/18#issuecomment-5492408009) | Operator, regime, mode and transition conditions must be distinguished; lexicographic veto, cardinal scalarization and constrained optimization can coexist in different modes; external signals can trigger a transition | RA must assess **observable applicability**, not simply redetect an already declared transition |
| [Pam on identifiability](https://github.com/FG-TIDA/themes/issues/18#issuecomment-5494021998) | A declaration is the measurement reference; from outputs alone, mode transition, operator drift and measurement bias can be jointly unidentified; authority matters for external triggers and probes | No unique-cause or probe-success claim without observation-channel and authority assumptions |
| [#18 / #6 cross-theme mapping](https://github.com/FG-TIDA/themes/issues/18#issuecomment-6171043104) and [#36](https://github.com/FG-TIDA/themes/issues/36) | #18 supplies the referenced choice rule; #6 checks a **single action at act time** against a pinned authored reference, with permit/remediate/block/escalate/indeterminate vocabulary; #5 supplies grant standing | RA and EA produce **evidence/adequacy assessments**, never #6 verdicts or grants |
| [X.dmst linkage proposed by Arnaud](https://github.com/FG-TIDA/themes/issues/18#issuecomment-6247541576) and [Cyril's reply](https://github.com/FG-TIDA/themes/issues/18#issuecomment-6255006005) | X.dmst design-time justification; declare voter set as well as operator/regime; distinguish versioned-voter change (stale reference visible per action) from unversioned change (population question) | Preserve versioned set of objectives/"voters" and reference provenance. Do not present this discovery as ours |
| [#16 clarification](https://github.com/FG-TIDA/themes/issues/18#issuecomment-6301230176) and [#21 scope](https://github.com/FG-TIDA/themes/issues/21) | Oversight may be invoked by indeterminate, exceptional or materially changed circumstances; population evidence is different from a single conformance verdict | RA/EA hand off qualified findings to existing oversight/assessment owners; #21 may provide population evidence |
| [Iván's earlier evaluation and xSeil contributions](https://github.com/FG-TIDA/themes/issues/18#issuecomment-5501700348) / [mobility case](https://github.com/FG-TIDA/themes/issues/18#issuecomment-6147855004) | Determination, residual and contextual risk already discussed; fixed additive aggregation with **state-dependent utilities and constraints** already illustrated historically | New contribution must add **requalification criteria, payload and independent falsifiers**, not repeat these comments |

The source #18's practical work streams can be read as **internal assessment**, **external evaluation** and **regulatory alignment**, with a separate design-time link to X.dmst and a dual SG17/FG-TIDA track under discussion. No claim here of an accepted or ratified architecture.

## 2. Why the ACC social/economic model and its agentic reduction are useful

The [ACC social-economic model on main](../../MODEL.md) and [economic technical core](../../ECONOMIC_MODEL_TECHNICAL_CORE_v0.1.md) distinguish technical feasibility `F^T` from authorized/accessible feasibility `F^G \subseteq F^T`, mission output from utility/welfare, and feasible final states from executable transitions. Their multiple dimensions include resource efficiency, distribution, coordination, attribution, rights, cost and preservation of capability. They **do not** prescribe one ethical ranking or a scalar welfare metric. This is directly suitable for #18's *specified objectives as voters* and operator/constraint selection questions.

The [separate agentic reduction PR #57](https://github.com/dakleyer/structural-awareness-contributions/pull/57) supplies bounded vendor contracts, a presently equal functional output under different private marginal capacities, optional scoped source-Q information, authorization/consent/resource gates and a strong conventional peer. Its 30×6 decisions and 160 cost-grid cells are **synthetic model exercises**; the peer with equivalent Q is currently implemented through the same decision branch, so it does **not** measure a distinctive agentic advantage. Audit: [PR #58](https://github.com/dakleyer/structural-awareness-contributions/pull/58).

The present PR's [formal core 02](./02_FORMAL_CORE_AND_PROOFS.md) offers finite factorization/congruence and a four-state counterexample to continued *operational* adequacy. [03](./03_METAPROTOCOL_ALGORITHMS_AND_COST.md) offers a **proposed**, not deployed, bounded proposal/certificate process; [05](./05_INDEPENDENT_VALIDATION_PROTOCOL.md) demands honest strong peers.

**Important:** The mere presence of many agents, many objectives, conflict, uncertainty or internal complexity does not prove RA is necessary. A decision-sufficient existing interface may be adequate; a conventional monitor may implement exactly the same assessment.

## 3. Types: three different objects often called "regime"

Keep distinct identifiers and independent validity tests:

1. **Choice reference** `\mathcal D_{18}=(\mathcal V,\mathcal O,\mathcal R_c,m,T_c,F,\nu,\alpha)`: declared voter/objective set `\mathcal V`, aggregation family/operator `\mathcal O`, choice/axiom regime `\mathcal R_c` (ordinal/cardinal, hard vetoes, normalization/calibration and admissible constraints), mode `m`, authorized transition conditions `T_c`, feasible action/candidate domain `F`, version `\nu` and authored standing `\alpha`. This is a **candidate analytical record**, not the #18 standardized schema. A declared mode can contain layered regimes (e.g. safety veto above cardinal scoring). Units, order and preference comparability must be explicit.
2. **Observable operating regime (RA)** `\mathcal R_{\mathrm{obs}}`: a bounded relation between observation map `\Psi`, context/history `H_t(m)`, structural descriptor `I`, baseline, threshold `\tau` and permitted detection delay `\ell`. A qualified `P_{\mathrm{RA}}\in\{-1,0,+1\}` describes **direction relative to these premises only**; invalid context yields absent/UNKNOWN, never neutral. The broader `\Delta_{\mathrm{RA}}=[A_{\mathrm{RA}},B_{\mathrm{RA}},C_{\mathrm{RA}},D_{\mathrm{RA}}]` is a source-qualified architectural projection, not a physical change magnitude, action gradient or #18 operator.
3. **Mission/frame adequacy (EA)** `Q_{\mathrm{EA}}(d,t)`: whether the current evidence, context, dependencies, capacity and relevant residual still justify reliance on the declared reference **for decision `d` at time `t`**. EA's F3/F4→F5→F6 qualifies and composes, F7/F8 requests/communicates bounded requalification, F9 reopens changed assumptions. It does not select the governing policy or execute actions.

One mode transition may change choice regime without any detected environmental event; an environmental change may invalidate assumptions without changing `\mathcal O`; an operator drift may be measured while `\mathcal R_{\mathrm{obs}}` is stable; and a missing measurement may leave all three uncertain.

## 4. Candidate four-stage semantic handshake

**Not a mandatory runtime chain for every action.** Binding, confidence and status fields are proposed. Producer/consumer maps follow [RA corpus](../../../../../../regime-awareness/README.md), [EA–RA 01C](../../../../01C_EA_REGIME_AWARENESS_INTERFACE_ANNEX_v0.2.md) and [EA–RA–MSCA 01D](../../../../01D_EA_MSCA_RA_OPERATION_COMPOSITION_PROFILE_v0.1.md). Verify these links from the final repository tree before promotion.

| Step | Candidate record and source | Required meaning and failure semantics | Consumer |
|---|---|---|---|
| **C18-REF** | #18/X.dmst design reference: decision ID; authorship/standing under #5; `\nu`; objective/voter inventory, operator, choice regime and submodes; constraints, metric units, triggers, expiry | UNDECLARED distinct from OMITTED; invalid/unbound/stale reference is not a declaration of conformance. Authorized transition must have its own evidence | #6, RA assessment mandate, EA decision context, #21 |
| **RA-OBS** | RA qualification on `\Psi,H,I,B,\tau,\ell`; version/freshness/coverage; `P_{\mathrm{RA}}` or UNKNOWN; optional qualified `\Delta_{\mathrm{RA}}` and admissible source-Q opportunities | `P_{\mathrm{RA}}=0` means **qualified observable compatibility**, not "no frame risk"; no invariant/context/threshold ⇒ UNKNOWN; regime detection ≠ operator drift | EA F3/F4→F5/F6; optional #21 evidence stream |
| **EA-QUAL** | Decision-specific references to C18-REF and RA-OBS; material dependencies, competing evidence/source independence, qualified frame/answer status, residual, eligibility of queries, horizon/budget | Distinguish CERTIFIED_ADEQUATE_IN_SCOPE / REQUALIFICATION_REQUIRED / INSUFFICIENT_FOR_DECISION / UNDERDETERMINED / UNKNOWN. These are **local proposed labels**, not #6 verdicts. No automatic translation to P1/P2/P3 | Authorized policy owner / #18 external assessor / #16 / #13 / MSCA as applicable |
| **CONTROL** | #6 act-time per-action conformance record against pinned C18-REF plus #5 standing; independent authority/permit; #16 handling where required; #21 population evidence where relevant | A RA signal or EA certificate has **no actuation authority**. Expired grants, stale references and changed voters have separate verdict causes. Inaction and valid unrelated operations may remain permitted | Owner/oversight; F9 feedback after separately observed effects |

Proposed minimal interoperable envelope (informative illustrative example; not a deployed API):

~~~json
{
  "kind": "EA_RA_CHOICE_REFERENCE_REQUALIFICATION_CANDIDATE",
  "decision_id": "T18-FX-ENV-01",
  "as_of": "fixture-t2",
  "reference": {
    "ref_id": "choice-v3",
    "operator_id": "lexicographic-safety-then-cardinal-score",
    "voter_set_id": "voters-v3",
    "mode": "NORMAL",
    "choice_regime_id": "normal-v3",
    "transition_policy_id": "tp-v3",
    "authorship_status": "VERIFIABLE_IN_FIXTURE"
  },
  "ra": {
    "observation_map_id": "psi-environment-v1",
    "context_id": "H-window-v1",
    "baseline_id": "b-v1",
    "delta_family": "service-capacity",
    "signal": "DIRECTIONAL_DEPARTURE",
    "qualification": "QUALIFIED_IN_FIXTURE",
    "coverage_limits": ["unobserved-vendor-internals"]
  },
  "ea": {
    "review_question": "is choice-v3 still sufficient for decision T18-FX-ENV-01?",
    "frame_status": "REQUALIFICATION_REQUIRED",
    "residual": ["criticality-of-current-service-unverified"],
    "eligible_inquiries": ["authorised-service-criticality-source"],
    "next_step": "REQUEST_TARGETED_EVIDENCE"
  },
  "control": {
    "action_verdict": "NOT_EVALUATED_HERE",
    "authority": "EXTERNAL_TO_THIS_RECORD",
    "execution": "NONE"
  }
}
~~~

Required envelope fields, independently checked: type + versions, source/declarer/rights, reference-as-of and freshness, decision-scope and admissible-use bindings, `\Psi` coverage/context, source quality and independence, explicit incompatible evidence, residual/UNKNOWN, useful deadline and query/operational costs. Avoid pseudonymous IDs that conceal a genuinely absent mandate.

### Triggers and non-triggers

- **Triggers for scoped RA reevaluation:** eligible exogenous structural evidence; changed sensor/context/baseline; materially changed utility calibration or feasible domain; mode/operation transition affecting an observable regime claim; external participant/dependency composition changes; F9 observed effect departing from declared expectation; qualified #21 population signal.
- **Triggers for EA requalification without any positive RA detection:** change in decision/mission question; expanded operation signature breaking information sufficiency; new objective or voter set; invalid/expired rights; correlation of supposedly independent evidence; unavailable/unauthorized Q; new affected-party or service-criticality condition.
- **Non-trigger or limited trigger:** Condorcet cycle under an unchanged declared mode is a **choice-rule outcome**, not automatically a physical regime change. A versioned voter-set change is primarily a **reference mismatch** for #6. An optional RA monitor becoming unavailable must **not** automatically veto an independently supported authorized action. Ordinary noise below qualified thresholds and irrelevant C/D do not force a system-wide HOLD.

## 5. Formal conditions for the external-evaluation interface

Assume a **declared finite** candidate state domain `X`, qualified currently available observation `o:X\to O`, independently specified *exact* decision question `r:X\to R`, and eligible operations `\Sigma`. Separate the model from facts about the world.

**Static decision sufficiency (standard factorization):**
`r=h\circ o \iff \ker(o)\subseteq\ker(r).`
A conformance outcome alone may fail this condition for a *different* receiving question. It can also pass; complexity is not an insufficiency witness.

**Continued exact deterministic operational adequacy (PR #60 D1):**
`\ker(o)\subseteq\ker(r)` and, for each `f\in\Sigma`, `o(x)=o(y)\Rightarrow o(f(x))=o(f(y))`. Old-adequate quotient plus a newly admitted operation may fail the second term. **A sound set-valued conventional abstraction may still be sufficient for the actual decision**; failure of exact deterministic quotient does not establish mandatory system HOLD.

**Minimal supplementary evidence conditioned on what A already carries (correction required by [audit PR #59](https://github.com/dakleyer/structural-awareness-contributions/pull/59)):** for finite scoped `\widehat X` let
`U_{r\mid o}=\{\{x,y\}\subseteq\widehat X:o(x)=o(y),\ r(x)\ne r(y)\}.`
Choose qualified `Q_j` to separate these **remaining**, not all, pairs. Then `r` factors through `(o,(Q_j)_{j\in H})` exactly iff each pair in `U_{r\mid o}` is separated by at least one selected Q. Costs are the **incremental** permitted Q-acquisition/verification costs; prior A costs are retained separately, not recharged. If `r` has a set of acceptable actions rather than an exact target, this criterion may be **over-demanding**: characterize common admissible dispositions or use a sound conservative alternative.

**Residual action existence (distinct from exact identification):** given compatible states `X_o` and state-dependent admitted action sets `\mathcal A(x)`, a single action can be robustly admissible *in the declared finite frame* iff `\bigcap_{x\in X_o}\mathcal A(x)\ne\emptyset`. This is an existence claim; it does not certify rights, computability, latency or hidden-world coverage. If no common action is admitted, only the authorized fallback, refusal or escalation path may be used; **not a made-up new operator**.

**Change source separation:** current observations alone may fail to distinguish a legitimate mode transition from operator drift, metric distortion or a changed choice context. Even if output trace matches, #18 must retain a candidate set or indeterminate conclusion unless independent reference and measurement evidence identifies the alternatives. A drift score is not itself proof of one cause, nor a numerical "risk" for every mission.

## 6. Interfaces to actual programmes — ownership and no-claim boundaries

- **Theme #18:** owner of collective-choice reference and drift questions. We contribute proposed *continued adequacy* objects and test vectors, **not** a replacement formalism.
- **X.dmst (SG17, as described in #18):** design-time justification of attributes/"voters", weights/axioms, applicable subcontexts and standing. We do not assert that its work-item draft already prescribes this envelope.
- **Regime Awareness:** scientifically challengeable observable continuity/departure and contextual-window question. No hidden-cause recovery or unique effective-operator inference from inadequate traces.
- **Ecosystem Awareness:** decision-specific frame requalification; explicit source qualification and residual. A/B/C/D is **receiver/process relative**: B means characterized support/assessable reserve; C is a grounded *uncharacterized* exploration frontier; D is an effective evaluation barrier; UNKNOWN is neither automatic C nor D.
- **MSCA operation/repositioning:** owns its own eventual P1/P2/P3 posture, safety/capacity/authority interpretation and control plan. RA `P_{\mathrm{RA}}` is not MSCA posture.
- **#5 / #6 / #16 / #21 / #13:** grant origin/standing, action-level conformance, human oversight, population measurements and cross-ecosystem reassessment consume/provide evidence in their existing scopes. No guaranteed human principal per agent or central global orchestrator is presumed.

## 7. Evidence tiers, blockers and proposed next decision

**Established source facts:** what #18 participants actually wrote; finite mathematical identities under displayed assumptions; existence of synthetic ACC/agentic scenarios and reproducible local arithmetic. **Reconstructed/application design:** the four-stage envelope and candidate statuses. **Unproved:** sound use with arbitrary dynamic vendors, calibrated drift on hostile measurements, cost advantage, decision-quality improvement, independent human/technical validation, regulatory acceptance and cross-theme deployment.

Before external #18 publication or integration into normative corpus: (1) reconcile [PR #59 D26-F08](https://github.com/dakleyer/structural-awareness-contributions/pull/59)'s **conditional** query-cover bug in `02/`03; (2) independently audit finite proofs and original-source attribution in PR #60; (3) obtain a real #18-owned reference fixture (operator/voter set/mode/transition policy/identity and versions) rather than assuming our schema is adopted; (4) implement and run separate event/observation/adequacy and control comparators; (5) preregister positive/negative controls and a strong conventional evaluator with equal inputs, costs and authority. The linked [08](./08_THEME18_TEST_MODEL_AND_FIXTURES_v0.1.md) specifies this test design.

**Publication boundary:** this is deposited solely in our research PR. No GitHub comment has been made on FG-TIDA #18, no scope or approval is claimed from Arnaud, and no private document is attached.