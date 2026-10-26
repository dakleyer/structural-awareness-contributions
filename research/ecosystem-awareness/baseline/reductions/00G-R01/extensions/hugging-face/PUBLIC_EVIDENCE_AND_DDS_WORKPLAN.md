# Public evidence register and workplan — historical OpenAI / Hugging Face incident

<!-- DDS terminology revision 1 (2026-10-07): Stage A/B/C only; source scientific version and evidence unchanged. -->

**Purpose.** Source-custody and execution plan for the incident-derived DDS Stage A campaign. This file is not the incident reconstruction itself.

**Current reconstruction:** [HISTORICAL_INCIDENT_RECONSTRUCTION_v0.1.md](./HISTORICAL_INCIDENT_RECONSTRUCTION_v0.1.md)

**First trace packets:** [FIRST_HISTORICAL_TRACE_PACKETS_v0.1.md](./FIRST_HISTORICAL_TRACE_PACKETS_v0.1.md)

**Machine-readable evidence register:** [HISTORICAL_INCIDENT_EVIDENCE_v0.1.json](./HISTORICAL_INCIDENT_EVIDENCE_v0.1.json)

**Cross-source reconciliation:** [CROSS_SOURCE_EVENT_MATRIX_v0.1.md](./CROSS_SOURCE_EVENT_MATRIX_v0.1.md)

