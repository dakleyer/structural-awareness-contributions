# Fencing tokens and confused-deputy prevention — DDS/R01 extension study

**Canonical research integration — 6 October2026, document edition0.2.** The initial source/analytical text below remains its historical scoped analysis. [Current DDS study and controls](./HEW_DDS_STUDY_2026-10-06.md) record the new deterministic model integration. Native technology, real humans and independent review remain unexecuted/open. The original numerical results are not rewritten or pooled into a success rate.


Canonical research document0.2 / analytical predecessor0.1, editorial0.1.1 · 6 October 2026 · local internal research.
Prepared by Codex under Ivan's instruction: “añade esto también como extensión: fencing tokens, and work on the confused-deputy problem”.
Fourth study in the [extension register](./HEW_DDS_STUDY_2026-10-06.md), continuing the same [Human Escalation VNext](./HUMAN_ESCALATION_WHISPERING_VNext.md).

**Finding:** resource-enforced fencing can reject delayed effects from an older ownership generation. Scoped delegation can prevent a privileged deputy from supplying authority that the requester lacks for that action. Both are established controls. Their combination is a candidate application profile for HEW, with no demonstrated advantage over a competent existing implementation of the same controls. Neither produces qualified human review capacity or sufficient grounds for a decision.

## 1. Two questions, two control families

A fencing token answers a narrow ordering question: **is this request from an ownership generation that the resource still accepts?** Imagine an old executor holding generation 42. It pauses. Another executor receives generation 43 and takes over. If a delayed request from42 arrives after the actuator has advanced its accepted generation to43, the actuator rejects42. A lock held in another service cannot do this alone: the effect-producing resource must enforce the fence.

The confused-deputy problem asks a different question: **whose authority justifies this particular effect?** A service may be allowed to administer many resources while a requester is allowed to affect only one. If the service uses its own broad privilege whenever the requester supplies a resource name, it can perform an operation that the requester had no right to request. An authentic identity and a current fencing generation can coexist with that mistake.

The concepts are not interchangeable. Fencing is a coordination/enforcement pattern; confused deputy is a failure pattern addressed by authority confinement, explicit delegation and receiving policy. Their implementation belongs to the actual owners of the services and resources, not to a new universal EA authority.

### Primary-source basis, fixed at consultation

Sources read on 6 October 2026:

