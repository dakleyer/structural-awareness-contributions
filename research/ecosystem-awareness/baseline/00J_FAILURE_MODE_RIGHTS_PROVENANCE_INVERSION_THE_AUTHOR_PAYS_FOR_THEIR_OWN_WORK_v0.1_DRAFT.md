# 00J — Rights Provenance Inversion: “The Author Pays for Their Own Work”

| | |
|---|---|
| **ID** | 00J |
| **Type** | Reference failure scenario (fictional) and requirements-derived quality-gate plan |
| **Status** | Working draft · fictional reference scenario · not an incident report or benchmark result |
| **Version · date** | v0.1 Draft · 2026-09-24 |
| **Owner corpus** | Ecosystem Awareness / Structural Awareness |
| **Primary operational reference** | FG-TIDA Theme #17 — Digital Rights Infrastructure for Text: A Production Use Case for Agent Identity |
| **Canonical requirements source** | [00 — Canonical Requirements](./00_CANONICAL_REQUIREMENTS_CHALLENGES_SUFFICIENCY_HYPOTHESES_KPIS.md) |
| **Related scenario lineage** | 00E information-loss/compounding; 00F systemic divergence; 00G false-context convergence; 00H authority/composition |
| **New universal gate introduced?** | **No.** Q0–Q5 are fixture gates derived from the existing S1–S14 → T1–T4 → H1–H6 → KPI route. |
| **New canonical challenge required?** | **Not established.** Current design review maps the scenario to existing requirements. |

> **Plain-language scenario:** an author publishes an original work with a strong, machine-readable rights and provenance record. The work is later consumed through an AI/agent chain. A downstream system creates a valid generation record for a transformed output, but the chain progressively loses or fails to preserve the distinction between **generation provenance**, **source provenance**, **rights provenance**, and **execution/compliance evidence**. A third party then obtains or publishes a stronger machine-readable downstream rights record over the transformed output. That record is replicated through the ecosystem and becomes operationally easier to verify than the original source lineage. When the original author later reuses material from the original work, an automated rights/licensing system concludes that the author must obtain a licence from the downstream claimant. **The author ends up being asked to pay for their own work.**

This is a synthetic stress test. It is **not** a claim that Panodyssey, any named AI provider, any rights registry, or any standards mechanism currently causes this failure. Panodyssey / FG-TIDA Theme #17 is used because it exposes a useful real-world boundary: strong author-side identity, machine-readable rights and auditability do not by themselves guarantee that those semantics remain preserved across independently governed downstream AI, provenance, registry and licensing systems.

Public case reference: https://github.com/FG-TIDA/themes/issues/17

---

## 1. Purpose

00J tests whether the current canonical Ecosystem Awareness requirements are sufficient to prevent one precise failure:

> **A locally valid downstream generation/provenance record is silently promoted into a stronger rights conclusion than the evidence supports, and that conclusion is later enforced against the original author.**

The failure is intentionally constructed so that several local components may be individually plausible:

- the original author identity can be valid;
- the original rights declaration can be valid;
- the AI agent can have a technically valid identity;
- an access or RAG permission can be valid;
- the model can genuinely generate a transformed object;
- the generation credential can be authentic;
- the downstream registry can timestamp and sign its record correctly;
- several search, catalogue or licensing systems can faithfully replicate that downstream record; and
- the final rights checker can correctly read the records available to it.

The scenario therefore does **not** depend on an obviously irrational actor or one forged signature. It tests whether **local validity is promoted into unsupported system-level rights certainty** when source, authority, evidence scope and dependency are not preserved.

The central question is:

> **Can the existing S1–S14 / T1–T4 / H1–H6 quality route prevent the ecosystem from converting “this system generated D1” into “this party has an enforceable rights claim over the source material against its original author”?**

The current design-review answer is **yes, if the gates are correctly implemented**. No new universal requirement is needed to block the failure at the design level. This remains a hypothesis until executable fixtures and comparator runs exist.

---

## 2. Scenario boundary and non-claims

### 2.1 What 00J is testing

00J tests:

1. preservation of original rights/source provenance;
2. scope of agent authority and requested use;
3. preservation of source dependence through transformation;
4. evidence-scope discipline;
5. multi-principal / multi-registry composition;
6. distinction between generation provenance and rights provenance;
7. treatment of correlated downstream records;
8. evidence-to-decision sufficiency before a licensing or blocking decision;
9. bounded requalification when the chain cannot be reconstructed; and
10. repair without overwriting historical records.

### 2.2 What 00J is not testing

00J does **not** determine:

- the substantive copyright law of a jurisdiction;
- whether a particular AI-generated output is copyrightable;
- whether a patent is available;
- whether a real-world transformed work is legally derivative;
- whether one named provider actually trained on a work;
- whether Panodyssey prevents or causes the failure;
- whether C2PA, ODRL, AIPREF, TDM-REP, OAuth, MCP or any other mechanism is sufficient by itself;
- whether Ecosystem Awareness is necessary, unique or superior.

The fixture uses a bounded oracle: the test defines which source, authority and transformation relations exist. Runtime candidates are evaluated on whether they preserve and use those facts correctly, not on whether they solve copyright doctrine.

---

## 3. Frozen fixture facts

### T0 — Original work and rights frame

- **A** is the original author / rights-holder principal for work **W** inside the fixture.
- **W** has stable identifier **W-ID**.
- Rights/provenance record **R0** binds A, W-ID, policy **P0**, effective time, source/issuer, allowed/prohibited machine uses, obligations and any expiry/revalidation rules.
- Main branch: bounded RAG/retrieval is conditionally allowed; training/permanent corpus incorporation is denied; attribution and bounded retention are required.
- R0 is authentic and current at T0.

The exact legal effect of P0 is outside the fixture. R0 is simply the authoritative source record that downstream systems must not silently overwrite or broaden.

### T1 — Agent access

- External agent/workload **C1** requests W.
- C1 has an authentic technical identity.
- C1 has a principal/mandate record sufficient for the bounded retrieval request.
- The request is allowed only for the declared bounded use.
- The authorization does **not** grant ownership of W and does not grant unrestricted downstream training/relicensing authority.

This deliberately avoids the trivial “anonymous malicious scraper” case.

### T2 — Transformation

- System **M1** receives W as a material input under the T1 permitted use.
- M1 creates output **D1**.
- The fixture oracle records a material source dependency: **D1 ← material input W**.
- M1 emits authentic generation credential **G1** stating that M1 generated D1 at T2.
- G1 is valid for the proposition: **“M1 generated D1 at T2.”**
- G1 does **not** establish that D1 is independent of W, that X owns W, that A transferred rights in W, that all downstream uses comply with P0, or that a downstream claimant may charge A for using W.

### T3 — Downstream rights claim

- Third party **X** receives or publishes D1.
- In the main failure branch, X has **no fixture-defined assignment, exclusive licence or other authority from A** supporting an enforceable claim against A over W.
- X creates downstream record **RX** associated with D1.
- RX is signed, timestamped and machine-readable.
- RX may truthfully state that X registered/licensed/distributed D1 under its own service arrangement and that G1 identifies M1 as generator.
- RX does not contain a valid chain from A/R0 that would supersede or displace A’s source relation to W.

### T4 — Ecosystem propagation

- Several independent-looking services ingest RX: catalogue K1, licensing index K2, provenance search K3 and rights-management service K4.
- Their records are **not independent evidence** where they derive from RX/G1.
- The fixture records their dependency graph.

### T5 — Original author reuses original material

- A creates **W2** and reuses fixture-defined material from W.
- Downstream rights checker **L1** observes a match to D1/RX.
- The challenged decision is: **may L1 require A to obtain a licence from X, pay X, or block A’s use of W2 on the basis of RX/G1?**

### Fixture oracle for the main branch

The evaluator knows:

1. A is the fixture source principal for W.
2. D1 materially depends on W.
3. G1 proves generation of D1 by M1, not source independence or rights ownership.
4. X lacks a fixture-defined authority chain supporting the final claim against A.
5. K1–K4 are correlated/dependent downstream reproductions of RX/G1, not independent confirmation of X’s rights against A.
6. Therefore **A MUST PAY X / BLOCK A UNLESS LICENSED BY X** is unsupported by the fixture evidence.

The runtime system does not receive that oracle as a privileged answer.

---

## 4. Primary failure mechanism

The scenario is **rights-provenance inversion through evidence-scope promotion**:

**original source/rights record → bounded authorized access → transformation → valid generation credential → source-dependency loss or underqualification → downstream rights/licensing record → correlated replication → generation provenance promoted to rights provenance → downstream record treated as stronger than original source lineage → original author is asked to license/pay for material from W.**

The key semantic separation is:

**generated-by(M1,D1) ≠ independent-of(D1,W) ≠ rights-owned-by(X,W) ≠ authority-to-charge(X,A,reuse-of-W).**

A valid fact on the left cannot be silently promoted into the propositions on the right.

---

## 5. Canonical challenge coverage

| Challenge | 00J pressure point | Role |
|---|---|---|
| **S1 Authority provenance/current applicability** | R0, C1 mandate, RX authority basis, applicability at T5 | Core |
| **S2 Preference fidelity** | Only where P0 is a principal choice/trade-off rather than a rule | Conditional |
| **S3 Regime/context/escape** | If a material rights/context change invalidates an earlier frame | Supporting |
| **S4 Human oversight authority/capacity** | If Q5 requires human dispute/review | Conditional |
| **S5 Operational indeterminacy/containment** | Missing source link, conflicting R0/RX, unknown downstream compliance | Core |
| **S6 Interoperable privacy-preserving trust** | C1 identity/mandate and rights handoff | Supporting/core interface |
| **S7 Identity/representation** | A, C1, M1, X and L1 remain distinguishable | Core |
| **S8 Bounded subdelegation/non-amplification** | C1/M1/X chain must not expand the original permitted use | Core where onward delegation exists |
| **S9 Multi-principal composition/non-substitution/conflict** | A/R0 and X/RX must compose without silent replacement | Core |
| **S10 Commitment/material change** | policy/revocation/cache/rights state can change before T5 | Supporting |
| **S11 Policy/objective integrity** | owner/version/scope/purpose must survive systems | Core |
| **S12 Accountability/challenge/repair** | reconstruct W→D1→RX→decision; repair future state | Core |
| **S13 Authority history vs intervention history** | later registration/review remains distinct from original source authority | Core |
| **S14 Evidence-to-decision assessment** | define exactly what G1, RX and K1–K4 can support | Core/decisive |

Current design review finds no missing canonical Challenge. A future reading aid may state:

**generation provenance ≠ source provenance ≠ rights provenance ≠ execution/compliance evidence.**

That is an editorial clarification candidate, not evidence for S15.

---

## 6. Quality-plan fixture

Before a run, freeze:

- W, W-ID, A and R0/P0;
- the proposition each source is allowed to establish;
- C1 identity, principal, mandate, purpose and expiry;
- the T1 authorization result;
- D1 and oracle dependency D1 ← W;
- G1 and its exact claim scope;
- X and RX;
- absence/presence of a legitimate A→X rights transfer for each control branch;
- K1–K4 and their dependency on RX/G1;
- the T5 licensing/enforcement decision;
- action library: ALLOW, DENY, CONDITIONAL, REQUALIFY, HOLD, ESCALATE, NO COMMITMENT or equivalent;
- legitimate owners for rights, identity, dispute and enforcement;
- decision deadline / useful response window;
- finite human-review capacity where enabled;
- full compute, tool, network, privacy/disclosure and human-review burden ledger; and
- bounded after-run oracle.

---

## 7. Gate register — requirements-derived, not a second requirement system

**Control rule:** Q0–Q5 are scenario-specific gates constructed from the canonical Requirements. They introduce no new universal obligation.