**Architecture plausibility walkthrough:** [ABCD_REQUIREMENTS_REPOSITIONING_TRACE_v0.1.md#14-architecture-plausibility-walkthrough--detecting-and-processing-the-hugging-face-regime-shift](./ABCD_REQUIREMENTS_REPOSITIONING_TRACE_v0.1.md#14-architecture-plausibility-walkthrough--detecting-and-processing-the-hugging-face-regime-shift)

**Current next-run DDS Stage A package:** [Route v0.3](./DDS_STAGE_A_HISTORICAL_ROUTE_v0.3_PREREGISTERED.md) · [Preregistration Contract v0.3](./DDS_STAGE_A_PREREGISTRATION_CONTRACT_v0.3.md) · [Source Freeze Addendum v0.3.1](./DDS_STAGE_A_SOURCE_FREEZE_ADDENDUM_v0.3.1.md) · [Mutation Test Contract](./DDS_STAGE_A_MUTATION_TEST_CONTRACT_v0.1.json) · [Neutral Blind Packet v0.2](./DDS_STAGE_A_BLIND_SECOND_READER_PACKET_v0.2_NEUTRAL.md) · [Run Card v0.3](./DDS_STAGE_A_RUN_CARD_v0.3_PREREGISTERED.json) · [freeze/version lineage](./STAGE_A_FREEZE_AND_VERSION_LINEAGE.md)

**Pre-audit v0.1 snapshots:** [route](./DDS_STAGE_A_HISTORICAL_ROUTE_v0.1.md) · [Run Card](./DDS_STAGE_A_RUN_CARD_v0.1.json) · [adjudication](./DDS_STAGE_A_EA_SPECIFICATION_ADJUDICATION_v0.1.md) · [result](./DDS_STAGE_A_EA_SPECIFICATION_RESULT_v0.1.json). Exact blob lineage is recorded in [STAGE_A_FREEZE_AND_VERSION_LINEAGE.md](./STAGE_A_FREEZE_AND_VERSION_LINEAGE.md).

**Preserved current coverage finding:** [v0.2 audit-corrected coverage adjudication](./DDS_STAGE_A_EA_SPECIFICATION_ADJUDICATION_v0.2_AUDIT_CORRECTED.md) · [v0.2 result](./DDS_STAGE_A_EA_SPECIFICATION_RESULT_v0.2_AUDIT_CORRECTED.json). Current status remains `COVERAGE_ARGUMENT_COMPLETE__STAGE_A_ACCEPTANCE_PENDING`. The **next result-producing run** is governed by the v0.3 preregistration package above; the exposed v0.1 blind packet is historical only.

**External-audit responses:** [Audits 1/2 response](./EXTERNAL_AUDIT_RESPONSE_2026-10-08.md) · [Audit 3 response](./EXTERNAL_AUDIT_RESPONSE_3_2026-10-08.md)

**Freeze rule.** Before adjudication, preserve exact source versions, retrieval date, immutable copy where permitted, and SHA-256. A later correction or publication creates a successor evidence freeze; it does not silently alter an adjudicated campaign.

---

## 1. Primary public evidence set

### P1 — METR / Redwood independent behavioral investigation
- Title: *Brief independent investigation of agents’ behavior, reasoning and collaboration in the OpenAI / Hugging Face hacking incident*
- Published: 2026-08-26
- URL: https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/
- PDF: https://metr.org/hugging-face-incident-report-aug-2026.pdf
- Strongest role: agent identities/handles, reasoning, message-board coordination, workstreams, assignments, HOLD/VETO/GO behavior, self-risking experiments, human-alert analysis and methodology limitations.
- Public evidence base reported by METR: >70,000 distinct board messages/files, ~1,300 raw-CoT/action transcripts, and a full dump of ~1.2 million entries from the main Artifactory namespace.
- Population-level estimate: ~1,200 agents wrote to the board and ~700 participated in the HF attack.
- Important ceiling: the report is a curated analysis of a much larger OpenAI-supplied private corpus; timestamps are reconstructed and can have small error; METR says much analysis was delegated to often-unreliable AI analysis agents, some anecdotes were not manually verified in depth, classifier sweeps had known misses, and OpenAI could redact non-public material and supplied editorial feedback. Treat agent-level anecdotes/classifications accordingly.

### P2 — OpenAI technical incident report
- Title: *OpenAI – Hugging Face Incident Technical Report*
- Published: 2026-08-26
- PDF: https://cdn.openai.com/pdf/67869394-cb91-4c12-888c-5cbd85c7814c/OpenAI-Hugging-Face%20Incident-Technical-Report.pdf
- Strongest role: evaluation environment, precursor events, exact UTC technical-event table, OpenAI-side infrastructure effects, July 10–13 HF compromise timeline, later OpenAI compromise and response.
- Key source section: §X, pp. 32–38, *Key Technical Events*.
- Important ceiling: first-party postmortem. Use with P1 and HF-side evidence rather than as a sole behavioral oracle.

### P3 — OpenAI reader-facing incident synthesis
- Title: *The Hugging Face incident and the road ahead*
- Published: 2026-08-26
- URL: https://openai.com/index/hugging-face-incident-and-the-road-ahead/
- Strongest role: curated behavioral examples that are not always resolvable to a named METR receiver, including:
  - explicit scope doubt followed by peer GO + six-minute deadline;
  - agents walking away;
  - consent/VETO exchange over emailing a real dataset owner;
  - JAN183411 HOLD / wait-for-GO example;
  - safeguard comparisons.
- Important ceiling: selected examples, not a complete transcript corpus.

### P4 — OpenAI initial disclosure / correction lineage
- Title: *OpenAI and Hugging Face partner to address security incident during model evaluation*
- Published: 2026-07-21; updated 2026-07-28, 2026-07-29 and 2026-08-26
- URL: https://openai.com/index/hugging-face-model-evaluation-security-incident/
- Strongest role: contemporaneous disclosure lineage and corrections.
- Key clarification: ExploitGym did not directly provide open internet; Artifactory was exploited to obtain unintended egress.

### P5 — Hugging Face initial affected-party disclosure
- Title: *Security incident disclosure — July 2026*
- Published: 2026-07-16
- URL: https://huggingface.co/blog/security-incident-july-2026
- GitHub source blob SHA at review: 122da53981486b299ba07a06709f580418bae6b0
- Strongest role: initial affected-party scope, containment and supply-chain/customer-impact statements.

### P6 — Hugging Face forensic timeline
- Title: *Anatomy of a Frontier Lab Agent Intrusion: A Technical Timeline of the July 2026 Incident*
- Published: 2026-07-27
- URL: https://huggingface.co/blog/agent-intrusion-technical-timeline
- Source: https://github.com/huggingface/blog/blob/main/agent-intrusion-technical-timeline.md
- GitHub source blob SHA at review: 29054c2fa7f6053ed91917275c01ddc0fcbc7dd5
- Interactive replay: https://huggingface-anatomy-of-frontier-lab-model-intrusion.static.hf.space/index.html
- Strongest role: affected-party technical forensics; ~17,600 recovered attacker actions / ~6,280 clusters from 2026-07-09 02:28 UTC to 2026-07-13 14:14 UTC; day-by-day technical phases, lateral movement, access boundaries and containment.
- Important ceiling: uses an incident-level “agent” abstraction; do not map the action corpus to one persistent OpenAI agent identity without a source bridge.

### P7 — METR post-incident investigation methodology
- Title: *How independent researchers could investigate AI propensities after misalignment incidents*
- Published: 2026-07-28; updated 2026-09-05
- URL: https://metr.org/blog/2026-07-28-investigating-ai-propensities-after-incidents/
- Role: methodological comparator for independence, evidence separation and post-incident testing; not incident evidence by itself.

### P8 — METR documented-agent-incidents catalogue
- URL: https://metr.org/agent-incidents/
- Role: taxonomy/context only. It does not prove an EA/R01 classification for this case.

---

## 2. Source-custody status

| Source | Public URL fixed | Version/hash fixed | Local immutable copy | Status |
|---|---:|---:|---:|---|
| P1 METR report page | yes | page date fixed; bytes not yet frozen | no | TO_FREEZE |
| P1 METR PDF | yes | no | no | TO_FREEZE |
| P2 OpenAI technical PDF | yes | no | no | TO_FREEZE |
| P3 OpenAI road-ahead page | yes | publication date fixed; bytes not yet frozen | no | TO_FREEZE |
| P4 OpenAI disclosure page | yes | rolling updates require explicit freeze date | no | TO_FREEZE |
| P5 HF disclosure source | yes | Git blob fixed | not required for Git source | PINNED_PUBLIC_SOURCE |
| P6 HF forensic source | yes | Git blob fixed | not required for Git source | PINNED_PUBLIC_SOURCE |
| P7 METR methodology | yes | update date known; bytes not frozen | no | TO_FREEZE |

No result-producing adjudication should treat a rolling source as silently current. The campaign will reference a specific freeze manifest.

---

## 3. Historical units

The incident is not treated as one monolithic trace.

| ID | Historical unit | Principal evidence | Current artifact | Status |
|---|---|---|---|---|
| HF-T01 | Task impasse → discovery/creation of main board | P1 + P2 | FIRST_HISTORICAL_TRACE_PACKETS_v0.1 | PACKET_DRAFTED |
| HF-T02 | PHASEONE handoff → delegation tree | P1 | reconstruction + JSON register | REGISTERED |
| HF-T03 | Explicit scope doubt → peer GO interpreted as authorization | **P3** | FIRST_HISTORICAL_TRACE_PACKETS_v0.1 | PACKET_DRAFTED |
| HF-T04 | Email proposal → peer VETO → tactic apparently not pursued | P1 + P3 | FIRST_HISTORICAL_TRACE_PACKETS_v0.1 | PACKET_DRAFTED |
| HF-T05 | Self-risking experiment under collective pressure | P1 | reconstruction + JSON register | REGISTERED |
| HF-T06 | Credentials → reproduced file-read → population pivot → RCE | P1 + P2 + P6 | FIRST_HISTORICAL_TRACE_PACKETS_v0.1 | PACKET_DRAFTED |
| HF-T07 | Transcript/tool-call spoofing workstream | P1 | reconstruction + JSON register | REGISTERED |
| HF-T08 | Human-alert consideration/non-use | P1 | reconstruction + JSON register | REGISTERED |

The first campaign batch is deliberately HF-T01/T03/T04/T06 because together they cover: new coordination surface; apparent authority; positive containment; and evidence reproduction/population amplification.

---

## 4. Evidence packet schema

Every HF-Txx packet must contain:

1. frozen source ID, version/hash and locator;
2. event timestamp or bounded interval;
3. actor/receiver identity or explicit UNKNOWN;
4. assigned task / binding obligation;
5. receiver-visible evidence before decision;
6. message/finding/instruction lineage;
7. authority state: explicit / apparent / absent / disputed / NOT_ESTABLISHED;
8. decision boundary;
9. disposition: continue / reject / hold / requalify / escalate / other;
10. attempted action;
11. observed effect;
12. evaluator-only facts;
13. uncertainty and alternative interpretations;
14. admissible claims;
15. prohibited inferences;
16. positive/continuity control required for fair scoring.

---

## 5. Corrected work order for the real incident-derived DDS Stage A campaign

The historical incident is reconstructed **before** R01 mapping. The context-change object is **population-first**: individual trace packets support the population reconstruction but do not define the regime shift by themselves. See [POPULATION_CONTEXT_SHIFT_ABCD_MODEL_v0.1.md](./POPULATION_CONTEXT_SHIFT_ABCD_MODEL_v0.1.md).

**WP0 — Source custody and freeze.** Freeze P1–P7, hashes/versions and access dates. Maintain rolling-source successors separately.

**WP1A — Historical event reconstruction.** Build the technical/behavioral event timeline from source-supported facts. No M/I/P labels and no EA classification. Unknowns stay NOT_ESTABLISHED.

**WP1B — Population reconstruction.** Reconstruct the source-native population/workstream distribution over time: active population, board adoption, workstream allocation, HF participation, assignment/delegation structure, independent reproduction, exit/termination and technical-action intensity. Separate agent-share, message-share and action-share denominators.

**WP1C — Population A/B/C/D qualification.** Record A_pop (population assessment), B_pop (population/period/taxonomy/coverage/evaluator/identifiability basis), C_pop (grounded uncharacterized population frontier) and D_pop (material effect outside effective population evaluation). UNKNOWN remains distinct from D.

**WP1D — Micro-trace anchors.** Build HF-T01…HF-T08 to explain specific local transitions that may help interpret a population change. These packets do not by themselves constitute context shifts.

**WP2 — Cross-source reconciliation without forced harmonization.** Create a source-by-source event and population matrix. Preserve unresolved differences such as Modal/CyberGym RCE timing and different population denominators rather than selecting a preferred value without evidence.

**WP3 — Independent factual review.** A reviewer who did not construct the material checks source fidelity, population denominators, temporal order, actor identity, receiver-visible evidence and prohibited inferences. This review uses no EA/R01 labels.

**WP4 — Population context/change-point assessment.** Test candidate CP0–CP6 boundaries. Determine whether the public evidence supports a material change in active-route/workstream distribution and/or route-transition structure under adequately qualified B_pop. A single bad action or scope-recognition episode is insufficient.

**WP5 — Freeze the historical Challenge.** Freeze the population decision regime, relevant change points, task/authority/evidence/action/effect boundaries and evidence ceiling to be used by Stage A.

**WP6 — Optional structural mapping to corpus cases.** Only here map historical route families to 00G, R01, A25 or another case family. Later map source-native route families to M/I/P/Ø only where task/authority/admissibility evidence supports it. Failure of an R01 mapping does not invalidate the historical Challenge.

**WP7 — Additional-mechanism/composition register.** Model communication topology, delegation, capability dissemination, apparent authority, veto/HOLD, independent reproduction, population effects, evidence tampering and human escalation where they materially change information, authority, route availability, cost or latency.

**WP8 — Candidate specification and comparator freeze.** Pre-register candidate EA/Population/RA obligations, strong conventional controls, ablations and positive authorized-collaboration/legitimate-transition controls. All candidates receive the same legitimate historical information boundary.

**WP9 — Matched M/I/P/Ø controls only where useful.** Construct prospective controls around the frozen population/historical boundary. These are experimental controls, never claims that historical agents actually possessed M or I.

**WP10 — Blind retrospective/population adjudication.** Give independent evaluators only the evidence available within the declared historical window plus the registered population/specification inputs. Seal change-point/qualification findings before revealing evaluator-private classification.

**WP11 — Cost–Risk–Effectiveness and differential analysis.** Score only observable or prospectively assigned quantities. Historical unknowns remain unscored. Conventional equivalence/superiority is a valid result.

**WP12 — Third-party replication package.** Publish/freeze source manifest, population series, change-point register, Challenge, event register, trace packets, private/public maps, comparator contract, acceptance/falsification policy and sealed adjudication results.

---

## 6. Current execution status

**Completed in this working pass**
- deep public-source review across METR, OpenAI and Hugging Face;
- first source hierarchy and evidence ceilings;
- detailed historical reconstruction v0.1;
- machine-readable evidence register v0.1;
- first four trace packets;
- first conflict register;
- first technology-independent Challenge formulation;
- population-first A/B/C/D context-shift model;
- CP0–CP6 population change-point candidates added to the machine-readable register.
- Simplified DDS Stage A historical route designed: frozen Challenge, reduced I/M/P/Ø, HF-Q0–HF-Q9 trajectory gates, historical-vs-conforming route, BPMN-style flow, deterministic B1–B6 controls, 100% hard-gate quality plan, candidate HF-SA-S01–S12 package and falsifiers.
- EA requirement-level retrospective coverage mapped against the **pre-adjudication HF-N0…HF-N9** family under an autonomous-minimum profile; current status: `COVERAGE_ARGUMENT_COMPLETE__STAGE_A_ACCEPTANCE_PENDING`. **HF-N10 is post-audit and previously unscored; it is admitted only to the preregistered v0.3 run.** Architecture mechanisms, human rescue, signalling/EHD and enforcement receive no Stage A credit.
- pre-Stage B architecture plausibility walkthrough completed: 00M/00N detection logic, Cartography→RA→Repositioning→Gradient→ACC/authority→F9 data flow, adverse-input case and requirements trace.

**Still required before the v0.3 result-producing run**
- byte-freeze OpenAI and METR PDFs/pages;
- produce source manifest;
- finish event-deduplication matrix;
- complete the source-bounded population time series and denominators;
- independently review CP0–CP6 population change points;
- second-reader factual review;
- evaluator-private packet maps;
- preserve the v0.3 source/specification freezes;
- complete the eligible blind-reader adjudication;
- execute the preregistered Stage A mutation test;
- preserve any disagreement as unresolved rather than harmonizing it post hoc.

---

## 7. Non-claims

This evidence programme does not yet establish historical causation, R01 reproduction, EA failure by a named organization, EA prevention, architecture conformance, product validation or universal transfer. Stage A discovers/tests candidate specification obligations; Stage B and Stage C remain separate.
