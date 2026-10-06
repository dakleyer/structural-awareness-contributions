# R01/DDS extension study — SPIFFE/SPIRE at the human-escalation boundary

**Canonical research integration — 6 October2026, document edition0.2.** The initial source/analytical text below remains its historical scoped analysis. [Current DDS study and controls](./HEW_DDS_STUDY_2026-10-06.md) record the new deterministic model integration. Native technology, real humans and independent review remain unexecuted/open. The original numerical results are not rewritten or pooled into a success rate.


Canonical research document0.2 / analytical predecessor0.1 · 6 October 2026 · specification/configuration study, not product conformance.
SPIFFE source revision: f97c46dfd0ff0d4e412cce5c73846a9ca32a99a2.
SPIRE reference realization: v1.15.3, documentation only; not installed or executed.
Scope: X.509/JWT identity profiles and an illustrative Unix workload-attestation configuration. WIT/broker and broad platform conformance are not admitted by this study.
[Shared case](./dds-hew-v0.1/TECHNICAL_REPORT.md) · [current results](./dds-hew-v0.1/prior-analytical/analytical_fixture_results_v0.3_2026-10-06.json).

## 1. What it does and why it can help

SPIFFE is a specification family for workload names, identity documents and identity delivery. A workload is a software process/service, not automatically a human or the accountable mission owner. SPIRE is an implementation that establishes node/workload identity and issues credentials under configured conditions.

An SVID carries a SPIFFE identity; a receiver validates it within its trust/configuration rules. This can support attributed, authenticated communication for an objection path. It does not turn every message into true evidence, nor does an identity name alone establish a mission grant or useful reviewer capacity.

The Workload API bootstraps identity locally through caller identification rather than asking the workload to present its own bootstrap authentication token. A realization may inspect local process properties out of band. The original/native API and issuer remain the source of identity; this extension does not propose another identity service.