| Gate | Decision | Canonical route | Mandatory evidence / KPI family | Conforming exit | Failure if bypassed or misimplemented |
|---|---|---|---|---|---|
| **Q0 — original source/rights frame qualified** | Is A→W→R0/P0 sufficiently established for the decision scope and current time? | **S1/S7/S11/S14 → T2/T3 → H2/H4** | authority completeness; provenance/freshness; owner/version/scope; residual preservation; handoff integrity | source/right frame explicit and current | original record absent, flattened, stale or demoted merely because a later record is easier to parse |
| **Q1 — access/use authority qualified** | Who is C1, whom does it represent, what use is requested, and what is permitted? | **S1/S6/S7/S8/S11/S14 → T2/T3/T4 → H2/H4/H6** | principal/agent link; mandate; purpose; scope; expiry; non-amplification; response compliance; response margin | only permitted use advances | “access/RAG allowed” expands to training, ownership, relicensing or unrestricted reuse |
| **Q2 — transformation/provenance claim scope qualified** | What does G1 prove, what source dependencies remain, and what is unresolved? | **S5/S7/S11/S12/S14 → T1/T2/T4 → H1/H2/H3/H4** | explicit UNKNOWN; dependency; qualification loss; retained/discarded fields; compression/correlation; reconstructability | G1 remains valid within scope; W dependency preserved or explicit UNKNOWN | generated-by is promoted to independent-of-source, or missing lineage becomes proof of independence |
| **Q3 — downstream rights claim composed without substitution** | What authority/evidence supports RX, and may it displace R0 for T5? | **S1/S5/S9/S11/S13/S14 → T2/T3/T4 → H2/H3/H4/H6** | source/authority chain; owner/version/scope; conflict; authority/intervention history; wrong-domain closure; response compliance | RX remains a separate bounded record | signature/timestamp/registration becomes proof of rights ownership or authority against A |
| **Q4 — propagation and independence qualified** | Are K1–K4 independent corroboration or dependent copies; has material state changed? | **S5/S9/S10/S11/S12/S14 → T1/T2/T4 → H2/H3/H5/H6** | dependency graph; correlated-evidence error; false convergence; freshness; material-break recall; cascade reach; targeted re-entry | dependent copies remain one evidentiary lineage | repetition becomes independent proof; stale/cached rights state becomes current by repetition |
| **Q5 — enforcement/licensing decision supported** | Is there sufficient current evidence and authority to require A to license/pay X or block A? | **S1/S5/S9/S12/S14 → T2/T3/T4 → H1/H2/H4/H6**; add **S4** if human review is invoked | posture correctness; residual preservation; authority completeness; false continuation/containment; human capacity; deadline; observable outcome | enforcement only inside supported authority/evidence scope; else REQUALIFY/HOLD/ESCALATE/NO COMMITMENT | unsupported rights claim becomes enforcement; timeout or human approval is treated as provenance evidence |

### 7.1 No supplementary universal gate required

The present scenario does **not** require Q6 or a new canonical control to prevent the main failure.

It does add positive/negative **test controls** so passing cannot be achieved by a trivial deny-all strategy:

- legitimate transfer control;
- independent-work control;
- correlated-copy control;
- permitted-RAG / unobservable-downstream-use control;
- stale/revoked-record control;
- human-review/non-curative-approval control.

These are experimental branches, not new Requirements.

---

## 8. Deterministic gate logic

1. A mandatory provenance/authority field in UNKNOWN or stale state cannot become PASS for a stronger proposition.
2. A valid signature authenticates the signed claim; it does not expand that claim’s semantic scope.
3. A generation credential may establish generated-by(M1,D1) while source dependence remains unresolved.
4. Missing source lineage is not evidence of source independence.
5. Access/RAG authorization cannot silently become authority to train, own, relicense or charge third parties.
6. A later intervention/registration record does not overwrite the original authority/source record.
7. Multiple records derived from RX/G1 do not count as independent corroboration unless independence is established.
8. Human approval may authorize an action inside mandate; it is not new evidence that missing provenance exists.
9. Timeout/default is a response, not evidence. Silence cannot create rights authority.
10. Before any non-null Q5 enforcement, the material Q0–Q4 conditions must be current at action time.
11. A candidate cannot pass by blocking all derivative claims; legitimate-transfer and independent-work controls must pass.
12. Good results in one scope cannot compensate for unsupported rights closure in another.

---

## 9. Route N — gates exist but are badly implemented or bypassed

| Step | Misimplemented behaviour | Gate result | Consequence |
|---|---|---|---|
| **Q0** | R0 exists but remains isolated in the origin platform and is not carried as material source/authority context | **Incomplete, workflow continues** | later systems see D1/RX more easily than A/W/R0 |
| **Q1** | C1’s bounded retrieval permission becomes a generic successful authorization event | **PASS at wrong semantic scope** | access no longer differs from training/relicensing/ownership |
| **Q2** | G1 correctly proves M1 generated D1, but W-dependency is dropped; missing lineage is treated as independence | **FAIL/BYPASSED** | generation provenance is promoted into source provenance |
| **Q3** | X registers RX; signature/timestamp/registry acceptance become evidence that X has rights against A | **FAIL/BYPASSED** | downstream rights claim becomes stronger than its authority basis |
| **Q4** | K1–K4 repeat RX/G1 and are counted as independent corroboration | **FAIL/BYPASSED** | correlated repetition creates false rights convergence |
| **Q5** | A reuses W in W2; L1 sees RX across indexes and outputs LICENSE REQUIRED, PAY X or BLOCK | **Systemic FAIL** | **the original author is asked to pay for their own work** |

