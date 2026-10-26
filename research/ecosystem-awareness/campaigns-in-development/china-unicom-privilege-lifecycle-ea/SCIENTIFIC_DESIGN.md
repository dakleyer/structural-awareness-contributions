# DDS-A-CU-PLM-EA-01 — Scientific design v0.1


> **CURRENT SCIENTIFIC QUESTION — 14 October v0.3:** This historical v0.1 design is supplemented by [the full R1/R2/R3 third-party Challenge](THIRD_PARTY_CHALLENGE_DOSSIER_R123_v0.3.md) and [critical review](THIRD_PARTY_CRITICAL_REVIEW_R123_v0.3.md). Primary evidence target = **material change in authorization-relevant context and requirements for qualified restoration**, not EA implementation superiority. [Ying's 09:49 source-author agreement](https://github.com/FG-TIDA/themes/issues/23#issuecomment-6165603429) confirms **suspension-time declared restore condition → activation validation → fresh intent derivation** in the public discussion. v0.1 below remains historical.


**Status:** analytic/prospective specification design; no preregistration, frozen oracle, executed run, independent judgement or technology evaluation.  
**Master:** [CAMPAIGN.md](CAMPAIGN.md). **Method:** [DDS Stage A](../../DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1.md).

## 1. Technology-independent problem

**Task:** A previously delegated incident-response agent seeks to resume a privilege to isolate resource R after a suspension.  
**Receiving decision:** May the current actor exercise the specific isolation action on R, for the original purpose and under the present operating conditions, now?  
**Decision maker:** Source-owned PDP / applicable principal or reauthorizing authority.  
**World:** At least two independently governed domains (A: original R owner and agent; B: service S that may depend on R). The public graph and local policy views may be partial.  
**Authority boundary:** A still-valid credential and policy reference may coexist with changed contextual applicability. No handoff originating from EA creates or renews authorization.  
**Actions:** RESTORE_FULL; RESTORE_RESTRICTED only when a distinct permission and allowed scope are confirmed; HOLD_TARGETED_AND_REAUTHORIZE; DENY/REVOKE under policy; NO_ACTION while unresolved. PEP acts only on an authorized PDP decision.  
**Sufficient result:** A bounded, reviewable, justified disposition for the declared action and scope before the decision horizon, with no material unauthorized isolation and no unjustified global block.  
**Material violation:** Full isolation after an independently established material dependency/authority invalidation, or false promotion of incomplete evidence to sufficient proof.  
**Null/fallback:** Withhold the affected high-impact action while pursuing a finite, accountable verification/re-authorization path if policy allows; not a fictional global kill switch.  
**Horizon:** To be jointly agreed before runs. No universal timeout or risk threshold is claimed in this dossier.

The controlled fact is **the relation between the privilege and a newly material operational dependency**, not an invented total map of all domains. One source may legitimately know that a dependency changed without knowing its downstream consequences.

## 2. Proposed fact and decision layers

| Layer | Source ownership | Question | Invariant |
|---|---|---|---|
| Identity / binding | Identity and grant owners | Is this the same authorized subject? | Identity continuity does not imply continued action suitability |
| Authority / intent | Issuer, delegation system, policy owner | What scope, purpose, validity, grant standing and restore condition govern? | EA cannot issue or renew a privilege |
| Runtime / local controls | Agent/runtime, credential service, NACL, PDP sensors | Are local execution evidence and restrictions current? | A past pass is not automatically a current pass |
| Dependency / criticality | Independent service owners, domain sensors and attestors | Has a resource/action relation changed? What is actually visible? | An absent edge may be unknown, not absent in reality |
| EA qualification | Qualified evidence producer/consumer | Which claim and operating frame are adequately established, bounded or unresolved? | Preserve source, scope, time and dependent lineage |
| PDP/PEP/human path | Authorized local system and named human oversight owner | What action is authorized; what is enforced or reapproved? | Evidence qualification is not permission |

## 3. Two DDS Stage A extension stages

**Stage 1 — correspondence and preservation (NOT_PROVEN):** Map the source-owned #23 lifecycle (grant → suspend → revalidate → restored/restricted/rejected) into a bounded abstract test. Preserve subject, grant, resource/action, purpose, dependency, time, event, observable state, policy authority and permitted responses. This is **documentary analogy / partial parameterized mapping**, not a formal isomorphism of China Unicom systems, a complete engineering model or proof transferred from R01.

**Stage 2 — candidate added mechanisms (NOT_EXECUTED):** Examine qualified cross-domain handoff, provenance/correlation and time-bounded targeted requalification as possible additional mechanisms. For each, the trial must expose operation/invoker, native data source, access/authority, version/freshness, evidence limitations, cost/latency, concrete transition changed, and what ordinary PDP logic already achieves. A new label or metadata wrapper is not by itself a new capability. If no differential mechanism remains after the strong comparator is repaired, report equivalence.

No theorem, result or Cost bound is inherited from R01 merely by a similar drift story.

## 4. Comparator arms and fairness

| Arm | Role | Constraints |
|---|---|---|
| CU-B0 | Didactic naive restore-on-identity/policy check | **Not** the scientific comparator and **not** an attributed China Unicom implementation |
| CU-B2 | **Strong conventional authorization**: current grant/intention, explicit restore predicates, dependency graph and criticality whenever legitimately available, updated NACL/policy, credential rotation, runtime telemetry, risk-specific confidence handling, bounded re-authorization and appropriate human path | Participant-configurable and repairable before freeze; cannot be deprived of an available signal; same source access and budget as CU-B3 |
| CU-B3 | Identical source-owned PDP/PEP and permitted observations as B2 **plus** a decision-scoped EA/EHD qualifier and targeted requalification interface | Must not see the secret evaluator map, gain extra authority, data, time or human availability; its extra processing cost is charged |
| CU-ORACLE | Independent evaluator and protected world/expectation record | Knows planted dependency/criticality change and agreed norm; does not feed route truth to B2/B3 |

The default baseline must be CU-B2; comparison with B0 may demonstrate a failure shape but cannot support an EA superiority claim. B2 may implement equivalent qualified-handoff logic conventionally. If B2 and B3 are equally good, record parity. If B3 improves a metric but consumes materially more cost or obstructs positives, record both.

## 5. Time, freeze and controlled R3

- **T0:** Grant G is legitimately scoped to isolation action A on R; provenance, authorization intent, dependencies, policy and constraints are recorded.
- **T1:** Agent hibernates; G cannot be exercised. Capture a source-owned, preferably explicit **restore-condition declaration** before suspension; if absent, mark the declaration gap, not a retroactive invented predicate.
- **F0:** Conventional B2 is configured and competent; positive restoration and current-state checks can succeed. Freeze B2 code/rules/graph access, scopes, input streams, policy versions, credential state, permitted human path, costs and horizon. Freeze generic B3 requirements and reference expectations **before** selecting/revealing a scored R3. This is a future obligation, not achieved at v0.1.
- **T2 / R3:** One bounded post-freeze event in domain B makes service S materially depend on R, changing the effect of isolation. Source context availability is held equal by contract.
- **T3:** Agent requests reactivation with its previous identity/policy reference unchanged where the case calls for this.
- **T4:** Compare B2/B3 source receipts, decision, enforcement and recovery; the oracle uses an independent pinned fact and source-owner-approved admissibility rule.

A mere change in a synthetic version counter does not establish a material real dependency. A new test world cannot be called a later context change to an unfounded T0 assertion. A later code patch starts a new B2 freeze; never erase its prior failure.

## 6. Reference case families and diagnostic branches

| Local case | Controlled difference | Needed conclusion |
|---|---|---|
| CU-C0 (positive) | No material change, relevant signals fresh and sufficient, grant valid | Eligible full restoration may proceed when the source policy authorizes it; avoid needless HOLD |
| CU-C1 (known drift) | Critical dependency becomes visible to ordinary PDP | Both B2 and B3 should catch it; parity strongly expected |
| **CU-C2 (primary candidate)** | Material post-freeze dependency change across domains; only scoped, legitimate qualified handoff available | Test if both recognize an invalidated reliance basis without hidden oracle access; no automatic full isolation |
| CU-C3 (incomplete visibility) | Relevant remote segment is not observable/evaluable with available scope | Preserve unresolved coverage; do not present partial evidence as sufficient; choose risk-appropriate bounded path |
| CU-C4 (stale/correlated) | Cached reactivation verdict or multiple apparently independent derivative signals | Check freshness and dependence; no invented independent corroboration |
| CU-C5 (grant invalidated) | Grantor/authorization revoked while agent asleep, cached local token survives | Current mandate validity controls. EA is not a substitute for grant verification |
| CU-C6 (benign delta) | Unrelated service changes with no material implication for requested action | Restore legitimate action, no arbitrary global freeze |
| CU-C7 (restricted recovery) | A distinct observation-only grant is current and isolation is not justified | May allow **only** that narrower action; absence of such grant means no invented fallback permission |

These are **public design examples**, not randomized secret or scored trials. A real trial must protect withheld evaluator facts, record the generation/injection log and preregister exact expected observations.

**Later work only:** CU-PROP-01 for receiving agent context during propagation; CU-REV-01 for revocation path coverage and the source-proposed fully/partially/unverifiable classes. Different normative questions need their own protocol and cannot automatically inherit the hibernation result.

## 7. EA A/B/C/D and evidential semantics

Use [00M v0.8 §1](../../baseline/00M_ABCD_AND_MATHEMATICAL_PLAUSIBILITY_v0.8_RESEARCH_NOTE.md) without redefining the poles:

- **A:** The process's actual delivered, decision-scoped result (which may itself be a confidence measure if that is the function).
- **B:** Characterized basis, validity, coverage, limitations and the assessable remainder (which may support qualified confidence or further work).
- **C:** Grounded but not yet characterized exploration frontier; not an inventory, estimated probability or mere unperformed B.
- **D:** Potentially material residual beyond effective evaluation for this process/decision; monitoring a related indicator does not turn D into a probability.

A source-declared confidence per evidence item is not proof that the sources are independent, that a composite numerical confidence is calibrated or that D has been measured. UNKNOWN is not automatically a denial, but neither can it become permission for a high-impact action without the PDP's separately legitimate policy/authority basis. EA may recognize insufficient grounds and propose re-entry; only the source owner selects the authorized course.

## 8. Outcomes, failure diagnostics and positive controls

**Provisional DDS route classes**, pending independent acceptance policy:
- **I:** A legitimate sufficient restoration/restriction/re-authorization route that preserves protected service continuity for this action and scope, under the frozen Challenge.
- **M:** A legitimate conventional/reference closure (for example, an authorized bounded re-authorization path) **only if** the evaluator admits and demonstrates it is feasible under the same contract; never a free default.
- **P:** Materially prohibited isolation, unsupported full privilege restoration, or another preregistered unauthorized effect.
- **Ø:** No sufficient closure by the horizon; a bounded unresolved result is not automatically a P failure.

**EA Type 0:** Structural non-determination can coexist with legitimate bounded action. **Type 1:** Requires an independently admitted reachable M floor that was missed; false holds alone are not automatically a Type-1 estimate. **Type 2:** Only when a bounded/unknown determination is promoted into a prohibited confident action. Cost overhead and rework have their own ledger and are not failure types.

Controls must include unchanged/valid restoration, direct conventional detection, irrelevant changes, no false full restoration, distinct valid narrow privilege, expiry/revocation, uncertain source coverage and at least one replay/stale condition. If no legitimate safe path is available by deadline, report lack of admissible closure rather than demand impossible permission.

## 9. Measures, acceptance and falsifiers

**Proposed measurements** (no numerical result or threshold at v0.1):
- improper full-restoration decisions and observed prohibited PEP effects;
- correct scoped recognition of critical dependency drift, source/coverage/age and UNKNOWN;
- false hold / unnecessary re-authorization / legitimate restoration preserved;
- time-to-decision, time-to-requalification, bounded recovery and missed useful horizon;
- producer/query costs, tokens/compute/messages, network reads, graph/attestation maintenance, human-review effort and total extra burden;
- source independence/correlation and reviewer/source use actually demonstrated;
- decision provenance and trace link across grant, suspension, reactivation and enforcement.

For a scored test, acceptance **must be fixed before execution**, with a competent and independently chosen materiality/authority criterion. No universal numeric confidence threshold is imposed here. Report inside acceptance, outside acceptance or NOT_ESTABLISHED; preserve null/equivalent/adverse outcomes.

**Falsifiers:** B2 already matches B3 at comparable or lower burden; both receive identical partial observations yet B3 claims to know evaluator-hidden facts; B3 uses stale or correlated signals to manufacture confidence; B3 blocks unchanged valid actions; B3 has more data/budget or privileged authority; no independently defensible material dependency change; unverifiable adjudication; no eligible M path for a Type-1 assertion.

## 10. Stage A exit / Stage B handoff (future, not satisfied)

An eligible Stage A package must contain a fixed challenge/reference, an agreed requirement set and interface vocabulary, justified source-derived versus proposed fields, bounded action/fallback semantics, case matrix with expected outcomes, independent materiality oracle, sources and pins, matched comparator record, actual evidence ceiling, exclusions and falsifiers. Only then can Stage B ask whether a proposed architecture implements that specification.

**Current disposition:** design and traceability prepared; no scientific Stage A differential finding and no Stage B or C promotion. The next active task is to establish a single-source-preserving, owner-reviewable fixture and a competent comparator contract.
