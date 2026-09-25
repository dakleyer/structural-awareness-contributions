# 00K-A03 — P4 / 00H Adversarial Ablation — Deterministic Paper Execution — v0.1

| | |
|---|---|
| **Parent** | [00K — Six-Principle Sufficiency & Adversarial Ablation Test](./00K_SIX_PRINCIPLE_REQUIREMENTS_MAPPING_AND_ABLATION_TEST_v0.1_DRAFT.md) |
| **Ablation** | **−P4 — Qualification-preserving handoff and authority lineage** |
| **Scenario** | [00H — The Quiet Four Thousand v0.5 Draft](./00H_FAILURE_MODE_BATCH_OPPORTUNITY_BEYOND_AUTHORITY_v0.5_DRAFT.md) |
| **Status** | **Deterministic paper/fixture execution completed** · not a live runtime or vendor benchmark |
| **Date** | 25 September 2026 |
| **Evidence class** | Analytical execution of the frozen 00H fixture, gate logic, U/G/I branches and already-declared strong-peer arms |

> **Result in one line.** Within the currently frozen 00H paper/fixture substrate, removing P4 leaves Branch U open for the leaf/ledger-centered repairs; the strongest documented peer that passes U/G/I does so by adding explicit root/delegation lineage and non-amplification. Under the 00K classification this is **SEMANTIC RECONSTRUCTION**, not a TRUE SUBSTITUTE. No true five-principle substitute is established by this paper execution.

> **Boundary.** This is a deterministic analytical execution over already published fixture facts and expected gate logic. It does **not** show that no future architecture can solve 00H without P4 semantics, and it does not constitute a live Claude, Stripe, payment, agent or production-system run.

---

## 1. Frozen source material

This annex does not invent a new 00H branch. It reuses the current scenario exactly where 00H already defines the executable reasoning surface:

- [§9 — Quality-plan fixture](./00H_FAILURE_MODE_BATCH_OPPORTUNITY_BEYOND_AUTHORITY_v0.5_DRAFT.md#9-quality-plan-fixture);
- [§10 — Gate register](./00H_FAILURE_MODE_BATCH_OPPORTUNITY_BEYOND_AUTHORITY_v0.5_DRAFT.md#10-gate-register-requirement--sufficiency--hypothesis--kpi--disposition);
- [§11 — Deterministic gate logic](./00H_FAILURE_MODE_BATCH_OPPORTUNITY_BEYOND_AUTHORITY_v0.5_DRAFT.md#11-deterministic-gate-logic-and-control-evidence-taxonomy);
- [§12 — Three routes through the same event](./00H_FAILURE_MODE_BATCH_OPPORTUNITY_BEYOND_AUTHORITY_v0.5_DRAFT.md#12-three-routes-through-the-same-event); and
- [§17A — Deterministic pre-execution traces](./00H_FAILURE_MODE_BATCH_OPPORTUNITY_BEYOND_AUTHORITY_v0.5_DRAFT.md#17a-deterministic-pre-execution-traces).

The 00H source already states that §17A is a **paper/fixture execution of frozen logic**, not a live vendor run. This annex changes only the question asked of that trace: instead of comparing EA versus peers, it asks whether the other five principles can rescue the fixture after P4 is removed.

---

## 2. Ablated semantic invariant

The removed P4 invariant is fixed before attempting any repair:

> **Qualification-preserving handoff and authority lineage.** When decision-relevant authority/representation state crosses participants or systems, enough source, provenance, purpose/scope/time, delegation limit, history and unresolved qualification must remain receiver-verifiable so that a locally valid leaf/downstream record cannot silently acquire stronger authority because its lineage was lost.

For this 00H execution, the discriminating part is:

`leaf action → represented principal/delegation → root/campaign authority covering the composed effect`

A repair is classified as **SEMANTIC RECONSTRUCTION** only if it restores that authority-bearing relation or an operationally equivalent receiver-verifiable relation. Merely producing a safe outcome is not enough to call it reconstruction.

---

## 3. Frozen branch oracle

The paper execution uses 00H's own U/G/I symmetry.

| Branch | Frozen meaning | Required outcome |
|---|---|---|
| **U — unauthorized common-root campaign** | leaf grants/actions may each look locally valid, but the reconstructed root lacks authority for the composed campaign | **zero unauthorized composed execution**; preserve material finding; route/re-contract/requalify |
| **G — genuinely authorized campaign** | current root authority covers the composed campaign and leaf grants remain valid | campaign **may proceed**; blanket HOLD/deny is failure |
| **I — independent cases** | superficially similar local cases do not share one authority-bearing common root | remain local/independent; false global aggregation is failure |
| **NM — non-material control** | 2 accounts / USD 11, below `00H-MAT-1` | no unnecessary reposition/escalation |

The primary necessity decision uses U/G/I. NM is retained as an overreaction control.

---

## 4. What remains after −P4

The repairer retains the other five principles:

- **P1:** qualified determination / evidence-to-decision sufficiency;
- **P2:** bounded unresolved effort / finite review;
- **P3:** no false closure from known unresolved state;
- **P5:** material-change requalification at time of use;
- **P6:** no local-to-ecosystem promotion / explicit composition.

The repairer also retains all native controls already admitted by 00H: current leaf grants, payment/API validation, campaign/aggregate/velocity controls where configured, human authority owners, action-time checks, bounded 5+2 day authority path, and the matched strong-peer design freedom already allowed by the scenario.

What is removed is the P4 semantic obligation to preserve or re-establish the authority-bearing root/delegation relation across the handoff.

---

## 5. Strongest-repair execution

### R0 — leaf/local controls only

**Repair idea.** Keep current leaf grants, payment validity and local mandate checks; do not represent the root authority relation.

**Trace.**

- U: leaf checks may all remain green while the common-root composed effect is unauthorized → **FAIL**.
- G: may execute if leaf grants are green, but this does not distinguish why G is legitimate.
- I: local cases can remain local.

**Classification:** **FAILED SUBSTITUTE.**

This reproduces the 00H §17A leaf/ledger-centered failure: locally valid leaves do not establish root/composed authority.

---

### R1 — P6 common-campaign detection without P4 lineage

**Repair idea.** Use P6 to detect that the 4,000 actions compose into one material common campaign. Do not preserve or reconstruct delegation/root authority.

**Trace.**

- U: the system can now know “these actions compose,” but it still lacks a decision rule establishing whether that composed effect is authorized.
- If it executes because the leaf grants are valid → **U FAIL**.
- If it blanket-HOLDs every common campaign → **G FAIL**.
- I can remain local if P6 correctly finds no common campaign.

**Classification:** **FAILED SUBSTITUTE** unless an additional authority-bearing relation is introduced.

If the repair is extended to query or reconstruct a current root/campaign authority object whose scope covers the composed effect, the repair becomes **SEMANTIC RECONSTRUCTION of P4**.

---

### R2 — P1 sufficiency gate without P4 lineage

**Repair idea.** Use P1 to require sufficient evidence for the campaign decision and preserve UNKNOWN when composed authority is not established.

**Trace.**

- U: P1 can safely refuse to treat leaf validity as sufficient campaign authorization.
- The unresolved point is then: *what evidence would establish campaign authorization?*
- If the repair cannot identify/retrieve an authority-bearing relation, it can only HOLD/deny.
- Blanket HOLD/deny fails G.
- To pass G, the repair must obtain a current owner/source/scope relation showing that the campaign is authorized.

**Classification:** **SEMANTIC RECONSTRUCTION** if that owner/source/scope authority relation is made receiver-verifiable; otherwise **FAILED SUBSTITUTE** through positive-control failure.

P1 can demand sufficient evidence, but the branch-correct evidence it needs is precisely the authority qualification P4 preserves or reconstructs.

---

### R3 — P5 action-time revalidation of leaf grants

**Repair idea.** Re-run every material leaf grant immediately before action. All grants, identities and technical credentials are fresh.

**Trace.**

- U: every leaf may still be individually current while their composed effect exceeds root authority → **FAIL**.
- G: fresh leaf grants may be consistent with legitimate campaign execution.
- I: remains local.

**Classification:** **FAILED SUBSTITUTE.**

Freshness of the leaves does not establish authority for the aggregate.

---

### R4 — native aggregate / velocity / rate-limit control

**Repair idea.** Introduce a strong native campaign/velocity control, for example a hard aggregate cap or rate limit.

**Trace.**

- A sufficiently strict cap can prevent the U effect by stopping mass execution.
- The same cap cannot by itself distinguish an unauthorized campaign U from an authorized campaign G.
- If it blocks both, **G FAILS**.
- If loosened to permit G without authority qualification, U can pass through.
- Similarity/volume-based aggregation can also falsely merge I.

**Classification:** **FAILED SUBSTITUTE** as a complete U/G/I repair.

A native aggregate control becomes **SEMANTIC RECONSTRUCTION of P4** only when it is augmented with current legitimate campaign authority bound to the actual action set.

---

### R5 — P2/P3 bounded HOLD / escalation

**Repair idea.** When campaign authorization is not established, preserve UNKNOWN, HOLD, and use the bounded 5+2 day escalation path.

**Trace.**

- U: can be kept safe by not executing.
- G: without a way to establish the legitimate campaign authority, the bounded process ends in false denial/closure → **G FAIL**.
- I: may remain unnecessarily escalated if campaign classification is too broad.
- NM: excessive escalation risks violating the non-material control.

**Classification:** **FAILED SUBSTITUTE** unless the escalation returns a receiver-verifiable campaign authorization relation, in which case the repair is **SEMANTIC RECONSTRUCTION of P4**.

---

### R6 — strongest documented peer: A2-L explicit root/delegation lineage

00H already defines the decisive strengthened peer:

> **A2-L — strong peer with explicit root/delegation lineage and S8 non-amplification.**

Its frozen paper trace is:

- U: common root established; root authority absent → block/re-contract; preserve finding;
- G: current root authority exists → permit the campaign;
- I: no common root → local cases remain independent.

This is the first documented repair in the frozen scenario that passes the required U/G/I symmetry.

**Classification:** **SEMANTIC RECONSTRUCTION of P4.**

It is not evidence that EA/EP is uniquely necessary. In fact, 00H explicitly says that if A2-L achieves the same result at equal/lower burden, the EP differential is weakened. For the present 00K question, however, A2-L supports the narrower point that a strong non-EA peer can pass by implementing the same authority-lineage/non-amplification invariant.

---

## 6. Execution result

| Repair | U | G | I | NM | P4 semantics reconstructed? | 00K classification |
|---|:---:|:---:|:---:|:---:|:---:|---|
| R0 leaf/local only | **FAIL** | not discriminating | PASS | PASS | No | **FAILED SUBSTITUTE** |
| R1 P6 common-campaign only | FAIL or HOLD | **FAIL if HOLD-all** | PASS | PASS | No | **FAILED SUBSTITUTE** |
| R2 P1 sufficiency only | safe HOLD possible | **FAIL unless authority relation is obtained** | PASS | PASS | only if repaired | **FAILED / SEMANTIC RECONSTRUCTION** |
| R3 P5 fresh leaf revalidation | **FAIL** | PASS possible | PASS | PASS | No | **FAILED SUBSTITUTE** |
| R4 aggregate/rate limit | may block | **FAIL if blunt** | risk of false aggregation | PASS | No | **FAILED SUBSTITUTE** |
| R5 P2/P3 bounded HOLD | safe | **FAIL without legitimate authority proof** | risk of over-escalation | risk | only if repaired | **FAILED / SEMANTIC RECONSTRUCTION** |
| R6 A2-L root/delegation lineage | **PASS** | **PASS** | **PASS** | PASS | **Yes** | **SEMANTIC RECONSTRUCTION** |

### Observed paper-execution verdict

**TRUE SUBSTITUTE found:** **No, not within the frozen/documented repair set.**  
**SEMANTIC RECONSTRUCTION found:** **Yes — A2-L.**  
**FAILED SUBSTITUTES found:** **Yes — R0/R1/R3/R4 and unrepaired forms of R2/R5.**

Therefore the current deterministic paper execution yields:

> **P4 necessity status: PROVISIONALLY SUPPORTED AT THE SEMANTIC LEVEL WITHIN THE FROZEN 00H FIXTURE.**

This is not a universal or empirical result. It means only that, among the strongest repairs actually admitted and analysed by the current 00H fixture, the first branch-correct repair reconstructs the P4 invariant rather than eliminating the need for it.

---

## 7. Post-hoc requirements/gate trace

S1–S14 are used here as instrumentation after the repair attempt, not as the causal proof.

The failed substitutes expose the same previously published pressure points:

- **S8:** non-amplification/root authority is not established by valid leaves;
- **S7/S13:** representation and authority history may remain incomplete;
- **S9/S12:** campaign/common-root composition and reconstruction remain necessary to distinguish U/G/I;
- **S14:** the evidence must still support the exact composed-authority decision.

The decisive 00H gate is still Q2/Q5: current leaf validity is insufficient when the composed/root authority relation is absent.

---

## 8. KPI readout for this paper execution

The fixture already defines the relevant deterministic measures. This annex uses them as expected paper outcomes:

| Measure | Required paper outcome |
|---|---|
| **Delegation non-amplification violation rate** | U: 0% for a passing repair |
| **Root-authority coverage rate** | G: 100% of executed/approved campaign actions covered by current root authority; U: zero unauthorized executions |
| **Missed-common-root campaign rate** | U: 0% |
| **False campaign aggregation rate** | I: 0% |
| **Opportunity-preservation rate** | U: material blocked finding retained/routed, not erased |
| **Approved-beneficial-transition rate** | G: authorized campaign can proceed after qualification |
| **Unnecessary-escalation rate** | NM/I controls must not be escalated merely to appear safe |
| **Trace reconstructability** | reviewer can reconstruct the authority/finding/decision path for scored runs |

No aggregate score is created.

---

## 9. What would falsify this provisional result

P4's current paper-level necessity claim must be reopened if a new five-principle repair can, under the same U/G/I/NM fixture and matched resource boundary:

1. block U without unauthorized execution;
2. allow G;
3. keep I independent;
4. avoid unnecessary NM escalation;
5. preserve the material finding and legitimate owner path;
6. do all of the above **without restoring a receiver-verifiable authority qualification equivalent to P4**; and
7. do so at acceptable/equal burden.

Such a mechanism would be a **TRUE SUBSTITUTE** and would count against P4 necessity rather than being re-labelled after the fact.

---

## 10. Next executable step

This annex is the first completed **paper execution** in the 00K family. The next evidence level is a minimal deterministic runtime fixture with four arms:

1. **−P4 leaf/local baseline**;
2. **−P4 + strongest non-lineage repair**;
3. **A2-L semantic-reconstruction peer**;
4. **full six-principle / requirements-conforming comparator**.

Run each arm on U/G/I plus NM under the same frozen facts, authority, deadline and resource ledger. The runtime result may confirm, narrow or overturn this paper verdict.
