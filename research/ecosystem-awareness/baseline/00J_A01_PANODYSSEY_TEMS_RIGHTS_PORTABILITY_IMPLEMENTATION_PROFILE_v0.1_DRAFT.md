# 00J-A01 — Panodyssey Notice / TEMS Rights-Portability Implementation Trajectory

| | |
|---|---|
| **ID** | 00J-A01 |
| **Type** | Product / interoperability implementation-trajectory profile |
| **Status** | Source-reviewed working draft · unexecuted · not W3-admitted · not a product benchmark or failure claim |
| **Version · date** | v0.1 Draft · 2026-09-24 |
| **Evidence freeze** | 2026-09-24 |
| **Parent scenario** | [00J — Rights-Provenance Inversion](./00J_FAILURE_MODE_RIGHTS_PROVENANCE_INVERSION_v0.1_DRAFT.md) |
| **Primary implementation reference** | Panodyssey AI Transparency Notice / publisher-side rights stack |
| **Interoperability reference** | TEMS Trial 7 — rights portability across systems |
| **Public FG-TIDA reference** | Theme #17 — Digital Rights Infrastructure for Text |

> **Unexecuted implementation-path analysis.** This profile asks how a standard competent Panodyssey-side implementation, a defended top implementation extended through the agent/interoperability boundary, and that exact frozen top implementation under a latent downstream rights-resolution regime change interact with 00J Q0–Q5. It does **not** report that Panodyssey, TEMS, ODRL or any named AI/right-management system fails 00J.

---

## 1. Why Panodyssey/TEMS is the first implementation trajectory

Panodyssey is unusually well suited to 00J because the public FG-TIDA Theme #17 case already describes a strong publisher-side production chain rather than a hypothetical minimum implementation.

The Theme #17 contribution states that Panodyssey operates five publisher-side layers:

1. domain-level AI governance/access rules;
2. machine-readable discovery per publication;
3. structured rights declaration per work using ODRL/JSON-LD and distinguishing indexing, RAG and training;
4. auditable timestamped history of rights declarations; and
5. certified author/rightsholder identity.

The same contribution states the boundary clearly: the publisher-side chain can be correct while the **agent-side verifiable identity/representation counterpart is missing**. It also identifies interoperability beyond Panodyssey as a separate layer.

TEMS Trial 7 is a particularly relevant external boundary because it is explicitly about written-work interoperability and rights portability across systems. TEMS' public material notes that origin, authorship and conditions-of-use information can be lost as content moves across platforms and infrastructures.

That combination makes Panodyssey/TEMS stronger for 00J than a generic rights database:

- the source-side rights state is real and comparatively rich;
- the cross-system boundary is real;
- the missing/variable agent-side and downstream semantics are explicit;
- and the profile can fairly ask whether a strong rights stack remains sufficient when the **decision proposition itself changes downstream**.

The profile therefore does **not** treat Panodyssey as the weak baseline. It starts from a competent production-oriented source-side system.

---

## 2. Public source boundary

### 2.0 Public-only evidence rule

00J-A01 is intended to be independently reviewable by a third party.

**No private email, private meeting note, non-public demonstration or undocumented product claim is used as evidence for Panodyssey/TEMS capability in this profile.**

Every product/project assertion must be traceable to one of the public sources P1–P8 below. Where the profile needs a capability beyond those public sources, it is explicitly classified as one of:

- **strong-peer engineering extension** — something a competent defender is allowed to add for H1;
- **synthetic fixture fact** — a frozen condition created by 00J for comparison; or
- **regime-change mutation** — an externally changed resolver/identifier/lineage condition injected only in H2.

This prevents private implementation knowledge from becoming an unreviewable advantage and prevents H1/H2 from being misread as descriptions of the deployed Panodyssey product.

Public contributor attribution is likewise bounded. Theme #17 publicly identifies **Alexandre Leforestier (Panodyssey)** as proposer and GitHub **@AlexandreLeforestierITU** as the public contributor in the discussion. This profile relies only on what those public records and linked public Panodyssey/TEMS pages establish.

### P1 — FG-TIDA Theme #17

https://github.com/FG-TIDA/themes/issues/17

Used for:

