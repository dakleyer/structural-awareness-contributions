# R01/DDS extension study — RATS evidence consumption and effective human escalation

**Canonical research integration — 6 October2026, document edition0.2.** The initial source/analytical text below remains its historical scoped analysis. [Current DDS study and controls](./HEW_DDS_STUDY_2026-10-06.md) record the new deterministic model integration. Native technology, real humans and independent review remain unexecuted/open. The original numerical results are not rewritten or pooled into a success rate.


Canonical research document0.2 / analytical predecessor0.1 · 6 October 2026 · conceptual appraisal/consumption profile.
Primary reference: RFC9334, January2023, Informational.
Proposed profile name: RATS-HEW-SoftwareState-AP/v0.1, an internal semantic study profile, not an IETF profile or wire format.
Evidence: primary architecture-clause review, scoped logical construction and exact analytical case checks. No trusted device, native verifier, attestation protocol or human campaign executed.
[Shared case](./dds-hew-v0.1/TECHNICAL_REPORT.md) · [Run Card](./dds-hew-v0.1/prior-analytical/run_card_v0.3_2026-10-06.json) · [results](./dds-hew-v0.1/prior-analytical/analytical_fixture_results_v0.3_2026-10-06.json).

## 1. What RATS contributes

RATS separates the production of Evidence, its appraisal by a Verifier and the use of Attestation Results by a Relying Party. Its architecture includes policy, trust and freshness. A result may be used within the receiver's legitimate access/action policy.

The selected analytical profile concerns a case-service's supported software-state properties. The result is consumed within its declared purpose and time. Neither the source nor this profile automatically promises a qualified human response.