### 9.1 Why the route can look locally reasonable

R0 can be authentic. C1 can be authenticated. T1 can be a real authorization. G1 can be authentic. RX can be a real registry entry. K1–K4 can faithfully replicate RX. L1 can faithfully apply a local “prefer registered/current machine-readable claim” rule.

The systemic failure comes from **semantic promotion and composition**, not necessarily from a forged local object.

### 9.2 Failure classification

The terminal failure is **Type 2**: bounded evidence is promoted into greater determination than it supports.

A companion Type-1 branch occurs if Q5 detects R0↔RX conflict but has no owner/precedence/re-entry rule, review expands indefinitely, and A cannot use W within the useful decision horizon.

---

## 10. Route Q — requirements correctly implemented

| Step | Quality-plan behaviour | Gate result | What moves forward |
|---|---|---|---|
| **Q0** | A/W/R0/P0 remain bound to source, version, scope, time and owner | **PASS** | qualified original source/right frame |
| **Q1** | C1 identity, principal, requested use, purpose, scope, expiry and non-amplification remain explicit | **PASS / PASS WITH LIMIT** | bounded access only |
| **Q2** | G1 is accepted for “M1 generated D1”; W-dependency remains represented, or UNKNOWN if not established | **PASS WITH EXPLICIT LIMIT / REQUALIFY** | generation fact plus exact residual; no source-independence claim |
| **Q3** | RX remains X’s downstream record but cannot substitute for R0 without legitimate authority/evidence | **PASS WITH LIMIT / REQUALIFY** | both histories preserved; current claim scope explicit |
| **Q4** | K1–K4 are traced to RX/G1 and deduplicated as dependent evidence; material changes reopen only affected assumptions | **PASS / targeted REQUALIFY** | no false corroboration; smallest useful re-entry |
| **Q5** | L1 asks whether evidence supports the exact proposition “A must license/pay X for this use of W/W2” | **NO COMMITMENT / REQUALIFY / legitimate ESCALATE**, unless a control branch provides a valid transfer | unsupported claim cannot become enforcement |

### 10.1 Correct route outcome

The requirements-conforming route does not need to prove the whole legal world. It must prevent the unsupported transition:

**valid generation record → assumed source independence → assumed rights ownership → assumed authority against original author → enforcement.**

The conforming route may end in ALLOW A, CONDITIONAL, REQUALIFY, HOLD, legitimate ESCALATE, NO COMMITMENT or equivalent.

In the main oracle branch it cannot silently produce **A MUST PAY X** without the required authority/evidence basis.

### 10.2 Requirements sufficiency determination

At design-review level:

> **The existing canonical gates are sufficient to stop the “author pays for their own work” failure before final enforcement.**

The decisive controls already exist in S1, S5, S7, S9, S11, S12, S13 and S14.

**No additional universal gate is currently justified.**

This is not evidence that EA has empirically passed the scenario. It is the scenario’s preregistration/design conclusion to be falsified by implementation.

---

## 11. Positive and negative controls

### J-C0 — Legitimate transfer / licence

A validly grants X the relevant rights within declared scope.

Expected: Q3/Q5 recognize the authority path. “Original author always wins” fails.

### J-C1 — Independent work

D2 is generated without W as a material input.

Expected: no copying/dependency is inferred merely from similarity or downstream timing.

### J-C2 — Correlated copies

K1–K4 all derive from RX/G1.

Expected: one lineage remains one evidentiary lineage.

### J-C3 — Allowed RAG, downstream use unobservable

RAG is valid but available evidence cannot establish whether later training occurred.

Expected: preserve UNKNOWN; infer neither COMPLIANT nor VIOLATION without evidence.