- public identification of **Alexandre Leforestier (Panodyssey)** as Theme #17 proposer;
- five production publisher-side layers;
- indexing/RAG/training distinction;
- timestamped rights-declaration history;
- certified author identity;
- explicit statement that the chain stops at the agent-side identity/legal-representation boundary;
- proposed evidence/rejection classes such as current, replayed, expired, malformed and signed-but-out-of-mandate.

Public Alexandre Leforestier reply used for KYC / missing AI identity / TEMS Trial 7 interoperability statements:

https://github.com/FG-TIDA/themes/issues/17#issuecomment-5523072385

Public Alexandre Leforestier comment used for Case Study → Challenge → Use Case alignment and V2.1 deployment statement:

https://github.com/FG-TIDA/themes/issues/17#issuecomment-5542576491

### P2 — Panodyssey AI Transparency Notice launch

https://www.panodyssey.com/en/article/technology/press-release-panodyssey-launches-the-ai-transparency-notice-tpbhc7snppcb

Used for:

- Panodyssey Security / AI Transparency Notice as a public source-side content-origin, traceability and AI-use-control mechanism;
- CREA Trust AI context.

### P3 — Panodyssey Notice V2.1 public update

https://www.panodyssey.com/fr/article/technologie/nouvelle-version-de-la-notice-ia-panodyssey-celle-qui-vous-dit-toujours-la-verite-dekmf956we6w

Used only for:

- public evidence that Panodyssey continued versioning the Notice;
- the statement that V2.1 corrected inconsistencies in AI-readable signals in code/meta tags.

It is **not** used as evidence that V2.1 or Panodyssey causes 00J.

### P4 — Panodyssey licensing / certified human content description

https://www.panodyssey.com/en/article/technology/panodyssey-offers-ai-companies-licensed-access-to-certified-human-content-the-author-decides-publication-by-publication-ai-by-ai-wd7wg7c36e67

Used for:

- publication-by-publication / AI-by-AI control framing;
- RAG/inference licensing as a distinct use;
- certified/timestamped/attributed content;
- stated TEMS rights-portability context.

### P5 — TEMS Trial 7

https://tems-dataspace.eu/trials/
https://tems-dataspace.eu/tems-trial-7-how-rights-travel-across-systems/
https://tems-dataspace.eu/tems-trial-7-protecting-and-valuing-cultural-content-in-the-age-of-ai/
https://tems-dataspace.eu/tems-trial-7-making-intellectual-property-visible-and-actionable-in-the-age-of-ai/

Used for:

- interoperability/connectors for written works;
- rights portability across systems;
- public statement that origin/authorship/conditions-of-use information can be lost across platforms/infrastructures.

### P6 — W3C ODRL

https://www.w3.org/TR/odrl-model/

Used for:

- scope-specific permissions/prohibitions/duties/parties/assets/constraints;
- distinction between an expressed permission and generic downstream authority.

### P7 — C2PA provenance boundary

https://spec.c2pa.org/specifications/specifications/2.4/specs/ContentCredentials.html
https://spec.c2pa.org/specifications/specifications/2.2/explainer/Explainer.html

Used only as an external technical comparator for the proposition that provenance may be incomplete and that verifiable provenance does not automatically settle a stronger truth/rights proposition.

### P8 — European Commission 2026 TDM opt-out registry feasibility study

https://op.europa.eu/en/publication-detail/-/publication/5c5cd1ec-7cce-11f1-bf5e-01aa75ed71a1/language-en

Used for:

- official evidence that current rights-reservation mechanisms are fragmented and work-based metadata can be stripped or not reliably processed;
- the explicit boundary that the proposed registry would improve durable/interoperable signalling and traceability while **not itself being a rights-management or licensing system**.

This is important for 00J because a registry/resolver result can be highly useful and current without automatically carrying the stronger authority semantics needed for final enforcement.

---

## 3. Three implementation arms

The three arms intentionally mirror the existing 00E/00H implementation-profile discipline.