| Source | Version/date and actual reading | Established contribution credited |
|---|---|---|
| [Hazelcast FencedLock](https://docs.hazelcast.com/hazelcast/5.6/data-structures/fencedlock) | documentation branch5.6; page read; no installation | monotonically increasing ownership tokens, external resource enforcement and session-loss scenario; CP configuration matters |
| [Mike Burrows, Chubby](https://static.googleusercontent.com/media/research.google.com/en//archive/chubby-osdi06.pdf) | OSDI2006; selected §2.1 and §2.3–2.6 read, not all 16 pages | sequencers carry lock/mode/generation; receiving server checks validity; highest-observed and current-cache approaches are distinct |
| [Norm Hardy, The Confused Deputy](https://people.csail.mit.edu/alinush/6.858-fall-2014/papers/confused-deputy.pdf) | 1988 paper, complete 3-page mirror read | compiler mixes caller-directed output with its own file privilege; capability-based designation/authority is an established response |
| [AWS IAM confused-deputy prevention](https://docs.aws.amazon.com/IAM/latest/UserGuide/confused-deputy.html) | living official documentation; page read on consultation date | cross-account and cross-service mitigations; provider-assigned customer ExternalId and supported source restrictions |
| [OAuth2 Token Exchange, RFC8693](https://www.rfc-editor.org/rfc/rfc8693.html) | January2020, Standards Track; targeted §2.1/2.1.1 and delegation claim/example material | subject/actor and resource/audience/scope; token exchange does not generally propagate revocation by itself |

No unversioned documentation is described as an immutable implementation pin. This study independently specifies its small analytical law; it does not implement or copy vendor code.

## 2. What a fence actually promises

Let e be the request's verified generation for resource r, and F_r the resource's accepted generation floor. In the declared maximum-generation profile:

```
reject if e < F_r
otherwise, if other receiving conditions hold:
    atomically update F_r := max(F_r, e) and commit the effect
```

Equal-generation operations are permitted in this profile: one owner may perform several legitimate operations. Fencing therefore does not, by itself, ensure one effect per request, prevent all replay, or order commands within the same generation. Idempotency/request identity and, where required, per-command sequencing are separate obligations. Other native protocols may impose additional rules; preserve them when selecting a realization.

The conditional invariant is simple: if trusted generation issuance is ordered, resource scope is correct, the floor cannot regress and comparison/update/effect share a valid atomic boundary, then no request with e < F_r at that boundary is accepted. Accepted effect generations do not decrease. This is a statement about the admitted law, not a guarantee supplied by putting an integer in a message.

### Conditions that must be supplied by the realization

1. A legitimate generation issuer and validated resource/holder binding. An attacker-selected large number is not a valid fence.
2. Generation ordering that survives issuer failover, restart and resource reincarnation. Define the incarnation and overflow/recovery treatment rather than assuming a counter can never repeat.
3. Resource-side enforcement on every relevant effect path. Checking at a gateway cannot cover an unchecked actuator/admin path.
4. Atomic exclusion of the check/write race. A check that passed before a later generation commits is not permission to write afterward without the needed recheck/transaction.
5. Non-regressing retained floor at the relevant durability/replication boundary. Loss of this state can re-admit an old request.
6. A declared handover completion point and useful-time/continuity policy.

Hazelcast's documentation describes a CP FencedLock and notes weaker guarantees in its default unsafe CP-subsystem mode. Its exactly-once claims concern the documented lock API, not every external business action. A future Hazelcast arm must pin edition/version, CP configuration, session settings, reentrancy and external enforcement; this draft has none installed.

### The handover visibility limit

“A new owner received 43” and “every effect resource now excludes 42” are different events. A resource remembering only the greatest token it has seen can still accept 42 if it has not received 43. An explicit barrier can install43 before handover is declared complete, or a receiving protocol can establish current ownership at the effect boundary. The precise guarantee and cost depend on the chosen protocol.

Example: the authority issues 43; an old 42 request reaches an actuator whose floor remains 42; a highest-seen guard accepts it. After the actuator installs 43, it rejects the same 42 request. This is a limit of the stipulated weak receiving profile, not a claim that all Chubby sequencer validation or all current-ownership protocols share that limit. Chubby documents both validity checks using its state/cache and comparison with the latest observed sequencer.

A later fence does not undo an effect already applied. Revocation of a mission grant, expiration of a lease and advancing a resource floor are separate events, with separate observation/enforcement semantics.

## 3. Confused deputy: current ownership can still be misused

For HEW, a case-service may file objections, select a route and ask an actuator to apply an approved corrective action. Its service identity could have wider infrastructure privileges than the governed agent or human principal. A good-faith objection must not become an implicit grant to use all those privileges.

Declared example:
- principal-A is permitted to request an approved safe pause on actuator-A;
- the deputy case-service can communicate with both actuator-A and actuator-B;
- a request naming actuator-B arrives with the deputy's genuine current fence for B;
- a fence check can pass while the principal's requested action remains outside its admitted grant.

The receiving rule must establish an applicable delegation or another legitimate authority basis. It must not select an unrelated deputy privilege merely because that privilege makes the named operation executable. The same issue applies to reading private case records, cancelling a critical duty, changing policy, or suppressing an objection.

### Proposed case-specific delegation contract

This is an application-level semantic profile, not a new SPIFFE SVID, RATS claim or OAuth standard field set. Keep native tokens/results intact and bind the existing objects through an explicit receiving interpretation:

| Binding | Question answered | Important limit |
|---|---|---|
| Subject/principal and acting deputy | on whose behalf, and who is acting? | authenticated caller need not hold the requested grant |
| Tenant/resource and receiving audience | what object and intended recipient? | aliases, redirects and cross-tenant mapping require actual validation |
| Case, decision and permitted operation | which decision supports which effect? | “reviewed” without action scope is insufficient |
| Purpose/conditions | which declared use and constraints are admitted? | matching a label does not establish true intent or sufficient grounds |
| Issuer, policy version, validity and current grant | which legitimate authority and current policy? | freshness/expiration alone do not propagate all revocations |
| Protected filing versus adverse action | may this signal be recorded, and may a separate effect occur? | failure of action authorization does not establish misconduct in filing |

AWS's documented ExternalId and source conditions are concrete examples of contextual trust restrictions, not a universal recipe for this profile. ExternalId is not a replacement for all action/resource policy; source-condition support is service-dependent. No AWS account, trust policy or role assumption was modified.

RFC8693 supplies useful existing delegation terminology. A subject/actor trail still needs a policy deciding which authority is acceptable for this action, and a chosen revocation protocol. We do not manufacture a live token exchange or immediate-revocation guarantee from documentary fields.

## 4. Application to the shared HEW case

The [shared case](./dds-hew-v0.1/TECHNICAL_REPORT.md) has arrival 2, an independent acknowledgement deadline 3, a three-tick substantive review, decision deadline 6, application deadline 7 and delivery deadline 8. Its primary reviewer is occupied over [1,10). Qualified authorized H2 can decide 5, apply 6 and deliver 7. These are illustrative model coordinates, not measured human service times.

Add the following actuation slice without changing that calendar law:

1. Preserve protected case receipt and owner acknowledgement.
2. Establish sufficient review/basis and a legitimate scoped decision.
3. If execution ownership changes, establish the selected fence/handover boundary.
4. At the effect boundary, validate current receiving delegation and resource generation under the declared consistency contract.
5. Confirm application separately from approval or token issuance; preserve unresolved states and legitimate continuation.

The new local fixture examines steps 3–4 and selected limits. It does not simulate the full sequence, measure added delay, or execute the fourteen calendar cases again. Those original results remain unchanged.

An acknowledgement-only owner may still lack review authority. A qualified reviewer may approve only a particular corrective action. An executor's current generation may still be outside the action grant. A correctly authorized current operation may still lack sufficient human review or sufficient basis. Each successful layer retains its scope.

For critical-duty continuity, qualify any handover/pause/reassignment separately. Fencing an executor does not authorize interrupting H1 or magically supply H2. If no permissible useful continuation exists, record that limit rather than claim recovery because an unsafe operation was blocked.

## 5. Relationship to the other three extension studies

| Study | Useful contribution in this composition | What this fourth study adds as a question |
|---|---|---|
| [STAMP/STPA](./STAMP_STPA_EXTENSION.md) | analyze unsafe control actions, causal assumptions and feedback | old executor acts after handover; deputy uses wrong principal/purpose; check/write and missing effect feedback scenarios |
| [SPIFFE/SPIRE](./SPIFFE_SPIRE_EXTENSION.md) | authenticated workload origin and native assertion interpretation | identity versus applicable delegation; identity remains accepted while grant changes |
| [RATS](./RATS_EXTENSION.md) | appraised evidence with declared scope/time/policy | an acceptable result is not the principal's grant or a resource-enforced execution fence |

The new questions should return to the sole owning documents' review routes before a canonical integration. This table is a proposed compatibility map; it does not rewrite their native contracts or retroactively extend their executed evidence.

## 6. Kernel correspondence and own conditional arguments

| Obligation | Preserved | Added condition or limit |
|---|---|---|
| E1 | source, actor, role, case, decision and effect references | principal/deputy and resource ownership must be distinguished |
| E2 | causal order and actual intervention/effect | issuer, barrier, receiving check and commit events; checks are not effects |
| E3 | original mandate and applicable world law | explicit atomic/durable fence law and scoped receiving-policy law |
| E4 | only admitted participant observations | highest-seen floor may lag issuer; policy-known is not global omniscience |
| E5 | all work/resources needed for the result | issuance, handover, validation, durability, retry, source and human work |
| E6 | useful legitimate delivery remains the objective | correct rejection alone is not complete service delivery |
| E7 | positive, adverse and changed-condition cases | current legitimate return, cross-scope request, race/restart/path limits |

This is a correspondence checklist, not proof of full operational isomorphism with R01.

**Argument A — old-generation exclusion:** under §2's exact law and conditions, induction over resource events gives a nondecreasing floor. Every accepted write is at least that floor, which includes prior accepted/installed generations. The finite checker explores a small declared grid of these events. It does not prove a consensus or durable-storage implementation satisfies the law.

**Argument B — a fence alone cannot select the principal's authority:** two requests can share a valid resource generation, resource, deputy and source validation while differing only in the principal's action entitlement. If the receiving policy inspects only fencing inputs, its response is identical for both. A current fence therefore does not entail legitimate delegation. The fixture supplies explicit wrong-principal/action/tenant witnesses; this is a scoped information/authority argument, not a new cryptographic result.

**Argument C — delegation alone does not order an old executor's delayed effect:** a principal's action grant can remain applicable while execution ownership changes. A request-specific grant check can accept both generations if it has no ownership/effect ordering condition. A conventional combined policy may close both A and B with exactly the same outcomes as this proposal.

## 7. Extension-scoped virtual FCD/R1,R2,R3

These are virtual constructions, distinct from original R01 R1/R2/R3, DBC-R# and vendor arms.

**FCD/R1 — strongest relevant conventional reference.** Admit authenticated source, legitimate scoped policy, resource-enforced current ownership/fencing, durability and ordinary idempotency where the use case requires them. Admit the same real reviewer pool/observations as the candidate. A conventional correct combined receiver rejects both stale-generation and wrong-grant requests and permits legitimate current continuation. This is the primary comparator, even when it removes any differential.

**FCD/R2 — proposed HEW consumption/composition.** Reuse those controls and link case/decision/basis/authority, useful timing, acknowledgement, application evidence and protected unresolved handling. Only an actually absent function may be credited as additional. New fields or a renamed predicate are not proof of improved outcomes. The current fixture does not run R1 and R2 as deployed controllers.

**FCD/R3 — changed conditions with the same obligations.** Examine handover before floor visibility, grant revocation with accepted identity, policy unavailability, resource restart, wrong resource/audience/action, same-generation replay, unchecked alternate paths and recovery to a newly legitimate grant. Require legitimate continuation as well as correct exclusion. A capacity or basis failure remains visible even when the combined control passes.

## 8. Analytical run and evidence boundary

Prospective [Run Card](./dds-hew-v0.1/prior-analytical/fencing_deputy_run_card_v0.1_2026-10-06.json), [checker](./dds-hew-v0.1/prior-analytical/check_fencing_deputy_fixture_v0.1_2026-10-06.py), [result](./dds-hew-v0.1/prior-analytical/fencing_deputy_results_v0.1_2026-10-06.json).

The run is an in-memory Python model. Identity, token verification, grant truth and capacity/basis are stipulated inputs. The authority predicate compares one declared policy contract; purpose comparison validates a field, not a person's actual intent. Maximum-floor atomicity is a model transition, not a tested hardware/database transaction.

The card fixes 20 cases before execution: legitimate current and renewed continuation; stale generation before/after barrier; wrong principal/tenant/resource/action/purpose/audience/deputy/decision; expired or revoked delegation; unknown policy; unverified large generation; wrong token scope; and accepted controls with missing human capacity or basis.

The finite trace grid contains 6 possible event kinds/generations, length 4: 1,296 sequences and5,184 modeled events. It audits accepted writes against the history maximum and nondecreasing generation. A separate race grid enumerates6 legal interleavings of two checks and two commits. It is designed to retain the unsafe check-then-unchecked-write witness and examine atomic rechecking. Additional declared constructions concern persistence loss, missing effect-path coverage, same-generation operations/repeated request IDs and the inability to undo earlier effects.

Executed result: all 20 declared cases matched;1,296 event sequences (5,184 modeled events) satisfied the admitted non-regression law. Of6 legal check/commit interleavings, 2 allowed generation regression under separate check/unchecked commit; 0 did under atomic resource rechecking. These are exhaustive counts only within the registered finite grids, not deployment failure rates. The hard-coded expected case contract is authored by the same assistant; finite enumeration is reproducible support, not independent adjudication. Idempotency/restart/bypass examples are algebraic constructions, not database, crash or penetration tests.

The field `conditional_hew_path` means only combined fencing/delegation plus stipulated capacity/basis. It does not evaluate all deadlines, successful human action, receipt protection, append-only storage, privacy, non-retaliation, application confirmation or full mission conformance. F13 can pass this field while demonstrating that a resource has not learned a new ownership generation; it must never be presented as an end-to-end safe handover verdict.

No Chubby, Hazelcast, AWS IAM, OAuth token exchange, SPIRE, RATS or human runtime was executed. Mechanism ablations clarify different functions; they are not weak vendor baselines used to claim superiority.

## 9. Technical C–R–E and deployment BV–R–C

Keep R01's technical Cost–Risk–Effectiveness definitions and original results. For this added slice, prospective effectiveness measures are:
- exclusion of stale effects after the declared handover boundary;
- exclusion of out-of-grant deputy actions;
- successful current legitimate effects, with useful latency and continuity;
- separately, duplicate/reordered command handling where admitted.

Residual-risk dimensions: untrusted/reused generations, barrier visibility, issuer/resource state loss, stale policy, aliases/cross-tenant confusion, check/write races, bypass surfaces, overly broad delegation, unavailable legitimate recovery and real human review limits. Frequencies are not estimated by counting these synthetic cases.

Technology lifecycle cost can be decomposed without assigning prices:

```
C_control = C_design_and_integration + C_policy_and_mapping + C_state_migration
          + C_maintenance_and_recovery
          + N_issue*c_issue + N_receive*c_validate
          + N_handover*(c_barrier + c_state_persistence + c_confirmation)
          + N_retry*c_retry + N_policy_refresh*c_refresh
          + C_idempotency_if_required + C_current_sources
```

Variables include resources/partitions, handover rate, consistency/durability, policy refresh/validation, availability targets, all actuator paths, retry volume and storage/receipt requirements. Consensus, recovery and barrier work are not free because a token is small. Policy and fence checking can have shared infrastructure; do not double-count it. Added latency and recovery interruption must enter the original useful-window test before any deployment success claim. No runtime timings, money or linear scaling law are admitted here.

Deployment Business Value–Risk–Cost additionally asks what legitimate service is delivered: continuity of a critical duty, trustworthy corrective action, appropriately protected objections, useful turnaround and reduced recovery/manual burden. Limits include late/unavailable human review, insufficient grounds, lack of action authority, irreversible prior effects and lost useful delivery despite correct rejection. The DDS service fee is separate from the technology's cost and the deployment's value. A commissioned DDS buys scoped work/deliverables, not a guaranteed PASS.

## 10. Initial own review — first four passes

Auditoría realizada por Codex, 6 October 2026, within this chat; no independent reviewer or source-owner confirmation. Draft corpus correspondence checked against commit65517160658e6485f2dd63415a7365674e9bd6ea and existing local extension documents.

1. **Logic:** read the definitions, conditional law, handover boundary, delegation profile, HEW composition and kernels. Separated ordering from entitlement, source validation from asserted integers, same-generation effects from idempotency, and action authorization from actual useful review. Retained the pre-barrier acceptance counterexample.
2. **Evidence:** contrasted the primary-source clauses in§1 with the draft's attributions and future realization conditions. Chubby selected-section reading, current Hazelcast/AWS documentary scope and RFC reading limits remain explicit. Native source behavior is not inferred from model booleans.
3. **Editorial/trace:** examined terminology, links, native/profile object separation, E/R namespaces and outcome naming. Original calendar law, earlier source cuts and results remain distinct. Canonical incorporation proposals stay at the end; this is one new study under the same local parent, not a VNext of VNext or a new campaign.
4. **Comprehension:** same-assistant simulated external reading of the examples and conclusions. The reader should distinguish an old executor, a wrongly empowered deputy, a properly authorized current action and missing human review. This is not factual review by Nell, a manufacturer or an external client.

These own readings cover this draft's stated scope. They do not close the corpus review, native fidelity or the complete service study. Final execution/structural verification is recorded separately in the delivery receipt.

## 11. Fifth pass — external work, differential and reuse

Auditoría realizada por Codex, 6 October 2026, following the fifth-pass instruction added in [CORPUS_REVIEW_PROCEDURE at the consulted cut](https://github.com/dakleyer/structural-awareness-contributions/blob/65517160658e6485f2dd63415a7365674e9bd6ea/governance/CORPUS_REVIEW_PROCEDURE_2026-10-06.md). This is a scoped external comparison of this fourth draft, after§10; it is not retrospective completion of the other three studies' fifth passes.

Search question: what existing control already handles obsolete ownership or a privileged service's action on another party's behalf, and what can the HEW workflow reuse? Routes/terms explored: official FencedLock/fencing documentation; Chubby publication and sequencers; Hardy original confused-deputy paper; official IAM confused-deputy prevention; RFC8693 delegation/resource/revocation. Primary sources and actual coverage are fixed in§1. Secondary search hits were not used as technical evidence.

| External work | Relation and scoped judgement | Concrete reuse and compatibility conditions | Still open |
|---|---|---|---|
| Chubby and Hazelcast FencedLock | overlap with generation-based stale-effect exclusion; **reusable with conditions**; differential not established | use the established resource-enforcement/barrier question and negative delayed-effect scenario; preserve chosen native sequencer/token semantics and consistency profile | choose a native realization; provider fidelity, current-owner visibility, durability and all effect paths |
| Hardy | prior formulation of mixed-authority failure and capability-oriented response; **reusable with conditions** | retain principal/deputy separation and explicit object/action authority in the analytical contract; credit original formulation | actual capability/delegation architecture, revocation and scope-preserving adaptation |
| AWS IAM | concrete trust-context mitigation, not merely a theoretical analogy; **candidate pending deployment** | if AWS is the declared deployment, review applicable role/resource trust restrictions and actual condition support; preserve service/customer mapping | no AWS deployment chosen; no policy imported or tested |
| RFC8693 | existing subject/actor and token-exchange concepts; **reusable terminology with conditions**, implementation pending | use correct delegation vocabulary and check the exact target/grant/revocation protocol; do not alter native token fields | chosen STS/token profile, receiving policy and resource consistency |
| Existing [00D benchmark](https://github.com/dakleyer/structural-awareness-contributions/blob/65517160658e6485f2dd63415a7365674e9bd6ea/research/ecosystem-awareness/baseline/00D_CANONICAL_ARCHITECTURE_BENCHMARK_AND_REFERENCE_SCENARIO_EVIDENCE_v0.2.md) | already credits delegated authority/OAuth2 exchange and identity/state controls; **overlap credited** | connect the new bounded actuation witnesses through owning reviews; no claim that delegation is newly discovered here | exact proposed integration and native/reference reconstruction |
| FG-TIDA/Nell linkage | supplied duplication-check instruction is relevant context; **specific attribution pending** | preserve human-supplied wording and existing Theme13↔16 source task; do not claim Nell requested this fourth subject or endorsed the profile | original quote URL and a focused FG-TIDA/comment search for this fourth subject; no full external/FG-TIDA coverage claimed |

No exact “fencing” or “confused deputy” match was found in the consulted00D text. That is a lexical result within one pinned source, not proof of conceptual novelty or worldwide absence of prior art. The source already includes materially related delegated-authority controls.

Reuse here means attributed ideas/terminology and independently authored analytical examples. No third-party code, diagrams, full text or datasets were imported. Distribution/copying of a chosen implementation or source artifact still requires its exact version/license review; a public URL grants no blanket permission. A code-candidate selection is not an authorization to deploy it.

**Differential Contribution Finding:** no comparative advantage is established. A competent reference that enforces both resource ordering and applicable delegation can obtain the same model outcomes. The proposed additional contribution is a case-specific composition and measurement plan joining these controls to sufficient human review, timing, protected filing and confirmed application. Its benefit must be examined only where those functions are actually absent, under equal sources/resources/authority, with the costs and scope of any new information declared.

## Current DDS model delivery and scoped external comparison —6 October2026

Auditoría realizada por Codex, same assistant, on this study's source/consumer boundary and the current frozen HEW model. Prior four-pass/source records above remain historical; this is a scoped current comparison/reuse judgement, not retrospective native conformance or a global corpus closure.

Question:Resource generations and principal/deputy scope, both necessary questions.

Source coverage:Hazelcast5.6, Chubby selected sections, Hardy paper, AWS IAM and RFC8693 retained; official fenced-lock, IAM and token-exchange routes refreshed. No copied code/native deployment.

Current evidence boundary:Local SQLite effect/floor transaction, reopening, command identity, current source-grant and caller-case binding tested. Highest-seen visibility is still bounded by installation; no distributed/hardware/physical guarantees or universal immediate revocation.

The [HEW DDS study](./HEW_DDS_STUDY_2026-10-06.md), [Run Card](./dds-hew-v0.1/RUN_CARD.json), [controls](./dds-hew-v0.1/DDS_CONTROLS.json) and [actual results](./dds-hew-v0.1/runs/HEW-DDS-MODEL-20261006-04/RESULTS.json) retain sufficient delivery, unresolved response and violation separately.48 instrument assertions/42 reference checks do not become a native performance result for this subject. No population human rate or comparator superiority is established.

Reuse judgement:existing relevant native concepts/control techniques are reusable with their scope/authority/version conditions. A competent conventional composition may obtain the same outcome; a new field or combined diagram is not a differential. Code here is independently authored; code/data/full-text copying from a source would require its exact license/attribution review. No third-party artifact imported.

FG-TIDA scope:Theme13/16 and UC21 relevant comments were consulted; the grant-existence/purpose-applicability distinction is retained. Discussion and contributor review are not adoption. The original URL for the human-supplied STAMP duplication-check fragment is still not established. Further native/source-owner/independent comparison remains open.

Consumer compatibility:the original mathematical/calendar/event fixtures retain their laws; this document consumes their actual limited results. The new SQLite profile is separately declared. Any native adapter must preserve source claims/results, current grant and effect meanings and return through the existing M13/M17/C02 owners before stronger claims.

## 12. Proposed incorporation and next concrete work — pending

Internal authoring/analytical work is authorized. Public/canonical source changes remain proposed and follow the existing owner reviews; no new active queue is opened.

**FCD-DELTA-001 — study entry through the owning technical index review.**
Before: no entry for this fourth local study at the proposed corpus route.
After, proposed addition only: “Fencing tokens and confused-deputy prevention — an analytical HEW actuation/delegation study; 20 declared cases and bounded event/race constructions; no native technology campaign or demonstrated superiority.” Exact public placement/anchor requires the owning README VNext and three-level reader-map review. Do not invent a public file URL.

**FCD-DELTA-002 — HEW action-boundary requirement for the owning profile review.**
Before: preserve existing intervention/decision/application paragraphs and their results.
After, proposed additional paragraph: “For a realization with transferable execution ownership, qualify the effect boundary separately from approval. Declare the resource's ownership-generation enforcement and handover completion point, and the principal/deputy/resource/action delegation policy. A current generation or authenticated service identity is not itself the principal's action grant. These controls do not establish sufficient human review, available capacity or protected-channel conformance.” Source anchor and consumers must be checked before any application.

**Next autonomous research:** strengthen source-clause/compatibility matrices and analyze explicit visibility/consistency laws or command sequencing without changing old results. Before native work, select the actual deployment/implementation, legitimate policy/issuer, effect resources and durability boundary; register the run and compare the strongest applicable conventional policy. Before a commissioned DDS finding, also fix business objective, useful timing, cost/value and factual review. Full native/runtime and human results remain open.