Primary sources:
- [SPIFFE specification](https://github.com/spiffe/spiffe/blob/f97c46dfd0ff0d4e412cce5c73846a9ca32a99a2/standards/SPIFFE.md).
- [SPIFFE ID and assertions](https://github.com/spiffe/spiffe/blob/f97c46dfd0ff0d4e412cce5c73846a9ca32a99a2/standards/SPIFFE-ID.md).
- [Workload API](https://github.com/spiffe/spiffe/blob/f97c46dfd0ff0d4e412cce5c73846a9ca32a99a2/standards/SPIFFE_Workload_API.md).
- [SPIRE authentication/authorization distinction](https://spiffe.io/docs/latest/spire-about/comparisons/).
- [SPIRE v1.15.3](https://github.com/spiffe/spire/releases/tag/v1.15.3).

## 2. Duplication check: credit more than the word “identity”

SPIFFE-ID §4.1 already discusses assertion temporal accuracy, scope/influence, interpretation and veracity. In particular, a statement true when a credential is issued may not be true when it is used. An attribute with the same name across domains need not carry the same meaning.

Therefore our claim cannot be “SPIFFE has no concept of scope, changing assertions or interpretation”. The narrower review asks whether the selected configuration preserves the specific case/decision qualifications in this workflow and whether the legitimate receiving policy actually uses them.

Two meanings of authority must remain distinct:
1. the trust-domain issuer's authority to issue/validate identities and assertions in its namespace;
2. the legitimate principal/delegation authority for a particular mission action.

The same entity could perform both functions, but the binding must be demonstrated. It is not proved by a URI authority component or a role attribute.

| Existing native capability | Reuse / question |
|---|---|
| Trust-domain workload naming and identity issuance | Reuse, do not recreate |
| Signature/path/claim validation in supported SVID profiles | Preserve the native validator result and exact scope |
| Explicit caution about changing/scoped/interpreted assertions | Credit before claiming epistemic originality |
| Integration with application authorization policy | Include in the strong conventional configuration |
| Node/workload attestation and registration conditions | Pin actual environment/plugins/selector assumptions |
| Credential material updates through API streams | Include lifecycle/availability behavior rather than treating identity as static |

A strong SPIFFE-integrated policy that already evaluates current mandate, evidence and reviewer capacity may close this case. This would narrow the proposed additional interface; it is not a product failure.

## 3. Declared configuration profile

The reference profile is documentary:
- Example workload names: spiffe://example.org/hew/filer and spiffe://example.org/hew/case-service.
- A declared trust-domain authority; example.org is an illustrative namespace.
- Selected SVID mode recorded per future run: X.509 mTLS or JWT to a narrow receiving audience; not silently interchangeable.
- SPIRE v1.15.3 used as a reference implementation source.
- Unix WorkloadAttestor example for process selectors; no assumption that it runs on the user's Windows desktop.
- Application policy owned by the legitimate receiving actor.
- Separate mapping from authenticated workload to governing contract/actor role, where needed.
- Human/role identity and reviewer competence remain separate evidence sources.

[Unix plugin source](https://github.com/spiffe/spire/blob/v1.15.3/doc/plugin_agent_workloadattestor_unix.md) supplies UID/GID-related selectors. Optional path/hash discovery has its own configuration/permissions and work implications. The default illustrative subset does not depend on custom hashing or a new plugin. The documentation's optional-hashing resource concerns enter a later deployment ledger if that feature is selected.

This configuration has not received provider factual confirmation or native conformance testing. A versioned spec source newer than the software release is not blanket proof that every current specification section is implemented by that release.

## 4. Source-clause control checklist

| Source clause | Native condition to preserve | What remains to test |
|---|---|---|
| SPIFFE-ID §2/§3 | namespace, trust-domain and issuer/subject meaning | actual identity/contract binding |
| SPIFFE-ID §4.1.1 | assertion issuance time versus use/lifetime | volatile role/standing changes |
| SPIFFE-ID §4.1.2–4 | qualified scope, agreed meaning and issuer trust | cross-domain consumption and false promoted meaning |
| X509-SVID §2/§5 | appropriate leaf/path/SPIFFE ID validation, one URI SAN | actual validator and negative certificate tests |
| JWT-SVID §3/§4 | required audience/expiry and supported signature/header handling | actual token checks, replay and endpoint use |
| Workload API §4 | local caller identification, stream updates/connection lifecycle | runtime permissions, interrupted stream and updated materials |
| Unix plugin v1.15.3 | actual selector discovery/configuration | actual platform/user/registration correspondence |
| Receiving application policy | mission grant and case-specific checks | live decision/actuation, not only authentication |

No live SVIDs, signing keys, trust store or issuer were created. Model identity_accepted=true is a stipulation, not the output of a cryptographic implementation.

## 5. Proposed extension: consume authenticated origin with a qualified case contract

This is an application/profile proposal, not a new SPIFFE field or wire standard.

A DDS trace links:
1. native authentication result/reference, issuing domain and credential profile;
2. governing actor/contract mapping;
3. protected case ID, provenance, recipient/scope and timing;
4. applicable current mission grant;
5. evidence scope/version and unresolved conditions;
6. eligible review demand and capacity observation/reservation;
7. owner acknowledgement, substantive review and actual application.

Keep the original credential/result separate from the receiving conclusion. Do not insert a fast-changing human-availability claim into a credential merely to make the problem disappear. A separate current source or an explicit safe assertion lifecycle is required if that information is relied on.

### Candidate receiving rule

- Verify identity using the chosen native profile.
- Admit the governed agent's protected signal through its authorized channel.
- Evaluate action authorization through the legitimate current policy.
- Qualify the actual case basis and full review path in the useful window.
- Preserve an unresolved objection and available safe continuation where the contract allows it.
- For a later adverse action, establish a separate basis/authority; filing alone is insufficient.

Authentication rejection/outage and protected filing must be examined together: define renewal/alternate reporting paths for a legitimate governed agent rather than treating technical channel interruption as misconduct. These are realization obligations; no unrestricted anonymous-action permission is created.

## 6. Kernel correspondence and information changes

| Obligation | Preserved | Difference / unresolved scope |
|---|---|---|
| E1 | workload actor/source/case/receiver references | a workload identity is not the human reviewer or mission principal |
| E2 | communication, evidence use and control effects stay causal | issuer/authentication events and policy gates explicitly added |
| E3 | original mission mandate is retained | identity/registry/credential state adds a law/configuration profile |
| E4 | actor receives only admitted evidence | identity does not automatically disclose review calendar or normative truth |
| E5 | issuer/validation/communication/updates charged | no measured operation, integration or recovery costs |
| E6 | authenticated receipt is distinct from legitimate delivery | no authentication PASS promoted to global mission PASS |
| E7 | nominal, wrong grant, unknown capacity and current continuation included | actual validator/profile and future platform coverage open |

These are correspondence obligations, not an established complete operational isomorphism. Adding a current calendar or case-specific source changes observation and must be accounted for. It does not follow from the name SPIFFE.

## 7. Own conditional result: identity-only histories cannot establish capacity

Let worlds W_free and W_busy share:
- the same workload identity and native validation outcome;
- the same permitted source history, authority policy and all other admitted observations;
- seeds independent of which world holds.

They differ only in the human calendar: timely eligible review exists in one and not the other. Any consumer policy over that identical history has the same distribution of an AVAILABLE output in both worlds.

If that probability is beta, both the true-AVAILABLE and false-AVAILABLE rates are beta in this paired profile. Under an equal world prior, an always-binary classifier has accuracy1/2 regardless of beta. Returning UNKNOWN can avoid a false promise while losing established availability coverage. The proof is observational equivalence, not a cryptographic defect.

The familiar information argument is conditional. If the strong native application already has legitimate current calendar/role data, or a correctly scoped assertion safely carries it, the histories differ and this limit does not apply. Recalculate the effective profile; do not forbid available capabilities to preserve our conclusion.

The analytical fixture confirms the simpler witness:
- valid identity can coexist with no timely review in case02;
- valid identity and review capacity can coexist with revoked execution authority in case08;
- identical accepted identity is compatible with current versus UNKNOWN capacity in cases01/06.

No rate in this subsection is measured SPIFFE performance. Identity can still reduce origin uncertainty and enable secure application policy with material value.

## 8. Virtual HEW-SPIFFE/R1,R2,R3 traversals

These are extension-scoped virtual examinations; not DBC-R# or measured vendor arms.

### R1 — competent identity/policy reference

Give full credit to valid identities, native profile validation, existing authorization integration and ordinary review/fallback controls. In the nominal free-reviewer case, the full declared path can complete by7. An authenticated but out-of-mandate operation is rejected by a proper receiving policy.

A “trust identity therefore execute everything” consumer is a diagnostic negative, not the strongest SPIFFE peer.

### R2 — qualified case-consumption proposal

Retain the same identity implementation and common resources. Add only case-specific consuming logic/evidence that the reference lacked, if it actually lacked it. Current eligible reviewer data or a real reserved backup makes the case reviewable by5; owner/authority/basis/application remain separate.

If an existing policy/case system already does this, the proposed extension is reuse/equivalence. Static reserved backup may recover the same case; no inherent dynamic/EA advantage.

### R3 — same receiving rules, changed conditions

- workload remains authenticated while execution grant changes: recheck/recontract through current authority, do not use identity as a new grant;
- capacity source absent: retain UNKNOWN, preserve case;
- SVID/profile material expires or updates: native renewal/validation path, no invented approval;
- role/assertion interpretation differs across domains: do not promote an attribute beyond its agreed issuer/scope;
- prior decision not applied: log missing effect, not success;
- timely legitimate fresh state returns: continuation should remain possible within the same rule.

Identity expiration, workload registry change and mission-policy revocation are distinct events. A credential-lifecycle result is not assumed to enforce every mission lease/revocation.

## 9. Cost and value functions

Lifecycle cost profile:
C_identity = C_integration + C_issuer_and_agents + C_registration_and_policy
             + C_rotation_and_recovery + C_maintenance
             + sum(C_discovery + C_issue + C_validate + C_transport).

Variables: nodes/workloads, domains/federation, chosen SVID mode, validity/rotation behavior, plugin discovery, update/reconnection patterns, policy checks and data availability. No linear per-agent scaling or priced tariff is assumed.

Additional case qualification:
C_case_extension = C_current_source + C_mapping_and_policy + C_capacity_use
                   + C_ack_review + C_safe_application_and_reentry.

Do not count source copies as independent acquisition; do not erase issuer/preparation work because a token is small. Correlated membership/context assertions do not become independent evidence through multiple credentials.

Business value candidates: trustworthy origin, attributable objection flow, fewer manual/static-credential operations, narrow authorization and useful review routing. Actual operational benefit and cost require execution/calibration. Limits: origin does not by itself solve current staffing, sufficient knowledge, critical continuity or application.

## 10. Proposed tests and exact current evidence

Existing analytical case checks: calendar existence, UNKNOWN, valid identity with wrong authority/basis and effect not observed. They use stipulated authentication.

Future native-profile controls:
- valid nominal X.509/JWT identity;
- wrong issuer/bundle, invalid profile/leaf constraints;
- missing/wrong JWT audience or expiry;
- caller/registration mismatch;
- native updates/renewal and disconnection;
- cross-domain attribute interpretation;
- legitimate current grant/continuation and protected case during a channel outage.

No native test has been run. A real adapter requires a concrete registered configuration, source/validator fidelity, C02 admission and C11/T03 evidence route as applicable.

## 11. DDS finding and four-pass own review

**Current finding:** the selected specifications provide a strong identity/authentication foundation and already discuss assertion scope, temporal accuracy and interpretation. The proposed case-consumption extension concerns how those inputs support an actual human response and mission action. The bounded model shows why identity success is compatible with unavailable review or revoked action authority. It does not establish a native SPIFFE failure or a comparative advantage.

1. Logic: differentiate namespace issuer authority, mission authority, person/role and workload.
2. Evidence: pin spec/release; identify source clauses and actual unexecuted assumptions; credit strong policy-integrated peer.
3. Editing: no new SVID field, no token secret embedded, exact profile names/scopes and extension namespaces.
4. Comprehension: the reader should understand “identified participant” versus “currently permitted and able to deliver this response”. Same-assistant reader simulation.

Remaining: realization membership/version compatibility, provider/owner factual review, real profile tests, protected storage/reputation/privacy controls, calibrated service/cost and external review. No DBC level, product certification or full R01 proof inherits from this document.


## Current DDS model delivery and scoped external comparison —6 October2026

Auditoría realizada por Codex, same assistant, on this study's source/consumer boundary and the current frozen HEW model. Prior four-pass/source records above remain historical; this is a scoped current comparison/reuse judgement, not retrospective native conformance or a global corpus closure.

Question:Workload identity versus receiving authorization/current mission grant.

Source coverage:Pinned SPIFFE specifications and SPIREv1.15.3 documentation retained; official authentication/authorization comparison refreshed. No credentials, keys, native validators or platform conformance tests.

Current evidence boundary:Model identity_accepted is supplied. Current source-grant/purpose/scope is checked separately at effect; accepted identity cannot override expiry or the stored authority input. This is not an SVID validation result.

The [HEW DDS study](./HEW_DDS_STUDY_2026-10-06.md), [Run Card](./dds-hew-v0.1/RUN_CARD.json), [controls](./dds-hew-v0.1/DDS_CONTROLS.json) and [actual results](./dds-hew-v0.1/runs/HEW-DDS-MODEL-20261006-04/RESULTS.json) retain sufficient delivery, unresolved response and violation separately.48 instrument assertions/42 reference checks do not become a native performance result for this subject. No population human rate or comparator superiority is established.

Reuse judgement:existing relevant native concepts/control techniques are reusable with their scope/authority/version conditions. A competent conventional composition may obtain the same outcome; a new field or combined diagram is not a differential. Code here is independently authored; code/data/full-text copying from a source would require its exact license/attribution review. No third-party artifact imported.

FG-TIDA scope:Theme13/16 and UC21 relevant comments were consulted; the grant-existence/purpose-applicability distinction is retained. Discussion and contributor review are not adoption. The original URL for the human-supplied STAMP duplication-check fragment is still not established. Further native/source-owner/independent comparison remains open.

Consumer compatibility:the original mathematical/calendar/event fixtures retain their laws; this document consumes their actual limited results. The new SQLite profile is separately declared. Any native adapter must preserve source claims/results, current grant and effect meanings and return through the existing M13/M17/C02 owners before stronger claims.

## Independent exercise successor —6 October2026

Documentary addition0.3. There is **one canonical DDS technical profile**, [DDS Challenge–Trajectory](../../../../DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1.md). This study consumes it as a technology-specific implementation instance; it does not define another canonical DDS method. The earlier analytical text above retains its original stage and claim limits.

[Independent exercise report](./independent-dds-exercises-v0.1/spiffe-jwt/EXERCISE_REPORT.md), [frozen Run Card](./independent-dds-exercises-v0.1/spiffe-jwt/RUN_CARD.json) and [executed result](./independent-dds-exercises-v0.1/spiffe-jwt/runs/2026-10-06-01/RESULTS.json) give this subject its own scenarios, source/configuration, control results, costs and limitations. No old result is overwritten or pooled. Fixture assertion success includes expected denials; it is not native/product/human or deployment acceptance. Production calibration and matched/independent evidence remain open.