| Arm | Configuration | Purpose |
|---|---|---|
| **PANO-H0 — standard competent source-side implementation** | **Publicly documented as of the 24 Sep 2026 evidence freeze:** publisher-side Panodyssey/Notice capabilities described in Theme #17 and public Panodyssey/TEMS sources, including certified author identity, per-publication machine-readable rights, ODRL/JSON-LD-style rights state, timestamps/history, domain/discovery signals and rights-portability context | Establish what the public source-side implementation already supports without importing private implementation detail or pretending it controls the entire downstream ecosystem |
| **PANO-H1 — premium / defended top interoperability implementation** | H0 plus verifiable agent principal/representation, current mandate/purpose/scope, signed access/right-decision receipt, versioned source/right identifiers across TEMS-style handoff, explicit claim-supported-proposition, source/dependency lineage, expiry/revocation, bounded challenge/re-entry **and a stable downstream enforcement resolver that must pass the unsupported-claim and legitimate-transfer controls before H2 is admitted** | Give the strongest reasonable peer the controls needed to attack 00J directly; “premium” is an analysis label, not a Panodyssey commercial tier |
| **PANO-H2 — same frozen top implementation under latent resolver/lineage regime change** | Freeze H1 code/resources/interfaces after it correctly resolves the same final licensing/enforcement proposition. Then change the external resolver/identifier/evidence contract: D1/RX remain authentic and current, but the source-dependency/authority relation that H1 previously relied on is no longer required, represented or retrievable with the same semantics | Test whether the excellent implementation detects that its previously sufficient evidence contract has become invalid for the **same Q5 enforcement decision**, rather than merely handling a new decision type |

A future EA-enabled arm is admitted only if H1/H2 leave a measurable differential. H1 is allowed to be strengthened before fixture freeze by a competent defender. No post-result patching is permitted.

---

## 3A. Public capability versus constructed test architecture

| Element | Classification | Evidence / boundary |
|---|---|---|
| Panodyssey publisher-side five-layer chain | **Publicly documented** | Theme #17 P1 |
| Certified author/rightsholder identity on publisher side | **Publicly documented** | Theme #17 P1 + Alexandre Leforestier public reply |
| Per-publication machine-readable rights and indexing/RAG/training distinction | **Publicly documented** | Theme #17 P1 |
| Timestamped/versioned rights declaration history | **Publicly documented** | Theme #17 P1 |
| Panodyssey / TEMS Trial 7 interoperability and rights-portability context | **Publicly documented** | Theme #17 public reply + TEMS P5 |
| Panodyssey Notice launch / V2.1 / certified-human-content licensing claims | **Public vendor/project documentation** | P2–P4 |
| Agent principal/mandate binding used by PANO-H1 | **Constructed strong-peer extension** | not attributed to current Panodyssey unless separately evidenced |
| Proposition-bound decision receipt used by PANO-H1 | **Constructed strong-peer extension** | test architecture |
| Explicit W→D1 source-dependency service used by PANO-H1 | **Constructed strong-peer extension** | test architecture; C2PA/ODRL are neighboring public references, not proof Panodyssey implements this exact service |
| Original lineage-aware Q5 resolver used by H1 | **Synthetic/constructed strong-peer fixture** | must pass paired negative/legitimate-transfer controls before H2 |
| Resolver/identifier/lineage mutation in H2 | **Synthetic regime-change fixture** | not claimed to be a Panodyssey/TEMS incident |

This classification table is controlling whenever prose elsewhere could be read ambiguously.

---

## 4. PANO-H0 — standard competent source-side route

### 4.1 What H0 legitimately does well

A competent Panodyssey-side implementation can establish a strong Q0 source frame:

- verified/certified author identity;
- publication/content identifier;
- machine-readable rights declaration;
- use distinctions such as indexing/RAG/training;
- timestamped/versioned changes;
- auditable history;
- domain/discovery signals;
- a route toward licensing for declared uses.

This materially reduces trivial 00J failures.

### 4.2 What remains outside H0's guaranteed boundary

H0 does not, by the public Theme #17 case itself, establish:

- a universally verifiable agent-side legal identity;
- the agent's current principal/mandate/purpose in every downstream system;
- proof of actual downstream execution/compliance;
- complete source/dependency lineage after transformation outside the publisher's boundary;
- how an independent downstream registry composes a new D1/RX claim with A/W/R0;
- which proposition a future third-party enforcement system is entitled to infer from G1/RX.

Therefore H0 can be entirely healthy while Q2–Q5 remain underdetermined downstream.

### 4.3 H0 gate reading

