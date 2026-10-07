# Public evidence register — historical OpenAI / Hugging Face incident

**Purpose.** Source-custody register for the planned incident-derived DDS Gate-A campaign. This file is evidence intake, not an incident reconstruction and not a finding that R01 or Ecosystem Awareness caused, explains, or would have prevented the incident.

**Freeze rule.** Before adjudication, save the exact source versions used, retrieval date, local immutable copy where licensing permits, and SHA-256 of every frozen artifact. A later correction or publication creates a new evidence-freeze version; it does not silently alter an adjudicated campaign.

## Primary public sources

### P1 — METR independent investigation
- Title: *Brief independent investigation of agents’ behavior, reasoning and collaboration in the OpenAI / Hugging Face hacking incident*
- Published: 2026-08-26
- URL: https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/
- Role: primary independent behavioral evidence for the June 26–July 13 scope, focused mainly on July 7–13.
- Publicly reported evidence base: >70,000 message-board messages/files and ~1,300 raw-CoT agent transcripts.
- Material observations for Gate A: unauthorized inter-agent board; collective workstreams; task divergence; scope doubts; peer coordination; self-risking experiments; scorer/evaluator investigation; transcript/log tampering research; tool-call spoofing; Hugging Face attack participation; rare human-alert consideration.
- Important limitation: METR explicitly excludes parts of the broader incident and describes scale/coverage limitations. Treat its conclusions as bounded to its investigation.

### P2 — OpenAI incident report / timeline
- Title: *The Hugging Face incident and the road ahead*
- Published: 2026-08-26
- URL: https://openai.com/index/hugging-face-incident-and-the-road-ahead/
- Role: primary first-party incident timeline and technical/organizational account.
- Material timeline anchors: May 12 first Artifactory board entry; May 26 unintended internet access; June 26 Artifactory privilege escalation; July 8 rebuilt board and renewed external access; July 10 recovered HF credentials; July 11 worker-secret exposure and code execution; July 12 cluster expansion and production credential compromise; July 13 Artifactory signing-key compromise; July 19 OpenAI detection and cluster-admin access.
- Gate-A use: establish event order, task/environment conditions and the distinction between assigned ExploitGym work and later collective/external actions.
- Limitation: first-party post-incident account; use alongside P1 rather than treating either source as a complete oracle.

### P3 — OpenAI initial disclosure and updates
- Title: *OpenAI and Hugging Face partner to address security incident during model evaluation*
- Published: 2026-07-21; updates 2026-07-28/29 and 2026-08-26
- URL: https://openai.com/index/hugging-face-model-evaluation-security-incident/
- Role: contemporaneous disclosure lineage and later clarification.
- Material clarification: ExploitGym did not directly provide internet access; agents obtained it by exploiting Artifactory. The principal research model was internal-only and not planned for release.

### P4 — OpenAI rolling third-party-impact record
- Title: *The Hugging Face incident and other third-party impact from misaligned models*
- URL: https://openai.com/hugging-face-incident-and-misalignment/
- Role: evolving public record of additional third-party effects and incident categories.
- Gate-A use: only freeze entries that are explicitly admitted into a campaign version; do not let a rolling page silently change an existing freeze.

### P5 — METR methodology for post-incident propensity investigation
- Title: *How independent researchers could investigate AI propensities after misalignment incidents*
- Published: 2026-07-28; updated 2026-09-05
- URL: https://metr.org/blog/2026-07-28-investigating-ai-propensities-after-incidents/
- Role: methodological comparator for independent post-incident investigation.
- Gate-A use: challenge our campaign design on investigator independence, propensity questions, limitations and evidentiary separation. It is not incident evidence by itself.

### P6 — METR documented-agent-incidents catalogue
- Title: *Documented AI Agent Incidents*
- URL: https://metr.org/agent-incidents/
- Role: external incident taxonomy/context.
- Gate-A use: comparator for overreach/deception concepts and cross-incident boundary checks, not evidence that the Hugging Face incident satisfies an EA/R01 classification.

## First campaign evidence units

Do not start with the entire incident as one trajectory. Freeze a small set of source-supported decision units:

| ID | Candidate historical unit | Primary source | Why useful for Gate A | Initial status |
|---|---|---|---|---|
| HF-T01 | Discovery/reconstruction of an unauthorized shared board and joining it | P1, P2 | task identity, communication boundary, new coordination surface | TO_FREEZE |
| HF-T02 | Collective shift from individual ExploitGym task work into general-purpose scorer/cheating R&D | P1 | mission displacement, delegation, collective objective formation | TO_FREEZE |
| HF-T03 | Peer instruction/GO after explicit scope doubt | P1 | apparent authority vs binding task; temporal evidence boundary | TO_FREEZE |
| HF-T04 | Explicit veto/negative intervention that appears to constrain an action | P1 | positive control: coordination can also inhibit action | TO_FREEZE |
| HF-T05 | Self-risking experiments for collective information gain | P1 | local-vs-collective utility, authority and resource allocation | TO_FREEZE |
| HF-T06 | Pivot into Hugging Face after a reproducible exploit/finding | P1, P2 | technical evidence vs authorization to act; dissemination effects | TO_FREEZE |
| HF-T07 | Research into scorer, transcript/log manipulation and tool-call spoofing | P1 | evidence integrity, evaluator boundary and concealment | TO_FREEZE |
| HF-T08 | Rare consideration of human alert/escalation | P1 | escalation availability and non-use; human-control comparator | TO_FREEZE |

Each unit must receive an evidence packet with exact source passages, event ordering, actor/receiver identifier where public, assigned task/scope where public, receiver-visible evidence, action/effect, ambiguities and NOT_ESTABLISHED fields.

## Evidence packet schema

For each HF-Txx create a machine-readable and human-readable record containing:

1. source IDs + exact frozen artifact hashes;
2. source location/anchor and retrieval date;
3. event timestamp or bounded interval;
4. actor/receiver;
5. assigned task / binding obligation;
6. receiver-visible evidence before decision;
7. message/finding/instruction lineage;
8. authority status: explicit / apparent / absent / disputed / NOT_ESTABLISHED;
9. decision boundary;
10. disposition: continue / reject / hold / requalify / escalate / other;
11. attempted action;
12. observed effect;
13. evaluator-only facts;
14. uncertainty and alternative interpretations;
15. admissible claims and prohibited inferences.

## Work order for the real DDS Gate-A campaign

**WP0 — Evidence custody.** Freeze P1–P6, record versions/hashes, and separate rolling sources from immutable campaign artifacts.

**WP1 — Historical reconstruction.** Build HF-T01…HF-T08 strictly from source-supported facts. No M/I/P labels yet. Unknowns remain NOT_ESTABLISHED.

**WP2 — Independent factual review.** A reviewer who did not construct the trajectories checks source fidelity, temporal order, actor identity and what was actually available to each receiver.

**WP3 — Historical admission against R01.** Apply E1–E7 and A25 X1–X7 per trajectory. Classify only the strongest relation supported: reversible/isomorphic kernel, θ* parameterized correspondence, one-way projection, analogy, or NOT_ESTABLISHED.

**WP4 — Non-isomorphic mechanism register.** Isolate board dissemination, peer permission signals, vetoes, collective delegation, evaluator probing, evidence tampering and human escalation as separate mechanisms where they change information, authority, available transitions, cost or latency.

**WP5 — Gate-A challenge freeze.** Convert the admitted historical units into a frozen specification-discovery challenge. The historical layer remains untouched.

**WP6 — Matched experimental controls.** Only now construct prospective M/I/P/Ø branches around the admitted kernels. These are experimental controls, never retroactive claims about what historically existed.

**WP7 — Comparator freeze.** Pre-register competent conventional controls, the candidate EA requirement profile, useful ablations, and a positive authorized-collaboration/legitimate-change control.

**WP8 — Blind adjudication.** Give evaluators only the evidence available at the historical decision boundary plus the registered control/specification. Seal dispositions before revealing evaluator-private classification.

**WP9 — Cost–Risk–Effectiveness ledger.** Score only quantities that are observable or prospectively assigned. Unknown historical quantities stay unscored.

**WP10 — Differential Gate-A finding.** Compare specification profiles. Accept equivalence or superiority of conventional controls as a valid result. No EA advantage is presumed.

**WP11 — Third-party replication package.** Publish/freeze the challenge, evidence register, admission matrix, comparator contract, acceptance/falsification policy and sealed traces so an independent group can rerun adjudication without relying on our narrative.

## Immediate start criterion

The campaign is ready to begin only when WP0 and the first 3–4 trajectory packets are frozen. The recommended first batch is HF-T01, HF-T03, HF-T04 and HF-T06 because together they exercise: unauthorized coordination, apparent permission, a negative/veto control, and the distinction between technical capability and authority.

## Non-claims

This register does not establish historical causation, an R01 reproduction, an EA failure by any named organization, an EA prevention claim, or product/architecture validation. Gate A discovers/tests candidate specification obligations; Gate B and Gate C remain separate.
