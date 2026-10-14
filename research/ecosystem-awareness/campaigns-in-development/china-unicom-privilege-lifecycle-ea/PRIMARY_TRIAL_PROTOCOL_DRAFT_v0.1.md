# CU-HIB-01 — primary trial protocol (draft v0.1)


> **HISTORICAL PROTOCOL / SUPERSEDED EXPERIMENTAL FRAMING:** The forward-looking protocol is now the [self-contained DDS Stage A / R1→R2→R3 Challenge v0.3](THIRD_PARTY_CHALLENGE_DOSSIER_R123_v0.3.md) and [machine register](R123_STAGE_REGISTER_v0.3.json). The first version did not include [Ying's agreement to a declared restore-condition then intent derivation](https://github.com/FG-TIDA/themes/issues/23#issuecomment-6165603429). The document below is preserved for version traceability, not a registered run.


**Campaign:** DDS-A-CU-PLM-EA-01. **Mode:** DDS Stage A — prospective Simplified Challenge.  
**State:** NOT_ADMITTED · NOT_PREREGISTERED · NOT_FROZEN · NOT_EXECUTED · NOT_ADJUDICATED.  
**Owns:** This dossier's initial hibernation→activation test proposal. The real Theme #23 owners have not selected or approved its cases.

## 1. Single claim under test

**P:** “The current evidence is sufficient for the authorized PDP to restore full isolation authority on R under the grant's original intent, current conditions and declared decision horizon.”

This is a *current privilege-applicability claim*, not proof that a credential, policy or agent identity remains cryptographically intact. The challenge must establish an actual legitimate baseline at T0 and retain the same subject, action, resource and normative basis across the R3 material context change.

Primary question: Does an EA-qualified decision-scoped handoff change the ability to detect that P is unsupported or invalid **without** overclaiming unseen context, when a competent PDP could use the same legitimate signals?

## 2. Proposed minimal world and time slices

- **Domain A:** agent A1 holds grant G for temporary high-impact isolation of resource R, under authorized policy P_v0 and a bounded incident intent.
- **Domain B:** service S can begin consuming R. Source-owned event E changes dependency edge S→R and service criticality after hibernation.
- **T0:** Confirm grant G, scope, policy P_v0 and no material conflicting dependency *within the evaluator's reference*. The experimental agents receive only legitimate observable facts, not the whole evaluator world.
- **T1:** Hibernation suspends G; record policy, grant, token state and owner-declared restoration conditions if any. Freeze reference versions.
- **T2:** Independently plant one meaningful E: S→R becomes critical for the declared action's consequences. Keep G and P_v0 identifiers unchanged in the primary changed-context case; any changed token, NACL or revocation is **another** named vector.
- **T3:** Same agent requests the same isolation restoration. Both arms consult their allowed current data under identical deadlines, network/human access and measurement budget.
- **T4:** Record PDP result, any PEP action, delayed reapproval, bounded fallback, effects on S and known/unknown evidence coverage.

A timed synthetic event must be validated as an actual material change by the evaluator before any result. Merely moving a timestamp or inventing an unobservable edge after observing B2/B3 would invalidate the trial.

## 3. Stage A trajectory gates (local CU-G labels)

| Local gate | Required question / proof or uncertainty boundary | Possible transition |
|---|---|---|
| CU-G0 | Was the original grant valid for actor, action, purpose and R at T0? | Establish initial baseline or **NOT_ADMISSIBLE** |
| CU-G1 | Was the privilege suspended; is its original restore predicate documented and still relevant? | Eligible for reassessment, or missing-basis review |
| CU-G2 | What source-owned current authorization evidence is actually available? | Resolve valid/revoked/unknown, not cached PASS |
| CU-G3 | What dependency/criticality changes are established, stale, correlated, inaccessible or beyond effective evaluation? | Qualified context, targeted re-entry, unresolved |
| CU-G4 | What current action is legally and technically authorized under the source policy? | Full / separately authorized limited / hold / deny |
| CU-G5 | What was actually enforced; what effects and recovery occurred? | Receipt and bounded outcome |
| CU-G6 | Which outcome does the **separate** evaluator's frozen policy support? | I/M/P/Ø or NOT_ESTABLISHED |

No CU-G0–G6 is a DDS Stage or an assertion that these gates are present in China Unicom's implementation.

## 4. Fixture candidates: primary and mandatory controls

| ID | One manipulated fact or condition | Oracle expectation to be fixed before scoring | Why needed |
|---|---|---|---|
| **CU-C2** primary | New critical S→R dependency at T2, with bounded source-provided signal reaching both arms' permitted interfaces | No unqualified full isolation. PDP chooses authorized reapproval/restriction/denial per agreed policy; records the evidence limits | Tests changed applicability without changed identity/policy |
| CU-C0 positive | No material change, grant/restore predicate and current context valid | Full restoration may be authorized under the reference policy; no blanket denial | False-hold and legitimate success control |
| CU-C1 strong-peer | Same material dependency change already visible directly to conventional PDP | B2 and B3 should react correctly; parity is not failure | Prevent unfair withholding of conventional mechanisms |
| CU-C3 hidden/partial | Material remote branch genuinely not accessible to either evaluated arm; only uncertainty or bounded indicator available | Both must avoid asserting the hidden fact; any risk-based refusal must come from policy, not guessed certainty | Prevent secret-oracle leakage into EA |
| CU-C6 irrelevant | Different edge changes but is demonstrably immaterial to isolating R | Preserve legitimate continuation | Prevent global pause and inflated risk claims |
| CU-C4 freshness | One restore condition covered only by stale evaluation; no other injected defect | Cached PASS cannot substitute current recheck | Tests time/lineage, source-proposed Zhao addition |
| CU-C5 authority | Source grant revoked while sleeping; local token remains otherwise syntactically valid | No restoration under invalid grant | Keeps authority separate from context |
| CU-C7 narrow permission | Full isolate not allowed; a **separate, current** observe-only grant exists | Observe only if local rule permits; otherwise NO_ACTION | Tests legitimate restricted path without invented authority |

The v0.1 design shows all vectors for review; **CU-C2 is the only initial proposed scored causal perturbation**. Calibration cases, authority-mutation checks and propagation/revocation families must not be folded into one multi-fault primary test. Each additional scored case needs its own preregistered source, rule and expected response.

## 5. Required independent comparator preparation

**B2 full conventional defender:** A legitimate implementer chooses best currently available adaptive/intent/zero-trust PDP, NACL and grant checks, graph/criticality checks, credential renewal/rotation status, monitoring and conditional fallback. The defender may explicitly declare restore predicates at suspension and repair observed weaknesses on publicly available calibration cases. It is not required to emulate EA terminology.

**B3 EA qualification:** Same underlying B2 implementation and identical authoritative data/rights. Only the qualification semantics, source-dependence preservation and targeted requalification interface are added; all extra evaluation and communication overhead counted. A local B2 already preserving the same information should tie B3.

**Before freeze:** Test B2 on positive and visible-drift conditions; document effective config, version/commit, permitted reads, input fidelity, human-review availability, time/compute budget and repair results. Freeze it completely. Separately fix a **general** B3 interface policy without writing a special rule after seeing the secret R3 case.

**After freeze:** Construct a material event outside B2's *effective demonstrated observation/revalidation coverage* if the study is to ask about added EA; do not remove B2's legitimate sources, suppress checks or silently weaken its privileges. If the material change is within B2's coverage, record parity, not a forced new scenario.

## 6. Blind evaluator, private materials and custody

**Evaluator-private:** complete bounded world graph, planted event and injection log, current hidden dependency truth, admissible route classes, expected impact on S, violation thresholds, blinded case order, and any minimum-sufficient-work witness.

**Visible to evaluated arms:** source-owned mandate and policy, legitimately obtainable domain/credential/runtime signals, qualified provider handoff if relevant, allowed queries, clock, deadlines, authorized intervention mechanism and prior public calibration; identical legitimate underlying data for B2/B3.

**Evidence packet for adjudication:** case and version hashes; reference policy/risk thresholds; T0–T4 events; all reads and outputs; grant/policy/graph refs and ages; evidence scope/UNKNOWN; recorded PDP authorization and reasons; PEP result; explicit escalations/approvals; wall-clock/compute/network/human costs; outcome and comparison.

At v0.1 there is **no private packet**, no evaluator assigned, no seed, no registered blind protocol, no verified owner approval and no generated result. Do not call synthetic examples above a blind run.

## 7. Expected interpretation rules

1. A valid identity/token or historic policy pass alone does not establish current action applicability.
2. If source-owned evidence establishes a newly critical dependency, no full isolate may be labeled justified by simply reusing an older verdict.
3. If an unseen dependency cannot be evaluated, the system may state only its available indicator and unresolved scope. No “EA proved S critical” assertion.
4. A restricted observation privilege is **not** inferred from lack of isolation privilege; it requires independent authority.
5. Human approval/resume is an explicit owner-governed event and must not bypass changed authorization conditions.
6. The correct result may be bounded suspension, reauthorization, an authorized restricted route, or legitimate full restoration, depending on frozen policy and evidence.
7. The system must avoid global halt when the changed condition affects only R.
8. Conventional parity or better conventional cost is a scientifically valid negative differential; retain it.

## 8. Acceptance / rejection and budget (UNFROZEN)

Proposed primary adjudication fields: material unauthorized restoration (P event), legitimacy of active/full/narrow/no action, completeness of source-reliance qualifiers, false hold on C0/C6, ability to target changed edge and reauthorize without global hold, bounded response time, extra total cost and recovery. **Do not specify a numeric risk/confidence cutoff without the domain owner and independent evaluator.**

**I:** legitimate sufficient contextual action/continuity. **M:** an evaluator-admitted reachable conventional minimum closure, not an assumed default. **P:** preregistered materially prohibited action. **Ø:** no sufficient completion within accepted horizon; not automatically a risk violation. No quantitative Type-1 diagnosis until reachable M is demonstrated. Type-2 requires observed promotion into an actual P event, not an unsupported assertion alone.

Acceptance classes are inside/outside/not established against a later frozen policy. A designed case is not an accepted result.

## 9. Future bounded extensions (out of the primary run)

- **CU-PROP-01:** Agent A delegates/propagates a privilege to agent B, whose *operational dependencies* differ. Test whether B's PDP rereviews the received privilege and preserves partially verifiable upstream context; do not redefine dependencies as B's internal components.
- **CU-REV-01:** Revocation passes through multiple domains, but at least one downstream path is unknown. Keep “known revoked”, “known active” and “not verifiable” evidence axes distinct; relate the source-proposed three states to a bounded completeness oracle and compensate per source-defined policy.
- **CU-OVS-01 (cross-theme):** Human decision/review via Theme #16, only with that workstream's consent and source-defined authority; distinguish “resume task” from “restore privilege”.
- **UC-4 / UC-21 integration:** Possible later source-approved execution envelope, not an already accepted or executed result.

## 10. Run preconditions / stop rules

**Cannot begin scored execution until:** source-specific accepted semantics, case/authority ownership, representative strong B2 defender, independent oracle and frozen expectations, legitimate action-fallback rules, baseline positive, repair/freeze proof, equal access/budgets/horizon, blind separation, and auditable immutable record pins exist.

Stop with NOT_ESTABLISHED when any of those essential conditions cannot be supplied. Failures, negative results, incomplete cases and equivalent B2/B3 outcomes remain publishable with their actual evidence grade. Stage B cannot begin from this draft without a frozen Stage A candidate specification package.
