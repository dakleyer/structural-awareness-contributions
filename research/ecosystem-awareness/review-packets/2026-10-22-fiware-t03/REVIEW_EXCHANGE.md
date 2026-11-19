# UC21 / S2 / T03 — FIWARE technical review and Tegrity.AI response (22–23 October 2026)

**Record type:** author-maintained, attributed **documentary technical-review exchange**, drawn from the original email correspondence.  
**Record prepared:** 19 November 2026 · **Status:** review comments received; Tegrity.AI clarification sent; subsequent technical confirmation **not received** in the checked thread.  
**Evidence level:** third-party factual/technical review of a **hypothetical documentation-based walkthrough**; **not** an executed FIWARE product test, independent validation, an endorsement by FIWARE Foundation, or adoption by FG-TIDA/ITU.  
**Source correspondence:** Chandra Challagonda, **22 October 2026**, subject *FG-TIDA, ITU’s focus group on trust and identity for humans and AI agents*; Tegrity.AI reply by Iván Abril Palma, **23 October 2026**, same thread, with first clarification attachment *Tegrity UC21 T03 V2.pdf*. Original correspondence and full attachments are retained in the author's restricted email evidence; this public record excludes private message headers, telephone numbers, automatic replies and irrelevant personal details.

## 1. Scope, attribution and agreed communication channel

The eight technical observations below were **written by Chandra Challagonda (CEO, FIWARE Foundation)** in his email of 22 October. Chandra included or invited the following colleagues in the exchange: **Juanjo Hierro** (Chair, FIWARE Technical Steering Committee), **Martin Bauer** (Vice Chair, FIWARE Technical Steering Committee), **Franck Le Gall** (EGM CEO and ETSI TC DATA Vice Chair), and **Alberto Abella** (Smart Data Models lead). They were requested to examine particular technical questions; **being copied or invited is not evidence that any of them individually authored, endorsed or approved the eight observations or the reply**.

Chandra offered a choice between feedback **by email or directly on GitHub** to coordinate a consolidated response. Tegrity.AI selected email for the technical exchange, expressly stating on 23 October: **“Email would suit us for your consolidated technical feedback, however, final revisions should live in github.”** The subsequent author-maintained public account below preserves the content and proper attribution without presenting the correspondence as an official FIWARE statement or disclosing the full private email archive.

## 2. Chandra Challagonda — technical observations received 22 October 2026

The numbered passages in this section reproduce the **technical content of Chandra's eight email bullets**, with their original scope, qualifications and ordering; the labels match his review. These are **reviewer observations**, not measurements from a product execution.

1. **Naming and scope.** “NGSI-LD is an ETSI specification, not a FIWARE product, and the FIWARE community offers several implementations (Orion-LD, Scorpio, Stellio).” Since T03 assessed **Orion-LD 1.12.0**, Chandra proposed the more precise title **“NGSI-LD context management as implemented in FIWARE (Orion-LD 1.12.0)”**.

2. **Distributed operations.** The Orion-LD implementation-status documentation reports forwarding, while its implementation is **not fully aligned with NGSI-LD v1.6**. Federation claims should therefore be qualified, or a broker focusing on federation should also be assessed.

3. **Source independence and the stress case (§§5.3, 7.2–7.3).** Choosing the most recent `observedAt` is a tutorial behaviour, **not a structural limit of NGSI-LD**. Multi-attributes (`datasetId`) preserve distinct per-source values; properties of properties can retain provider/upstream-processing provenance; and sensors, gateways and upstream dependencies can be modelled as queryable/subscribable entities and relationships. Chandra explicitly asked that the **defended R1 configuration include these capabilities**, since otherwise an apparent common-cause failure could merely be an omission in the scenario's modelling, not a technology limit.

4. **Missing or delayed feeds (Q1).** “Periodic subscriptions and temporal queries can surface absence and staleness instead of treating them as ‘no change’.” Actual broker/version support must be checked.

5. **Conflict logic (Q2).** Temporally valid corridor reservations can be represented as **NGSI-LD entities**, with compatibility checks through filtered subscriptions or stream processing; do not presume that a separate and vaguely named “purpose-built service” is the only possibility. Chandra suggested that a **Smart Data Model for resource-time reservations** might itself be useful.