| 00J gate | H0 strength | Remaining boundary |
|---|---|---|
| **Q0 original rights frame** | Strong | source state can be well qualified |
| **Q1 access/use authority** | Strong on publisher-side policy; weak/variable on agent principal/mandate | identity/access signal may not equal current legal representation/mandate |
| **Q2 transformation/source dependency** | Outside source platform once downstream transformation occurs | W→D1 may be lost or not represented |
| **Q3 downstream claim** | Outside H0 control | RX can be locally authentic without a complete upstream authority chain |
| **Q4 propagation/corroboration** | Outside H0 control | replicated RX may appear independent |
| **Q5 enforcement** | Outside H0 control | final rights checker may consume a stronger proposition than H0 ever issued |

An H0 failure here is not evidence that Panodyssey is defective. It is evidence that a strong source-side rights system is not automatically a whole-ecosystem rights-adjudication system.

---

## 5. PANO-H1 — defended top interoperability implementation

PANO-H1 is **not claimed to be the current Panodyssey product**. It is the strongest reasonable implementation a competent defender can build using Panodyssey/TEMS as the source/interoperability substrate.

### 5.1 Additional H1 controls

For each material access/handoff, H1 binds:

- work identifier;
- source-rights-record identifier;
- source-rights version;
- rights-holder/principal;
- agent-instance identity;
- agent operator/provider;
- represented principal;
- mandate/reference;
- requested use;
- purpose;
- scope;
- jurisdiction/territory where material;
- expiry/revalidation;
- downstream-use conditions;
- claim-supported proposition;
- source dependency;
- decision-receipt identifier;
- decision owner;
- challenge/re-entry route.

The signed receipt says what was decided. It does not assert future behavior beyond the evidence available.

### 5.2 H1 gate behavior

| Gate | H1 expected behavior |
|---|---|
| **Q0** | Preserve A/W/R0 identity, version, policy scope and currentness |
| **Q1** | Bind access to verifiable agent/principal/mandate/use rather than technical identity alone |
| **Q2** | Carry W→D1 dependency where known; otherwise preserve explicit UNKNOWN; keep generated-by separate from independent-source |
| **Q3** | Accept RX only as a bounded downstream claim until authority/source relation for the final proposition is established |
| **Q4** | Preserve registry/source dependencies and deduplicate dependent copies |
| **Q5** | Enforce only where current evidence/authority supports the exact licensing/blocking proposition |

### 5.3 Expected H1 result on original regime

H1 should pass:

- valid continuity;
- permitted RAG;
- explicit training prohibition;
- current agent mandate;
- legitimate transfer to X;
- independent-work control;
- correlated-copy control;
- unknown downstream-use control;
- stale/revoked-record revalidation;
- **stable downstream enforcement, negative branch:** RX exists without the required A→X authority chain and the resolver returns REQUALIFY/DENY/no-enforcement rather than PAY/BLOCK;
- **stable downstream enforcement, positive branch:** the legitimate-transfer control supplies the required A→X authority chain and the same resolver accepts the qualified X claim.

Those last two branches are mandatory before H2. They establish that H1 already handles the **same final Q5 proposition** correctly under the original resolver regime.

If H1 cannot pass these under the original regime, the failure is ordinary missing control engineering and cannot be attributed to a latent EA differential.

---

## 6. PANO-H2 — same top implementation under regime change

This is the decisive trajectory.

### 6.1 Freeze H1 first

Before H2:

- freeze H1 code;
- freeze H1 schemas and interface contracts;
- freeze resources, human capacity and deadlines;
- freeze the positive-control results;
- freeze the source/rights records and normal access-time decision semantics.

H2 is not allowed to add a new field after observing the failure.

### 6.2 Original qualified resolver regime

Under H1's original operating regime, the **same final decision** that 00J will later stress is already exercised:

> **May downstream claimant X require A to license/pay or may the relying system block A's use of W/W2 on the basis of D1/RX?**

The frozen H1 resolver/interoperability contract is lineage-aware. For this decision it requires, directly or through an authoritative dependency service:

- current RX identity/version;
- the asserted right and its scope;
- the source/dependency relation relevant to D1;
- the authority chain needed for the claim against A;
- conflict with R0;
- freshness/expiry;
- the proposition actually supported by the returned status.

