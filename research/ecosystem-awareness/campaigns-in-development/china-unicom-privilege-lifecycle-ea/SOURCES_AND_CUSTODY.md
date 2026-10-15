# China Unicom Theme #23 campaign — sources, ownership and custody v0.1


> **Source chronology UPDATE — 14 October 2026, 09:49:50 UTC:** The initial v0.1 source register did **not** include [Ying Wang's second same-day #23 reply](https://github.com/FG-TIDA/themes/issues/23#issuecomment-6165603429). She states agreement with Zhao's suspension-time **declared restore-condition anchor**, to be validated at activation **before fresh intent derivation**; she welcomes the suggested test cases. The earlier open question (“does #23 envisage a declared predicate?”) is therefore **resolved as a source-author discussion preference**, not as an adopted ITU text or finalized implementation. The complete [six-comment chronology](THIRD_PARTY_CHALLENGE_DOSSIER_R123_v0.3.md#2-primary-source-chronology--all-current-comments-in-theme-23) is now the current source cut. Original passages below remain historical, not the final source-status authority.


**Campaign:** DDS-A-CU-PLM-EA-01. **Review cutoff:** 14 October 2026. **Source mode:** publicly visible GitHub texts, not external technical validation.  
**Method:** [DDS index](../../DDS_CANONICAL_METHOD_INDEX_v0.1.md). **Publication policy:** [Repository contributing rules](../../../../CONTRIBUTING.md).

## 1. Source register: what each item actually supports

| ID | Owner / primary source | Source fact or proposal supported | Limitation |
|---|---|---|---|
| CU-S01 | Ying Wang, Ye Tao / China Unicom: [FG-TIDA Theme #23](https://github.com/FG-TIDA/themes/issues/23) | A proposed authorization and agent privilege-lifecycle security framework covering initialization, changes, suspension, activation, revocation and governance; cites ITU-T SG17 C-0676 | Proposal/draft; **not** proof of adopted ITU Recommendation, an approved implementation or tested compliance |
| CU-S02 | Iván Abril Palma: [questions on 30 September](https://github.com/FG-TIDA/themes/issues/23#issuecomment-5915019756) | Three questions: evidence for valid restoration; context at inter-agent propagation; incomplete revocation visibility. Synthetic hibernation example and EA relation | A question/example, not an experimental observation |
| CU-S03 | Ying Wang (@Snoopywy): [reply 14 October](https://github.com/FG-TIDA/themes/issues/23#issuecomment-6164646309) | Proposes multi-source reassessment (intent/scope, graph, criticality, NACL/policy, credential rotation, telemetry), risk-specific confidence, restricted/re-authorized fallback; receiving-PDP review; partially verifiable upstream context; fully/partially/unverifiable revocation outcomes; welcomes optional EA signals and further hibernation discussion | Conceptual design response. Invitation to explore ≠ approval of this DDS campaign, of EHD or of an executed trial |
| CU-S04 | Zhao Xinghua (@zhaoxinghua09-cell): [9 October comment on #23](https://github.com/FG-TIDA/themes/issues/23#issuecomment-6072991126) | Suggests a declared restore predicate at suspension and known-answer cases for revoked-grant/stale-cached reevaluation | Independent contributor suggestion; not accepted requirement in #23 |
| CU-S05 | Lei Gao: [comment on #23, 16 September](https://github.com/FG-TIDA/themes/issues/23#issuecomment-5700157082) | Proposed boundary between privilege decision #23 and human-intervention lifecycle #16 | Interface view proposed in discussion, not a merged normative text |
| CU-S06 | FG-TIDA: [Theme #16](https://github.com/FG-TIDA/themes/issues/16) | External theme context for human intervention | Its authors own its meaning and acceptance |
| CU-S07 | Zhao Xinghua: [Theme #33](https://github.com/FG-TIDA/themes/issues/33) | Evidence-driven re-evaluation of prior governed decisions as a distinct topic | Related proposal; not part of the scored #23 primary trial |
| CU-S08 | FG-TIDA: [Theme #13](https://github.com/FG-TIDA/themes/issues/13) | Ecosystem-level Agent Defense, cross-party signals, containment/privacy and open authority boundaries | Theme charter, not proof that EA has been implemented |
| CU-S09 | Iván Abril / EA: [04 General Functional Interfaces v0.5](../../baseline/04_GENERAL_FUNCTIONAL_INTERFACES_AGENTIC_SECURITY_v0.5_INTEGRATED.md) | EHD semantic handoff, IF-S1–IF-S4 and owner-preserving security/authorization interfaces, UNKNOWN and source-dependence handling | Working architecture/contract; not externally adopted or executed for #23 |
| CU-S10 | Iván Abril / EA: [00M A/B/C/D v0.8](../../baseline/00M_ABCD_AND_MATHEMATICAL_PLAUSIBILITY_v0.8_RESEARCH_NOTE.md) | Canonical A/B/C/D semantic definitions; mathematical plausibility argument | Draft research; no universal completeness, calibrated advantage or proof of deployed correctness |
| CU-S11 | Iván Abril / EA: [00N scientific plausibility v0.7](../../baseline/00N_FROM_MECHANISM_TO_REQUIREMENTS_SCIENTIFIC_PLAUSIBILITY_v0.7_RESEARCH_NOTE.md) | Motivation for qualified metadata, partial context and targeted requalification | Plausibility, not demonstrated operational DDS result |
| CU-S12 | EA research: [DDS Canonical Index](../../DDS_CANONICAL_METHOD_INDEX_v0.1.md) and [Stage A](../../DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1.md) | Stage A/B/C ownership, Simplified profile, technology extension, comparator and trace/evidence discipline | Method working corpus, not external certification |
| CU-S13 | FG-TIDA: [UC-4](https://github.com/FG-TIDA/use-cases/issues/4) and [UC-21](https://github.com/FG-TIDA/use-cases/issues/21) | Possible external matching/negative test contexts and interface precedents | Neither is admitted here as a native executable run nor does any result transfer |
| CU-S14 | ITU-T: [SG17 C-0676](https://www.itu.int/md/T25-SG17-C-0676/en) | Referenced *by the original #23 proposal* as a proposed new work item X.aplm-aia | This campaign has **not independently verified document contents, current ITU stage or normative adoption** |

## 2. Citation, mutable sources and verification limits

The GitHub links above are primary discussion records **as inspected on 14 October**. Issue body and comments can be edited; a URL/comment ID establishes where a statement was read, but not an immutable cryptographic freeze. A future scored study must separately preserve a read-only text snapshot or defensible version pin, date/sha of source evidence actually used, owner-approved interpretation and (when material) policy/graph/credential fixtures.

The newly created local campaign files will be immutable through their Git blob/commit history only after GitHub has accepted them. File presence/hash establishes **text custody**, not truth, independent replication or correctness of a security implementation. No external secrets, operational production data, real NACLs or topology have been requested or acquired.

If source #23 is amended, record: old link/claim, new link/claim, observed time, changed interpretation, case impact, successor version. Do not silently rewrite the case oracle.

## 3. Intellectual and institutional boundaries

- **Original proposal ownership:** Ying Wang and Ye Tao, China Unicom. Their work remains at its original link. This repository holds a **locally authored analytic mapping**, not a copy of their report or a jointly issued China Unicom document.
- **Contributor ownership:** Zhao's restore predicate, Lei's oversight interface and any third-party controls remain attributed to the original contributors.
- **Local research owner:** Iván Abril Palma / The Integral Management Society; the EA scientific/methodological proposal is not China Unicom IP or official ITU language.
- **Re-use status:** Cite public source discussions with authorship; do not import proprietary text, diagrams, executable tests or institutional names as endorsements.
- **Consent:** NO_EXTERNAL_CAMPAIGN_AGREEMENT, NO_SOURCE_OWNER_CONFIRMATION_OF_OUR_EXPECTATIONS, NO_INDEPENDENT_ADJUDICATOR, NO_LAB_ACCESS at v0.1.

## 4. Unconfirmed questions to resolve with source owners

1. Does #23 envisage declared restore predicates at suspension time, or only a fresh evaluation at activation? Is Steven's suggestion within scope?
2. Is there a defined operational coverage representation beyond per-evidence confidence, especially for correlated, unavailable and contradictory domain information?
3. Which conditions authorize a **restricted observation grant** rather than merely declining isolation? Who issues it and how does the PDP trace it?
4. Is “partially revoked” about known residual privileges, while “revocation unverifiable” is about unseen propagation paths? Could both apply within one multi-domain record?
5. What is the minimum result that a domain owner can safely share with another PDP without disclosing private dependency graphs?
6. Which #16 human decision is evidence or a policy input, and which #23 privilege transition must still be independently validated?
7. What horizon, materiality, false-hold criterion and risk-specific thresholds would the real application owner agree to for a single bounded challenge?

Answers must be recorded as **external replies** or explicitly marked as **local assumptions**. Silence is not approval.

## 5. Lineage and separation from other campaigns

Only local files in **china-unicom-privilege-lifecycle-ea/** and the additive campaigns register/index are in scope for this v0.1. No other corpus text, China Unicom issue, Flores dataset or prior external commit is modified by this campaign. Do not retroactively transfer prior UC21/R01/00I numerical evidence to this challenge.

A future reviewer may reproduce our **documentary mapping**, but cannot reproduce a native #23 trial until its reference configurations, grants, event generator and trace/oracle packets exist.