[Primary RFC](https://datatracker.ietf.org/doc/html/rfc9334), especially §§4,8.4,8.5,10.

## 2. Duplication check and responsibility boundary

The current 00D benchmark already credits RATS. This extension does not claim invention of producer/verifier/consumer separation or discovery that evidence can age. RFC9334 §10 explicitly describes an interval/race in which state or policy may change after evidence/results are generated.

The question is case-specific: does the admitted profile observe and preserve the facts needed by this receiving mission decision, and does its legitimate policy use them at the point of action? If the strong native profile already does so, give it full credit.

No native Attestation Result is translated into a global A/B/C/D position, DDS outcome or new authority by renaming it. Multiple roles in one entity do not establish independent evidence; two appraisals of the same measurement need an explicit dependence treatment.

## 3. Declared analytical profile

### Roles and subject

- Attester: the declared case-service/software environment.
- Verifier: appraises supported software measurements against the declared reference/policy.
- Relying Party: the component receiving the result for the case-service use decision.
- Policy owners and source providers: identified in a later realization; their scope is not inferred from a signature.
- Accountable human owner/review pool: separate roles and evidence.

This study uses a conceptual passport-style consumption path, with a result available to the receiver. No encoding, attestation hardware, token format or root of trust is silently admitted. A real study must choose those and verify the implementation.

### Declared predicate

P_SW = the specified service software/configuration measurements meet the chosen appraisal policy for the named attestation subject.

P_SW does not, in this chosen profile, mean:
- H1/H2 is currently free;
- a reviewer has the required competence;
- the mission action is currently delegated;
- the objection is correct;
- the affected intervention is applied;
- the mission is completed.

A broader legitimate profile can support further observations. Its source, law, costs and relying policy must be incorporated rather than excluded to save a negative example.

### DDS side record

The case record can link the original native artifact to its subject/predicate, source/policy references, appraisal context, validity and receiving decision. This is a trace/profile relationship, not an invented mandatory field in RFC9334 or a new wire protocol.

Protected case content and broad raw device measurements need not be broadcast wholesale. Actual disclosure/privacy controls remain obligations of the selected realization.

## 4. Source-clause review register

| Reference | What must survive in the profile | Realization still required |
|---|---|---|
| §§3–4 | roles and native artifacts remain distinguishable | actual attester/verifier/consumer binding |
| §§7–8 | declared trust, sources/reference/policies | actual trust/material/measurement validity |
| §8.4 | result interpreted for the receiver's supported action purpose | actual consuming policy/current owner |
| §8.5 | appraisal constraints and policy meaning | actual claims/constraints used |
| §10 | freshness rule and its temporal limits | concrete time/nonce/epoch behavior |
| §11 | treatment of sensitive evidence/results | actual disclosure controls |
| Shared HEW contract | actual calendar/competence/authority/application | sources outside the software-state predicate |

The boolean attestation_accepted in the fixture stipulates that the selected precondition is accepted. It does not validate a signed result, reference values, hardware, protocol freshness or a real Verifier. The timer example is pure analytical arithmetic.

## 5. Own logical results

### Proposition RATS-HEW-1 — scoped appraisal is not an unobserved capacity fact

Suppose W_free and W_busy have the same admitted P_SW evidence/result and all allowed receiver observations, but differ in whether a timely qualified reviewer exists. Any receiver policy over that same information returns the same distribution of a capacity conclusion in both worlds.

An accepted software-state result cannot therefore establish which calendar holds without an additional relation/source that distinguishes those worlds. This is the familiar observational-equivalence argument. It is a limit of the declared profile, not of every RATS realization.

If the native profile or application already includes applicable current capacity evidence, the equal-view assumption is false and the profile must be recalculated. Our finding can then be reuse rather than difference.

### Proposition RATS-HEW-2 — recent snapshot does not imply unchanged operational state

A state assertion can be true at t0 and satisfy an age rule at t2 without remaining sufficient for an action at t2. To infer the action-time fact, the contract needs a justified persistence/change/reservation relation, or suitable new evidence.

Case07: observation at0, new non-preemptible duty at1, case arrival2, age bound5. Age2≤5; observed-calendar forecast starts review2 and decides5. The actual calendar starts review10 and decides13>6. Acceptance of the age bound and lack of timely review are compatible.

This matches a change problem already recognized by the source. It is not evidence that RATS lacks freshness. If the result covers software state only, that state may even remain correct throughout; the human calendar is simply outside that predicate.

### Proposition RATS-HEW-3 — a policy/action binding is necessary

An appraised result can be used by a legitimate receiving policy, but its cryptographic/appraisal success alone does not establish a different mission grant. In case08 a review slot exists while execution authority is revoked. A proper policy preserves denial/recontracting regardless of the favorable unrelated result.

These are scoped constructions, not proofs of native protocol failure, product risk rates or universal trilemma persistence.

## 6. Proposed extension alternatives

### Alternative A — sufficient native profile, no extra component

The existing realization already supplies the relevant state evidence, supported meaning, current policy and action-time controls. Use it and remove or narrow an unnecessary additional layer. This is a valid DDS contribution.

### Alternative B — application-level consumption profile

The native result is useful for P_SW but needs a separate case contract for human capacity, basis and current mandate. Preserve its native result and add only the necessary current references/controls in the consumer. Charge every source query, interpretation and maintenance cost.

### Alternative C — broader attestation/application evidence scope

A producer can legitimately measure additional operational state. Review whether it supports the precise capacity/queue proposition and its validity, not merely whether a JSON/token field can hold it. Fix source, costs, reference policy and measurement uncertainty.

### Alternative D — validated reservation/change coordination

The action requires a future review slot. Establish an admitted reservation or other scheduling/control guarantee; propagate invalidation and current authority. Attesting a snapshot is not the same operation as reserving resources.

These alternatives must be reviewed before implementing a combined identity/attestation/capacity solution. None is automatically a new requirement or proprietary mechanism.

## 7. Proposed receiving control and virtual trace

In this effective profile, the receiver:
1. consumes the native result for its admitted scope/policy/time;
2. preserves the protected objection and source lineage;
3. separately qualifies available human review and acknowledgement;
4. separately checks current applicable basis and action mandate;
5. admits an appropriate gate/continuation/backup decision;
6. confirms actual application and final delivery;
7. reports UNKNOWN, owner non-response or limited capability with the actual cause.

Do not output “human response guaranteed” from only a software result. Do not treat holding the mission indefinitely as sufficient usefulness. If the receiving policy may act on a result, record its legitimate owner and scope.

## 8. Kernel correspondence and changes

| Obligation | Preserved / mapped | Change or gap |
|---|---|---|
| E1 | source, evaluator/receiver, predicate, case and mandate identified | a Verifier is not automatically the private R01 evaluator |
| E2 | produce/appraise/consume messages distinct from review/apply effects | native protocol transitions not implemented here |
| E3 | source law/policy and case calendar explicit | different from original R01 sufficient-alert law |
| E4 | observation scope excludes hidden task labels | new capacity/basis evidence changes history; no free solving oracle |
| E5 | production/use/update and round-trip costs recorded | no calibrated actual measurement or verification cost |
| E6 | result success versus decision/application/completion distinguished | no local appraisal PASS promoted to global admissibility |
| E7 | good state, stale/expired data, valid continuation and changed grant included | actual interoperable realization and coverage remain open |

This table does not establish operational isomorphism. It identifies the contract to verify. Additional evidence may recover a profile; original H1 numbers require the full H1 law and ledger, not a renamed result bit.

## 9. Virtual HEW-RATS/R1,R2,R3 traversals

### R1 — strong native appraisal/reference

Apply the native predicate/policy correctly, including freshness. A software-state result can be accepted for that purpose; it does not claim human capacity outside scope. Current legitimate ordinary operation should continue where its other conditions are met.

A consumer that treats any signed result as unlimited truth/permission is a diagnostic negative, not a fair RATS comparator.

### R2 — effective case-consumption proposal

With the same underlying technology and resources, make only an actually missing case qualification explicit. A genuine current eligible H2 plus current action/basis can satisfy the calendar by5/6/7. A strong existing relying policy can obtain this same result, so additional-architecture value remains an open hypothesis.

### R3 — frozen rules, changed state/policy/time

- acceptable old age, changed calendar: no unjustified capacity claim;
- result outside allowed time or expected policy: native/profile reappraisal path;
- allowed source result, changed mandate: evaluate current action authority separately;
- no observation/producer coverage: retain UNKNOWN rather than infer healthy/available;
- valid current scope and sufficient response returns: legitimate timely continuation remains possible;
- command not applied: retain effect failure, even if appraisal and human decision were correct.

Late or conservative rejection can preserve an integrity condition while losing the mission window. Report that value/cost consequence rather than upgrading it to complete success.

## 10. Cost functions and business interpretation

C_profile = C_integration_and_trust + C_measurement_source + C_policy_and_reference_maintenance
            + sum(C_produce + C_transmit + C_appraise + C_consume + C_refresh).

Variables: observation scope, platform/profile, state volatility, policy updates, chosen freshness route, cache/reuse, retries, payload/parse burden and verification/application topology. These are functions to measure, not monetary estimates.

C_HEW additionally counts actual staffing/reserve, case preparation, human review, handover, corrected reentry and effect confirmation. A small output result does not make the producer work free. A later native test must keep private evaluator-only work separate from participant operations.

Business-value hypotheses: better supported admission decisions, fewer ungrounded reliance claims, useful current preconditions, bounded requalification and review/application accountability. Limits: unsupported/out-of-scope facts, post-observation changes, missing forecasts/reservations, verifier/source trust and the useful deadline. More frequent checks can add latency and lose useful response.

## 11. Evidence, future tests and DDS finding

Current evidence:
- source-clause interpretation and own logical constructions;
- case07 arithmetic witness (age bound passes, actual review cannot meet6);
- case08 current action-authority separation;
- cases06/13/14 UNKNOWN and ack/review separation;
- exact calendar comparison, not protocol execution.

Future realization tests:
- nominal valid source/result/policy and useful operation;
- invalid subject/result/reference/policy, source errors and unsupported meaning;
- expiry, state/policy change between observation and use;
- actual consumer handling of opaque/original native result and unknown scope;
- supported current operational data and reservation invalidation;
- safe fallback, actual application and final completion;
- privacy/protected signal handling and source dependency;
- matched strong relying-policy baseline and bounded ablation.

**Current Differential Contribution Finding:** RATS offers an existing evidence/appraisal/consumption architecture with explicit policy and freshness. The proposed HEW application asks whether its selected evidence scope actually supports the timely human and mission decision. The finite witness establishes a limitation of snapshot/scope inference in this model, not a deficiency of every RATS system. A suitable existing profile/policy can close the function and eliminate a claimed added differential.

Four-pass own review:
1. Logic: scope/time/policy versus future capacity, current grant and observed effect.
2. Evidence: source-native roles/results preserved; bools/time arithmetic not sold as native attestation.
3. Structure: explicit conceptual profile, no standardized encoding or mandatory schema invented.
4. Comprehension: “a result supports this predicate” does not mean “the whole process is justified and completed”. Same-assistant simulated reader.

Open before an applied study: wire/measurement profile, trust and implementation fidelity, owner factual review, capacity/source calibration, protected-channel controls, prospective comparison and independent/applied evidence. No automatic DBC-EL, assurance opinion, external-body adoption or product certification.


## Current DDS model delivery and scoped external comparison —6 October2026

Auditoría realizada por Codex, same assistant, on this study's source/consumer boundary and the current frozen HEW model. Prior four-pass/source records above remain historical; this is a scoped current comparison/reuse judgement, not retrospective native conformance or a global corpus closure.

Question:Evidence/appraisal/result consumption, freshness and policy ownership.

Source coverage:RFC9334 architecture/freshness source retained and official RFC route refreshed. Conceptual SoftwareState-AP remains an internal semantic profile, not an IETF wire profile.

Current evidence boundary:The model rejects stale/inapplicable supplied state results but does not generate trustworthy evidence. A false accepted basis still causes the retained source-truth diagnostic violation. Actual attestation and source correctness remain open.

The [HEW DDS study](./HEW_DDS_STUDY_2026-10-06.md), [Run Card](./dds-hew-v0.1/RUN_CARD.json), [controls](./dds-hew-v0.1/DDS_CONTROLS.json) and [actual results](./dds-hew-v0.1/runs/HEW-DDS-MODEL-20261006-04/RESULTS.json) retain sufficient delivery, unresolved response and violation separately.48 instrument assertions/42 reference checks do not become a native performance result for this subject. No population human rate or comparator superiority is established.

Reuse judgement:existing relevant native concepts/control techniques are reusable with their scope/authority/version conditions. A competent conventional composition may obtain the same outcome; a new field or combined diagram is not a differential. Code here is independently authored; code/data/full-text copying from a source would require its exact license/attribution review. No third-party artifact imported.

FG-TIDA scope:Theme13/16 and UC21 relevant comments were consulted; the grant-existence/purpose-applicability distinction is retained. Discussion and contributor review are not adoption. The original URL for the human-supplied STAMP duplication-check fragment is still not established. Further native/source-owner/independent comparison remains open.

Consumer compatibility:the original mathematical/calendar/event fixtures retain their laws; this document consumes their actual limited results. The new SQLite profile is separately declared. Any native adapter must preserve source claims/results, current grant and effect meanings and return through the existing M13/M17/C02 owners before stronger claims.

## Independent exercise successor —6 October2026

Documentary addition0.3. The [DDS Canonical Method Index](../../../../DDS_CANONICAL_METHOD_INDEX_v0.1.md) is the single DDS method entry point. This study is incorporated as a **Simplified DDS Gate-A** technology-specific implementation instance under the [Gate-A challenge–trajectory contract](../../../../DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1.md); it does not define another DDS method, Gate-B architecture verification or Gate-C native validation. The earlier analytical text above retains its original stage and claim limits.

[Independent exercise report](./independent-dds-exercises-v0.1/rats-jws/EXERCISE_REPORT.md), [frozen Run Card](./independent-dds-exercises-v0.1/rats-jws/RUN_CARD.json) and [executed result](./independent-dds-exercises-v0.1/rats-jws/runs/2026-10-06-01/RESULTS.json) give this subject its own scenarios, source/configuration, control results, costs and limitations. No old result is overwritten or pooled. Fixture assertion success includes expected denials; it is not native/product/human or deployment acceptance. Production calibration and matched/independent evidence remain open.