Under this original regime H1 MUST pass both paired controls:

- **N — no A→X authority:** D1 materially depends on W; RX is authentic; X lacks the required authority chain → no enforcement against A.
- **G — legitimate A→X authority:** same general topology, but A has granted X the relevant right → qualified X enforcement may proceed.

Only after N and G pass is H1 frozen for H2.

### 6.3 Latent interoperability / rights-resolution regime shift

Now mutate **one external ecosystem relation without changing the Q5 proposition**.

Primary H2 branch:

- the downstream ecosystem migrates to a new resolver, registry profile or canonical-identifier regime;
- D1 becomes a first-class/root-resolved asset under that regime;
- G1 and RX remain authentic, current and technically valid;
- the new resolver can answer the same high-level rights query, but its represented/required evidence contract no longer guarantees the W→D1 source dependency or the upstream A/R0 authority relation with the semantics H1 previously relied on;
- the mapping from the old W/source namespace to the new D1/root namespace is absent, optional, stale or outside the resolver's declared coverage;
- several downstream services consume the new resolver result;
- no credential revocation, signature error, API outage or conventional security alert is required.

The important change is **not** that a new business question suddenly appears. The business question is held constant. What changed is the ecosystem relationship that made a particular source/resolver result sufficient evidence for that question.

This is a genuine 00J regime/dependency stress:

**same Q5 proposition + same H1 code + technically healthy records + changed resolver/lineage semantics.**

### 6.4 Why this is a regime change rather than an ordinary integration bug

H2 does not score a trivial missing-field implementation.

Before the mutation, the frozen H1 integration is demonstrated to be sufficient on N and G. After the mutation:

- the source/resolver identity or semantic version is observable or discoverable within the declared fixture;
- the old evidence contract is no longer entitled to the same decision reliance;
- local records may all remain authentic/current;
- the correct response is to requalify the resolver coverage, source lineage and supported proposition before enforcement.

A candidate that simply ignores an explicit incompatible API error is an ordinary bad implementation and is not credited as an H2 regime failure. H2 is admitted only where the interface remains technically usable while its **decision-sufficiency semantics or lineage coverage have materially changed**.

### 6.5 Expected H2 failure without dynamic requalification

| Gate | What remains locally healthy | What changed in the ecosystem relation | Failure mode |
|---|---|---|---|
| **Q0** | A/W/R0 current | new resolver no longer guarantees that the original-source relation participates in the final resolution | source frame becomes non-fungible but is treated as covered |
| **Q1** | C1 access/mandate receipt valid | old access semantics remain true but say nothing new about resolver coverage | valid permit is over-relied upon downstream |
| **Q2** | G1 authentic; D1 current | D1 is now resolved as a root/first-class asset without the previously required W lineage | evidence-scope / lineage promotion |
| **Q3** | RX authentic/current | resolver's rights status is derived under a different authority/lineage contract | unsupported authority promotion if old trust mapping is reused |
| **Q4** | replicated records consistent | replicas inherit the new resolver result and can look mutually corroborating | false convergence from one changed dependency |
| **Q5** | same licensing/enforcement question | H1 trusts a result whose semantic coverage has changed since qualification | author can be asked to pay/block despite technically green local controls |

This is the 00J analogue of the LangGraph/Agent-365 stress:

> an excellent implementation can remain operationally correct against its frozen local contract while the **external relation that made that contract decision-sufficient has changed**.

---

## 7. What H2 must do to pass

A passing H2 does not need omniscience.

It must detect that the final decision depends on a proposition not established by the current evidence contract and then:

1. reopen the material source/dependency/authority boundary;
2. preserve R0 and RX as distinct records;
3. identify that G1/RX supports a narrower proposition than the requested enforcement decision;
4. avoid counting dependent replicas as independent corroboration;
5. request only the missing authority/source relation or route to the legitimate owner;
6. remain inside the response horizon;
7. allow legitimate-transfer controls to pass;
8. avoid universal denial.

Expected disposition in the negative branch:

**REQUALIFY, bounded HOLD, legitimate ESCALATE, or NO CONCLUSION.**

Not:

**PAY_X, LICENSE_REQUIRED_FROM_X or BLOCK_FOR_X.**