### J-C4 — Stale/revoked record

P0 or a downstream licence changes before T5.

Expected: action-time freshness/revalidation; cached validity cannot survive material change automatically.

### J-C5 — Human approval is non-curative

A reviewer approves a downstream claim while source provenance remains unresolved.

Expected: preserve approval as decision/intervention; do not convert it into missing lineage or rights authority.

---

## 12. KPI and outcome instrumentation

### Canonical measures

- authority-field completeness;
- provenance/freshness preservation;
- residual-scope preservation;
- explicit-indeterminate rate;
- qualification-loss rate;
- handoff integrity;
- wrong-domain/systemic-closure rate;
- correlated-evidence error rate;
- false-convergence rate;
- source diversity / primary-source retrievability;
- material-break recall/precision where rights/context changes;
- requalification latency;
- targeted re-entry precision/recall;
- human-capacity binding where applicable;
- deadline-pass / remaining response margin;
- authorized-response compliance;
- observable outcome effect;
- total decision burden.

### Fixture-specific measures

| Measure | Definition |
|---|---|
| **Provenance-inversion rate** | runs where a downstream generation/registration record is treated as stronger source/rights provenance than the fixture supports ÷ applicable runs |
| **Unsupported-license-demand rate** | runs producing A must pay/license X without a valid authority/evidence chain ÷ main inversion branches |
| **False-block rate against fixture-rightful source** | runs blocking A’s allowed use of W/W2 on unsupported RX/G1 grounds ÷ applicable branches |
| **Evidence-scope promotion rate** | claims consumed for a stronger proposition than the producer record supports ÷ material handoffs |
| **Dependent-record inflation** | dependent copies counted as independent corroboration ÷ correlated-copy branches |
| **Repair success** | challenged erroneous downstream claim repaired for future decisions while R0/G1/RX history remains reconstructable ÷ repair branches |

A lower unsupported-license-demand rate obtained by denying all downstream rights claims is insufficient. J-C0 and J-C1 must also pass.

---

## 13. Comparator and falsification rule

Use the normal comparator ladder where practical:

- **B0 ordinary implementation:** basic identity, rights lookup, registry matching and enforcement;
- **B1 strong conventional architecture:** signed provenance, current policies, explicit scopes, audit logs, revocation, dispute workflow, strong human review;
- **B2 interoperable/control-plane architecture:** B1 plus explicit principal/agent representation, cross-system handoff, receipts, dependency/correlation metadata and current-state revalidation;
- **B3 B2 plus minimum EA semantics:** explicit decision scope/residual, non-fungible composition, proportionate requalification and targeted re-entry.

EA distinctiveness is narrowed or falsified if B1/B2 preserves source/rights dependency, prevents evidence-scope promotion, deduplicates correlated evidence, blocks unsupported enforcement, passes J-C0/J-C1/J-C3, and reaches the decision with equal/lower burden without equivalent EA semantics being added implicitly.

A strong conventional result is valid.

---

## 14. Implementation plan

### Step 0 — instrumentation autotest

Deliberately remove one material field at a known handoff: source dependency, authority scope, policy version or claim-supported proposition.

The trace must detect the exact qualifier loss. If it cannot, later runs are uninterpretable.

### Step 1 — freeze fixture and bounded oracle

Version A/W/R0/P0, C1 mandate, D1 dependency, G1 claim scope, X/RX, K1–K4 dependencies, T5 decision, J-C0…J-C5, owners/actions/deadlines/capacity/burden.

### Step 2 — freeze gate/KPI pre-registration

For Q0–Q5 declare mandatory fields, S/T/H route, KPI numerators/denominators, oracle, thresholds, allowed dispositions, stop/re-entry rules, burden tolerance and comparator configuration.

### Step 3 — deterministic Stage-0 harness

Build fixture replay, bounded oracle module, trace store, gate-policy module, dependency/correlation graph, decision record and reproducible report.

### Step 4 — continuity and controls first

Run J-C0/J-C1 before the inversion branch. A candidate that passes by refusing all rights claims or transformations is rejected.

### Step 5 — execute Route N

Exercise scope flattening, missing source dependency, generation→rights promotion, correlated registry inflation, stale/cached rights and non-curative approval. Record whether each control is absent, bypassed or executed incorrectly.

### Step 6 — execute Route Q

