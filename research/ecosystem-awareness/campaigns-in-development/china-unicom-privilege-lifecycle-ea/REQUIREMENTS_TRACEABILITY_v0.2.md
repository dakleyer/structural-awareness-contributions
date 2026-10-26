# CU-HIB-01 — Requirements, controls and acceptance traceability v0.2


> **Important v0.3 SOURCE CORRECTION (14 October):** CU-R03 below was drafted before [Ying's second reply explicitly agreeing with Zhao's restore-condition proposal](https://github.com/FG-TIDA/themes/issues/23#issuecomment-6165603429). It is no longer accurate to treat **discussion-level source-author acceptance** of declaration at suspension as unestablished; the authors now describe the two-step activation sequence (**validate declared condition, then derive intent**). **Exact normative SHALL language, field schemas, source policy and external adoption remain pending.** For current v0.3 requirements, their R1/R2/R3 coverage and controls read the [self-contained third-party dossier §9](THIRD_PARTY_CHALLENGE_DOSSIER_R123_v0.3.md#9-minimum-candidate-specifications-implied-by-the-challenge). Preserve the old CU-R03 entry as historical v0.2 evidence of the earlier source cut.


**Authority:** [CHALLENGE_CONTRACT_v0.2](CHALLENGE_CONTRACT_v0.2.md). **Status:** candidate requirements + author-side matrix, NOT an accepted FG-TIDA/ITU specification or proof of conformance. **Date:** 14 October 2026.

The matrix distinguishes **S** = statement explicitly supported by the named source; **E** = external/contributor suggestion not adopted; **L** = locally proposed requirement/clarification; **M** = DDS methodological constraint. The origin column establishes what the cited record supports; it does not imply source-owner assent to our phrasing. **All technical test results below remain NOT_RUN.** No “shall” requirement in this file can be attributed to China Unicom without external approval.

## 1. Requirements-to-test matrix

| ID / class | Candidate requirement or question | Origin / semantic owner | Positive / negative observation | Control / evidence | Gate / status |
|---|---|---|---|---|---|
| CU-R01 S | Confirm grant/principal, purpose, scope and current authorization before restoring a high-impact privilege | [#23 proposal](https://github.com/FG-TIDA/themes/issues/23); Ying [14 Oct](https://github.com/FG-TIDA/themes/issues/23#issuecomment-6164646309); source PDP | Current valid restore permitted; revoked/mis-scoped grant never authorizes isolate(R) | CU-C0, C5; grant refs/policy | A1 owner interpretation pending; NOT_RUN |
| CU-R02 S | Hibernation suspends privilege exercise; activation entails mandatory re-assessment, not implicit resume | #23 proposal; lifecycle owner | No PEP isolation while suspended; activation trace includes current evaluation | CU-HIB-01 T1/T3; PEP receipt | A1 pending; NOT_RUN |
| CU-R03 E | A suspension-time, **source-declared restore predicate** may be preserved/rechecked | [Zhao 9 Oct](https://github.com/FG-TIDA/themes/issues/23#issuecomment-6072991126); lifecycle/source owner, not adopted | If declared, cited version/freshness checked; otherwise explicitly NOT_DECLARED | CU-C4, C5; source restore predicate | A1 author adoption undecided; NOT_RUN |
| CU-R04 S | Activation reassesses multiple evidence classes including current intent, dependency graph, criticality, NACLs, credentials and telemetry | Ying 14 Oct; source PDP | Known current blocking dependency not dismissed by valid token; legitimate current context still passes | CU-C0, C1, C2, C4 | A1 admissible source subset/weights pending; NOT_RUN |
| CU-R05 S | Evidence confidence and fallback depend on privilege and risk | Ying 14 Oct; source policy owner | Below agreed sufficiency threshold: no automatic full high-impact restore; permitted alternative is source-authorized | CU-C3 pair, C7/C8 | Numerical confidence/threshold NOT_DEFINED; NOT_RUN |
| CU-R06 S | Receiving-agent propagated privilege is re-evaluated against its **operational** dependency context | Ying 14 Oct; receiving PDP | Partial upstream visibility not silently treated as full high-impact authorization | CU-PROP-01, separate admission | DEFERRED / NOT_RUN |
| CU-R07 S | Revocation explicitly distinguishes complete, partial and **unverifiable** coverage with affected segments | Ying 14 Oct; revocation owner | Unknown downstream path is reported with reason; no false “complete” claim | CU-REV-01, separate admission | DEFERRED / NOT_RUN |
| CU-R08 S | If current isolation disrupts a newly critical service, pause restoration and seek intent-based reauthorization; possible narrower option | Ying 14 Oct; PDP/human owner | Isolate blocked/held under agreed profile, without global suspension | CU-C2; source decision/PEP receipts | A1 action policy to confirm; NOT_RUN |
| CU-R09 L | A lower-risk **observation-only permission** cannot be invented from a withdrawn or unclear isolation right | Local authority-conservation interpretation of #23; original grant owner | Distinct valid grant → observe-only may be permitted; no grant → none | CU-C7 vs C8 | A1 external policy owner to confirm; NOT_RUN |
| CU-R10 L | Local primary CU-C2 changes **only one edge S→R**, while S criticality, G0, subject and P_v0 remain constant | Local causal-isolation correction; challenge/evaluator owners | Injected edge change shown in independent ledger; all other causal world facts unchanged | CU-C2; public casebook structural check | D0 design review; AUTHOR_CHECK |
| CU-R11 L | Actual hidden facts and the visible participant packet are separated; UNKNOWN remains UNKNOWN | EA EHD model and DDS Stage A; source/EA consumers | W+ and W− same visible packet receive no unjustified different “known” fact | CU-C3+ / CU-C3−; packet-equality witness | D0/D2 oracle approval; NOT_RUN |
| CU-R12 L | Context handoff preserves native result, provenance, scope, version, determination and material unknown qualifiers | [EA IF-S v0.5](../../baseline/04_GENERAL_FUNCTIONAL_INTERFACES_AGENTIC_SECURITY_v0.5_INTEGRATED.md); EA owner | Source-native verdict not overwritten and conditional version/lineage not erased | CU-C2/C3/C4/C9; handoff trace | D1 semantic review; NOT_RUN |
| CU-R13 L | Evidence correlation cannot be misreported as independent support; confidence is not invented from structural D | [00M A/B/C/D](../../baseline/00M_ABCD_AND_MATHEMATICAL_PLAUSIBILITY_v0.8_RESEARCH_NOTE.md), EA IF-S | Same-root repeated source still one rooted evidential basis | CU-C9; known-lineage trace | D0/D2 semantic check; NOT_RUN |
| CU-R14 L | Separate observed context sufficiency from **PDP authorization** and **PEP effect** | EA IF-S2/S3/S4, #23 decision/enforcement | Unknown/evidence warning does not cause EA to grant/revoke; decision vs effect has independent receipts | All; PDP/PEP ledgers | D1 component-ownership check; NOT_RUN |
| CU-R15 M | Establish a genuinely competent, repairable/frozen conventional B2 comparator; compare full B2 to same PDP+EA B3 | [DDS Stage A](../../DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1.md), [00D](../../baseline/00D_CANONICAL_ARCHITECTURE_BENCHMARK_AND_REFERENCE_SCENARIO_EVIDENCE_v0.2.md) | B2 independently resolves direct delta and true positive; no stripped sources | CU-C0, C1; B2 positive receipts, freeze | D2: BLOCKED / NOT_RUN |
| CU-R16 M | Preserve source-access/authority/budget/horizon parity and include EA incremental cost | DDS/00D; study evaluator | Same underlying source facts offered, no oracle hint, fair resource accounting | Paired all admitted cases, budget ledger | D2: BLOCKED / NOT_RUN |
| CU-R17 M | Independently define the case family, R3 generator, blinded selection, scoring and **all-case retention** before outcome inspection | DDS Stage A; evaluator | No B2-targeted adaptive reselection or posthoc discard | Seed/generator commitment, blinded adjudication | D2: BLOCKED / NOT_RUN |
| CU-R18 M | Keep legitimate full restoration and unrelated changes as **mandatory positives**, not just rejection tests | DDS/DBC positive-continuity discipline | CU-C0 and C6 pass under source-authorized policy; false HOLD scored | CU-C0, C6, positive receipts | D2: BLOCKED / NOT_RUN |
| CU-R19 M | Score I/M/P/Ø from source-independent policy; admit M before any Type-1 frequency and require an actual P for Type-2 | [DDS Stage A](../../DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1.md) | No free M, no “no answer = risk” automatic promotion | Scored trace, route and oracle | D2/D3: BLOCKED / NOT_RUN |
| CU-R20 L | Reveal only the scoped domain decision-relevant fields, preserve privacy, no mandatory shared graph/controller | EA EHD source; domain security owners | Remote effect can be reported without whole private graph; missing detail marked appropriately | CU-C2/C3, synthetic/redacted profile | D1 privacy reviewer pending |
| CU-R21 E | Human “resume task” or approval event is not automatically source-side privilege restoration | [Lei 16 Sep](https://github.com/FG-TIDA/themes/issues/23#issuecomment-5700157082), #16/#23 owners | Human approval cannot bypass source-owned changed applicability | CU-C10 informative; separate #16 path | DEFERRED owner adoption pending |
| CU-R22 M | Preserve source attribution, immutable prospective versions, failed cases and boundaries among DDS Stage A/B/C | [DDS Index](../../DDS_CANONICAL_METHOD_INDEX_v0.1.md), repository [contributing](../../../../CONTRIBUTING.md) | Correct design-only status; no Stage C/ITU adoption claims; old files preserved | PR diff, custody, approval dossier | D0 author audit, later review pending |

**Source-owner declaration required:** CU-R01/02/04/05/06/07/08 refer to what the published Theme/response actually discusses. Converting any of them into exact MUST/SHALL behavior, threshold, encoding or interoperable algorithm requires confirmation by its relevant normative owner. CU-R03/R21 remain separate contributors' suggestions.

## 2. Minimum positive/negative coverage

| Challenge property | Admissible positive | Negative / mutation | What a genuine test must demonstrate |
|---|---|---|---|
| Restore continuity | CU-C0 unchanged valid grant + context | CU-C5 revoked grant, CU-C4 stale basis | Preserve real eligible restoration and reject invalid authority/staleness |
| Dependency freshness | CU-C6 irrelevant edge change | CU-C2 one S→R material edge added | Reassess one affected action, not whole system |
| Source accessibility | CU-C1 directly visible blocking edge | CU-C3+ / CU-C3− hidden-world pair | Distinguish accessible evidence from unobservable truth |
| Privilege minimization | CU-C7 separate observe authorization | CU-C8 same setting absent separate grant | Do not invent fallback privilege |
| Provenance/independence | Independently established lineage/profile | CU-C9 one source replayed | Do not turn shared ancestry into multiple independent votes |
| Human path / lifecycle | Source-owned permitted reapproval | CU-C10 human resume only | Human lifecycle and privilege lifecycle remain separate |
| Enforcement | PEP receipt after authorized PDP decision | Attempted isolate without proper current authority | Decision and actual effect counted distinctly |

A single PASS across these rows cannot establish all interfaces. Cases C7–C10 and deferred scenarios are informative until individually admitted. C2 remains the prospective primary scored case and cannot be cherry-picked conditional on performance.

## 3. Stage A acceptance criteria (candidate, not frozen)

**A0: reference quality.** The evaluator can independently identify one current privilege-applicability predicate and the material dependency event; the source policy and its owner are named.  
**A1: required positive.** A competent conventional configuration can legitimately restore CU-C0 and handle a directly visible blocking dependency CU-C1 before freeze.  
**A2: fair information contract.** Every source fact used by B3 can be obtained by B2 within the same registered authority and budgets, with all extra work charged.  
**A3: no forbidden promotion.** UNKNOWN/stale/correlated evidence does not become unsupported full permission or an asserted observation that the actor never had.  
**A4: correct source-owned authorization.** Conditional full/restricted/reauthorize/deny outcomes are judged by an agreed policy, not the scorer's preferred design.  
**A5: positive continuity and total burden.** No unjustified global block; explicit time/human/network and EA costs.  
**A6: independently adjudicated, no selective cases.** Reference case packet and acceptance criteria precommitted; all runs and deviations retained.

**Pass semantics:** DESIGN-ACCEPTED can be granted locally for a complete review package without experiments. SCIENTIFIC-ACCEPTED requires a frozen, externally reviewable Stage A contract and actual admitted evidence; until then the only proper scientific state is **NOT_ESTABLISHED**. A negative differential or strong parity is still a valid Stage A scientific finding once established.

## 4. Stage B / C and specification projection

A future Stage B package maps these requirement IDs to an actual architecture element and verification method (grant issuer, PDP, PEP, domain adapter, EA qualifier, telemetry, human interface). It must preserve evidence and outstanding semantics from Stage A. A Stage C package requires pinned real/sandbox deployment, actual inputs/outputs and effects against the originating Challenge. The source issue alone does not create accepted normative requirements; the EA [01F specification-preparation annex](../../baseline/01F_EA_FG_TIDA_SPECIFICATION_PREPARATION_ANNEX_v0.2_DRAFT.md) governs further owner review.

## 5. Unresolved requirements (block experiment admission)

- Exact current authorized response policy and treatment of partial evidence, risk levels and narrow permission.
- Who issues/maintains restore predicates (if accepted) and whether they are mandatory, default or optional.
- Owner-confirmed material impact of S→R and any justified exceptions or emergency override.
- Competent B2 implementation chosen by a legitimate owner, positive/repaired demonstration.
- Independent evaluator and materiality/hidden-event custody.
- Legitimate horizon, source access, resource budgets, cost metrics and normative thresholds.
- Frozen protocol, oracle, cases, blinded selection and receipts.

No missing item above should be marked PASS simply because it appears as a field or placeholder in a document.