6. **Trust and identity.** T03's generic “identity/access controls” treatment misses the **FIWARE Data Space Connector** and its verifiable-credential-based identity, ODRL policy enforcement and trust anchors. Chandra identified this as an especially relevant potential FIWARE contribution to FG-TIDA.

7. **Framing and responsibility.** The Q0–Q5 residual questions largely concern **context-management/data-exchange layers generally**, not shortcomings unique to FIWARE. Chandra asked for an explicit statement that the findings **are not FIWARE-specific product limitations**. The broker is not automatically the emergency commander.

8. **Editorial and versions.** Correct the numbering discontinuity **§9.1 → §12**, and check whether an ETSI NGSI-LD specification newer than **V1.9.1** had been published before fixing a standards version.

**Review participation:** Chandra explicitly sought additional specialist feedback on items 2 and 4 (broker behaviour), 3 (NGSI-LD specification), 5 (Smart Data Models) and 6 (data-space identity). The available email record does **not** establish a completed consolidated position from those colleagues.

## 3. Tegrity.AI / Iván Abril Palma — response sent 23 October 2026

This is a **close, selective restatement of the actual sent reply**, not a newly invented response, and not an acceptance by Chandra. The original email remains the authoritative full text.

**Recognition and delimitation.** “We hold ETSI NGSI-LD in high regard,” selected precisely for interoperable context management. The purpose is to give full credit to its strongest existing controls **before** suggesting any complementary requirement. “T03 was conceived as a hypothetical, documentation-based exploration of specifications and their applicability, rather than an assessment of a deployed FIWARE product or an audit of Orion-LD.” ETSI NGSI-LD, FIWARE architectural approaches and specific broker implementations must be distinguished.

**The changed-context example.** The reply proposes operating conditions evolving **C0 → C1** without a single city-wide trigger. Different agents observe different subsets, retain distinct responsibilities, evidence and time horizons, and can legitimately make **different local transitions**. A changed local condition for one actor does not automatically invalidate every other actor's route.

**Two separately testable questions.**
- **Residual indeterminacy:** an agent using its available controls may still lack sufficient evidence, before action is required, to determine whether material conditions have changed. Missing or degraded input is **not automatically a failure**: another decision may remain justified.
- **Partial communication of decisions:** two different evidentiary situations may yield the same outward message, for example **“ROUTE OPEN”**, even where the information supporting the sender's decision differs. The receiver may lack the relevant validity limits, dependencies or residuals. NGSI-LD can already convey richer information via `datasetId`, provenance, `Relationships`, temporal information and Smart Data Models; **the open research question is what must actually reach the receiving decision**.

**Central Bridge, S2.** Evacuation may require movement **east** over the bridge while fire/rescue requires **westbound** access. Other fleets may continue normally or enter HOLD. Locally reasonable decisions can combine into obstruction of a resource-time corridor. This is an **illustrative hypothetical**, not a prediction that the FIWARE stack fails.

**Strong conventional comparison first.** The reply acknowledges that well-modelled NGSI-LD can represent source provenance, dependencies, temporal validity, reservations, confidence/decision margins and conditions for review. Together with competent operating controls these can prevent many variants of Central Bridge, including some changed-context branches. These **successful defences must receive full credit**.

**Bounded question remaining.** Only if divergence remains plausible **after** crediting those mechanisms should a complementary interoperability profile be considered: is there a *requirement*, and not merely a possibility in a flexible data format, to convey decision-material uncertainty, dependencies, validity limits and requalification reasons to a relying actor as roles or conditions change? This is **not** a proposed defect or responsibility of ETSI NGSI-LD, and is not a proposal for FG-TIDA to standardise municipal traffic command.

**Candidate, not conclusion.** The reply mentions an optional mechanism for communicating non-fungible residual indeterminacy and provenance limits. It was presented only as **a research candidate for comparison** with existing implementations, not a prescribed architecture, proven advantage or FIWARE feature request. Other lines of study (human escalation, STAMP/STPA, coordination, incident command and trust controls) remain distinct but can be composed in a stronger prospective comparison.