Run the same facts/resources with Q0–Q5 implemented according to the canonical route.

Expected main-branch result: **unsupported A→pay-X enforcement = 0**, subject to the control branches and frozen assumptions.

### Step 7 — strong-peer comparison

Register B0–B3 and equalize facts, evidence access, compute/tools, records, deadline, human capacity and allowed actions. If B1/B2 closes the gap with equal/lower burden, record the negative EA differential.

### Step 8 — implementation profiles

Only after the technology-neutral fixture is frozen, project it into dated profiles. Candidate families may include author/rights-side systems such as Panodyssey, machine-readable rights semantics, provenance/credential mechanisms, agent identity/delegated-authority stacks, and downstream rights/licensing registries.

A product profile may not change the frozen event or oracle.

### Step 9 — independent producer/receiver stage

Use at least one independently implemented producer and receiver so rights/source records cross a real interface and qualifier loss/correlation can be observed externally.

### Step 10 — real decision-context stage

Only after deterministic evidence, consider a real Panodyssey or other industry context with its own legal/operational owner. The real-world stage defines its own legal/policy boundary and does not inherit the fixture oracle as substantive law.

---

## 15. Result classes for 00J

1. **Failure route reproduced:** locally plausible records compose into unsupported enforcement against A.
2. **Requirements-conforming route blocks inversion:** unsupported enforcement is prevented without deny-all behaviour.
3. **Strong peer closes the gap:** the need exists but EA differentiation narrows.
4. **Requirements gap discovered:** a candidate correctly follows the actual current S/T/H requirements yet the inversion still passes because a necessary solution-neutral obligation is absent.

Only result 4 would justify reopening the canonical Requirements for a possible new obligation.

At v0.1 design review, result 4 is **not** demonstrated.

---

## 16. Horizontal extensibility

The scenario can extend to media/licensing, software/code provenance, industrial design assets, scientific datasets, model/data lineage, enterprise knowledge bases and digital twins where the same semantic distinction exists.

The invariant is:

> **A downstream credential may be locally authentic while still being insufficient for a stronger source, ownership, authority or enforcement proposition.**

If a target domain lacks that distinction, 00J should not be forced onto it.

---

## 17. Public/reference provenance

- FG-TIDA Theme #17 — Digital Rights Infrastructure for Text  
  https://github.com/FG-TIDA/themes/issues/17
- 00 — Canonical Requirements  
  ./00_CANONICAL_REQUIREMENTS_CHALLENGES_SUFFICIENCY_HYPOTHESES_KPIS.md
- 00E — 100 Million Tokens  
  ./00E_FAILURE_MODES_100M_TOKEN_COMPOUNDING_v0.1.md
- 00F — Smart-City Mobility Divergence  
  ./00F_FAILURE_MODE_SMART_CITY_MOBILITY_SYSTEMIC_DIVERGENCE_v0.1.md
- 00G — Collective False-Context Convergence  
  ./00G_FAILURE_MODE_COLLECTIVE_FALSE_CONTEXT_CONVERGENCE_v0.3_DRAFT.md
- 00H — Batch Opportunity Beyond Authority  
  ./00H_FAILURE_MODE_BATCH_OPPORTUNITY_BEYOND_AUTHORITY_v0.4_DRAFT.md
- 00D-A01 — Bounded Oracle Construction and Test Design  
  ./00D_A01_REFERENCE_SCENARIO_TEST_ARTIFACTS_AND_BOUNDED_ORACLE_CONSTRUCTION_AND_TEST_DESIGN_v0.1.md

---

## 18. Current disposition

**Scenario status:** working draft, not W3-admitted, not executed.

**Requirements disposition:** current design review finds the canonical S1–S14 / T1–T4 / H1–H6 route sufficient to prevent the principal terminal failure when correctly implemented.

**No new universal gate is introduced.**

**No new canonical Challenge is currently justified.**

00J is therefore a new **failure fixture and quality-plan stressor**, not a new requirements family.

The decisive falsification question is:

> **If a system follows the current canonical requirements correctly, can an original author still be required—on the basis of the fixture’s downstream records—to pay a third party for reuse of the author’s own source work?**

At v0.1 design level, the expected answer is **no**. The implementation programme exists to test whether that expectation survives actual execution.