---

## 8. Matched stress tests

### Test A — normal source continuity

No downstream claim conflict. H0/H1/H2 should preserve normal publication/use without unnecessary blocking.

### Test B — agent identity/mandate

Authenticated agent, valid bounded RAG mandate.

H1/H2 should allow the declared use and preserve purpose/scope.

### Test C — legitimate transfer

A grants X the relevant right.

H1/H2 must recognize the qualified X claim. Deny-all fails.

### Test D — source-dependency preservation

D1 materially depends on W.

H1 should preserve the dependency under the original interface.

### Test E — correlated replication

K1–K4 ingest RX.

H1/H2 must not treat multiplicity as source independence.

### Test F — latent rights-resolution regime shift

Freeze H1 only after the paired Q5 enforcement controls pass under the original lineage-aware resolver: unsupported X claim blocked/requalified; legitimate A→X transfer accepted. Then apply the resolver/identifier/lineage mutation in §6 while keeping the **same Q5 licensing/enforcement proposition**.

Passing requires requalification of the **resolver coverage, source lineage and evidence contract**, not merely revalidation of signatures.

### Test G — strengthened conventional falsifier

Before fixture freeze, a defender may strengthen H1 with:

- mandatory upstream dependency retrieval for every derivative-rights decision;
- explicit evidence-purpose contracts;
- current authority lineage;
- dependency-aware registry resolution;
- action-time source/rights revalidation.

If strengthened H1 passes Test F at equal or lower burden, the proposed EA differential is narrowed or eliminated for this envelope.

---

## 9. Q0–Q5 implementation matrix

| Gate | PANO-H0 | PANO-H1 | PANO-H2 stress |
|---|---|---|---|
| **Q0 source/right frame** | strong publisher-side record | source/version/owner/currentness bound to receipt | original frame remains valid, but changed resolver coverage may no longer include it in the same way |
| **Q1 access authority** | rights signal; agent-side representation gap remains | verifiable agent/principal/mandate/use | access remains valid but cannot compensate for changed downstream resolver semantics |
| **Q2 transformation/source dependency** | outside publisher boundary after transformation | explicit source-dependency / UNKNOWN | new resolver/identifier regime treats D1 as root or no longer guarantees W→D1 lineage |
| **Q3 downstream claim** | outside source platform | bounded RX claim with authority/source checks | same rights-status query is answered under a changed authority/lineage evidence contract |
| **Q4 propagation** | no whole-ecosystem correlation guarantee | dependency-aware replication | multiple consistent copies inherit one changed resolver/dependency basis |
| **Q5 enforcement** | external | same proposition-specific enforcement check passes N/G under original regime | same Q5 proposition can false-pass if H1 continues to trust the obsolete resolver semantics |

---

## 10. Measures

Use the parent 00J measures plus:

- **resolver/evidence-contract invalidation detection** — H2 runs where the external resolver/lineage contract changes materially and the dependency is exposed before enforcement ÷ applicable H2 runs;
- **evidence-contract mismatch rate** — final decisions consuming a resolver result outside its currently qualified semantic/lineage coverage ÷ applicable material decisions;
- **source-lineage availability at enforcement**;
- **rights-resolution requalification latency**;
- **false enforcement after regime change**;
- **legitimate-transfer acceptance after regime change**;
- **total interoperability burden**.

These remain scenario/profile observables, not new canonical KPI families.

---

## 11. Falsification rule

The proposed differential is weakened or rejected if a frozen strong H1 implementation:

- passes all original-regime controls;
- detects the H2 decision-proposition shift;
- retrieves/preserves the required upstream dependency/authority state;
- blocks unsupported enforcement;
- accepts legitimate transfer/independent work;
- does so within the same response horizon and equal/lower burden;
- and does not require EA-specific semantics beyond ordinary strong rights/provenance engineering.

Conversely, a H2 failure counts only if H1 was genuinely strong under the original regime. A weak source-side implementation is not evidence for regime-awareness differentiation.

---

## 12. Relationship to Panodyssey product claims

This profile distinguishes three layers.

### Documented Panodyssey/TEMS capability

Public source evidence supports the publisher-side rights/identity/audit stack and the cross-system rights-portability work.