**Practical next steps.** The reply offered to handle technical **documentation, version and attribution corrections** internally; attached the first clarification note; invited consolidated substantive feedback **by email** and committed that **final revisions should live in GitHub**. It also suggested, without claiming agreement, a more realistic data-based comparison that retains strong conventional controls, resource-time reservations, finite human review and realistic response deadlines. The author clarified that participation in FG-TIDA was **as an individual contributor**, not on behalf of the Focus Group.

## 4. Author-controlled disposition and follow-up

| Review area | Tegrity.AI documentation action | Status as of 19 November |
|---|---|---|
| Terminology, broker and normative version | Separate ETSI NGSI-LD, FIWARE architecture and **Orion-LD 1.12.0** claims; verify standard and broker version alignment | **Accepted for author-side editorial correction**; not a FIWARE sign-off |
| Federation and source dependence | Credit supported forwarding, `datasetId`, per-source/processing provenance and dependency graph modelling in the strong comparator | **Accepted for R1 competitor strengthening** |
| Missing feeds, Q1 | Include periodic/temporal absence detection where supported; check per broker release | **Accepted for version-bounded factual verification** |
| Corridor conflict, Q2 | Model temporal resource reservations in NGSI-LD with reasonable filtered/stream checks; retain any true remaining authority gap | **Accepted for strong comparator**; Smart Data Model suggestion open |
| Identity/trust | Describe Data Space Connector / VC / ODRL / anchors within the relevant source scope | **Accepted for review**; no conformance assertion |
| Non-FIWARE-specific scope | Explicitly state that the general failure hypothesis cannot be attributed to FIWARE itself | **Accepted for limitation statement** |
| Numbering and citations | Repair §9.1→§12 and verify referenced ETSI edition | **Accepted for editorial correction** |
| Additional empirical study | Separately consider a preregistered, costed DDS run against a frozen strong comparator | **Proposed, not agreed or executed** |

**Next author milestone — proposed 19 November:** prepare the corrected author-side T03/00F review disposition **before 30 November 2026**, maintaining a comparison of the strongest defensible conventional controls and publishing a versioned technical change note. **This date is a new Tegrity.AI planning target, not a deadline requested or agreed by FIWARE.** The source email of 23 October did not commit FIWARE to any response date.

**Open external status:** Chandra's 22 October comments are received and attributable; our 23 October reply is sent and attributable. No substantive acceptance, rejection, independent execution result or agreement to collaborate on a subsequent work item is inferred from the absence of a further reply. The technical reviewer remains free to correct this author-recorded account.

## 5. Public reading route (distinct objects and authorities)

- [FG-TIDA UC21 public proposal and historical provenance](https://github.com/FG-TIDA/use-cases/issues/21) — submitted proposal, **not adopted standard**.
- [Source-side T03 documentary annex](https://github.com/dakleyer/use-cases/blob/main/contributions/when-controls-work-system-fails/annexes/technology/T03.md) — author-controlled source text, **not native FIWARE test results**.
- [Ecosystem Awareness 00F-A01 FIWARE/NGSI-LD working profile](../../baseline/00F_A01_FIWARE_NGSI_LD_IMPLEMENTATION_PROFILE_v0.2_DRAFT.md) — separate working research profile.
- [00F Central Bridge / Smart City Challenge](../../baseline/00F_FAILURE_MODE_SMART_CITY_MOBILITY_SYSTEMIC_DIVERGENCE_v0.2_DRAFT.md) — constructed Challenge and controls.
- [DDS Stage A source](../../DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1.md) and [DDS method index](../../DDS_CANONICAL_METHOD_INDEX_v0.1.md) — method authority, separate from this review note.

**Documentary-integrity boundary:** This note records a review-and-response exchange and proposed source corrections. It does not retrospectively amend the pinned September source, modify a frozen scenario, assert that the four invited colleagues endorsed the comments, or confer FG-TIDA, FIWARE Foundation or ITU approval.
