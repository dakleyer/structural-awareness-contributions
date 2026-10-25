# Corpus Document Control — DC-GH-01

**Edition:** v1.0.1 · **Effective:** 25 October 2026 (owner-authorized clarifications)  
**Owner:** Iván Abril Palma · **Scope:** dakleyer/structural-awareness-contributions  
**Status:** Current repository document-control policy. **Implementation is progressive; publication is not a claim of corpus-wide conformity.**

**Latest conformity audit:** [25 October 2026 — second assessment](./governance/DOCUMENT_CONTROL_CONFORMANCE_AUDIT_2026-10-25.md#second-conformance-audit--25-october-2026) · [VNext-link inventory with dated assessments](./governance/review/DOCUMENT_CONTROL_VNEXT_LINK_INVENTORY_2026-10-25.json).

**Preserved predecessor:** [DOCUMENT_CONTROL v1.1, complete pre-consolidation text](./governance/preserved-public-snapshots/2026-10-25_DOCUMENT_CONTROL_v1.1_PRE_CONSOLIDATION.md). The [24 October v0.1 conventions](./governance/CORPUS_DOCUMENT_CONTROL_CONVENTIONS_v0.1.md) are a historical predecessor, not an independently operative second policy. For working historical hyperlinks, [read the original at its original pinned location](https://github.com/dakleyer/structural-awareness-contributions/blob/21e200cd4c9a0558e4ae3669c55f7256c03a005a/DOCUMENT_CONTROL.md); the relocated custody snapshot retains its original relative strings.

This document consolidates the repository's documentary identity, classification, navigation, VNext, preservation and maintenance rules. It replaces the operative document-control instructions scattered across the prior two controls, **without replacing domain-specific scientific, freeze, review or institutional requirements**.

## 1. Authority, scope and precedence

This file is the single current repository-wide rule for document identity, role, lifecycle, canonical/VNext relationships, document navigation, controlled changes and technical document-control verification.

The [Corpus Review Procedure](./governance/CORPUS_REVIEW_PROCEDURE_2026-10-06.md) remains authoritative for the **method of substantive document reviews**, including human-readable review passes and specific before/after proposals. [Claim and Attribution Boundaries](./governance/CLAIM_BOUNDARIES.md) govern the proper qualification of scientific, institutional and external claims. The [EA Canonical Corpus Manifest](./research/ecosystem-awareness/baseline/CANONICAL_CORPUS_MANIFEST.md) and applicable source-specific freeze, release, provenance and custody records govern **their own identified sources and editions**, not all repository documents.

Preserve signed, frozen, submitted and preregistered source obligations within their exact scope. **Until the register is reconciled, source-specific owner restrictions in the preserved predecessor remain binding for the exact named files and decisions** (including protected routers, append-only materials and canonical presentations); the legacy document is not thereby a second general policy. An owner-authorized file-specific restriction may be stricter than this general policy. Later scoped owner decisions take precedence over earlier contradictory historical status notes only when verified; unresolved conflicts must be reported. No generic cleanup instruction silently overrides such restrictions.

## 2. GitHub is the technical change record

Use GitHub commits, diffs, file revisions, pull requests, issue links, reviews and workflow results for technical provenance. Do **not** duplicate their timestamps, changed-path lists or revision SHAs in every Markdown header or in a continuously appended administrative log.

Explicit dates and edition labels are appropriate when they carry **semantic** meaning: a formal decision, scientific cutoff, research freeze, edition applicability, external submission or institutional effective date. A commit timestamp is not an approval, experimental observation or date of institutional effect.

GitHub publication, merge, issue label and a passing check do not themselves establish scientific validity, owner approval, operational readiness, external endorsement or institutional adoption. Cite a pinned commit when historical interpretation or exact public content matters.

## 3. Keep identity, role, lifecycle and claim status separate

1. **Logical identity:** which subject/document is owned, independently of its filename or location.
2. **Document role:** canonical, VNext, optional/contextual, router/control, evidence/execution, historical source or external submission.
3. **Lifecycle/edition:** active working, under review, frozen, historical, superseded or released within a declared scope.
4. **Claim maturity:** definition, hypothesis, proposal, analytical/model result, executed observation, independently reviewed result or unresolved question, as supported by the source.

**Canonical** means the current primary reading source for a defined logical subject and scope. It does **not** mean scientifically demonstrated, legally binding, independently validated, institutionally received or adopted by FG-TIDA/ITU or another external body. A canonically recorded hypothesis remains a hypothesis. Roles and lifecycle states may overlap: a canonical document may be frozen for one exact edition; a README may be a canonical router.

## 4. Minimal logical-document register

The repository shall progressively maintain a machine-readable `governance/DOCUMENT_REGISTRY.yml` as the single operational mapping for identities and role-dependent checks. Wave 1 collects and adjudicates the read-only inventory; Wave 2 creates the registry from those supported mappings. The registry is not yet present. **Its nonexistence or incomplete coverage is an audit finding, not grounds to invent document roles.**

For registered sources, use only the fields needed to disambiguate: stable logical ID, repository path, role, lifecycle, accountable owner where required, canonical companion/owner relation for VNext, protection mode and approved blob for specially protected files, and relevant decision/exception reference when material. A current logical canonical may have **at most one active VNext**. Historical versions and historical VNext records may remain preserved under their exact editions but must not be counted as additional active companions.

A logical ID must not silently denote two competing current canons. A relocation retains the logical ID; a genuine split or new subject requires a justified identity/lineage decision. Filenames and path suffixes are useful hints, never sufficient proof of canonicality. Ambiguous or unregistered roles shall be reported as **unclassified**, not assumed to be compliant or noncompliant.

Do not rename all existing files, duplicate Git technical timestamps/SHA in document headers, or backfill every contextual record. Register first the protected sources, controlled routers, active canonical/VNext pairs and other documents needed to evaluate actual link findings.

## 5. Canonical and VNext link contract

A VNext is the cumulative review/development shadow **of a specific logical canonical document**. Repeated review passes remain in that one active shadow. A VNext of a VNext is not permitted.

| Source | Direct link to own VNext | Direct link to foreign VNext | Links to canonical, contextual or evidence sources |
| --- | --- | --- | --- |
| Canonical (including canonical router) | Allowed; normally once, when safely editable | **Not allowed** | Allowed |
| VNext | No VNext-of-VNext | **Allowed** | Allowed |
| Optional/contextual | Allowed | **Allowed** | Allowed |
| Historical/frozen | Preserve original edition; do not retrofit | Preserve historical citations | Preserve original references |

A canonical document may therefore reference other canonical, optional, contextual, scientific, evidential and historical materials; **among VNext documents, it may directly reference only its own companion VNext**. Cross-VNext review links and optional/contextual-to-VNext references are legitimate and useful for development of the next corpus. Label proposals clearly when the reader could mistake them for adopted content.

If a canonical source is frozen or externally signed, use its authorized reader index or review card to expose the current review route instead of altering frozen bytes. A hyperlink neither promotes the linked proposal nor transfers document ownership or approval.

## 6. Navigation ownership and preservation

Keep the public programme navigation distinct from internal technical reading routes:

- **Public route:** Iván Abril Palma profile → Structural Awareness Programme → four human programme areas (Mathematical Contributions; Field Notes/Research Series; Field Practice/Engineering; Architectural Contributions/pre-standardization) → Ecosystem Positioning.
- **Technical architecture:** Ecosystem Positioning routes to Ecosystem Awareness, Regime Awareness and Minimum Sufficient Control, with their own canonical technical indexes, work packages, evidence and applications.

The maintained technical corpus has **exactly three canonical README reading levels: Ecosystem Positioning entry → Awareness entry → technical corpus indexes**. The nine controlled owner paths below are not nine reading levels. Package/fixture READMEs and the three existing additional-work catalogues provide subordinate or optional reading; they do not add canonical levels. This carries forward the owner instruction in the [Corpus Review Procedure](./governance/CORPUS_REVIEW_PROCEDURE_2026-10-06.md#redistribución-de-archivos-y-tres-niveles-de-readme--instrucción-de-iván).

Each controlled navigation family has one owner. Cross-links do not transfer ownership. The existing nine controlled navigation owner paths are the transitional baseline: root README; Ecosystem Positioning README; EA entry README; EA baseline README; EA FG-TIDA README; RS-00E-Q1a fixture README; Regime Awareness README; MSCA README; submissions README. The register shall identify these explicitly. Other package READMEs may describe executable packages without becoming extra programme-level navigation owners.

Do not delete or merge a README merely to reduce its numerical count. Moves, renames, splits, consolidation and hierarchy changes require scoped authorization, preserved source content, inbound-link/anchor assessment, reader continuity and exact before/after verification. A presentation-link update must never truncate or regenerate the substantive Ecosystem Positioning router. Canonical presentation editions, original exports and presentation-specific integrity controls retain their existing provenance. Current README and link counts should be **generated**, not manually restated as invariant numbers.

## 7. Review, incorporation and promotion

Use a bounded GitHub issue or pull request to identify the proposed source, reason, material before/after difference, affected consumer meanings and relevant decision authority when substantive or structural change is intended. GitHub already records the technical authoring and file diff. A reviewer must distinguish AI-assisted analysis, human decision and independent external review.

The responsible owner expressly accepts, rejects or defers material proposals before their promotion. Incorporation edits only the approved living canonical target and any authorized consumers, preserving historical editions, external statuses, claims, results and link anchors. Promotion of a **canonical hypothesis** never upgrades it automatically into an experimentally established result.

Routine editorial fixes should have proportionate checks; do not create institutional approval steps for every spelling or link correction. External communications, standards submissions and institutional adoption remain subject to their distinct authority gates.

## 8. Protected, append-only, frozen and historical sources

A registered protection rule may specify owner-gated changes, append-only content, byte-frozen evidence, or historical preservation. The EA entry README and Ecosystem Positioning README have existing owner restrictions; the Ecosystem Positioning Development Strategy additionally carries an append-only instruction in the preserved control history. These protections remain effective pending precise register reconciliation.

For a **specially SHA-protected file**, maintain one current *approved* blob SHA in the register after a verified owner decision; older editions remain in Git history or relevant custody records. A different observed SHA is a finding to investigate, **not** an instruction to overwrite the expected SHA or restore the predecessor. Acceptance of a successor, corrective replacement or deferred review must be explicitly recorded.

Where exact binary/data/frozen bytes matter, preserve their applicable study-specific hashes, pinned sources and custody manifests. Git revision history alone is not a substitute for institutionally authentic records, cryptographic signatures or externally controlled originals.

## 9. Technical checks and enforcement

Extend the **existing** documentation-integrity workflow and script instead of creating a competing control mechanism. Build staged checks for:

1. Logical ID and path uniqueness; missing or conflicting current canonical/VNext relationships.
2. VNext-of-VNext and mutable canonical → foreign VNext direct links.
3. Existing Markdown path integrity and protected router/navigation checks.
4. Special protected SHA and append-only constraints where executable.
5. Bounded reports of link occurrences, distinct edges, source files, declared classes, exceptions and unclassified sources.

Keep the broad documentation link checker on pull requests/manual runs unless its false positives and notifications are separately resolved. A lightweight protected-file check may also run on pushes, but **post-push detection alone does not prevent a change**. Genuine merge-time enforcement requires applicable GitHub branch/ruleset controls and required checks/reviews to be configured and verified.

A green CI result certifies only the checks actually run. Missing classifications, frozen exceptions and semantic claims require separate human assessment; do not claim complete corpus reconciliation from a passing link scan.

## 10. Institution and programme boundaries

This public research corpus has a technical GitHub document authority, not automatic normative authority for The Integral Management Society.

When an IMSV body formally adopts a document under its applicable statutes, the institutional record, authenticated exemplar, scope, date and registered reception (*Receptio*) remain under the **IMSV institutional system**. GitHub may reference that decision; it must not create a parallel institutional register or infer adoption from a merge. Canonical research documentation needs no Receptio unless an institutional norm is actually being enacted.

No GitHub link or publication implies approval, validation or adoption by FG-TIDA, ITU, WIPO, a university, funder, industry organization or technology provider.

## 11. Exceptions, conservation and historical citations

Retain superseded sources, review records, submitted packets, frozen tests and negative results for their exact provenance. Historical links may legitimately point to older paths or pinned Git commits. Do not silently rewrite historical records for a current link-style convention.

Record any exception with its scope, source, justification, responsible decision and reference. Avoid a separate administrative log of all commits; issues/PRs and Git history already provide that trail. Use a distinct record only where the semantic decision cannot be inferred from the technical change.

## 12. Bounded rollout and acceptance

- **Wave 0 — effective policy and custody:** preserve predecessor texts, publish this single current policy and audit link, identify protected-source discrepancies. No mass corpus changes.
- **Wave 1 — read-only inventory:** enumerate VNext references; distinguish occurrences, unique edges, source roles and historical citations. Resolve identity ambiguities before labeling violations.
- **Wave 2 — safeguards:** create `governance/DOCUMENT_REGISTRY.yml` from the adjudicated logical identities, extend the existing check, and configure enforceable review/branch settings proportionately.
- **Wave 3 — approved corrections:** amend only confirmed incompatible mutable canonical links and ownership ambiguities, in small evidence-backed PRs.
- **Wave 4 — conformance closure:** rerun checks, record unresolved exceptions/owner decisions, verify actual GitHub enforcement, and close the follow-up only to its demonstrated scope.

The [dated conformance audit](./governance/DOCUMENT_CONTROL_CONFORMANCE_AUDIT_2026-10-25.md) is the **baseline of actual versus required state** and remains linked from this policy. It is not a certification of scientific results or institutional norms.

## 13. Maintenance

This file is the one active repository-wide document-control policy. CONTRIBUTING and routing READMEs should link here without copying competing control rules. The Corpus Review Procedure governs substantive audit method; scientific and frozen-source manifests retain their own narrow source authority.

Amendments require a scoped GitHub change record and responsible-owner decision where relevant. Git supplies technical modification dates; do not keep a manually updated changelog inside this current policy. Preserve previous approved editions and their reader links.


## 14. Corpus action, promotion and verification plan — 25 October 2026

**Purpose:** put document control into everyday practice and move settled development out of VNext into the maintained corpus. This is the single cross-corpus action plan, connected to the [second control audit](./governance/DOCUMENT_CONTROL_CONFORMANCE_AUDIT_2026-10-25.md#second-conformance-audit--25-october-2026). Its scope is all Contributions, including EA, RA, MSCA, DDS, case/campaign interfaces, optional material and the controls that publish changes.

**Iván’s instruction:** the global plan belongs here, includes the specific VNext blocks to incorporate, and specifies complete surgical text/link pairs and verification. The existing VNext remain the source-owned audit/development spaces. Publication of this plan records the proposed work; Iván gives the GO for each incorporation wave. Sections 1–13 above remain operative until their identified amendments are accepted. No proposed pair, registry, workflow or GitHub setting is executed by appending this section.

### 14.1 What changes in daily work

A contributor starts from the current source and its one logical VNext, identifies the issue and receivers, then proposes a complete unit for incorporation. The owner decides the named wave. The publisher applies only those units, verifies the entire diff and reader routes, and publishes through a bounded PR. After public readback, the existing VNext records the application, removes the applied item from its pending queue and keeps a short receipt pointing to its complete immutable history. The next wave is drawn from the remaining real backlog.

Three controls carry different responsibilities: **the registry identifies documents and their protection; the verifier checks content, relationships and preservation; GitHub permissions/reviews prevent an unapproved merge.** A green content check is not the human decision, and a human decision does not excuse an incorrect diff.

### 14.2 Ordered work packages

| Order | Package and deliverable | Expected impact | Risk / effort | Exit test |
| --- | --- | --- | --- | --- |
| First | Reconcile current identities, protection and already-applied proposals; establish the small register seed below | High | Medium / Medium | Nine navigation owners, three specially protected sources, the 75 review-candidate population and material logical parts have supported mappings or named open decisions |
| First promotion wave | Incorporate eight selected explanatory/evidence blocks through three complete source pairs below; receive them in the owning reviews | High | Low–Medium / Medium | Literal current units, complete proposed additions, source/receiver review and named GO; frozen predecessors stay exact |
| In parallel after mapping | Extend the existing integrity check and resolve the four exact historical quote contexts; distinguish split sources and semantic review aliases | High | Medium / High | Valid examples pass and each relevant adverse case below blocks or reports exactly the required condition |
| Next promotion waves | Review all 75 existing review units in three reading batches of 25, then incorporate accepted blocks in small waves of 5–10 units | High | Medium / High | Every review has a current disposition and receiving source; each settled block is incorporated, rejected, superseded or assigned a concrete evidence task |
| After content reception | Adjust the ten confirmed foreign-review router occurrences, including benchmark aliases; repair the additional living 05A cross-review route | High | Medium / Medium | Every new route reaches the intended canonical reading and its own review; EP/EA owner restrictions and frozen editions are respected |
| After verifier and actor tests | Activate one native main-branch protection configuration, explicit code ownership and an identifiable required check | High | Medium / Medium | A non-bypass actor cannot merge an adverse example; authorized owner review and a valid exact wave can merge |
| Final acceptance | Rerun the scoped corpus checks and repeat public readback after each wave | High | Low / Medium | Complete evidence packet, unchanged unrelated blobs, known exceptions and genuine remaining decisions visible |

### 14.3 VNext promotion subplan: content, receivers and closure

**Promote settled content, not audit administration.** Definitions, readable explanations, qualified source updates, interface clarifications, accepted design changes and explicitly identified research hypotheses can enter their proper maintained source. Audit conversations, before/after cards, reviewer disagreements, approval notes and verification logs remain in review/history. A hypothesis enters as a hypothesis; an observed result keeps its actual version, method and evidence limits.

For every promotion unit, record: source VNext section and blob; exact selected material; receiving logical source/edition; old complete receiving unit; proposed complete unit; rationale; positive impact/risk/effort; affected producers/consumers; conflicting alternatives; applicable protection; decision; application evidence; and what leaves the pending queue. The code/link pairs later in this plan provide the concrete first units. A shared roadmap does not replace their source-level reception when applied.

**First substantive selection — eight blocks, three receiving documents:**

1. **Requirements VNext, CAND-R1:** bound role versus observed effective function; preserve the distinction between identity/behaviour and legitimate authority.
2. **Requirements VNext, CAND-R2:** opportunity, admissibility, authority and execution remain separate decisions, with legitimate re-contracting/requalification before action.
3. **Requirements VNext, CAND-R3:** locally permitted actions do not by themselves authorize a material aggregate effect. The authority owner defines that aggregate scope.
4. **04 VNext §6:** qualification validity and useful response time are different clocks; keep each where material.
5. **04 VNext §7:** a human-produced review result retains the same bounded result, assurance, capacity and residual distinctions used for other handoffs.
6. **05A VNext §2.15:** receive the UC-6 Stage-0 reference at its reported, bounded evidence level.
7. **05A VNext §2.15:** receive H1’s four prospective cases as a proposed protocol, with source, decision, acknowledgement and independent effect observations separate.
8. **05A VNext §2.15:** receive the distinction between reported content identity and latest decision-applicable source state; qualify the latter against its own freshness evidence.

Blocks 1–3 enter the existing owner-approved Requirements successor. A separate, explicit five-unit identity packet makes that existing edition the current maintained canonical reading and updates its status/version/scope consistently; the 17 September frozen test baseline stays exact and controls studies that cite it. The receiving manifest/index must acknowledge the same edition before that role promotion closes. Blocks 4–5 enter the living 04 integrated reader without changing the earlier controlled 04 sources. Blocks 6–8 enter a clearly dated reception section in the public working 05A bridge; the 19 September text remains its original snapshot. The proposed texts are editorial/evidence qualifications, not extra S/T/H identifiers, a new EHD kernel or an external contract adoption. Their joint receiver check includes 00H/DBC, S10, IF-S6, 05 Ideal, UC-6/H1 and the case/campaign route.

**Subsequent promotion families:**

| Family | Specific material to resolve | Receiving route and required decision |
| --- | --- | --- |
| Remaining Requirements development | CAND-R4/S10 receipt and CAND-R1–R3 after the first wave; separate later assessor-meta hypotheses | Existing working successor plus the one Requirements review; CAND-R4 is already incorporated there, so verify rather than repeat it |
| 04 /05 ideal /05A current interfaces | Generic A versus A_ref, profile-specific input/output relations, Theme 13/16/21/18/5/9 material, current-source versus ideal classifications | Living 04 and 05A for supported amendments; frozen 05 v0.4 needs a specifically approved later edition before a contract change. Carry the complete contracts and part order forward |
| 00D benchmark v0.3 | Positioning design, ablations/complexity, Requirements traceability, prior-art audit and fixture admission | Keep v0.2 current until design-adoption gates are examined. Adopt bounded design as design; comparative execution is a separate evidence claim |
| Foundation/01A/02A/00M/00N and gradient | Already-adopted hypothesis language versus additional causal/computation claims, source sufficiency and burden limits | Existing source units and companions; verify 24 October editorial reception and earlier applied cards. FH-C/FH-E are already canonical research hypotheses, not new unaccepted promotions |
| EA/RA/MSCA composition | Producer/result, sufficiency, operating regime, authority and qualified response; actual operation/scope/version/time/capacity/burden | Existing 01B/01C/01D and RA/MSCA source units; reconcile both ends before incorporating a changed contract |
| DDS, R01, extensions and instruments | Accepted methodological explanation, exact custody, finding scope, comparator credit, return path and remaining test questions | Current DDS/method/source owners; keep frozen runs/results. Resolve the RATS/protocol parallel scopes before declaring one current logical pair |
| Cases, applications, campaigns and exercises | Challenges versus technology-specific scenarios; UC-21 objectives→Challenges→DDS→campaigns→results; controlled historical sources | Maintained Contributions route. Earlier fork proposals are history to reconcile, not an instruction to republish the fork as canon; official FG-TIDA actions retain their separate decision route |

All 75 current review candidates are listed below with their observed source candidates and disposition work. The list is a **coverage queue**, not75 newly approved pairs or proof that all scientific readings are complete. After the first three reading batches, no unit remains merely “pending”: it has selected blocks and an incorporation wave, a concrete evidence task, an explicit owner decision, or a completed/rejected/superseded receipt. If the same block remains pending across two later approved waves, the owner states the next deliverable and receiver decision. This is a work cadence, not a timer or automatic promotion deadline.

### 14.4 Current ledger reconciliation before promotion

The existing 150-entry priorities ledger mixes lifecycle fields: 56 entries have `application_status=applied`;90 lack that field; four carry `pending_specific_GO`. The missing field is not evidence of an unimplemented change. Human states also identify 53“Aplicado”, four “Aplicado en sucesor de trabajo”, seven “Ya publicado”,52 applied/removed receipts and other retired/research states; these categories overlap the machine field and must not be added as independent changes.

Revalidate block 83–90 against the maintained Contributions/official routes, rather than revive its old fork targets. Compare 144–147 by exact proposal edition and current official body; later 147 adoption cannot be inferred solely from earlier 144 or from one older state flag. Research 43–51 are nine work lines without a complete executable delta; identify their next research deliverable instead of presenting them as nine low-risk edits. Applied 148–150 stay applied. Exact current-state normalization is proposed only where public source/application evidence supplies a witness; no blanket flag replacement is authorized.

### 14.5 Verification contract for each wave

1. **Select:** read current GitHub head and the operative control; identify logical source, existing companion, frozen parts and consumers. Stop a particular ambiguous unit at its named decision; continue independent units.
2. **Preserve:** retain authentic complete preimages before edits; pin source head/blob and full old units. For an addition, show its complete old context, location and full added block. For a new file, verify absence and give its complete proposed content.
3. **Authorize:** Iván’s GO names the units/wave and any precise protected-file exception. An append-only EP rule cannot be satisfied by changing a historic href and calling it an addition. The EP replacement pairs below explicitly require that narrow exception; otherwise retain the exact old bytes and defer the incompatible replacement.
4. **Apply:** patch the identified source region only. Literal old units in this plan’s code fences are quotations, not substitute targets. Locate operative source sections outside fenced plans, verify offsets/context and reject a stale or ambiguous match. Do not regenerate entire sources from summaries.
5. **Check preservation:** compute expected candidate bytes; reverse just the approved operations to recover exact preimages; compare the complete changed-path set, modes, protected/frozen blobs and unrelated blobs. For append-only files require an exact predecessor-byte prefix. Concatenated logical parts also retain their declared order and source bytes.
6. **Check meaning and navigation:** inspect producer→consumer→return; current/source/edition authority; GFM paths, explicit IDs and heading fragments; inbound anchors; canonical→own-review relations including aliases; all previously reachable reader routes. Material additional files stay linked as supporting reading through the existing owners.
7. **Incorporate and read back:** verify current main/PR heads, actual required reviews/checks, publish without force, and download the exact public merged version. Require byte equality and the same approved diff before marking a unit applied.
8. **Close reception:** remove the exact applied proposal from the pending queue, retain its original anchor on a short applied receipt and link its complete pinned card. Update both affected source reviews and any existing ledger entry. Keep audit arguments, dissent and frozen evidence. Report unincorporated candidates by their real reason.

**Acceptance evidence:** one bounded PR links the source review, complete pairs, responsible decision, changed-path/diff verification, source-aware link/anchor report, relevant tests, public readback and current queue state. GitHub supplies the technical chronology; no parallel manually copied changelog is required in every document.

### 14.6 Enforcing the contract in this repository

**Observed starting point:** main is unprotected; rulesets are empty; no CODEOWNERS or global document register exists. Several checks publish the same context name, `verify`, from GitHub Actions application 15368. That name is ambiguous for a future required-check rule. Use the unique proposed context **Document control verification** and confirm its actual published identity before enabling the rule.

**Identify first.** The registry seed later in this plan records supported owners/protection and the exact prospective relationships needed by the first wave. Expand it to the 75 review candidates and their actual source/part/edition units, then to remaining active material. Unknown legacy roles remain visible; a new/changed unclassified active source requires adjudication rather than automatic promotion or silent exemption. Filename-hinted and semantic aliases enter the same logical-owner check.

**Extend the existing verifier.** Keep the existing eight architectural-section minima, four routes and two presentation checks. Add deterministic GFM path/fragment/role checks; one active canonical/companion per logical identity; no VNext-of-VNext; protected-byte/prefix checks; exact-diff validation; and a scope report separating covered, excepted and unclassified sources. Preserve historical data as data. The implementation must take base/head identities and supported registry mappings explicitly and validate the candidate without running its research programs. This plan specifies its acceptance contract; a code wave must publish the complete function-level before/after implementation and tests before GO.

**Use narrow historical contexts.** The two 04manifest references and two 00K/A22A13/A14 references are four exact quote occurrences with valid original receivers. Bind each exception to its actual quote span/section, quote-byte SHA256, original source context, expected occurrence count, receiver and decision. If quoted bytes or the live surrounding destination change, re-evaluate it; do not exclude whole reviews. Register UC-EA-03part01→part02→part03 as a logical split source so its Annex-I URL is evaluated after exact concatenation. Historical snapshots retain their source-relative strings and immutable byte checks.

**Separate authorship and approval before activating mandatory owner review.** Existing public PRs are authored as @dakleyer. That account cannot approve its own PR. For the target mode, automation publishes feature-branch PRs through a distinct, narrowly permitted installation/actor; Iván reviews through the owner identity. Automation has no administration, bypass or owner credential. Confirm the actual actor, repository permissions and independent reviewer path before activation. Until that separation exists, owner GO is a procedural record and must not be described as machine-enforced human approval.

**Protect the checker and its inputs.** Code ownership covers the controls, registry, workflow, verifier and maintained corpus. A candidate cannot gain authority just by adding `approved:true` or modifying its own verifier to print success: structural checking and the native required-owner-review are separate gates. Changes to enforcement, exceptions or mappings receive explicit control-owner review. Execute a trusted verifier version, treat candidate Markdown/registries as data and use read-only workflow permissions. If a stronger trusted-workflow guarantee is needed, the personal repository needs a separately trusted check publisher or an explicitly scoped organization-level design; an arbitrary check name or copied boolean is insufficient.

**Activate one native mechanism.** The complete branch-protection target below is proposed for main; do not also install a second competing ruleset. Require the uniquely identified check from the observed application, an up-to-date branch, PR review and conversation resolution, reject force pushes/deletion and include administrators. Use no normal automation bypass. The owner can still administer GitHub; controlled exceptional recovery requires a named decision, preserved states and verified restoration. Broad link checking remains on PR/manual events, preserving the existing notification policy.

GitHub supports selecting the expected check publisher and notes that required contexts can include skipped/neutral results: the required final verification step must actually execute and assess missing coverage/dependencies, rather than rely on a skipped job. CODEOWNERS requests/requirements are effective through base-branch content and review configuration. Consult the [required-check rules](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets), [branch protection](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches), [code ownership](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners) and [author-review restriction](https://docs.github.com/en/pull-requests/how-tos/review-pull-requests/approving-a-pull-request-with-required-reviews). Organization-managed required-workflow facilities must not be presumed available in this personally owned repository. A `pull_request_target` design would require separate security review and must never execute untrusted candidate code; see [GitHub’s event guidance](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#pull_request_target).

### 14.7 Adverse-case acceptance matrix

These are mandatory future tests on disposable candidate objects or an explicitly approved test branch. The present plan does not push deliberately invalid content or change settings.

| Test | Candidate | Required result |
| --- | --- | --- |
| Valid surgical wave | Accepted complete units only, current source and all receivers | Checks and distinct owner review permit incorporation; public bytes equal candidate |
| Unrelated comma | One extra change outside the approved spans | Exact-scope/inverse check rejects |
| Lost text/file | Truncation, delete, rename or mode change outside scope | Reject with exact path/span |
| Append-only damage | Alter one prior EP/strategy byte while appending a note | Prefix check rejects |
| Freeze change | Modify a result, historical/source binary or frozen part | Reject unless a separately scoped authorized successor is used; original stays exact |
| Duplicate companion | Second active VNext under another alias/version | Logical-identity check rejects |
| VNext-of-VNext | Review points to a review as its owning source | Reject; ordinary cross-review references remain allowed |
| Foreign review | Canonical router directly links another source’s VNext, including benchmark v0.3alias | Reject new live edge; justified frozen/historical citation keeps its scoped disposition |
| Own/context link | Own companion or declared optional/contextual cross-review route | Accept within declared role; do not promote a target by hyperlink |
| Broken section | Existing file but missing/changed fragment | Reject actionable route; explain exact original-context exception |
| Applied-card cleanup | Retire a card but omit its incoming old anchor | Reject; receipt retains anchor and pinned full card |
| Frozen quote | Unchanged04/00Kquote plus valid original receiver | Exact contextual disposition, not false missing-file claim |
| Quote broadening | Change the quoted span or add a live bad href nearby | Old exception no longer covers it; reject/report the new defect |
| Split source | Complete UC-EA-03 parts versus a missing/reordered/changed part | Assemble and validate the complete declared unit; reject the latter |
| Self-approval | Candidate flips a registry flag without owner review | Native merge gate remains blocked; flag is not authority |
| Stale decision | Source/head changes after review or another commit is pushed | Revalidate pairs, dismiss stale approval as configured and require current-head checks |
| Wrong check publisher/name | Same display label from another publisher or ambiguousverify | Cannot satisfy the configured unique expected context/source |
| Disabled verifier | Required step skipped or candidate changes verifier to return success | Trusted verification/owner-review tests expose the change; no claim of completed assessment |
| Direct push/force/delete | Non-bypass actor targets main directly or force-updates/deletes it | Actual GitHub rejection; feature-branch proposal remains possible |
| Self-review lockout | Owner-authored PR with owner-only approval rule | Detect before activation; establish the distinct-author/reviewer route first |
| Partial incorporation | Three of four accepted units reach main | Remain partial; untouched unit stays pending; do not retire it |
| Duplicate old application | An already-incorporated paragraph is proposed again | Identify current witness; close/reconcile without adding it again |
| Claim upgrade | Research hypothesis/reference fixture becomes validated/native/adopted by wording alone | Semantic review rejects the unsupported status change |
| Recovery | Authorized correct wave after an adverse example | Rules still enforce; valid wave succeeds without weakening the rule |

Closure requires both a valid wave and representative rejected cases with actual actor, head, rule/check result and resulting branch state recorded. A textual configuration proposal, a local content check or one successful merge does not establish that a non-bypass actor was blocked.

### 14.8 Exact prospective changes

The following units are proposals for later named waves. All source units below were checked against `2aa0c10af14b80035d845ec8ebdcf83d2a0a2887`; source blob, byte location, complete old/proposed text, link transitions, dependencies and acceptance are stated with each. The first implementation step revalidates the then-current source region. The prospective registry/CODEOWNERS have no current file; their complete candidate contents are shown. No status or setting below is an observation that it has already been applied.


#### Unit 1 — Make the registry serve incorporation, not just filenames

**Source:** `DOCUMENT_CONTROL.md` · current blob `984ba6c35cc161c57c757faf0a98295548b7fe40` · line 42, bytes 5703–6246 at the pinned source cut. **Expected impact:** High; **risk:** Medium; **effort:** Medium.

**Why:** Bind the mapping to actual source/receiver and decision evidence rather than invent roles from paths.

**Dependencies and decision:** Named wave GO and current source/receiver validation

**Texto antes — complete current unit**

````````````text
For registered sources, use only the fields needed to disambiguate: stable logical ID, repository path, role, lifecycle, accountable owner where required, canonical companion/owner relation for VNext, protection mode and approved blob for specially protected files, and relevant decision/exception reference when material. A current logical canonical may have **at most one active VNext**. Historical versions and historical VNext records may remain preserved under their exact editions but must not be counted as additional active companions.
````````````

**Texto después — complete proposed unit**

````````````text
For registered sources, use only the fields needed to disambiguate: stable logical ID, repository path, role, lifecycle, accountable owner where required, canonical companion/owner relation for VNext, protection mode and approved blob for specially protected files, and relevant decision/exception reference when material. A current logical canonical may have **at most one active VNext**. Historical versions and historical VNext records may remain preserved under their exact editions but must not be counted as additional active companions. For each incorporation wave, the accepted packet identifies the exact source edition, selected review blocks, receiving source, complete old/new units and affected consumers. Registry fields describe the resulting identity and protection; a candidate cannot authorize itself by changing a status flag.
````````````

**Acceptance:** exact source-region match and inverse; complete proposed unit appears once in the intended receiving body; all unrelated bytes, claim levels and frozen sources remain exact. Check source/receiver meanings, route targets and incoming anchors, then public readback and the owning review/queue receipt.


#### Unit 2 — Give every settled VNext block an incorporation outcome

**Source:** `DOCUMENT_CONTROL.md` · current blob `984ba6c35cc161c57c757faf0a98295548b7fe40` · line 50, bytes 6956–7147 at the pinned source cut. **Expected impact:** High; **risk:** Low; **effort:** Medium.

**Why:** Turn the existing one-companion rule into an active promotion and queue-maintenance obligation.

**Dependencies and decision:** Named wave GO and current source/receiver validation

**Texto antes — complete current unit**

````````````text
A VNext is the cumulative review/development shadow **of a specific logical canonical document**. Repeated review passes remain in that one active shadow. A VNext of a VNext is not permitted.
````````````

**Texto después — complete proposed unit**

````````````text
A VNext is the cumulative review/development shadow **of a specific logical canonical document**. Repeated review passes remain in that one active shadow. A VNext of a VNext is not permitted. Its purpose is to develop an incorporable next edition. Resolve settled blocks through a named promotion wave; keep only real unresolved proposals in its pending queue, with a concrete next deliverable or owner decision. After incorporation, retain the audit argument and an anchored receipt of the complete historical card.
````````````

**Acceptance:** exact source-region match and inverse; complete proposed unit appears once in the intended receiving body; all unrelated bytes, claim levels and frozen sources remain exact. Check source/receiver meanings, route targets and incoming anchors, then public readback and the owning review/queue receipt.


#### Unit 3 — Specify the owner decision and exact incorporation acceptance

**Source:** `DOCUMENT_CONTROL.md` · current blob `984ba6c35cc161c57c757faf0a98295548b7fe40` · line 80, bytes 11121–11514 at the pinned source cut. **Expected impact:** High; **risk:** Medium; **effort:** Medium.

**Why:** Make the approval and acceptance concrete for publishers and reviewers without adding an institutional approval process.

**Dependencies and decision:** Named wave GO and current source/receiver validation

**Texto antes — complete current unit**

````````````text
The responsible owner expressly accepts, rejects or defers material proposals before their promotion. Incorporation edits only the approved living canonical target and any authorized consumers, preserving historical editions, external statuses, claims, results and link anchors. Promotion of a **canonical hypothesis** never upgrades it automatically into an experimentally established result.
````````````

**Texto después — complete proposed unit**

````````````text
The responsible owner expressly accepts, rejects or defers identified material units before their promotion. The decision names the source/receiver editions, complete old/new passages, dependencies, changed-path scope and any precise protected-file exception. Incorporation edits only those targets and authorized consumers, verifies exact candidate bytes and unrelated-file preservation, and is complete after public readback and source-owned review reception. Promotion of a **canonical hypothesis** preserves its hypothesis status; stronger claims need their own supporting evidence.
````````````

**Acceptance:** exact source-region match and inverse; complete proposed unit appears once in the intended receiving body; all unrelated bytes, claim levels and frozen sources remain exact. Check source/receiver meanings, route targets and incoming anchors, then public readback and the owning review/queue receipt.


#### Unit 4 — Check protection against the trusted pre-change state

**Source:** `DOCUMENT_CONTROL.md` · current blob `984ba6c35cc161c57c757faf0a98295548b7fe40` · line 88, bytes 12268–12696 at the pinned source cut. **Expected impact:** High; **risk:** Medium; **effort:** Medium.

**Why:** Prevent an edited expected SHA or same-PR permission flag from laundering an unrelated source change.

**Dependencies and decision:** Named wave GO and current source/receiver validation

**Texto antes — complete current unit**

````````````text
For a **specially SHA-protected file**, maintain one current *approved* blob SHA in the register after a verified owner decision; older editions remain in Git history or relevant custody records. A different observed SHA is a finding to investigate, **not** an instruction to overwrite the expected SHA or restore the predecessor. Acceptance of a successor, corrective replacement or deferred review must be explicitly recorded.
````````````

**Texto después — complete proposed unit**

````````````text
For a **specially SHA-protected file**, maintain one current *approved* blob SHA in the register after a verified owner decision; older editions remain in Git history or relevant custody records. A different observed SHA is a finding to investigate, **not** an instruction to overwrite the expected SHA or restore the predecessor. Acceptance of a successor, corrective replacement or deferred review must be explicitly recorded. Validate a protected change against the trusted pre-change rule and the specific accepted delta. A register edit in the same PR is a proposed successor decision, not proof that the prior protection was satisfied. For append-only sources, require exact preservation of every predecessor byte as a prefix unless the owner explicitly accepts a named replacement exception.
````````````

**Acceptance:** exact source-region match and inverse; complete proposed unit appears once in the intended receiving body; all unrelated bytes, claim levels and frozen sources remain exact. Check source/receiver meanings, route targets and incoming anchors, then public readback and the owning review/queue receipt.


#### Unit 5 — Make future merge safeguards executable for the actual actors

**Source:** `DOCUMENT_CONTROL.md` · current blob `984ba6c35cc161c57c757faf0a98295548b7fe40` · line 102, bytes 13605–14006 at the pinned source cut. **Expected impact:** High; **risk:** Medium; **effort:** Medium.

**Why:** Avoid ambiguous verify contexts, self-review lockout and candidate-controlled authority.

**Dependencies and decision:** Unique check published; distinct author/reviewer path confirmed; complete verifier tests pass

**Texto antes — complete current unit**

````````````text
Keep the broad documentation link checker on pull requests/manual runs unless its false positives and notifications are separately resolved. A lightweight protected-file check may also run on pushes, but **post-push detection alone does not prevent a change**. Genuine merge-time enforcement requires applicable GitHub branch/ruleset controls and required checks/reviews to be configured and verified.
````````````

**Texto después — complete proposed unit**

````````````text
Keep the broad documentation link checker on pull requests/manual runs unless its false positives and notifications are separately resolved. A lightweight protected-file check may also run on pushes, but **post-push detection alone does not prevent a change**. Genuine merge-time enforcement requires applicable GitHub branch/ruleset controls and required checks/reviews to be configured and verified. Use an unambiguous required-check name and its verified publisher. Before enabling owner-required reviews, establish distinct automation authorship and a human owner reviewer; the author account cannot approve its own PR. Keep the control implementation and its mappings under owner review and treat candidate content as data.
````````````

**Acceptance:** exact source-region match and inverse; complete proposed unit appears once in the intended receiving body; all unrelated bytes, claim levels and frozen sources remain exact. Check source/receiver meanings, route targets and incoming anchors, then public readback and the owning review/queue receipt.


#### Unit 6 — Make historical exceptions and applied-card retirement exact

**Source:** `DOCUMENT_CONTROL.md` · current blob `984ba6c35cc161c57c757faf0a98295548b7fe40` · line 118, bytes 15380–15683 at the pinned source cut. **Expected impact:** High; **risk:** Low; **effort:** Medium.

**Why:** Preserve genuine history while rejecting a newly broken live route beside an old quotation.

**Dependencies and decision:** Named wave GO and current source/receiver validation

**Texto antes — complete current unit**

````````````text
Record any exception with its scope, source, justification, responsible decision and reference. Avoid a separate administrative log of all commits; issues/PRs and Git history already provide that trail. Use a distinct record only where the semantic decision cannot be inferred from the technical change.
````````````

**Texto después — complete proposed unit**

````````````text
Record any exception with its scope, source, justification, responsible decision and reference. Avoid a separate administrative log of all commits; issues/PRs and Git history already provide that trail. Use a distinct record only where the semantic decision cannot be inferred from the technical change. For quoted or split historical sources, bind the disposition to the exact source unit/quote bytes, original context, expected occurrences and valid receiver; a blanket VNext, directory or blockquote exclusion is insufficient. Retiring an applied proposal keeps its incoming anchor on an application receipt and its complete pre-application card at an immutable revision.
````````````

**Acceptance:** exact source-region match and inverse; complete proposed unit appears once in the intended receiving body; all unrelated bytes, claim levels and frozen sources remain exact. Check source/receiver meanings, route targets and incoming anchors, then public readback and the owning review/queue receipt.


#### Unit 7 — Put substantive promotion before routing cleanup

**Source:** `DOCUMENT_CONTROL.md` · current blob `984ba6c35cc161c57c757faf0a98295548b7fe40` · line 125, bytes 16321–16474 at the pinned source cut. **Expected impact:** High; **risk:** Low; **effort:** Medium.

**Why:** Make mature content available in the actual corpus rather than hide a living proposal behind a replacement hyperlink.

**Dependencies and decision:** Named wave GO and current source/receiver validation

**Texto antes — complete current unit**

````````````text
- **Wave 3 — approved corrections:** amend only confirmed incompatible mutable canonical links and ownership ambiguities, in small evidence-backed PRs.
````````````

**Texto después — complete proposed unit**

````````````text
- **Wave 3 — promotion and approved corrections:** incorporate accepted VNext blocks into the proper maintained sources, reconcile their receivers, retire applied pending cards with anchored historical receipts, and then amend confirmed incompatible mutable canonical review links in small evidence-backed PRs. Preserve frozen source editions and keep unresolved material assigned to a concrete decision or research task.
````````````

**Acceptance:** exact source-region match and inverse; complete proposed unit appears once in the intended receiving body; all unrelated bytes, claim levels and frozen sources remain exact. Check source/receiver meanings, route targets and incoming anchors, then public readback and the owning review/queue receipt.


#### Unit 8 — Promote Requirements CAND-R1–R3 into the working successor

**Source:** `research/ecosystem-awareness/baseline/00_REQUIREMENTS_WORKING_SUCCESSOR_2026-10-12.md` · current blob `c0226a1ba9a45976ad0c887dd9afb97b103e6c37` · line 227, bytes 46863–47110 at the pinned source cut. **Expected impact:** High; **risk:** Medium; **effort:** Medium.

**Why:** Give readers three current, implementation-neutral distinctions already developed in the sole Requirements review; keep the frozen test contract intact.

**Dependencies and decision:** Named wave GO and current source/receiver validation

**Material selected from VNext:**

- `research/ecosystem-awareness/baseline/00_REQUIREMENTS_VNEXT_REVIEW_AND_DELTA_v0.1_DRAFT.md` — CAND-R1 — effective-role drift within S7 / S10 / S12 / S13
- `research/ecosystem-awareness/baseline/00_REQUIREMENTS_VNEXT_REVIEW_AND_DELTA_v0.1_DRAFT.md` — CAND-R2 — make opportunity / admissibility / authority / execution separation visually explicit
- `research/ecosystem-awareness/baseline/00_REQUIREMENTS_VNEXT_REVIEW_AND_DELTA_v0.1_DRAFT.md` — CAND-R3 — per-action compliance does not establish aggregate authorization

**Texto antes — complete current unit**

````````````text
Any such extension must be introduced through an explicit, version-controlled requirements change with traceability to the affected S/T/H/KPI routes. Existing pre-registrations and tests remain interpretable against the version they actually cite.
````````````

**Texto después — complete proposed unit**

````````````text
Any such extension must be introduced through an explicit, version-controlled requirements change with traceability to the affected S/T/H/KPI routes. Existing pre-registrations and tests remain interpretable against the version they actually cite.

## Interpretive clarifications — role, opportunity and composed authority

**Effective role and bound role.** A material mismatch between the function being performed and the assigned role calls for requalification under S7/S10/S12/S13. Observed behaviour, a stable identity or a newly available capability does not establish an expanded grant. The legitimate authority owner determines the permitted role and response.

**Opportunity, admissibility, authority and execution.** A useful and reachable option can be preserved and ranked while it remains outside the current grant. Check admissibility and authority separately; request or re-contract through the legitimate owner, requalify the changed basis, and execute only the authorized action.

**The unit of authority includes the material composed effect.** Permission for each atomic action does not by itself authorize a cumulative or composed outcome. Where the owner's constraint is cumulative, campaign-level or resource-time-based, evaluate that declared effect boundary. S1/S8/S9/S10/S12/S13/S14 supply the existing scope, non-amplification, composition and transition duties; no universal aggregation window or centralized ledger is introduced.

These are reading clarifications of the existing S/T/H system in this maintained reading. The 17 September frozen baseline and each study's identified test contract retain their versions.
````````````

**Acceptance:** exact source-region match and inverse; complete proposed unit appears once in the intended receiving body; all unrelated bytes, claim levels and frozen sources remain exact. Check source/receiver meanings, route targets and incoming anchors, then public readback and the owning review/queue receipt.


#### Unit 9 — Promote the two-clock and human-output clarifications into 04

**Source:** `research/ecosystem-awareness/baseline/04_GENERAL_FUNCTIONAL_INTERFACES_AGENTIC_SECURITY_v0.5_INTEGRATED.md` · current blob `30e492c671efed802f7b881ed67e9f4dcd4bb079` · line 1869, bytes 92745–92852 at the pinned source cut. **Expected impact:** High; **risk:** Medium; **effort:** Medium.

**Why:** Expose the useful generic handoff guidance in the programme-independent current reader while preserving frozen predecessors.

**Dependencies and decision:** Named wave GO and current source/receiver validation

**Material selected from VNext:**

- `research/ecosystem-awareness/baseline/04_GENERAL_FUNCTIONAL_INTERFACES_AGENTIC_SECURITY_VNEXT_REVIEW_AND_DELTA_v0.1_DRAFT.md` — 6. Semantic/qualification validity window versus response window
- `research/ecosystem-awareness/baseline/04_GENERAL_FUNCTIONAL_INTERFACES_AGENTIC_SECURITY_VNEXT_REVIEW_AND_DELTA_v0.1_DRAFT.md` — 7. Human-review outputs under the general handoff discipline

**Texto antes — complete current unit**

````````````text
The controlled/repaired v0.4 source blobs remain preserved separately for historical/freeze reconstruction.
````````````

**Texto después — complete proposed unit**

````````````text
The controlled/repaired v0.4 source blobs remain preserved separately for historical/freeze reconstruction.

## Qualified timing and human-review handoff — maintained reading

**Two clocks.** A qualification validity window states when its evidence, authority, policy, configuration and assumptions remain applicable. A response window states when an intervention can still affect the outcome. Preserve both when material; a valid result may arrive too late to help, and remaining response time does not make a stale result applicable. An epistemic decision to continue, stop, redirect or corroborate is distinct from permission for operational intervention.

**Human-produced results.** IF-S6/EHD reading keeps the review decision/result, assurance in the received review event, capacity qualification and inherited residual distinct. Authentication or an authorized actor does not erase those evidence questions. Use the lightest categorical or structured qualifiers that preserve the material distinction; assurance in a particular review event is not a general score of a person's competence. This clarification adds no mandatory EHD-kernel field.
````````````

**Acceptance:** exact source-region match and inverse; complete proposed unit appears once in the intended receiving body; all unrelated bytes, claim levels and frozen sources remain exact. Check source/receiver meanings, route targets and incoming anchors, then public readback and the owning review/queue receipt.


#### Unit 10 — Promote the dated UC-6/H1 evidence distinctions into 05A

**Source:** `research/ecosystem-awareness/fg-tida/interfaces/05A_FG_TIDA_CURRENT_STATE_CONFORMANCE_BRIDGE_v0.1.md` · current blob `71abf26cd885d8567ca7d87dfcb4e44a2a5709d5` · line 165, bytes 22664–23014 at the pinned source cut. **Expected impact:** High; **risk:** Medium; **effort:** Medium.

**Why:** Make the supported contributor-source status available in the maintained bridge, with reported reference, prospective protocol and unresolved applicability evidence separated.

**Dependencies and decision:** Named wave GO and current source/receiver validation

**Material selected from VNext:**

- `research/ecosystem-awareness/fg-tida/interfaces/05A_FG_TIDA_CURRENT_STATE_CONFORMANCE_BRIDGE_VNEXT_REVIEW_AND_DELTA_v0.1_DRAFT.md` — 2.15 Theme #13 — UC-6 Stage-0 and H1 receiver evidence (21 October 2026)

**Texto antes — complete current unit**

````````````text
This is less than the ideal 05 contract, but it is the most complete profile currently supportable without claiming FG-TIDA adoption, inventing absent fields or converting a testbed into a control plane. It preserves a clear path from public discussion to reviewed adapters, fixtures and conformance evidence while keeping later extension reversible.
````````````

**Texto después — complete proposed unit**

````````````text
This is less than the ideal 05 contract, but it is the most complete profile currently supportable without claiming FG-TIDA adoption, inventing absent fields or converting a testbed into a control plane. It preserves a clear path from public discussion to reviewed adapters, fixtures and conformance evidence while keeping later extension reversible.

## Source-state reception — 21 October 2026

This later reception preserves the 19 September bridge as its dated source snapshot. It adds three qualified reading points from the public source record reviewed on 21 October, without changing the ideal 05 contracts.

**UC-6 Stage-0 reference.** [Nelson's UC6_Stage0_Theme13_v0.4.1-r1 report](https://github.com/FG-TIDA/themes/issues/13#issuecomment-5949120841) describes reference assertions, deliberately corrupted applicability controls and offline replay. Its demonstrated claim remains that bounded reference/mapping work; authority calculation, measured response-window performance and executed cross-organizational intervention are separate investigations.

**H1 prospective handoff.** The [H1 protocol proposal](https://github.com/FG-TIDA/themes/issues/13#issuecomment-6188764689) specifies four prospective cases: an unchanged applicable finding; material amendment before action; an irrelevant change that preserves legitimate work; and acknowledgement without independent effect readback. These are proposed observations for a future mapped investigation. Preserve source meaning, local authority, decision, acknowledgement, attempted action, effect and recovery as separate records.

**Identity and current applicability.** The [proposed receiver-visible record fields](https://github.com/FG-TIDA/themes/issues/13#issuecomment-6271168964) and [author's executable-diagnostic report](https://github.com/FG-TIDA/themes/issues/13#issuecomment-6279011475) are candidate record/test material. Matching dispatch and receiver-used digests can support identity at those declared observation points. Latest decision-applicable state at action time additionally needs a source-state/freshness witness covering relevant changes, or a bounded NOT_ESTABLISHED qualification. The contributor-reported field/token checks do not establish that stronger proposition.
````````````

**Acceptance:** exact source-region match and inverse; complete proposed unit appears once in the intended receiving body; all unrelated bytes, claim levels and frozen sources remain exact. Check source/receiver meanings, route targets and incoming anchors, then public readback and the owning review/queue receipt.


#### Unit 11 — Requirements current-canon promotion — identity unit 1

**Source:** `research/ecosystem-awareness/baseline/00_REQUIREMENTS_WORKING_SUCCESSOR_2026-10-12.md` · current blob `c0226a1ba9a45976ad0c887dd9afb97b103e6c37` · line 1, bytes 0–642 at the pinned source cut. **Expected impact:** High; **risk:** High; **effort:** Medium.

**Why:** Complete the canonical-role decision for the existing successor rather than leave accepted content in another perpetual working edition. Preserve the frozen predecessor and test-version meanings.

**Dependencies and decision:** Accept all five identity units together with the selected Requirements content pair, reconcile the manifest/index/consumer roles and seed registry, and name this canonical-role promotion explicitly in Iván’s GO. Revalidate the complete source status after incorporation.

**Texto antes — complete current unit**

````````````text
> **Owner-approved working successor · 12 October 2026.** This edition implements the approved #16 changes. The [frozen predecessor](./00_CANONICAL_REQUIREMENTS_CHALLENGES_SUFFICIENCY_HYPOTHESES_KPIS.md) remains unchanged at commit `77fc61447d3f278072d13f566bbedd7ccfe245d3`, blob `4fe3d69b50fef1e82ba7f889324b70a7f6b1a81c`. Its identification and freeze statements retained below describe that predecessor. This successor is the working text for the approved changes, not a replacement of a frozen test contract or its results. [The existing sole review workspace](./00_REQUIREMENTS_VNEXT_REVIEW_AND_DELTA_v0.1_DRAFT.md) owns both editions.
````````````

**Texto después — complete proposed unit**

````````````text
> **Current maintained canonical Requirements reading edition.** This existing successor carries the owner-approved S10 action-time binding and the separately accepted interpretive clarifications below. The [17 September frozen predecessor](./00_CANONICAL_REQUIREMENTS_CHALLENGES_SUFFICIENCY_HYPOTHESES_KPIS.md) remains exact and controls studies that identify that frozen edition; this maintained reading does not retrospectively alter their test contracts or results. The [single Requirements review](./00_REQUIREMENTS_VNEXT_REVIEW_AND_DELTA_v0.1_DRAFT.md) owns both editions, further proposals and promotion receipts.
````````````

**Acceptance:** exact source-region match and inverse; complete proposed unit appears once in the intended receiving body; all unrelated bytes, claim levels and frozen sources remain exact. Check source/receiver meanings, route targets and incoming anchors, then public readback and the owning review/queue receipt.


#### Unit 12 — Requirements current-canon promotion — identity unit 2

**Source:** `research/ecosystem-awareness/baseline/00_REQUIREMENTS_WORKING_SUCCESSOR_2026-10-12.md` · current blob `c0226a1ba9a45976ad0c887dd9afb97b103e6c37` · line 9, bytes 865–992 at the pinned source cut. **Expected impact:** High; **risk:** High; **effort:** Medium.

**Why:** Complete the canonical-role decision for the existing successor rather than leave accepted content in another perpetual working edition. Preserve the frozen predecessor and test-version meanings.

**Dependencies and decision:** Accept all five identity units together with the selected Requirements content pair, reconcile the manifest/index/consumer roles and seed registry, and name this canonical-role promotion explicitly in Iván’s GO. Revalidate the complete source status after incorporation.

**Texto antes — complete current unit**

````````````text
| **Status** | **Frozen canonical baseline** · requirements/test protocol · not evidence that EA satisfies the requirements |
````````````

**Texto después — complete proposed unit**

````````````text
| **Status** | **Maintained canonical reading edition** · requirements/test-protocol interpretation · source-specific frozen study contracts retained |
````````````

**Acceptance:** exact source-region match and inverse; complete proposed unit appears once in the intended receiving body; all unrelated bytes, claim levels and frozen sources remain exact. Check source/receiver meanings, route targets and incoming anchors, then public readback and the owning review/queue receipt.


#### Unit 13 — Requirements current-canon promotion — identity unit 3

**Source:** `research/ecosystem-awareness/baseline/00_REQUIREMENTS_WORKING_SUCCESSOR_2026-10-12.md` · current blob `c0226a1ba9a45976ad0c887dd9afb97b103e6c37` · line 10, bytes 993–1048 at the pinned source cut. **Expected impact:** High; **risk:** High; **effort:** Medium.

**Why:** Complete the canonical-role decision for the existing successor rather than leave accepted content in another perpetual working edition. Preserve the frozen predecessor and test-version meanings.

**Dependencies and decision:** Accept all five identity units together with the selected Requirements content pair, reconcile the manifest/index/consumer roles and seed registry, and name this canonical-role promotion explicitly in Iván’s GO. Revalidate the complete source status after incorporation.

**Texto antes — complete current unit**

````````````text
| **Version · date** | Freeze snapshot · 2026-09-17 |
````````````

**Texto después — complete proposed unit**

````````````text
| **Version · date** | Maintained reading edition 1 · lineage: 12 October 2026 working successor; frozen reference: 17 September 2026 |
````````````

**Acceptance:** exact source-region match and inverse; complete proposed unit appears once in the intended receiving body; all unrelated bytes, claim levels and frozen sources remain exact. Check source/receiver meanings, route targets and incoming anchors, then public readback and the owning review/queue receipt.


#### Unit 14 — Requirements current-canon promotion — identity unit 4

**Source:** `research/ecosystem-awareness/baseline/00_REQUIREMENTS_WORKING_SUCCESSOR_2026-10-12.md` · current blob `c0226a1ba9a45976ad0c887dd9afb97b103e6c37` · line 12, bytes 1092–1293 at the pinned source cut. **Expected impact:** High; **risk:** High; **effort:** Medium.

**Why:** Complete the canonical-role decision for the existing successor rather than leave accepted content in another perpetual working edition. Preserve the frozen predecessor and test-version meanings.

**Dependencies and decision:** Accept all five identity units together with the selected Requirements content pair, reconcile the manifest/index/consumer roles and seed registry, and name this canonical-role promotion explicitly in Iván’s GO. Revalidate the complete source status after incorporation.

**Texto antes — complete current unit**

````````````text
| **Supersedes / superseded by** | Current frozen canonical Requirements baseline; earlier 00A/00C inputs preserved separately; no successor promoted — review changes through the linked vNext delta |
````````````

**Texto después — complete proposed unit**

````````````text
| **Supersedes / superseded by** | Current maintained Requirements reading; the frozen predecessor remains the controlling contract for studies citing it. Earlier 00A/00C inputs and all previous editions retain their provenance. |
````````````

**Acceptance:** exact source-region match and inverse; complete proposed unit appears once in the intended receiving body; all unrelated bytes, claim levels and frozen sources remain exact. Check source/receiver meanings, route targets and incoming anchors, then public readback and the owning review/queue receipt.


#### Unit 15 — Requirements current-canon promotion — identity unit 5

**Source:** `research/ecosystem-awareness/baseline/00_REQUIREMENTS_WORKING_SUCCESSOR_2026-10-12.md` · current blob `c0226a1ba9a45976ad0c887dd9afb97b103e6c37` · line 14, bytes 1295–1889 at the pinned source cut. **Expected impact:** High; **risk:** High; **effort:** Medium.

**Why:** Complete the canonical-role decision for the existing successor rather than leave accepted content in another perpetual working edition. Preserve the frozen predecessor and test-version meanings.

**Dependencies and decision:** Accept all five identity units together with the selected Requirements content pair, reconcile the manifest/index/consumer roles and seed registry, and name this canonical-role promotion explicitly in Iván’s GO. Revalidate the complete source status after incorporation.

**Texto antes — complete current unit**

````````````text
> **Frozen canonical requirements baseline.** This is the single canonical document that states what a solution to the EA problem must address and how its underlying hypotheses are assessed. Its S1–S14 / T1–T4 / H1–H6 / KPI semantics are frozen at this baseline while vNext review is open. Proposed semantic changes are reviewed in the linked delta before any later explicit versioned promotion; editorial routing/link updates do not alter this freeze. It does not define a product, implementation, benchmark result, standards adoption, or a claim that EA or another candidate has passed.
````````````

**Texto después — complete proposed unit**

````````````text
> **Version-specific Requirements reading.** The current maintained edition states the accepted reading of the EA requirements and their S1–S14 / T1–T4 / H1–H6 / KPI framework. The identified frozen predecessor remains its historical test contract; compare a study against the exact edition it cites. Later semantic changes require explicit source-owned review and versioned acceptance. Canonical status identifies the primary reading source, not product efficacy, comparative superiority, standards adoption or a completed test result.
````````````

**Acceptance:** exact source-region match and inverse; complete proposed unit appears once in the intended receiving body; all unrelated bytes, claim levels and frozen sources remain exact. Check source/receiver meanings, route targets and incoming anchors, then public readback and the owning review/queue receipt.


#### Unit 16 — Receive the Requirements canon promotion in the technical index

**Source:** `research/ecosystem-awareness/baseline/README.md` · current blob `8cb270ecd4ee4eb87356fa3b6550a0ec582ba791` · line 367, bytes 78921–79417 at the pinned source cut. **Expected impact:** High; **risk:** Medium; **effort:** Medium.

**Why:** Make the primary reader acknowledge the accepted edition while keeping UC-EA-03 a distinct working successor and registered studies on their identified contracts.

**Dependencies and decision:** Requirements identity/content packet accepted; preserve the frozen index row and align the register current path.

**Texto antes — complete current unit**

````````````text
The [Requirements working successor](./00_REQUIREMENTS_WORKING_SUCCESSOR_2026-10-12.md) adds the approved action-time decision-basis binding to S10. The [UC-EA-03 v0.5 working successor](./UC-EA-03_v0.5_WORKING_SUCCESSOR.md) clarifies the response owner and bounded fallback when a reviewer is unavailable. Their frozen predecessors remain linked and unchanged; an existing registered study continues to use its own frozen contract. The existing Requirements and UC-EA-03 VNext own both editions.
````````````

**Texto después — complete proposed unit**

````````````text
The [current maintained canonical Requirements reading](./00_REQUIREMENTS_WORKING_SUCCESSOR_2026-10-12.md) contains the approved S10 action-time binding and the accepted effective-role, opportunity/authority and composed-effect reading clarifications. The [UC-EA-03 v0.5 working successor](./UC-EA-03_v0.5_WORKING_SUCCESSOR.md) clarifies the response owner and bounded fallback when a reviewer is unavailable. The Requirements maintained-reading promotion and the UC-EA-03 working-successor status are distinct. Their frozen predecessors remain linked and unchanged; an existing registered study continues to use its own frozen contract. The existing Requirements and UC-EA-03 VNext own both editions.
````````````

**Acceptance:** exact source-region match and inverse; complete proposed unit appears once in the intended receiving body; all unrelated bytes, claim levels and frozen sources remain exact. Check source/receiver meanings, route targets and incoming anchors, then public readback and the owning review/queue receipt.


#### Unit 17 — Receive the Requirements role promotion in its domain manifest

**Source:** `research/ecosystem-awareness/baseline/CANONICAL_CORPUS_MANIFEST.md` · current blob `db54700c6a1b2b81beff84e2eac1727dd28aea61` · line 262, bytes 59167–59461 at the pinned source cut. **Expected impact:** High; **risk:** Medium; **effort:** Medium.

**Why:** Keep the maintained public-reading role, historical test contracts and controlled Drive freeze authority legible together.

**Dependencies and decision:** Named wave GO and current source/receiver validation

**Texto antes — complete current unit**

````````````text
This corpus is public research / pre-standardization material. It is not an ITU-T deliverable, adopted FG-TIDA architecture, NIST submission, product certification, or proof of novelty/superiority. Public FG-TIDA references document contributor-level provenance and third-party discussion only.
````````````

**Texto después — complete proposed unit**

````````````text
This corpus is public research / pre-standardization material. It is not an ITU-T deliverable, adopted FG-TIDA architecture, NIST submission, product certification, or proof of novelty/superiority. Public FG-TIDA references document contributor-level provenance and third-party discussion only.

## Maintained Requirements reading and frozen study contracts

The [existing 12 October Requirements successor](./00_REQUIREMENTS_WORKING_SUCCESSOR_2026-10-12.md) is the maintained canonical public reading after its accepted identity/content promotion. It carries S10 action-time binding and the accepted effective-role, opportunity/authority and composed-effect clarifications. The [17 September frozen Requirements](./00_CANONICAL_REQUIREMENTS_CHALLENGES_SUFFICIENCY_HYPOTHESES_KPIS.md) remains the contract for studies that cite that exact edition. Update the operational registry's current path to the maintained edition only with the named promotion decision; retain the frozen predecessor/parts and all source-specific test versions.

The controlled Google Drive revision anchors above continue to identify their own frozen editions. This public reading adoption does not certify a new equality between a later public reader and those controlled freeze records.
````````````

**Acceptance:** exact source-region match and inverse; complete proposed unit appears once in the intended receiving body; all unrelated bytes, claim levels and frozen sources remain exact. Check source/receiver meanings, route targets and incoming anchors, then public readback and the owning review/queue receipt.


#### Unit 18 — Route ecosystem-positioning readers through maintained sources

**Source:** `architectural-contributions/ecosystem-positioning/README.md` · current blob `9bd2c1d10a8d440fa947abb7bc834d99ec97ff9b` · line 132, bytes 13381–14399 at the pinned source cut. **Expected impact:** High; **risk:** Medium; **effort:** Medium.

**Why:** Replace a confirmed direct foreign-review edge with the intended canonical reading while retaining old proposals through their owning sources. Benchmarkv0.3 is treated by its declared role, not its filename.

**Dependencies and decision:** Apply the corresponding accepted content pair first where it supplies a new section; preserve proposal access through the canonical source’s own companion. Iván names this routing wave. EP is append-only: its exact label/href replacement requires an expressly named owner exception; absent that decision, defer this pair rather than claim an append fixed the old edge.

**Texto antes — complete current unit**

````````````text
[Requirements & Evidence PPTX](../../presentations/ecosystem-positioning/Ecosystem_Positioning_Requirements_Evidence_Canonical_v1.2.pptx) ·
[Architecture & Implementation PPTX](../../presentations/ecosystem-positioning/Ecosystem_Positioning_Architecture_Implementation_Canonical_v1.2.pptx) ·
[Visual Guide](../../research/ecosystem-awareness/VISUAL_GUIDE.md) ·
[Presentation manifest](../../presentations/ecosystem-positioning/PRESENTATION_MANIFEST.md) ·
[Canonical Requirements](../../research/ecosystem-awareness/baseline/00_CANONICAL_REQUIREMENTS_CHALLENGES_SUFFICIENCY_HYPOTHESES_KPIS.md) ·
[Canonical Benchmark v0.2](../../research/ecosystem-awareness/baseline/00D_CANONICAL_ARCHITECTURE_BENCHMARK_AND_REFERENCE_SCENARIO_EVIDENCE_v0.2.md) ·
[Benchmark vNext v0.3](../../research/ecosystem-awareness/baseline/00D_CANONICAL_ARCHITECTURE_BENCHMARK_v0.3_DRAFT_ECOSYSTEM_POSITIONING.md) ·
[Applied validation / evidence-maturity challenge](../../research/ecosystem-awareness/DECISION_BOUNDARY_CHALLENGE_v0.2.md)
````````````

**Texto después — complete proposed unit**

````````````text
[Requirements & Evidence PPTX](../../presentations/ecosystem-positioning/Ecosystem_Positioning_Requirements_Evidence_Canonical_v1.2.pptx) ·
[Architecture & Implementation PPTX](../../presentations/ecosystem-positioning/Ecosystem_Positioning_Architecture_Implementation_Canonical_v1.2.pptx) ·
[Visual Guide](../../research/ecosystem-awareness/VISUAL_GUIDE.md) ·
[Presentation manifest](../../presentations/ecosystem-positioning/PRESENTATION_MANIFEST.md) ·
[Canonical Requirements](../../research/ecosystem-awareness/baseline/00_CANONICAL_REQUIREMENTS_CHALLENGES_SUFFICIENCY_HYPOTHESES_KPIS.md) ·
[Canonical Benchmark v0.2](../../research/ecosystem-awareness/baseline/00D_CANONICAL_ARCHITECTURE_BENCHMARK_AND_REFERENCE_SCENARIO_EVIDENCE_v0.2.md) ·
[00D current benchmark and development route](../../research/ecosystem-awareness/baseline/00D_CANONICAL_ARCHITECTURE_BENCHMARK_AND_REFERENCE_SCENARIO_EVIDENCE_v0.2.md) ·
[Applied validation / evidence-maturity challenge](../../research/ecosystem-awareness/DECISION_BOUNDARY_CHALLENGE_v0.2.md)
````````````

**Enlace antes / enlace después:**

- Before: `../../research/ecosystem-awareness/baseline/00D_CANONICAL_ARCHITECTURE_BENCHMARK_v0.3_DRAFT_ECOSYSTEM_POSITIONING.md`
- After: `../../research/ecosystem-awareness/baseline/00D_CANONICAL_ARCHITECTURE_BENCHMARK_AND_REFERENCE_SCENARIO_EVIDENCE_v0.2.md`

**Acceptance:** exact source-region match and inverse; complete proposed unit appears once in the intended receiving body; all unrelated bytes, claim levels and frozen sources remain exact. Check source/receiver meanings, route targets and incoming anchors, then public readback and the owning review/queue receipt.


#### Unit 19 — Route ecosystem-positioning readers through maintained sources

**Source:** `architectural-contributions/ecosystem-positioning/README.md` · current blob `9bd2c1d10a8d440fa947abb7bc834d99ec97ff9b` · line 492, bytes 50159–50559 at the pinned source cut. **Expected impact:** High; **risk:** Medium; **effort:** Medium.

**Why:** Replace a confirmed direct foreign-review edge with the intended canonical reading while retaining old proposals through their owning sources. Benchmarkv0.3 is treated by its declared role, not its filename.

**Dependencies and decision:** Apply the corresponding accepted content pair first where it supplies a new section; preserve proposal access through the canonical source’s own companion. Iván names this routing wave. The Requirements route also depends on the five identity units and accepted manifest/index/registry reception; it must not appoint an unadopted working source as the current canon. EP is append-only: its exact label/href replacement requires an expressly named owner exception; absent that decision, defer this pair rather than claim an append fixed the old edge.

**Texto antes — complete current unit**

````````````text
[Requirements-vNext review](../../research/ecosystem-awareness/baseline/00_REQUIREMENTS_VNEXT_REVIEW_AND_DELTA_v0.1_DRAFT.md) checks whether later Ecosystem Positioning mechanisms require a new requirements version. The current bounded review finds that the later mechanisms can still be mapped to the existing requirements, with clarification candidates rather than an automatic S15/T5/H7 expansion.
````````````

**Texto después — complete proposed unit**

````````````text
[Requirements working source and clarifications](../../research/ecosystem-awareness/baseline/00_REQUIREMENTS_WORKING_SUCCESSOR_2026-10-12.md) checks whether later Ecosystem Positioning mechanisms require a new requirements version. The current bounded review finds that the later mechanisms can still be mapped to the existing requirements, with clarification candidates rather than an automatic S15/T5/H7 expansion.
````````````

**Enlace antes / enlace después:**

- Before: `../../research/ecosystem-awareness/baseline/00_REQUIREMENTS_VNEXT_REVIEW_AND_DELTA_v0.1_DRAFT.md`
- After: `../../research/ecosystem-awareness/baseline/00_REQUIREMENTS_WORKING_SUCCESSOR_2026-10-12.md`

**Acceptance:** exact source-region match and inverse; complete proposed unit appears once in the intended receiving body; all unrelated bytes, claim levels and frozen sources remain exact. Check source/receiver meanings, route targets and incoming anchors, then public readback and the owning review/queue receipt.


#### Unit 20 — Route ecosystem-positioning readers through maintained sources

**Source:** `architectural-contributions/ecosystem-positioning/README.md` · current blob `9bd2c1d10a8d440fa947abb7bc834d99ec97ff9b` · line 816, bytes 83477–83964 at the pinned source cut. **Expected impact:** High; **risk:** Medium; **effort:** Medium.

**Why:** Replace a confirmed direct foreign-review edge with the intended canonical reading while retaining old proposals through their owning sources. Benchmarkv0.3 is treated by its declared role, not its filename.

**Dependencies and decision:** Apply the corresponding accepted content pair first where it supplies a new section; preserve proposal access through the canonical source’s own companion. Iván names this routing wave. EP is append-only: its exact label/href replacement requires an expressly named owner exception; absent that decision, defer this pair rather than claim an append fixed the old edge.

**Texto antes — complete current unit**

````````````text
[**00D v0.3 Draft — Ecosystem Positioning Benchmark vNext**](../../research/ecosystem-awareness/baseline/00D_CANONICAL_ARCHITECTURE_BENCHMARK_v0.3_DRAFT_ECOSYSTEM_POSITIONING.md) extends the design from EA alone to the complete composition: signalling, Cartography, Regime Awareness, MSCA, effective-role drift, Gradient, ACC/authority and repositioning. It introduces module attribution, later positioning branches, choreography/partition tests and complexity/accountability measures.
````````````

**Texto después — complete proposed unit**

````````````text
[00D current benchmark and development route](../../research/ecosystem-awareness/baseline/00D_CANONICAL_ARCHITECTURE_BENCHMARK_AND_REFERENCE_SCENARIO_EVIDENCE_v0.2.md) extends the design from EA alone to the complete composition: signalling, Cartography, Regime Awareness, MSCA, effective-role drift, Gradient, ACC/authority and repositioning. It introduces module attribution, later positioning branches, choreography/partition tests and complexity/accountability measures.
````````````

**Enlace antes / enlace después:**

- Before: `../../research/ecosystem-awareness/baseline/00D_CANONICAL_ARCHITECTURE_BENCHMARK_v0.3_DRAFT_ECOSYSTEM_POSITIONING.md`
- After: `../../research/ecosystem-awareness/baseline/00D_CANONICAL_ARCHITECTURE_BENCHMARK_AND_REFERENCE_SCENARIO_EVIDENCE_v0.2.md`

**Acceptance:** exact source-region match and inverse; complete proposed unit appears once in the intended receiving body; all unrelated bytes, claim levels and frozen sources remain exact. Check source/receiver meanings, route targets and incoming anchors, then public readback and the owning review/queue receipt.


#### Unit 21 — Route ecosystem-awareness readers through maintained sources

**Source:** `research/ecosystem-awareness/README.md` · current blob `3ff5c26946b25608cea5cc1c9df8519dc61e1afd` · line 92, bytes 18339–18689 at the pinned source cut. **Expected impact:** High; **risk:** Medium; **effort:** Medium.

**Why:** Replace a confirmed direct foreign-review edge with the intended canonical reading while retaining old proposals through their owning sources. Benchmarkv0.3 is treated by its declared role, not its filename.

**Dependencies and decision:** Apply the corresponding accepted content pair first where it supplies a new section; preserve proposal access through the canonical source’s own companion. Iván names this routing wave. First resolve EA’s recorded-versus-observed protected-successor decision; no automatic SHA acceptance.

**Texto antes — complete current unit**

````````````text
**Benchmark vNext:** the bounded [00D v0.3 Ecosystem Positioning draft](./baseline/00D_CANONICAL_ARCHITECTURE_BENCHMARK_v0.3_DRAFT_ECOSYSTEM_POSITIONING.md) extends the design toward the later positioning architecture but does **not** supersede v0.2. v0.2 remains the current canonical benchmark for EA-H1–EA-H4 until the v0.3 adoption gates close.
````````````

**Texto después — complete proposed unit**

````````````text
**Benchmark vNext:** the bounded [00D current benchmark and development route](baseline/00D_CANONICAL_ARCHITECTURE_BENCHMARK_AND_REFERENCE_SCENARIO_EVIDENCE_v0.2.md) extends the design toward the later positioning architecture but does **not** supersede v0.2. v0.2 remains the current canonical benchmark for EA-H1–EA-H4 until the v0.3 adoption gates close.
````````````

**Enlace antes / enlace después:**

- Before: `./baseline/00D_CANONICAL_ARCHITECTURE_BENCHMARK_v0.3_DRAFT_ECOSYSTEM_POSITIONING.md`
- After: `baseline/00D_CANONICAL_ARCHITECTURE_BENCHMARK_AND_REFERENCE_SCENARIO_EVIDENCE_v0.2.md`

**Acceptance:** exact source-region match and inverse; complete proposed unit appears once in the intended receiving body; all unrelated bytes, claim levels and frozen sources remain exact. Check source/receiver meanings, route targets and incoming anchors, then public readback and the owning review/queue receipt.


#### Unit 22 — Route ecosystem-awareness readers through maintained sources

**Source:** `research/ecosystem-awareness/README.md` · current blob `3ff5c26946b25608cea5cc1c9df8519dc61e1afd` · line 276, bytes 49719–52212 at the pinned source cut. **Expected impact:** High; **risk:** Medium; **effort:** Medium.

**Why:** Replace a confirmed direct foreign-review edge with the intended canonical reading while retaining old proposals through their owning sources. Benchmarkv0.3 is treated by its declared role, not its filename.

**Dependencies and decision:** Apply the corresponding accepted content pair first where it supplies a new section; preserve proposal access through the canonical source’s own companion. Iván names this routing wave. First resolve EA’s recorded-versus-observed protected-successor decision; no automatic SHA acceptance.

**Texto antes — complete current unit**

````````````text
- **Five minutes:** this page → [100 Million Tokens](./baseline/00E_FAILURE_MODES_100M_TOKEN_COMPOUNDING_v0.1.md) → [Mobility Chaos — The City That Stopped Safely](./baseline/00F_FAILURE_MODE_SMART_CITY_MOBILITY_SYSTEMIC_DIVERGENCE_v0.2_FREEZE_EDITION.md) → [00I Freeze Edition — The Patch That Undid the Fix](./baseline/00I_FAILURE_MODE_SEMANTIC_TOCTOU_v0.5_FREEZE_EDITION.md) → [benchmark status](./baseline/00D_CANONICAL_ARCHITECTURE_BENCHMARK_AND_REFERENCE_SCENARIO_EVIDENCE_v0.2.md).
- **Architecture:** [canonical EA corpus](./baseline/README.md) → topology → documents 01–04 → 01H/01I/01J → interface annexes.
- **Validation:** benchmark → A01/A03 → validation profiles → fixture/pre-registration → [published Stage-0 traces](./baseline/fixtures/RS-00E-Q1a/EXECUTION_RECORD_v0.5.md) and [00L records](./baseline/00L_REINFORCED_PAPER_TRAVERSALS_00E_00J_v0.1/README.md) → independent comparison and replication.
- **UC-21 / S5 source-to-evidence route:** start with the [UC-21 case](https://github.com/dakleyer/use-cases/blob/aec08fb5b0fac2ee399372370e9ee2a82a2d5779/contributions/when-controls-work-system-fails/USE_CASE.md), then the [S5 scenario](https://github.com/dakleyer/use-cases/blob/aec08fb5b0fac2ee399372370e9ee2a82a2d5779/contributions/when-controls-work-system-fails/annexes/scenarios/S5.md) and [T08 AWS documentary profile](https://github.com/dakleyer/use-cases/blob/aec08fb5b0fac2ee399372370e9ee2a82a2d5779/contributions/when-controls-work-system-fails/annexes/technology/T08.md); the [00I-STATEFUL report](./baseline/fixtures/00I-STATEFUL/README.md) records separately executed local synthetic effects. [UC-4](https://github.com/FG-TIDA/use-cases/issues/4) owns the external testbed review/admission discussion.
- **Claim custody and review:** [limited claim source/consumer register](./DDS_CLAIM_SOURCE_CONSUMER_REGISTER_v0.1.md) tracks ten reader-facing claims, their source, observed consumers and update triggers; [EA README VNext](./README_VNext.md) retains editorial changes and [Stage A VNext](./DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1_VNext.md) retains diagnostic proposals. Source documents remain authoritative.
- **Institutional application:** [**current Theme #13 charter-preparation draft (01G)**](./fg-tida/charter/THEME_13_WORKING_GROUP_CHARTER_PREPARATION_DRAFT_v0.1.md) for the direct working document; use the broader [EA / FG-TIDA package](./fg-tida/README.md) for specifications/interfaces → cases/tests → provenance.
````````````

**Texto después — complete proposed unit**

````````````text
- **Five minutes:** this page → [100 Million Tokens](./baseline/00E_FAILURE_MODES_100M_TOKEN_COMPOUNDING_v0.1.md) → [Mobility Chaos — The City That Stopped Safely](./baseline/00F_FAILURE_MODE_SMART_CITY_MOBILITY_SYSTEMIC_DIVERGENCE_v0.2_FREEZE_EDITION.md) → [00I Freeze Edition — The Patch That Undid the Fix](./baseline/00I_FAILURE_MODE_SEMANTIC_TOCTOU_v0.5_FREEZE_EDITION.md) → [benchmark status](./baseline/00D_CANONICAL_ARCHITECTURE_BENCHMARK_AND_REFERENCE_SCENARIO_EVIDENCE_v0.2.md).
- **Architecture:** [canonical EA corpus](./baseline/README.md) → topology → documents 01–04 → 01H/01I/01J → interface annexes.
- **Validation:** benchmark → A01/A03 → validation profiles → fixture/pre-registration → [published Stage-0 traces](./baseline/fixtures/RS-00E-Q1a/EXECUTION_RECORD_v0.5.md) and [00L records](./baseline/00L_REINFORCED_PAPER_TRAVERSALS_00E_00J_v0.1/README.md) → independent comparison and replication.
- **UC-21 / S5 source-to-evidence route:** start with the [UC-21 case](https://github.com/dakleyer/use-cases/blob/aec08fb5b0fac2ee399372370e9ee2a82a2d5779/contributions/when-controls-work-system-fails/USE_CASE.md), then the [S5 scenario](https://github.com/dakleyer/use-cases/blob/aec08fb5b0fac2ee399372370e9ee2a82a2d5779/contributions/when-controls-work-system-fails/annexes/scenarios/S5.md) and [T08 AWS documentary profile](https://github.com/dakleyer/use-cases/blob/aec08fb5b0fac2ee399372370e9ee2a82a2d5779/contributions/when-controls-work-system-fails/annexes/technology/T08.md); the [00I-STATEFUL report](./baseline/fixtures/00I-STATEFUL/README.md) records separately executed local synthetic effects. [UC-4](https://github.com/FG-TIDA/use-cases/issues/4) owns the external testbed review/admission discussion.
- **Claim custody and review:** [limited claim source/consumer register](./DDS_CLAIM_SOURCE_CONSUMER_REGISTER_v0.1.md) tracks ten reader-facing claims, their source, observed consumers and update triggers; [EA README VNext](./README_VNext.md) retains editorial changes and [Stage A source](./DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1.md) retains diagnostic proposals. Source documents remain authoritative.
- **Institutional application:** [**current Theme #13 charter-preparation draft (01G)**](./fg-tida/charter/THEME_13_WORKING_GROUP_CHARTER_PREPARATION_DRAFT_v0.1.md) for the direct working document; use the broader [EA / FG-TIDA package](./fg-tida/README.md) for specifications/interfaces → cases/tests → provenance.
````````````

**Enlace antes / enlace después:**

- Before: `./DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1_VNext.md`
- After: `./DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1.md`

**Acceptance:** exact source-region match and inverse; complete proposed unit appears once in the intended receiving body; all unrelated bytes, claim levels and frozen sources remain exact. Check source/receiver meanings, route targets and incoming anchors, then public readback and the owning review/queue receipt.


#### Unit 23 — Route baseline readers through maintained sources

**Source:** `research/ecosystem-awareness/baseline/README.md` · current blob `8cb270ecd4ee4eb87356fa3b6550a0ec582ba791` · line 147, bytes 19587–29420 at the pinned source cut. **Expected impact:** High; **risk:** Medium; **effort:** Medium.

**Why:** Replace a confirmed direct foreign-review edge with the intended canonical reading while retaining old proposals through their owning sources. Benchmarkv0.3 is treated by its declared role, not its filename.

**Dependencies and decision:** Apply the corresponding accepted content pair first where it supplies a new section; preserve proposal access through the canonical source’s own companion. Iván names this routing wave. The Requirements route also depends on the five identity units and accepted manifest/index/registry reception; it must not appoint an unadopted working source as the current canon.

**Texto antes — complete current unit**

````````````text
| Step | Document / route | Question it answers | Status |
|---|---|---|---|
| **1** | [01 — Integrated Foundational Theory v0.5](./01_FOUNDATIONAL_THEORY_v0.5_INTEGRATED.md) | Why can a bounded representation not close an open, changing ecosystem? | **Integrated working successor** |
| **1** | [02 — Epistemic Safety Principles & Control Matrix v0.4](./02_EPISTEMIC_SAFETY_PRINCIPLES_CONTROL_MATRIX_v0.4.part01.md) | Which epistemic/control boundaries prevent bounded evidence from becoming an unjustified global conclusion? | **Controlled / frozen** source route |
| **2** | [00 — Canonical Requirements: S1–S14, Sufficiency Conditions, Hypotheses and KPIs](./00_CANONICAL_REQUIREMENTS_CHALLENGES_SUFFICIENCY_HYPOTHESES_KPIS.md) | What must a sufficiently good solution demonstrate, and how can it fail? | **Frozen canonical baseline**; post-freeze changes route through the linked Requirements delta |
| **2 — review** | [Requirements vNext Review & Delta v0.1 Draft](./00_REQUIREMENTS_VNEXT_REVIEW_AND_DELTA_v0.1_DRAFT.md) | Do later EP developments require new S/T/H/KPI, or do they map to the existing requirement system? | **Working review only**; current determination: no canonical requirement change |
| **2 — ablation** | [00K — Six-Principle Sufficiency & Adversarial Ablation Test v0.1 Draft](./00K_SIX_PRINCIPLE_REQUIREMENTS_MAPPING_AND_ABLATION_TEST_v0.1_DRAFT.md) · [A01 preserved reviewed design](./00K_A01_REVIEWED_PRE_PRINCIPLE_FIRST_DESIGN_ADDENDUM_v0.1.md) · [A02 coverage matrix](./00K_A02_REQUIREMENTS_COVERAGE_MATRIX_ADDENDUM_v0.1.md) · [A03 P4 paper execution](./00K_A03_P4_00H_PAPER_ABLATION_EXECUTION_v0.1.md) · [A4 runnable P4 harness](./fixtures/00K-A4-P4-00H/README.md) · [A15 complete six-principle testbook](./00K_A15_COMPLETE_SIX_PRINCIPLE_ABLATION_TESTBOOK_v0.1.md) · [02A foundation→principles proof](./02A_FOUNDATION_TO_OPERATIONAL_PRINCIPLE_DERIVATION_PROOF_v0.1.md) · [A19 principle↔requirement proof](./00K_A19_PRINCIPLE_REQUIREMENT_TRACEABILITY_AND_CONSERVATION_PROOF_v0.1.md) · [A16 corpus-grounded independence](./00K_A16_FORMAL_RELATIVE_INDEPENDENCE_PROOF_P1_P6_v0.1.md) · [A20 shared-substrate independence](./00K_A20_SHARED_SUBSTRATE_MATHEMATICAL_INDEPENDENCE_P1_P6_v0.1.md) · [A17 documentation map](./00K_A17_DOCUMENTATION_REPRODUCIBILITY_AND_PROOF_MAP_v0.1.md) | Can the six principles survive a strongest-repair leave-one-out test, with S1–S14 used as observable traceability rather than causal proof? | **Executable symbolic milestone**; first-pass harnesses now exist for all six principles: P1 corrected matched-semantic 42/42, P2 matched-prefix strongest-repair 58/58, P3 corrected matched-conflict 49/49, P4 minimal-authority audit 76/76, P5 exhaustive material-basis 47/47, P6 transitive-dependency 74/74 — **346 passing core symbolic regression tests** in total. The original A1 pair, original HOLD-marked P3 base pair and naive 00G P6 pair are preserved as falsified/insufficient isolations with concrete shortcuts; P4 additionally yields a refinement result: full receiver-side delegation history is not necessary in 00H, but a current decision-sufficient non-amplifying authority basis remains necessary in the tested surface. Supplemental packages bring the registered campaign to **379 tests**; GitHub Actions [run 36108965548](https://github.com/dakleyer/structural-awareness-contributions/actions/runs/36108965548) records an earlier reproduction at **379/379** across all 10 jobs; the corrected revision also passes [run 36196286646](https://github.com/dakleyer/structural-awareness-contributions/actions/runs/36196286646); live product/runtime validation remains pending |
| **3–4** | [00E — 100 Million Tokens](./00E_FAILURE_MODES_100M_TOKEN_COMPOUNDING_v0.1.md) · [00F — Smart-City Mobility Divergence v0.2](./00F_FAILURE_MODE_SMART_CITY_MOBILITY_SYSTEMIC_DIVERGENCE_v0.2_DRAFT.md) · [Freeze Edition](./00F_FAILURE_MODE_SMART_CITY_MOBILITY_SYSTEMIC_DIVERGENCE_v0.2_FREEZE_EDITION.md) | Where can locally plausible systems fail under compounding context loss or distributed divergence? | **Canonical working** reference scenarios; not executed benchmark results |
| **5** | [00G — Collective False-Context Convergence](./00G_FAILURE_MODE_COLLECTIVE_FALSE_CONTEXT_CONVERGENCE_v0.4.md) | How can correlated narrative/signalling produce false contextual convergence and authority confusion while still permitting genuine regime change? | **Canonical working v0.4**; integrated scenario + quality plan + OpenAI implementation trajectories; unexecuted; 00D/W3 execution pending |
| **5** | [00H — Batch Opportunity Beyond Authority](./00H_FAILURE_MODE_BATCH_OPPORTUNITY_BEYOND_AUTHORITY_v0.2_DRAFT.md) | How can a materially valid opportunity exceed the acting participant’s current authority, and how must it be preserved/re-contracted without unauthorized execution? | **Additive annex / candidate scenario**; executable admission pending |
| **5** | [00I — Semantic TOCTOU / The Patch That Undid the Fix](./00I_FAILURE_MODE_SEMANTIC_TOCTOU_v0.5_DRAFT.md) · [Freeze Edition](./00I_FAILURE_MODE_SEMANTIC_TOCTOU_v0.5_FREEZE_EDITION.md) | How can a correctly qualified queued action become wrong before use while its token/job/API remain technically valid, and which quality gates must force current-state requalification? | **Additive annex / candidate scenario**; Q0–Q6 + OOTB/top-notch/frozen-top-notch-under-drift quality plan; zero-loss Freeze Edition published; W3 execution pending |
| **5** | [00J — Rights-Provenance Inversion](./00J_FAILURE_MODE_RIGHTS_PROVENANCE_INVERSION_v0.1_DRAFT.md) | Can a valid generation/provenance statement be promoted through broken lineage into an unsupported downstream rights claim, and do the existing canonical gates prevent the inversion? | **Working draft / candidate scenario**; current design finding: existing S/T/H/KPI route is sufficient, execution pending |
| **5 — profile** | [00J-A01 — Panodyssey Notice / TEMS trajectory](./00J_A01_PANODYSSEY_TEMS_RIGHTS_PORTABILITY_IMPLEMENTATION_PROFILE_v0.1_DRAFT.md) | How do standard, defended-top and latent-regime-change implementations behave when the **same final licensing/enforcement decision** is held constant but the downstream resolver/identifier/lineage contract changes? | **Source-reviewed working draft**; H0/H1/H2 unexecuted |
| **5 — visuals** | [00J visual-aid package](./assets/00J/README.md) | Four embedded reader aids for evidence scope, end-to-end lineage, Q0–Q5 and Route N/Route Q | **Additive public reading aids**; no semantic or evidentiary authority over the parent scenario |
| **6** | [00 — Canonical Architecture Topology](./00_CANONICAL_ARCHITECTURE_TOPOLOGY.md) | How do Ω, U, R_U, W(d,t), A/B/C/D and participant-local qualification fit together? | **Canonical working** reader / reconciliation page |
| **6** | [03 — Functional Architecture v0.4](./03_FUNCTIONAL_ARCHITECTURE_v0.4.part01.md) | Which F1–F9 functions implement decision-scoped qualification, composition, requalification and learning? | **Controlled / frozen** source route |
| **6 — input contract start** | [04 — EA Input Interface Contract v0.4](./04_INPUT_INTERFACE_CONTRACT/04_INPUT_INTERFACE_CONTRACT_v0.4.md) | How do producers share existing B/C/D about A without sending A or requiring new epistemic computation? Includes guide, diagram, 176-input mapping and examples. | **Working input-contract proposal within 04**; H06 and O2 integration remain open; no EA outputs or executed adapter claims |
| **6** | [04 — General Functional Interfaces & Agentic Security v0.5](./04_GENERAL_FUNCTIONAL_INTERFACES_AGENTIC_SECURITY_v0.5_INTEGRATED.md) | How does qualified state cross agent, security, evidence and governance boundaries? | **Integrated working successor** |
| **6 — review** | [04 General Interfaces vNext Review & Delta v0.1 Draft](./04_GENERAL_FUNCTIONAL_INTERFACES_AGENTIC_SECURITY_VNEXT_REVIEW_AND_DELTA_v0.1_DRAFT.md) | Do post-baseline Requirements/corpus changes require generic O#/IF-S#/EHD changes, or only clarification/profile/test deltas? | **Working review only**; current determination: no new O7/IF-S14/EHD-kernel expansion |
| **6 — extensions** | [01H](./01H_PARTICIPANT_LOCAL_ECOSYSTEM_POSITIONING_AND_DECISION_SCOPED_EPISTEMIC_OPPORTUNITY_v0.1.md) · [01I](./01I_AGENTIC_CITIZENSHIP_CONTRACT_HUMAN_GOVERNED_PARTICIPATION_PROFILE_v0.1.md) · [01J](./01J_ECOSYSTEM_SIGNALLING_SELECTIVE_DISCLOSURE_AND_CHOREOGRAPHED_REPOSITIONING_v0.1.md) · [01K](./01K_HUMAN_INTELLIGENCE_CAPACITY_ESCALATION_AND_DEBT_PROFILE_v0.1.md) | How are participant locality, admissible participation, qualified ecosystem signalling and runtime Human Capacity and Human Intelligence Debt projected into the wider positioning architecture? | **Additive working extensions**; distinct semantic ownership retained |
| **7** | [00D — Canonical Architecture Benchmark & Reference-Scenario Evidence v0.2](./00D_CANONICAL_ARCHITECTURE_BENCHMARK_AND_REFERENCE_SCENARIO_EVIDENCE_v0.2.md) | How is the EA differential EA-H1–EA-H4 compared against B0–B3 under explicit evidence/falsification rules? | **Canonical working** benchmark design; comparative execution pending |
| **7 — vNext** | [00D v0.3 Draft — Ecosystem Positioning](./00D_CANONICAL_ARCHITECTURE_BENCHMARK_v0.3_DRAFT_ECOSYSTEM_POSITIONING.md) | How should the benchmark extend to signalling, Cartography, RA/MSCA composition, drift-first repositioning, Gradient and ACC/authority without silently broadening v0.2? | **Working draft only**; does not supersede v0.2 until adoption gates close |
| **Application** | [EA / FG-TIDA application package](../fg-tida/README.md) | How is the general architecture projected into the current FG-TIDA source/process boundary? | **Application package**; cannot redefine general EA semantics |
````````````

**Texto después — complete proposed unit**

````````````text
| Step | Document / route | Question it answers | Status |
|---|---|---|---|
| **1** | [01 — Integrated Foundational Theory v0.5](./01_FOUNDATIONAL_THEORY_v0.5_INTEGRATED.md) | Why can a bounded representation not close an open, changing ecosystem? | **Integrated working successor** |
| **1** | [02 — Epistemic Safety Principles & Control Matrix v0.4](./02_EPISTEMIC_SAFETY_PRINCIPLES_CONTROL_MATRIX_v0.4.part01.md) | Which epistemic/control boundaries prevent bounded evidence from becoming an unjustified global conclusion? | **Controlled / frozen** source route |
| **2** | [00 — Canonical Requirements: S1–S14, Sufficiency Conditions, Hypotheses and KPIs](./00_CANONICAL_REQUIREMENTS_CHALLENGES_SUFFICIENCY_HYPOTHESES_KPIS.md) | What must a sufficiently good solution demonstrate, and how can it fail? | **Frozen canonical baseline**; post-freeze changes route through the linked Requirements delta |
| **2 — review** | [Requirements working source and clarifications](./00_REQUIREMENTS_WORKING_SUCCESSOR_2026-10-12.md) | Do later EP developments require new S/T/H/KPI, or do they map to the existing requirement system? | **Maintained canonical reading**; accepted clarifications preserve the frozen S/T/H baseline; further proposals stay in the owning review |
| **2 — ablation** | [00K — Six-Principle Sufficiency & Adversarial Ablation Test v0.1 Draft](./00K_SIX_PRINCIPLE_REQUIREMENTS_MAPPING_AND_ABLATION_TEST_v0.1_DRAFT.md) · [A01 preserved reviewed design](./00K_A01_REVIEWED_PRE_PRINCIPLE_FIRST_DESIGN_ADDENDUM_v0.1.md) · [A02 coverage matrix](./00K_A02_REQUIREMENTS_COVERAGE_MATRIX_ADDENDUM_v0.1.md) · [A03 P4 paper execution](./00K_A03_P4_00H_PAPER_ABLATION_EXECUTION_v0.1.md) · [A4 runnable P4 harness](./fixtures/00K-A4-P4-00H/README.md) · [A15 complete six-principle testbook](./00K_A15_COMPLETE_SIX_PRINCIPLE_ABLATION_TESTBOOK_v0.1.md) · [02A foundation→principles proof](./02A_FOUNDATION_TO_OPERATIONAL_PRINCIPLE_DERIVATION_PROOF_v0.1.md) · [A19 principle↔requirement proof](./00K_A19_PRINCIPLE_REQUIREMENT_TRACEABILITY_AND_CONSERVATION_PROOF_v0.1.md) · [A16 corpus-grounded independence](./00K_A16_FORMAL_RELATIVE_INDEPENDENCE_PROOF_P1_P6_v0.1.md) · [A20 shared-substrate independence](./00K_A20_SHARED_SUBSTRATE_MATHEMATICAL_INDEPENDENCE_P1_P6_v0.1.md) · [A17 documentation map](./00K_A17_DOCUMENTATION_REPRODUCIBILITY_AND_PROOF_MAP_v0.1.md) | Can the six principles survive a strongest-repair leave-one-out test, with S1–S14 used as observable traceability rather than causal proof? | **Executable symbolic milestone**; first-pass harnesses now exist for all six principles: P1 corrected matched-semantic 42/42, P2 matched-prefix strongest-repair 58/58, P3 corrected matched-conflict 49/49, P4 minimal-authority audit 76/76, P5 exhaustive material-basis 47/47, P6 transitive-dependency 74/74 — **346 passing core symbolic regression tests** in total. The original A1 pair, original HOLD-marked P3 base pair and naive 00G P6 pair are preserved as falsified/insufficient isolations with concrete shortcuts; P4 additionally yields a refinement result: full receiver-side delegation history is not necessary in 00H, but a current decision-sufficient non-amplifying authority basis remains necessary in the tested surface. Supplemental packages bring the registered campaign to **379 tests**; GitHub Actions [run 36108965548](https://github.com/dakleyer/structural-awareness-contributions/actions/runs/36108965548) records an earlier reproduction at **379/379** across all 10 jobs; the corrected revision also passes [run 36196286646](https://github.com/dakleyer/structural-awareness-contributions/actions/runs/36196286646); live product/runtime validation remains pending |
| **3–4** | [00E — 100 Million Tokens](./00E_FAILURE_MODES_100M_TOKEN_COMPOUNDING_v0.1.md) · [00F — Smart-City Mobility Divergence v0.2](./00F_FAILURE_MODE_SMART_CITY_MOBILITY_SYSTEMIC_DIVERGENCE_v0.2_DRAFT.md) · [Freeze Edition](./00F_FAILURE_MODE_SMART_CITY_MOBILITY_SYSTEMIC_DIVERGENCE_v0.2_FREEZE_EDITION.md) | Where can locally plausible systems fail under compounding context loss or distributed divergence? | **Canonical working** reference scenarios; not executed benchmark results |
| **5** | [00G — Collective False-Context Convergence](./00G_FAILURE_MODE_COLLECTIVE_FALSE_CONTEXT_CONVERGENCE_v0.4.md) | How can correlated narrative/signalling produce false contextual convergence and authority confusion while still permitting genuine regime change? | **Canonical working v0.4**; integrated scenario + quality plan + OpenAI implementation trajectories; unexecuted; 00D/W3 execution pending |
| **5** | [00H — Batch Opportunity Beyond Authority](./00H_FAILURE_MODE_BATCH_OPPORTUNITY_BEYOND_AUTHORITY_v0.2_DRAFT.md) | How can a materially valid opportunity exceed the acting participant’s current authority, and how must it be preserved/re-contracted without unauthorized execution? | **Additive annex / candidate scenario**; executable admission pending |
| **5** | [00I — Semantic TOCTOU / The Patch That Undid the Fix](./00I_FAILURE_MODE_SEMANTIC_TOCTOU_v0.5_DRAFT.md) · [Freeze Edition](./00I_FAILURE_MODE_SEMANTIC_TOCTOU_v0.5_FREEZE_EDITION.md) | How can a correctly qualified queued action become wrong before use while its token/job/API remain technically valid, and which quality gates must force current-state requalification? | **Additive annex / candidate scenario**; Q0–Q6 + OOTB/top-notch/frozen-top-notch-under-drift quality plan; zero-loss Freeze Edition published; W3 execution pending |
| **5** | [00J — Rights-Provenance Inversion](./00J_FAILURE_MODE_RIGHTS_PROVENANCE_INVERSION_v0.1_DRAFT.md) | Can a valid generation/provenance statement be promoted through broken lineage into an unsupported downstream rights claim, and do the existing canonical gates prevent the inversion? | **Working draft / candidate scenario**; current design finding: existing S/T/H/KPI route is sufficient, execution pending |
| **5 — profile** | [00J-A01 — Panodyssey Notice / TEMS trajectory](./00J_A01_PANODYSSEY_TEMS_RIGHTS_PORTABILITY_IMPLEMENTATION_PROFILE_v0.1_DRAFT.md) | How do standard, defended-top and latent-regime-change implementations behave when the **same final licensing/enforcement decision** is held constant but the downstream resolver/identifier/lineage contract changes? | **Source-reviewed working draft**; H0/H1/H2 unexecuted |
| **5 — visuals** | [00J visual-aid package](./assets/00J/README.md) | Four embedded reader aids for evidence scope, end-to-end lineage, Q0–Q5 and Route N/Route Q | **Additive public reading aids**; no semantic or evidentiary authority over the parent scenario |
| **6** | [00 — Canonical Architecture Topology](./00_CANONICAL_ARCHITECTURE_TOPOLOGY.md) | How do Ω, U, R_U, W(d,t), A/B/C/D and participant-local qualification fit together? | **Canonical working** reader / reconciliation page |
| **6** | [03 — Functional Architecture v0.4](./03_FUNCTIONAL_ARCHITECTURE_v0.4.part01.md) | Which F1–F9 functions implement decision-scoped qualification, composition, requalification and learning? | **Controlled / frozen** source route |
| **6 — input contract start** | [04 — EA Input Interface Contract v0.4](./04_INPUT_INTERFACE_CONTRACT/04_INPUT_INTERFACE_CONTRACT_v0.4.md) | How do producers share existing B/C/D about A without sending A or requiring new epistemic computation? Includes guide, diagram, 176-input mapping and examples. | **Working input-contract proposal within 04**; H06 and O2 integration remain open; no EA outputs or executed adapter claims |
| **6** | [04 — General Functional Interfaces & Agentic Security v0.5](./04_GENERAL_FUNCTIONAL_INTERFACES_AGENTIC_SECURITY_v0.5_INTEGRATED.md) | How does qualified state cross agent, security, evidence and governance boundaries? | **Integrated working successor** |
| **6 — review** | [04 maintained interface clarifications](./04_GENERAL_FUNCTIONAL_INTERFACES_AGENTIC_SECURITY_v0.5_INTEGRATED.md#qualified-timing-and-human-review-handoff--maintained-reading) | Do post-baseline Requirements/corpus changes require generic O#/IF-S#/EHD changes, or only clarification/profile/test deltas? | **Maintained editorial clarification**; no new O7/IF-S14/EHD-kernel expansion; further proposals stay in the owning review |
| **6 — extensions** | [01H](./01H_PARTICIPANT_LOCAL_ECOSYSTEM_POSITIONING_AND_DECISION_SCOPED_EPISTEMIC_OPPORTUNITY_v0.1.md) · [01I](./01I_AGENTIC_CITIZENSHIP_CONTRACT_HUMAN_GOVERNED_PARTICIPATION_PROFILE_v0.1.md) · [01J](./01J_ECOSYSTEM_SIGNALLING_SELECTIVE_DISCLOSURE_AND_CHOREOGRAPHED_REPOSITIONING_v0.1.md) · [01K](./01K_HUMAN_INTELLIGENCE_CAPACITY_ESCALATION_AND_DEBT_PROFILE_v0.1.md) | How are participant locality, admissible participation, qualified ecosystem signalling and runtime Human Capacity and Human Intelligence Debt projected into the wider positioning architecture? | **Additive working extensions**; distinct semantic ownership retained |
| **7** | [00D — Canonical Architecture Benchmark & Reference-Scenario Evidence v0.2](./00D_CANONICAL_ARCHITECTURE_BENCHMARK_AND_REFERENCE_SCENARIO_EVIDENCE_v0.2.md) | How is the EA differential EA-H1–EA-H4 compared against B0–B3 under explicit evidence/falsification rules? | **Canonical working** benchmark design; comparative execution pending |
| **7 — vNext** | [00D current benchmark and development route](./00D_CANONICAL_ARCHITECTURE_BENCHMARK_AND_REFERENCE_SCENARIO_EVIDENCE_v0.2.md) | How should the benchmark extend to signalling, Cartography, RA/MSCA composition, drift-first repositioning, Gradient and ACC/authority without silently broadening v0.2? | **Working draft only**; does not supersede v0.2 until adoption gates close |
| **Application** | [EA / FG-TIDA application package](../fg-tida/README.md) | How is the general architecture projected into the current FG-TIDA source/process boundary? | **Application package**; cannot redefine general EA semantics |
````````````

**Enlace antes / enlace después:**

- Before: `./00D_CANONICAL_ARCHITECTURE_BENCHMARK_v0.3_DRAFT_ECOSYSTEM_POSITIONING.md`
- After: `./00D_CANONICAL_ARCHITECTURE_BENCHMARK_AND_REFERENCE_SCENARIO_EVIDENCE_v0.2.md`
- Before: `./04_GENERAL_FUNCTIONAL_INTERFACES_AGENTIC_SECURITY_VNEXT_REVIEW_AND_DELTA_v0.1_DRAFT.md`
- After: `./04_GENERAL_FUNCTIONAL_INTERFACES_AGENTIC_SECURITY_v0.5_INTEGRATED.md#qualified-timing-and-human-review-handoff--maintained-reading`
- Before: `./00_REQUIREMENTS_VNEXT_REVIEW_AND_DELTA_v0.1_DRAFT.md`
- After: `./00_REQUIREMENTS_WORKING_SUCCESSOR_2026-10-12.md`

**Acceptance:** exact source-region match and inverse; complete proposed unit appears once in the intended receiving body; all unrelated bytes, claim levels and frozen sources remain exact. Check source/receiver meanings, route targets and incoming anchors, then public readback and the owning review/queue receipt.


#### Unit 24 — Route fg-tida readers through maintained sources

**Source:** `research/ecosystem-awareness/fg-tida/README.md` · current blob `063ce7443cd01df76ac613799ca911dc040e1879` · line 44, bytes 2973–3847 at the pinned source cut. **Expected impact:** High; **risk:** Medium; **effort:** Medium.

**Why:** Replace a confirmed direct foreign-review edge with the intended canonical reading while retaining old proposals through their owning sources. Benchmarkv0.3 is treated by its declared role, not its filename.

**Dependencies and decision:** Apply the corresponding accepted content pair first where it supplies a new section; preserve proposal access through the canonical source’s own companion. Iván names this routing wave.

**Texto antes — complete current unit**

````````````text
- [**05 — ideal FG-TIDA projection**](./interfaces/05_FG_TIDA_IDEAL_CROSS_THEME_INTERFACE_CONTRACTS_v0.4.part01.md) + [**05 Ideal Delta**](./interfaces/05_FG_TIDA_IDEAL_CROSS_THEME_INTERFACE_CONTRACTS_VNEXT_REVIEW_AND_DELTA_v0.1_DRAFT.md): the target architecture if the relevant Theme semantics, semantic owners, implementations and review/test capacity were available. It is the **maximum coherent application of 04 to FG-TIDA**, not a claim about present adoption.
- [**05A — current FG-TIDA bridge**](./interfaces/05A_FG_TIDA_CURRENT_STATE_CONFORMANCE_BRIDGE_v0.1.md) + [**05A Current-State Delta**](./interfaces/05A_FG_TIDA_CURRENT_STATE_CONFORMANCE_BRIDGE_VNEXT_REVIEW_AND_DELTA_v0.1_DRAFT.md): a **current-state filter over 05**, retaining only what the public FG-TIDA record presently supports and downgrading the rest to candidate, test-only or not established.
````````````

**Texto después — complete proposed unit**

````````````text
- [**05 — ideal FG-TIDA projection**](./interfaces/05_FG_TIDA_IDEAL_CROSS_THEME_INTERFACE_CONTRACTS_v0.4.part01.md) + [05 ideal source and owning review route](interfaces/05_FG_TIDA_IDEAL_CROSS_THEME_INTERFACE_CONTRACTS_v0.4.part01.md): the target architecture if the relevant Theme semantics, semantic owners, implementations and review/test capacity were available. It is the **maximum coherent application of 04 to FG-TIDA**, not a claim about present adoption.
- [**05A — current FG-TIDA bridge**](./interfaces/05A_FG_TIDA_CURRENT_STATE_CONFORMANCE_BRIDGE_v0.1.md) + [05A dated source-state reception](interfaces/05A_FG_TIDA_CURRENT_STATE_CONFORMANCE_BRIDGE_v0.1.md#source-state-reception--21-october-2026): a **current-state filter over 05**, retaining only what the public FG-TIDA record presently supports and downgrading the rest to candidate, test-only or not established.
````````````

**Enlace antes / enlace después:**

- Before: `./interfaces/05A_FG_TIDA_CURRENT_STATE_CONFORMANCE_BRIDGE_VNEXT_REVIEW_AND_DELTA_v0.1_DRAFT.md`
- After: `interfaces/05A_FG_TIDA_CURRENT_STATE_CONFORMANCE_BRIDGE_v0.1.md#source-state-reception--21-october-2026`
- Before: `./interfaces/05_FG_TIDA_IDEAL_CROSS_THEME_INTERFACE_CONTRACTS_VNEXT_REVIEW_AND_DELTA_v0.1_DRAFT.md`
- After: `interfaces/05_FG_TIDA_IDEAL_CROSS_THEME_INTERFACE_CONTRACTS_v0.4.part01.md`

**Acceptance:** exact source-region match and inverse; complete proposed unit appears once in the intended receiving body; all unrelated bytes, claim levels and frozen sources remain exact. Check source/receiver meanings, route targets and incoming anchors, then public readback and the owning review/queue receipt.


#### Unit 25 — Keep the 05A current-state reader on its own source/review boundary

**Source:** `research/ecosystem-awareness/fg-tida/interfaces/05A_FG_TIDA_CURRENT_STATE_CONFORMANCE_BRIDGE_v0.1.md` · current blob `71abf26cd885d8567ca7d87dfcb4e44a2a5709d5` · line 5, bytes 103–906 at the pinned source cut. **Expected impact:** High; **risk:** Medium; **effort:** Medium.

**Why:** The frozen05part retains its historical review links; this living 05A preface reaches05through its source rather than directly linking the foreign review.

**Dependencies and decision:** Named wave GO and current source/receiver validation

**Texto antes — complete current unit**

````````````text
> **Layering / reading note.** 05A is **not a third or competing interface architecture**. It is the **dated current-state filter over 05 Ideal**: start from the ideal FG-TIDA projection in [05 v0.4](./05_FG_TIDA_IDEAL_CROSS_THEME_INTERFACE_CONTRACTS_v0.4.part01.md) and its [05 Ideal vNext Delta](./05_FG_TIDA_IDEAL_CROSS_THEME_INTERFACE_CONTRACTS_VNEXT_REVIEW_AND_DELTA_v0.1_DRAFT.md), then retain only what the public FG-TIDA record can presently support, downgrading unsupported ideal relations to **Candidate**, **Test-only** or **Not established**. Post-snapshot changes after 19 September 2026 are accumulated in the [**05A Current-State vNext Review & Delta**](./05A_FG_TIDA_CURRENT_STATE_CONFORMANCE_BRIDGE_VNEXT_REVIEW_AND_DELTA_v0.1_DRAFT.md) rather than silently rewriting this dated bridge.
````````````

**Texto después — complete proposed unit**

````````````text
> **Layering / reading note.** 05A is **not a third or competing interface architecture**. It is the **dated current-state filter over 05 Ideal**: start from the ideal FG-TIDA projection in [05 v0.4](./05_FG_TIDA_IDEAL_CROSS_THEME_INTERFACE_CONTRACTS_v0.4.part01.md) and the current development route exposed by that source’s own companion, then retain only what the public FG-TIDA record can presently support, downgrading unsupported ideal relations to **Candidate**, **Test-only** or **Not established**. Post-snapshot changes after 19 September 2026 are accumulated in the [**05A Current-State vNext Review & Delta**](./05A_FG_TIDA_CURRENT_STATE_CONFORMANCE_BRIDGE_VNEXT_REVIEW_AND_DELTA_v0.1_DRAFT.md) rather than silently rewriting this dated bridge.
````````````

**Enlace antes / enlace después:**

- Before: `./05_FG_TIDA_IDEAL_CROSS_THEME_INTERFACE_CONTRACTS_VNEXT_REVIEW_AND_DELTA_v0.1_DRAFT.md`
- After: `./05_FG_TIDA_IDEAL_CROSS_THEME_INTERFACE_CONTRACTS_v0.4.part01.md (the existing source link in the complete paragraph)`

**Acceptance:** exact source-region match and inverse; complete proposed unit appears once in the intended receiving body; all unrelated bytes, claim levels and frozen sources remain exact. Check source/receiver meanings, route targets and incoming anchors, then public readback and the owning review/queue receipt.


#### Unit 26 — Publish one uniquely identifiable documentation check

**Source:** `.github/workflows/document-integrity.yml` · current blob `cabf2e08b417d9d05e134604aa1ca10cc93a4e04` · line 1, bytes 0–648 at the pinned source cut. **Expected impact:** High; **risk:** Low; **effort:** Medium.

**Why:** The current shared verify name is ambiguous. Name this existing job explicitly and retain its PR/manual triggers, architecture and presentation checks.

**Dependencies and decision:** This naming pair does not cure the four inherited quote reports. Implement/test the exact contextual dispositions and policy extension before enabling it as a required successful check.

**Texto antes — complete current unit**

````````````text
name: Documentation integrity

# Intentionally not triggered on every push.
# This repository is a high-churn research corpus; running the broad link checker
# on each documentation commit created repeated false-positive notification floods.
# Keep the check available for controlled review and pull requests.
on:
  workflow_dispatch:
  pull_request:

jobs:
  verify:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.12'
      - name: Check links, architecture sections and presentations
        run: python scripts/check_document_integrity.py

````````````

**Texto después — complete proposed unit**

````````````text
name: Documentation integrity

# Intentionally not triggered on every push.
# This repository is a high-churn research corpus; running the broad link checker
# on each documentation commit created repeated false-positive notification floods.
# Keep the check available for controlled review and pull requests.
on:
  workflow_dispatch:
  pull_request:

permissions:
  contents: read

jobs:
  verify:
    name: Document control verification
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.12'
      - name: Check links, architecture sections and presentations
        run: python scripts/check_document_integrity.py

````````````

**Acceptance:** exact source-region match and inverse; complete proposed unit appears once in the intended receiving body; all unrelated bytes, claim levels and frozen sources remain exact. Check source/receiver meanings, route targets and incoming anchors, then public readback and the owning review/queue receipt.


#### New-file candidate — `governance/DOCUMENT_REGISTRY.yml`

**Before:** no tracked file at this exact path in the pinned tree. **After — complete proposed content:**

````````````yaml
schema: 1
policy: DC-GH-01
decision_state: proposed-seed-awaiting-owner-GO
coverage: protected-sources-nine-owners-and-first-promotion-units
default_unclassified_action: report-legacy-and-adjudicate-changed-active-sources
documents:
  - id: programme.entry
    path: README.md
    role: canonical-router
    lifecycle: current
    human_owner: Ivan Abril Palma
    technical_reading_level: null
  - id: ep.entry
    path: architectural-contributions/ecosystem-positioning/README.md
    role: canonical-router
    lifecycle: current
    human_owner: Ivan Abril Palma
    technical_reading_level: 1
    active_vnext_path: architectural-contributions/ecosystem-positioning/README_VNext.md
    protection: owner-gated-append-only-unless-named-exception
    approved_blob: 9bd2c1d10a8d440fa947abb7bc834d99ec97ff9b
  - id: ea.entry
    path: research/ecosystem-awareness/README.md
    role: canonical-router
    lifecycle: current
    human_owner: Ivan Abril Palma
    technical_reading_level: 2
    active_vnext_path: research/ecosystem-awareness/README_VNext.md
    protection: owner-gated
    last_recorded_approved_blob: 4e41fc697bb2bd94d1f4dd2b75230937684b8152
    observed_blob: 3ff5c26946b25608cea5cc1c9df8519dc61e1afd
    baseline_decision: unresolved-do-not-accept-observation-as-approval
  - id: ea.technical-index
    path: research/ecosystem-awareness/baseline/README.md
    role: canonical-router
    lifecycle: current
    human_owner: Ivan Abril Palma
    technical_reading_level: 3
    active_vnext_path: research/ecosystem-awareness/baseline/README_VNext.md
  - id: ea.fg-tida-index
    path: research/ecosystem-awareness/fg-tida/README.md
    role: canonical-router
    lifecycle: current
    human_owner: Ivan Abril Palma
    technical_reading_level: 3
  - id: ea.rs00eq1a-package
    path: research/ecosystem-awareness/baseline/fixtures/RS-00E-Q1a/README.md
    role: fixture-index
    lifecycle: current
    human_owner: Ivan Abril Palma
    technical_reading_level: null
    active_vnext_path: research/ecosystem-awareness/baseline/fixtures/RS-00E-Q1a/README_VNext.md
  - id: ra.entry
    path: research/regime-awareness/README.md
    role: canonical-router
    lifecycle: current
    human_owner: Ivan Abril Palma
    technical_reading_level: 2
    active_vnext_path: research/regime-awareness/README_VNext.md
  - id: msca.entry
    path: standards/minimum-sufficient-control/README.md
    role: canonical-router
    lifecycle: current
    human_owner: Ivan Abril Palma
    technical_reading_level: 2
    active_vnext_path: standards/minimum-sufficient-control/README_VNext.md
  - id: submissions.entry
    path: submissions/README.md
    role: canonical-router
    lifecycle: current
    human_owner: Ivan Abril Palma
    technical_reading_level: null
  - id: ep.development-strategy
    path: architectural-contributions/ecosystem-positioning/DEVELOPMENT_STRATEGY.md
    role: strategy
    lifecycle: current
    human_owner: Ivan Abril Palma
    protection: owner-gated-append-only
    observed_prefix_blob: f25aef42574afa9d321b352b3d2b1e1447575556
  - id: ea.requirements
    path: research/ecosystem-awareness/baseline/00_CANONICAL_REQUIREMENTS_CHALLENGES_SUFFICIENCY_HYPOTHESES_KPIS.md
    role: canonical
    lifecycle: frozen-edition
    working_successor_path: research/ecosystem-awareness/baseline/00_REQUIREMENTS_WORKING_SUCCESSOR_2026-10-12.md
    active_vnext_path: research/ecosystem-awareness/baseline/00_REQUIREMENTS_VNEXT_REVIEW_AND_DELTA_v0.1_DRAFT.md
    proposed_current_path: research/ecosystem-awareness/baseline/00_REQUIREMENTS_WORKING_SUCCESSOR_2026-10-12.md
    promotion_gate: accept-five-identity-units-content-pair-and-reconcile-receivers-before-updating-current-path
    protection: preserve-frozen-predecessor-and-version-specific-test-contracts
  - id: ea.general-interfaces
    path: research/ecosystem-awareness/baseline/04_GENERAL_FUNCTIONAL_INTERFACES_AGENTIC_SECURITY_v0.5_INTEGRATED.md
    role: canonical
    lifecycle: maintained-reader
    active_vnext_path: research/ecosystem-awareness/baseline/04_GENERAL_FUNCTIONAL_INTERFACES_AGENTIC_SECURITY_VNEXT_REVIEW_AND_DELTA_v0.1_DRAFT.md
  - id: ea.fg-tida-ideal
    path: research/ecosystem-awareness/fg-tida/interfaces/05_FG_TIDA_IDEAL_CROSS_THEME_INTERFACE_CONTRACTS_v0.4.part01.md
    role: canonical
    lifecycle: frozen-edition
    ordered_parts:
      - research/ecosystem-awareness/fg-tida/interfaces/05_FG_TIDA_IDEAL_CROSS_THEME_INTERFACE_CONTRACTS_v0.4.part01.md
      - research/ecosystem-awareness/fg-tida/interfaces/05_FG_TIDA_IDEAL_CROSS_THEME_INTERFACE_CONTRACTS_v0.4.part02.md
      - research/ecosystem-awareness/fg-tida/interfaces/05_FG_TIDA_IDEAL_CROSS_THEME_INTERFACE_CONTRACTS_v0.4.part03.md
    active_vnext_path: research/ecosystem-awareness/fg-tida/interfaces/05_FG_TIDA_IDEAL_CROSS_THEME_INTERFACE_CONTRACTS_VNEXT_REVIEW_AND_DELTA_v0.1_DRAFT.md
    protection: preserve-original-parts-contracts-and-historical-citations
  - id: ea.fg-tida-current
    path: research/ecosystem-awareness/fg-tida/interfaces/05A_FG_TIDA_CURRENT_STATE_CONFORMANCE_BRIDGE_v0.1.md
    role: canonical
    lifecycle: dated-snapshot-with-scoped-later-reception
    active_vnext_path: research/ecosystem-awareness/fg-tida/interfaces/05A_FG_TIDA_CURRENT_STATE_CONFORMANCE_BRIDGE_VNEXT_REVIEW_AND_DELTA_v0.1_DRAFT.md
    protection: preserve-original-snapshot-and-source-status
  - id: ea.benchmark
    path: research/ecosystem-awareness/baseline/00D_CANONICAL_ARCHITECTURE_BENCHMARK_AND_REFERENCE_SCENARIO_EVIDENCE_v0.2.md
    role: canonical
    lifecycle: current-design-execution-pending
    active_vnext_path: research/ecosystem-awareness/baseline/00D_CANONICAL_ARCHITECTURE_BENCHMARK_v0.3_DRAFT_ECOSYSTEM_POSITIONING.md
    promotion_decision: v0.3-design-adoption-gates-open
unresolved_identity_decisions:
  - ea-protected-successor
  - r01-rats-extensions-versus-feasibility
  - r01-technology-protocol-extensions-versus-feasibility
coverage_next: adjudicate-75-review-candidates-and-their-logical-source-parts-before-global-closure
````````````

**Purpose/state:** One supported operational seed; proposed fields record existing scope and unresolved decisions without promoting a version. Resolve its proposed decision_state and exact source mappings before adoption. Proposed complete seed; owner/schema adjudication before executable enforcement. **Impact:** High; **risk:** Medium; **effort:** Medium.

**Verification:** validate syntax with duplicate keys rejected, all declared paths/parts and owner relationships, supported role/protection decisions and actual coverage. A new mapping or flag cannot approve its own source change. Adoption requires the named wave GO; no file is created by this plan.


#### New-file candidate — `.github/CODEOWNERS`

**Before:** no tracked file at this exact path in the pinned tree. **After — complete proposed content:**

````````````text
# Owner review for the maintained corpus and its enforcement controls.
# Activate required owner review after distinct automation authorship is verified.
* @dakleyer
````````````

**Purpose/state:** Keep source, control, workflow, register and verifier review with the known repository owner; no invented reviewer or team. Batch routine editorial fixes proportionately. Complete candidate; activate only after a distinct automation author and functioning human-owner reviewer are verified. **Impact:** High; **risk:** Medium; **effort:** Medium.

**Verification:** validate syntax with duplicate keys rejected, all declared paths/parts and owner relationships, supported role/protection decisions and actual coverage. A new mapping or flag cannot approve its own source change. Adoption requires the named wave GO; no file is created by this plan.


#### Dependent registry transition — receiving the Requirements promotion

This is part of the registry package. **Source:** the future `governance/DOCUMENT_REGISTRY.yml` seed shown above. It is absent today; the old unit below is verified against that complete proposed seed, not represented as current main text. Revalidate the actually adopted seed before this dependent transition. Accept the five Requirements identity units, content addition and manifest/index reception together; update this one logical record rather than appoint a second current canon.

**Texto antes — complete proposed-seed record**

````````````yaml
  - id: ea.requirements
    path: research/ecosystem-awareness/baseline/00_CANONICAL_REQUIREMENTS_CHALLENGES_SUFFICIENCY_HYPOTHESES_KPIS.md
    role: canonical
    lifecycle: frozen-edition
    working_successor_path: research/ecosystem-awareness/baseline/00_REQUIREMENTS_WORKING_SUCCESSOR_2026-10-12.md
    active_vnext_path: research/ecosystem-awareness/baseline/00_REQUIREMENTS_VNEXT_REVIEW_AND_DELTA_v0.1_DRAFT.md
    proposed_current_path: research/ecosystem-awareness/baseline/00_REQUIREMENTS_WORKING_SUCCESSOR_2026-10-12.md
    promotion_gate: accept-five-identity-units-content-pair-and-reconcile-receivers-before-updating-current-path
    protection: preserve-frozen-predecessor-and-version-specific-test-contracts
````````````

**Texto después — complete receiving record after the named promotion**

````````````yaml
  - id: ea.requirements
    path: research/ecosystem-awareness/baseline/00_REQUIREMENTS_WORKING_SUCCESSOR_2026-10-12.md
    role: canonical
    lifecycle: maintained-reading
    frozen_predecessor_path: research/ecosystem-awareness/baseline/00_CANONICAL_REQUIREMENTS_CHALLENGES_SUFFICIENCY_HYPOTHESES_KPIS.md
    active_vnext_path: research/ecosystem-awareness/baseline/00_REQUIREMENTS_VNEXT_REVIEW_AND_DELTA_v0.1_DRAFT.md
    protection: preserve-frozen-predecessor-and-version-specific-test-contracts
````````````

**Impact:** High; **risk:** High (edition authority/consumer contracts); **effort:** Medium. The frozen predecessor and its studies stay linked. Native owner review and exact source/public readback verify the transition; changing the record alone does not perform the source promotion.


#### Main protection — exact prospective configuration

**Before:** `main.protected=false`; repository rulesets `[]`; no required context/owner gate observed. **After:** one branch-protection mechanism targeting main, with the following complete proposed request fields, checked against the [GitHub endpoint schema](https://docs.github.com/en/rest/branches/branch-protection#update-branch-protection). No ruleset is added in parallel.

````````````json
{
  "required_status_checks": {
    "strict": true,
    "contexts": [],
    "checks": [
      {
        "context": "Document control verification",
        "app_id": 15368
      }
    ]
  },
  "enforce_admins": true,
  "required_pull_request_reviews": {
    "dismiss_stale_reviews": true,
    "require_code_owner_reviews": true,
    "required_approving_review_count": 1,
    "require_last_push_approval": true
  },
  "restrictions": null,
  "required_conversation_resolution": true,
  "allow_force_pushes": false,
  "allow_deletions": false
}
````````````

**Activation dependencies:** corrected/verifiable required check publishes the unique name from application 15368; distinct automation author and owner reviewer verified; CODEOWNERS on base; safe recovery agreed; valid/adverse candidate tests prepared. **Impact:** High; **risk:** Medium (self-review lockout and trust in mutable check definitions); **effort:** Medium. Re-read API settings after activation, prove an actual non-bypass rejection and valid owner-approved incorporation, then restore/confirm the intended branch state. User administration remains a separate authority; this proposal does not change access now.


### 14.9 Complete review-unit promotion coverage

<details>
<summary>75 existing review candidates: selected material, receivers and next decision</summary>

Paths below identify existing source/review units; they are not new VNext or new canonical designations. The linked control audit supplies the contextual review directory. Ambiguous source candidates are resolved in the register before a wave is accepted.

| Existing review unit | Observed source/edition candidates | Block selection and next decision |
| --- | --- | --- |
| `architectural-contributions/ecosystem-positioning/01_GRADIENT_VNext.md` | `architectural-contributions/ecosystem-positioning/01_OBJECTIVE_CONDITIONED_AGENTIC_GRADIENT_LAW.md`<br>`governance/review/MSCA-kernel-lineage-gradient-2026-10-06/evidence.json` | Compare source with accepted review conclusions, retain applied receipts and select only absent mature explanations Existing ledger IDs: 57, 58, 61. |
| `architectural-contributions/ecosystem-positioning/README_VNext.md` | `architectural-contributions/ecosystem-positioning/README.md`<br>`DOCUMENT_CONTROL.md`<br>`README.md`<br>`presentations/ecosystem-positioning/PRESENTATION_MANIFEST.md` | Compare source with accepted review conclusions, retain applied receipts and select only absent mature explanations Existing ledger IDs: 1, 2, 3, 4, 5, 71, 97, 114, 131, 132, 149. |
| `research/ecosystem-awareness/DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1_VNext.md` | `research/ecosystem-awareness/DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1.md`<br>`research/ecosystem-awareness/gate-diagnostic/check_gate_profile_v0.3_audit_candidate.py`<br>`research/ecosystem-awareness/DDS_CANONICAL_METHOD_INDEX_v0.1.md`<br>`README.md` | Compare source with accepted review conclusions, retain applied receipts and select only absent mature explanations Existing ledger IDs: 74, 75, 76, 77, 81, 88, 91, 92, 95, 96, 103, 104, 110, 112, 115, 119, 120, 144, 145, 146, 147, 148. |
| `research/ecosystem-awareness/DDS_RESEARCH_BASIS_AND_BENCHMARKING_2026-10-06_VNext.md` | `research/ecosystem-awareness/DDS_RESEARCH_BASIS_AND_BENCHMARKING_2026-10-06.md` | Compare source with accepted review conclusions, retain applied receipts and select only absent mature explanations |
| `research/ecosystem-awareness/README_VNext.md` | `research/ecosystem-awareness/README.md` | Compare source with accepted review conclusions, retain applied receipts and select only absent mature explanations |
| `research/ecosystem-awareness/baseline/00D_A01_REFERENCE_SCENARIO_TEST_ARTIFACTS_AND_BOUNDED_ORACLE_CONSTRUCTION_AND_TEST_DESIGN_v0.1_VNext.md` | `research/ecosystem-awareness/baseline/00D_A01_REFERENCE_SCENARIO_TEST_ARTIFACTS_AND_BOUNDED_ORACLE_CONSTRUCTION_AND_TEST_DESIGN_v0.1.md` | Compare source with accepted review conclusions, retain applied receipts and select only absent mature explanations |
| `research/ecosystem-awareness/baseline/00D_A03_RS_00E_Q1A_STAGE_0_DETERMINISTIC_HARNESS_DESIGN_v0.1_VNext.md` | `research/ecosystem-awareness/baseline/00D_A03_RS_00E_Q1A_STAGE_0_DETERMINISTIC_HARNESS_DESIGN_v0.1.md` | Compare source with accepted review conclusions, retain applied receipts and select only absent mature explanations |
| `research/ecosystem-awareness/baseline/00D_CANONICAL_ARCHITECTURE_BENCHMARK_v0.3_DRAFT_ECOSYSTEM_POSITIONING.md` | `research/ecosystem-awareness/baseline/00D_CANONICAL_ARCHITECTURE_BENCHMARK_AND_REFERENCE_SCENARIO_EVIDENCE_v0.2.md` | Resolve design-adoption gates, select bounded design blocks; retain separate execution claims Existing ledger IDs: 40, 41. |
| `research/ecosystem-awareness/baseline/00L_REINFORCED_PAPER_TRAVERSALS_00E_00J_v0.1/README_VNext.md` | `research/ecosystem-awareness/baseline/00L_REINFORCED_PAPER_TRAVERSALS_00E_00J_v0.1/README.md` | Compare source with accepted review conclusions, retain applied receipts and select only absent mature explanations |
| `research/ecosystem-awareness/baseline/00M_A01_VNext.md` | `research/ecosystem-awareness/baseline/00M_A01_MECHANISM_TO_REQUIREMENTS_TRACEABILITY_v0.1_WORKING_PROPOSAL.md` | Compare source with accepted review conclusions, retain applied receipts and select only absent mature explanations Existing ledger IDs: 6. |
| `research/ecosystem-awareness/baseline/00M_VNext.md` | `research/ecosystem-awareness/baseline/00M_ABCD_AND_MATHEMATICAL_PLAUSIBILITY_v0.8_RESEARCH_NOTE.md` | Compare source with accepted review conclusions, retain applied receipts and select only absent mature explanations Existing ledger IDs: 7, 8, 9. |
| `research/ecosystem-awareness/baseline/00N_ADDENDUM_VNext.md` | `research/ecosystem-awareness/baseline/00N_RESEARCH_NEIGHBOURS_AND_EXPERIMENTAL_PRECEDENTS_v0.1_ADDENDUM.md` | Compare source with accepted review conclusions, retain applied receipts and select only absent mature explanations Existing ledger IDs: 10. |
| `research/ecosystem-awareness/baseline/00N_VNext.md` | `research/ecosystem-awareness/baseline/00N_FROM_MECHANISM_TO_REQUIREMENTS_SCIENTIFIC_PLAUSIBILITY_v0.7_RESEARCH_NOTE.md` | Compare source with accepted review conclusions, retain applied receipts and select only absent mature explanations Existing ledger IDs: 11, 12, 13, 42. |
| `research/ecosystem-awareness/baseline/00_REQUIREMENTS_VNEXT_REVIEW_AND_DELTA_v0.1_DRAFT.md` | `research/ecosystem-awareness/baseline/00_REQUIREMENTS_WORKING_SUCCESSOR_2026-10-12.md`<br>`research/ecosystem-awareness/baseline/00_CANONICAL_REQUIREMENTS_CHALLENGES_SUFFICIENCY_HYPOTHESES_KPIS.md` | Selected exact content pair above; reconcile applied older cards and remaining scientific questions Existing ledger IDs: 14, 15, 16, 43, 44, 45. |
| `research/ecosystem-awareness/baseline/01A_A01_VNext.md` | `research/ecosystem-awareness/baseline/01A_FOUNDATIONAL_DUAL_ORIGIN_NOTE_v0.1.md`<br>`research/ecosystem-awareness/baseline/02A_FOUNDATION_TO_OPERATIONAL_PRINCIPLE_DERIVATION_PROOF_v0.1.md`<br>`research/ecosystem-awareness/baseline/01_FOUNDATIONAL_THEORY_v0.5_INTEGRATED.md`<br>`research/ecosystem-awareness/baseline/00M_ABCD_AND_MATHEMATICAL_PLAUSIBILITY_v0.8_RESEARCH_NOTE.md` | Receive already-adopted hypothesis/source pointers; select only genuinely additional explanatory material |
| `research/ecosystem-awareness/baseline/01A_VNext.md` | `research/ecosystem-awareness/baseline/01A_A01_MISSION_DRIFT_CAUSAL_PRIORITY_AND_EPISTEMIC_ECONOMY_HYPOTHESES_v0.1_RESEARCH_NOTE.md`<br>`research/ecosystem-awareness/baseline/02A_FOUNDATION_TO_OPERATIONAL_PRINCIPLE_DERIVATION_PROOF_v0.1.md`<br>`research/ecosystem-awareness/baseline/01_FOUNDATIONAL_THEORY_v0.5_INTEGRATED.md` | Receive already-adopted hypothesis/source pointers; select only genuinely additional explanatory material |
| `research/ecosystem-awareness/baseline/01B_VNext.md` | `research/ecosystem-awareness/baseline/01B_EA_MSCA_INTERFACE_ANNEX_v0.2.md`<br>`research/ecosystem-awareness/baseline/01B_EA_MSCA_INTERFACE_ANNEX_v0.1.md` | Reconcile qualified output, scope/time/authority and consumer return; select accepted contract/reader clarifications Existing ledger IDs: 72. |
| `research/ecosystem-awareness/baseline/01C_VNext.md` | `research/ecosystem-awareness/baseline/01C_EA_REGIME_AWARENESS_INTERFACE_ANNEX_v0.2.md` | Reconcile qualified output, scope/time/authority and consumer return; select accepted contract/reader clarifications Existing ledger IDs: 52, 54. |
| `research/ecosystem-awareness/baseline/01D_VNext.md` | `research/ecosystem-awareness/baseline/01D_EA_MSCA_RA_OPERATION_COMPOSITION_PROFILE_v0.1.md` | Reconcile qualified output, scope/time/authority and consumer return; select accepted contract/reader clarifications Existing ledger IDs: 17. |
| `research/ecosystem-awareness/baseline/01H_VNext.md` | Read the declared source/packet ownership; destination decision required | Compare source with accepted review conclusions, retain applied receipts and select only absent mature explanations |
| `research/ecosystem-awareness/baseline/01I_VNext.md` | `governance/review/MSCA-kernel-lineage-gradient-2026-10-06/evidence.json` | Compare source with accepted review conclusions, retain applied receipts and select only absent mature explanations |
| `research/ecosystem-awareness/baseline/01J_VNext.md` | `research/ecosystem-awareness/baseline/01J_ECOSYSTEM_SIGNALLING_SELECTIVE_DISCLOSURE_AND_CHOREOGRAPHED_REPOSITIONING_v0.1.md` | Compare source with accepted review conclusions, retain applied receipts and select only absent mature explanations Existing ledger IDs: 68, 69, 70. |
| `research/ecosystem-awareness/baseline/01K_A01_HUMAN_CAPACITY_HID_COMPONENT_SPEC_v0.1_VNext.md` | `research/ecosystem-awareness/baseline/01K_A01_HUMAN_CAPACITY_HID_COMPONENT_SPEC_v0.1.md` | Compare source with accepted review conclusions, retain applied receipts and select only absent mature explanations Existing ledger IDs: 107, 108. |
| `research/ecosystem-awareness/baseline/01K_VNext.md` | `research/ecosystem-awareness/baseline/01K_HUMAN_INTELLIGENCE_CAPACITY_ESCALATION_AND_DEBT_PROFILE_v0.1.md` | Compare source with accepted review conclusions, retain applied receipts and select only absent mature explanations Existing ledger IDs: 64, 67, 93, 130. |
| `research/ecosystem-awareness/baseline/01_FOUNDATIONAL_VNext.md` | `research/ecosystem-awareness/baseline/01_FOUNDATIONAL_THEORY_v0.5_INTEGRATED.md`<br>`research/ecosystem-awareness/baseline/02A_FOUNDATION_TO_OPERATIONAL_PRINCIPLE_DERIVATION_PROOF_v0.1.md` | Compare source with accepted review conclusions, retain applied receipts and select only absent mature explanations Existing ledger IDs: 73, 100. |
| `research/ecosystem-awareness/baseline/02A_VNext.md` | `research/ecosystem-awareness/baseline/01_FOUNDATIONAL_THEORY_v0.5_INTEGRATED.md`<br>`research/ecosystem-awareness/baseline/01A_A01_MISSION_DRIFT_CAUSAL_PRIORITY_AND_EPISTEMIC_ECONOMY_HYPOTHESES_v0.1_RESEARCH_NOTE.md`<br>`research/ecosystem-awareness/baseline/02A_FOUNDATION_TO_OPERATIONAL_PRINCIPLE_DERIVATION_PROOF_v0.1.md` | Receive already-adopted hypothesis/source pointers; select only genuinely additional explanatory material |
| `research/ecosystem-awareness/baseline/03_FUNCTIONAL_VNext.md` | Read the declared source/packet ownership; destination decision required | Compare source with accepted review conclusions, retain applied receipts and select only absent mature explanations |
| `research/ecosystem-awareness/baseline/04_GENERAL_FUNCTIONAL_INTERFACES_AGENTIC_SECURITY_VNEXT_REVIEW_AND_DELTA_v0.1_DRAFT.md` | `research/ecosystem-awareness/baseline/04_GENERAL_FUNCTIONAL_INTERFACES_AGENTIC_SECURITY_v0.5_INTEGRATED.md`<br>`research/ecosystem-awareness/baseline/04_INPUT_INTERFACE_CONTRACT/04_INPUT_INTERFACE_CONTRACT_v0.4.md` | Selected exact content pair above; reconcile applied older cards and remaining scientific questions Existing ledger IDs: 18, 19, 101, 102. |
| `research/ecosystem-awareness/baseline/README_VNext.md` | `research/ecosystem-awareness/baseline/README.md`<br>`research/ecosystem-awareness/baseline/00J_A01_PANODYSSEY_TEMS_RIGHTS_PORTABILITY_IMPLEMENTATION_PROFILE_v0.1_DRAFT.md`<br>`research/ecosystem-awareness/baseline/00J_CASE_STUDY_EXTENSIBILITY_PROFILE_v0.1.md`<br>`research/ecosystem-awareness/baseline/non-canonical/README.md` | Compare source with accepted review conclusions, retain applied receipts and select only absent mature explanations Existing ledger IDs: 20, 21, 63, 65, 66, 79, 94, 105, 106, 113, 116, 121, 122, 123, 129, 133, 134, 136, 137, 138, 139, 140, 141, 142, 143. |
| `research/ecosystem-awareness/baseline/UC-EA-03_VNext.md` | `research/ecosystem-awareness/baseline/UC-EA-03_v0.4_MAINTENANCE_FREEZE.md`<br>`research/ecosystem-awareness/baseline/UC-EA-03_v0.5_WORKING_SUCCESSOR.md` | Compare source with accepted review conclusions, retain applied receipts and select only absent mature explanations Existing ledger IDs: 22, 23, 109. |
| `research/ecosystem-awareness/baseline/fixtures/00G-HF-ORACLE-v0.4/README_VNext.md` | `research/ecosystem-awareness/baseline/fixtures/00G-HF-ORACLE-v0.4/README.md` | Compare source with accepted review conclusions, retain applied receipts and select only absent mature explanations |
| `research/ecosystem-awareness/baseline/fixtures/00I-STATEFUL/README_VNext.md` | `research/ecosystem-awareness/baseline/fixtures/00I-STATEFUL/README.md` | Compare source with accepted review conclusions, retain applied receipts and select only absent mature explanations |
| `research/ecosystem-awareness/baseline/fixtures/00K-SUITE/README_VNext.md` | `research/ecosystem-awareness/baseline/fixtures/00K-SUITE/README.md`<br>`research/ecosystem-awareness/baseline/00K_A25_FAILURE_CASE_STUDY_EXTENSIBILITY_AND_CONFORMANCE_TRANSFER_v0.1.md`<br>`research/ecosystem-awareness/baseline/00K_A04_SIX_PRINCIPLE_SYMBOLIC_EXECUTION_SUMMARY_v0.1.md` | Compare source with accepted review conclusions, retain applied receipts and select only absent mature explanations Existing ledger IDs: 124, 128. |
| `research/ecosystem-awareness/baseline/fixtures/RS-00E-Q1a/README_VNext.md` | `research/ecosystem-awareness/baseline/fixtures/RS-00E-Q1a/README.md` | Compare source with accepted review conclusions, retain applied receipts and select only absent mature explanations |
| `research/ecosystem-awareness/baseline/reductions/00G-R01/COMPUTABILITY_AND_ORACLE_PLAN_VNext.md` | `research/ecosystem-awareness/baseline/reductions/00G-R01/COMPUTABILITY_AND_ORACLE_PLAN.md` | Compare source with accepted review conclusions, retain applied receipts and select only absent mature explanations |
| `research/ecosystem-awareness/baseline/reductions/00G-R01/Escenario-creatividad-validacion_VNext.md` | `research/ecosystem-awareness/baseline/reductions/00G-R01/Escenario-creatividad-validacion.md` | Compare source with accepted review conclusions, retain applied receipts and select only absent mature explanations Existing ledger IDs: 126. |
| `research/ecosystem-awareness/baseline/reductions/00G-R01/extensions/FENCING_CONFUSED_DEPUTY_EXTENSION_VNext.md` | `research/ecosystem-awareness/baseline/reductions/00G-R01/extensions/FENCING_CONFUSED_DEPUTY_EXTENSION.md`<br>`research/ecosystem-awareness/baseline/reductions/00G-R01/extensions/dds-hew-v0.1/TECHNICAL_REPORT.md`<br>`research/ecosystem-awareness/baseline/reductions/00G-R01/extensions/TECHNICAL_AUDIT_2026-10-07.md` | Select accepted method/status/limit explanations for the existing study reader; preserve frozen code/cards/results |
| `research/ecosystem-awareness/baseline/reductions/00G-R01/extensions/HUMAN_ESCALATION_WHISPERING_VNext.md` | `research/ecosystem-awareness/baseline/reductions/00G-R01/extensions/HUMAN_ESCALATION_WHISPERING.md`<br>`research/ecosystem-awareness/baseline/reductions/00G-R01/extensions/HEW_DDS_STUDY_2026-10-06.md` | Select accepted method/status/limit explanations for the existing study reader; preserve frozen code/cards/results Existing ledger IDs: 118. |
| `research/ecosystem-awareness/baseline/reductions/00G-R01/extensions/RATS_EXTENSION_VNext.md` | `research/ecosystem-awareness/baseline/reductions/00G-R01/extensions/RATS_EXTENSION.md`<br>`research/ecosystem-awareness/baseline/reductions/00G-R01/extensions/dds-hew-v0.1/TECHNICAL_REPORT.md`<br>`research/ecosystem-awareness/baseline/reductions/00G-R01/extensions/TECHNICAL_AUDIT_2026-10-07.md` | Resolve parallel logical scope/current-versus-retained edition before promotion |
| `research/ecosystem-awareness/baseline/reductions/00G-R01/extensions/README_VNext.md` | `research/ecosystem-awareness/baseline/reductions/00G-R01/extensions/README.md`<br>`research/ecosystem-awareness/baseline/reductions/00G-R01/extensions/infoblox/README.md`<br>`research/ecosystem-awareness/baseline/reductions/00G-R01/extensions/CURRENT_DDS_COMPATIBILITY_2026-10-06.json` | Select accepted method/status/limit explanations for the existing study reader; preserve frozen code/cards/results Existing ledger IDs: 80, 127. |
| `research/ecosystem-awareness/baseline/reductions/00G-R01/extensions/SPIFFE_SPIRE_EXTENSION_VNext.md` | `research/ecosystem-awareness/baseline/reductions/00G-R01/extensions/SPIFFE_SPIRE_EXTENSION.md`<br>`research/ecosystem-awareness/baseline/reductions/00G-R01/extensions/dds-hew-v0.1/TECHNICAL_REPORT.md`<br>`research/ecosystem-awareness/baseline/reductions/00G-R01/extensions/TECHNICAL_AUDIT_2026-10-07.md` | Select accepted method/status/limit explanations for the existing study reader; preserve frozen code/cards/results |
| `research/ecosystem-awareness/baseline/reductions/00G-R01/extensions/STAMP_STPA_EXTENSION_VNext.md` | `research/ecosystem-awareness/baseline/reductions/00G-R01/extensions/STAMP_STPA_EXTENSION.md`<br>`research/ecosystem-awareness/baseline/reductions/00G-R01/extensions/dds-hew-v0.1/TECHNICAL_REPORT.md`<br>`research/ecosystem-awareness/baseline/reductions/00G-R01/extensions/TECHNICAL_AUDIT_2026-10-07.md` | Select accepted method/status/limit explanations for the existing study reader; preserve frozen code/cards/results |
| `research/ecosystem-awareness/baseline/reductions/00G-R01/extensions/TECHNOLOGY_EXTENSION_PROTOCOL_VNext.md` | `research/ecosystem-awareness/baseline/reductions/00G-R01/extensions/TECHNOLOGY_EXTENSION_PROTOCOL.md` | Resolve parallel logical scope/current-versus-retained edition before promotion Existing ledger IDs: 117. |
| `research/ecosystem-awareness/baseline/reductions/00G-R01/extensions/cache-ttl/README_VNext.md` | `research/ecosystem-awareness/baseline/reductions/00G-R01/extensions/cache-ttl/README.md`<br>`research/ecosystem-awareness/baseline/reductions/00G-R01/extensions/cache-ttl/CURRENT_STUDY_RECORD.json` | Select accepted method/status/limit explanations for the existing study reader; preserve frozen code/cards/results |
| `research/ecosystem-awareness/baseline/reductions/00G-R01/extensions/dds-study-completion-v0.1/README_VNext.md` | `research/ecosystem-awareness/baseline/reductions/00G-R01/extensions/dds-study-completion-v0.1/README.md` | Select accepted method/status/limit explanations for the existing study reader; preserve frozen code/cards/results Existing ledger IDs: 98, 99. |
| `research/ecosystem-awareness/baseline/reductions/00G-R01/extensions/durable-workflows-retries/README_VNext.md` | Read the declared source/packet ownership; destination decision required | Select accepted method/status/limit explanations for the existing study reader; preserve frozen code/cards/results |
| `research/ecosystem-awareness/baseline/reductions/00G-R01/extensions/extension-audit-v0.1/README_VNext.md` | `research/ecosystem-awareness/baseline/reductions/00G-R01/extensions/extension-audit-v0.1/README.md` | Select accepted method/status/limit explanations for the existing study reader; preserve frozen code/cards/results |
| `research/ecosystem-awareness/baseline/reductions/00G-R01/extensions/hugging-face/README_VNext.md` | `research/ecosystem-awareness/baseline/reductions/00G-R01/extensions/hugging-face/README.md`<br>`research/ecosystem-awareness/baseline/reductions/00G-R01/README.md`<br>`research/ecosystem-awareness/baseline/reductions/00G-R01/extensions/hugging-face/review-2026-10-11/traversals/first-channel-counterfactual-v0.4/README.md`<br>`research/ecosystem-awareness/baseline/reductions/00G-R01/extensions/hugging-face/review-2026-10-11/traversals/first-channel-counterfactual-v0.5/README.md` | Select accepted method/status/limit explanations for the existing study reader; preserve frozen code/cards/results Existing ledger IDs: 135, 150. |
| `research/ecosystem-awareness/baseline/reductions/00G-R01/extensions/mcp-tool-calling/README_VNext.md` | Read the declared source/packet ownership; destination decision required | Select accepted method/status/limit explanations for the existing study reader; preserve frozen code/cards/results |
| `research/ecosystem-awareness/baseline/reductions/00G-R01/extensions/oauth-oidc/README_VNext.md` | Read the declared source/packet ownership; destination decision required | Select accepted method/status/limit explanations for the existing study reader; preserve frozen code/cards/results |
| `research/ecosystem-awareness/baseline/reductions/00G-R01/extensions/observability-response/README_VNext.md` | `research/ecosystem-awareness/baseline/reductions/00G-R01/extensions/observability-response/README.md`<br>`research/ecosystem-awareness/baseline/reductions/00G-R01/extensions/observability-response/CURRENT_STUDY_RECORD.json` | Select accepted method/status/limit explanations for the existing study reader; preserve frozen code/cards/results |
| `research/ecosystem-awareness/baseline/reductions/00G-R01/extensions/queues-ack-redelivery/README_VNext.md` | `research/ecosystem-awareness/baseline/reductions/00G-R01/extensions/queues-ack-redelivery/README.md`<br>`research/ecosystem-awareness/baseline/reductions/00G-R01/extensions/queues-ack-redelivery/CURRENT_STUDY_RECORD.json` | Select accepted method/status/limit explanations for the existing study reader; preserve frozen code/cards/results |
| `research/ecosystem-awareness/baseline/reductions/00G-R01/extensions/rag/README_VNext.md` | Read the declared source/packet ownership; destination decision required | Select accepted method/status/limit explanations for the existing study reader; preserve frozen code/cards/results |
| `research/ecosystem-awareness/baseline/reductions/00G-R01/extensions/sql-transactions-idempotency/README_VNext.md` | Read the declared source/packet ownership; destination decision required | Select accepted method/status/limit explanations for the existing study reader; preserve frozen code/cards/results |
| `research/ecosystem-awareness/baseline/reductions/00G-R01/extensions/structured-output/README_VNext.md` | `research/ecosystem-awareness/baseline/reductions/00G-R01/extensions/structured-output/README.md`<br>`research/ecosystem-awareness/baseline/reductions/00G-R01/extensions/structured-output/CURRENT_STUDY_RECORD.json` | Select accepted method/status/limit explanations for the existing study reader; preserve frozen code/cards/results |
| `research/ecosystem-awareness/baseline/reductions/00G-R01/feasibility/FENCING_CONFUSED_DEPUTY_EXTENSION_VNext.md` | `research/ecosystem-awareness/baseline/reductions/00G-R01/feasibility/FENCING_CONFUSED_DEPUTY_EXTENSION.md` | Select accepted method/status/limit explanations for the existing study reader; preserve frozen code/cards/results |
| `research/ecosystem-awareness/baseline/reductions/00G-R01/feasibility/HUMAN_ESCALATION_WHISPERING_VNext.md` | `research/ecosystem-awareness/baseline/reductions/00G-R01/feasibility/HUMAN_ESCALATION_WHISPERING.md`<br>`research/ecosystem-awareness/baseline/reductions/00G-R01/feasibility/HEW_DDS_STUDY_2026-10-06.md` | Select accepted method/status/limit explanations for the existing study reader; preserve frozen code/cards/results |
| `research/ecosystem-awareness/baseline/reductions/00G-R01/feasibility/RATS_EXTENSION_VNext.md` | `research/ecosystem-awareness/baseline/reductions/00G-R01/feasibility/RATS_EXTENSION.md` | Resolve parallel logical scope/current-versus-retained edition before promotion |
| `research/ecosystem-awareness/baseline/reductions/00G-R01/feasibility/SPIFFE_SPIRE_EXTENSION_VNext.md` | `research/ecosystem-awareness/baseline/reductions/00G-R01/feasibility/SPIFFE_SPIRE_EXTENSION.md` | Select accepted method/status/limit explanations for the existing study reader; preserve frozen code/cards/results |
| `research/ecosystem-awareness/baseline/reductions/00G-R01/feasibility/STAMP_STPA_EXTENSION_VNext.md` | `research/ecosystem-awareness/baseline/reductions/00G-R01/feasibility/STAMP_STPA_EXTENSION.md` | Select accepted method/status/limit explanations for the existing study reader; preserve frozen code/cards/results |
| `research/ecosystem-awareness/baseline/reductions/00G-R01/feasibility/TECHNOLOGY_EXTENSION_PROTOCOL_VNext.md` | `research/ecosystem-awareness/baseline/reductions/00G-R01/feasibility/TECHNOLOGY_EXTENSION_PROTOCOL.md` | Resolve parallel logical scope/current-versus-retained edition before promotion |
| `research/ecosystem-awareness/baseline/reductions/00G-R01/feasibility/dds-study-completion-v0.1/README_VNext.md` | `research/ecosystem-awareness/baseline/reductions/00G-R01/feasibility/dds-study-completion-v0.1/README.md` | Select accepted method/status/limit explanations for the existing study reader; preserve frozen code/cards/results |
| `research/ecosystem-awareness/baseline/reductions/00G-R01/feasibility/partial-experiments/README_VNext.md` | `research/ecosystem-awareness/baseline/reductions/00G-R01/feasibility/partial-experiments/README.md` | Select accepted method/status/limit explanations for the existing study reader; preserve frozen code/cards/results |
| `research/ecosystem-awareness/baseline/reductions/00G-R01/oracle/README_VNext.md` | `research/ecosystem-awareness/baseline/reductions/00G-R01/oracle/README.md` | Compare source with accepted review conclusions, retain applied receipts and select only absent mature explanations Existing ledger IDs: 24, 25, 26, 27, 28, 29, 30, 46, 47, 48, 49, 50, 51, 111. |
| `research/ecosystem-awareness/baseline/reductions/00G-R01/oracle/UC4_INTEROPERABILITY_PROFILE_VNext.md` | `research/ecosystem-awareness/baseline/reductions/00G-R01/oracle/UC4_INTEROPERABILITY_PROFILE.md` | Compare source with accepted review conclusions, retain applied receipts and select only absent mature explanations |
| `research/ecosystem-awareness/baseline/traversals/00G-HF-DYNAMIC-REVIEW-v0.1/README_VNext.md` | `research/ecosystem-awareness/baseline/traversals/00G-HF-DYNAMIC-REVIEW-v0.1/README.md` | Compare source with accepted review conclusions, retain applied receipts and select only absent mature explanations |
| `research/ecosystem-awareness/fg-tida/interfaces/05A_FG_TIDA_CURRENT_STATE_CONFORMANCE_BRIDGE_VNEXT_REVIEW_AND_DELTA_v0.1_DRAFT.md` | `research/ecosystem-awareness/fg-tida/interfaces/05A_FG_TIDA_CURRENT_STATE_CONFORMANCE_BRIDGE_v0.1.md`<br>`research/ecosystem-awareness/baseline/00M_ABCD_AND_MATHEMATICAL_PLAUSIBILITY_v0.8_RESEARCH_NOTE.md` | Selected exact content pair above; reconcile applied older cards and remaining scientific questions Existing ledger IDs: 31, 32. |
| `research/ecosystem-awareness/fg-tida/interfaces/05_FG_TIDA_IDEAL_CROSS_THEME_INTERFACE_CONTRACTS_VNEXT_REVIEW_AND_DELTA_v0.1_DRAFT.md` | `research/ecosystem-awareness/fg-tida/interfaces/05_FG_TIDA_IDEAL_CROSS_THEME_INTERFACE_CONTRACTS_v0.4.part01.md`<br>`research/ecosystem-awareness/baseline/00M_ABCD_AND_MATHEMATICAL_PLAUSIBILITY_v0.8_RESEARCH_NOTE.md`<br>`research/ecosystem-awareness/baseline/04_GENERAL_FUNCTIONAL_INTERFACES_AGENTIC_SECURITY_v0.5_INTEGRATED.md` | Select ideal profiles and source/return semantics; decide a later05 edition, preserving frozen parts Existing ledger IDs: 33, 34. |
| `research/regime-awareness/README_VNext.md` | `research/regime-awareness/README.md`<br>`research/regime-awareness/minimalistic-early-warning-systems/README.md`<br>`research/ecosystem-awareness/baseline/01C_EA_REGIME_AWARENESS_INTERFACE_ANNEX_v0.2.md` | Reconcile qualified output, scope/time/authority and consumer return; select accepted contract/reader clarifications Existing ledger IDs: 35, 36. |
| `standards/minimum-sufficient-control/00_ARCHITECTURE_VNext.md` | `governance/review/MSCA-kernel-lineage-gradient-2026-10-06/evidence.json` | Reconcile qualified output, scope/time/authority and consumer return; select accepted contract/reader clarifications |
| `standards/minimum-sufficient-control/01_ACC_VNext.md` | `governance/review/MSCA-kernel-lineage-gradient-2026-10-06/evidence.json` | Reconcile qualified output, scope/time/authority and consumer return; select accepted contract/reader clarifications |
| `standards/minimum-sufficient-control/02_ROLE_VNext.md` | `standards/minimum-sufficient-control/02_MSCA_ARCHITECTURAL_ROLE.md` | Reconcile qualified output, scope/time/authority and consumer return; select accepted contract/reader clarifications Existing ledger IDs: 125. |
| `standards/minimum-sufficient-control/03_COMPOSITION_VNext.md` | `standards/minimum-sufficient-control/03_MSCA_ECOSYSTEM_COMPOSITION_AND_CONTROL.md` | Reconcile qualified output, scope/time/authority and consumer return; select accepted contract/reader clarifications Existing ledger IDs: 53, 56. |
| `standards/minimum-sufficient-control/04_OPERATION_VNext.md` | `standards/minimum-sufficient-control/04_CANONICAL_MSCA_OPERATION_AND_REPOSITIONING.md` | Reconcile qualified output, scope/time/authority and consumer return; select accepted contract/reader clarifications Existing ledger IDs: 37, 59, 60. |
| `standards/minimum-sufficient-control/README_VNext.md` | `standards/minimum-sufficient-control/README.md` | Reconcile qualified output, scope/time/authority and consumer return; select accepted contract/reader clarifications Existing ledger IDs: 38, 39, 55, 62. |

</details>

### 14.10 Wave decision sheet and completion measure

For each named wave present 5–10 complete units, the actual source/receiving editions, expected benefit/risk/cost, order and dependencies, owner exceptions and the exact verification evidence to be produced. Distinguish incorporated text from research design and from executed evidence. After application, report units incorporated and verified, applied cards retired, real remaining decisions and evidence tasks.

**First proposed decision package:** the three content pairs (eight selected blocks), their own-source review reception, and only the routing units whose receiving content and protection decisions are ready. The seven operative-policy refinements, registry seed, verifier implementation, unique check/CODEOWNERS and branch-setting activation are separate controllable packages. No requirement to accept all 29 prospective units together is created.

The plan is complete when the supported changes are in their maintained sources, every reviewed unit has a current disposition, the remaining VNext contain actual work rather than already-applied cards, and the demonstrated GitHub safeguards enforce that practice for the intended actors. Scientific evidence tasks keep their proper open status.