**Nothing in this section is sourced from the private email thread.** If a privately discussed implementation detail is not present in P1–P8, it is excluded from the documented-capability claim.

### Strong-peer engineering extension

PANO-H1 adds agent-side identity/mandate, signed decision receipts, explicit source dependency and proposition-bound evidence semantics as a **constructed defended peer**. These are not claimed to be current Panodyssey product features unless separately evidenced.

### Synthetic regime-change test

PANO-H2 is a fictional adversarial fixture over the frozen H1 architecture. It is not an incident report and does not state that Panodyssey/TEMS has experienced the described downstream rights inversion.

---

## 13. Why not use C2PA as A01

C2PA is valuable as a **future independent A02 strong provenance comparator**, because its explicit provenance and ingredient model is close to 00J Q2/Q4.

It is not the best A01 because 00J begins with **human author identity + machine-readable rights + allowed-use semantics + licensing/rights portability**, which Panodyssey/Theme #17 already exposes directly. C2PA's own guidance deliberately avoids treating provenance verification as a value judgment or complete truth/rights determination.

A future 00J-A02 could therefore ask whether a strong C2PA/Content-Credentials implementation closes the source-dependency gap more efficiently than PANO-H1/H2.

---

## 14. Evidence-source freeze and dating

**Evidence freeze:** 24 September 2026.

| Source | Public date / version used | Role in this profile |
|---|---|---|
| **FG-TIDA Theme #17** | Issue opened **31 Aug 2026**; public issue state reviewed 24 Sep 2026 | production-case boundary: publisher-side layers, agent-identity gap, evidence classes |
| **Panodyssey AI Transparency Notice launch** | page published **24 Mar 2026**; press-release dateline 20 Mar 2026 | source-side traceability / AI-use-control claim |
| **Panodyssey Notice V2.1 update** | **31 Aug 2026** | versioned correction of AI-readable signals; vendor statement |
| **Panodyssey licensed certified-human-content page** | **9 Jun 2026** | publication-by-publication / AI-by-AI permissions, licensing and TEMS context |
| **TEMS Trial 7 — Protecting and Valuing Cultural Content** | **17 Mar 2026** | fragmentation of metadata/licensing/rights information across systems |
| **TEMS Trial 7 — Making IP Visible and Actionable** | **17 Apr 2026** | origin/authorship/use-condition portability and Panodyssey Trial-7 role |
| **TEMS Trial 7 — How Rights Travel Across Systems** | **27 May 2026** | direct interoperability statement that origin/authorship/conditions can fragment or disappear across systems |
| **W3C ODRL Information Model 2.2** | Recommendation **15 Feb 2018** | scope-specific permission/prohibition/duty semantics |
| **C2PA Content Credentials 2.4** | **Apr 2026** technical specification; explainer lineage reviewed 24 Sep 2026 | derived/composed asset ingredients, bounded provenance semantics |
| **European Commission TDM opt-out registry study** | released **13 Jul 2026** | metadata-stripping / unreliable-processing evidence; registry ≠ licensing system boundary |

**Dating rule:** statements about the product/project surface are bounded to this evidence freeze. Later Panodyssey, TEMS, C2PA, standards or regulatory changes require an explicit source-basis refresh. H1/H2 remain synthetic implementation trajectories and are not back-attributed to the cited sources.

---

## 15. Current conclusion

The recommended first 00J implementation trajectory is:

> **PANO-H0 — strong publisher-side Panodyssey/Notice implementation**  
> → **PANO-H1 — premium/defended Panodyssey/TEMS + agent identity/mandate + proposition-bound receipt/source-lineage + stable Q5 resolver implementation**  
> → **PANO-H2 — exact frozen H1 under a resolver/identifier/lineage regime shift while the same Q5 enforcement proposition is held constant.**

This gives 00J the same architecture-testing discipline used in the LangGraph, Agent 365, Claude and Stripe profiles:

- do not compare against a strawman;
- let an excellent conventional implementation solve ordinary failures;
- freeze that excellent implementation;
- then change the material ecosystem relation without changing its code;
- test whether it recognizes that the old representation is no longer sufficient for the new decision.

**Status:** unexecuted implementation-trajectory draft; not a Panodyssey/TEMS product benchmark, incident report, certification or claim of comparative superiority.
