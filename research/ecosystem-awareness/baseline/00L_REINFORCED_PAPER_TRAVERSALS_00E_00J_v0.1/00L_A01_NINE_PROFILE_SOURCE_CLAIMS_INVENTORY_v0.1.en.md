<!-- English language edition of 00L_A01_INVENTARIO_FUENTES_NUEVE_PERFILES_v0.1.md; source commit 51fc686f45b6ef10c53b69f4c26d0e381b007ff8, blob aee756269b119b4253e0fbd5a6a86aaf8bb23302. Translation only: original, evidence status and scientific claims unchanged. -->

# 00L-A01 — Inventory of claims from the nine profiles

**Inventory consultation date:** 2026-09-25. The dates for each source are those stated in the current profiles; a live page is not considered frozen merely because it includes a URL.

| Profile | Decisive claim that may be used | Primary source / declared section | Date or version | Classification and gap |
|---|---|---|---|---|
| 00E-A01 Agent 365 | registration, relationships, permissions and observability of supported agents | M2–M7, §10 of the profile | docs updated 30 Apr–7 Jul 2026 | documented capability; check the live page and distinguish first-party/third-party agents |
| 00E-A02 LangGraph/LangSmith | persistence, interrupts, traces and evaluation make it possible to build reinforced controls | L1–L7, §12 | LangGraph 1.2.12; LangSmith SDK v0.14.0, 21 Sep 2026 | documented capability + proposed implementation; no proof of native EA semantics |
| 00F-A01 FIWARE/Orion-LD | broker, subscriptions, context sources and NGSI-LD support context distribution | F1–F7, §13 | Orion-LD 1.12.0; ETSI GS CIM 009 V1.9.1 | documented capability; do not attribute systemic coherence to the broker |
| 00F-A02 AWS IoT TwinMaker/Core | twin, connectivity, rules and shadows represent distributed state | A0–A6, §13 | A0 published 14 Sep 2026; live pages consulted 24 Sep | documented capability; mission coherence requires additional implementation |
| 00G-A01 OpenAI stack | agents, handoffs, guardrails, compaction and tracing offer control surfaces | O1–O9, §17.12 of scenario 00G | announcements 2025–2026; live docs 24 Sep | documented capability; source-dependence and authority are implementation hypotheses |
| 00H-A01 Claude Agent SDK | PreToolUse hooks may allow, deny, ask, modify or defer before tool use | §1 and §12 of the profile; hooks/subagents/compaction | docs consulted 24 Sep 2026 | documented capability; mandate, campaign and root authority are constructed controls |
| 00H-A02 Stripe Radar | rules, attributes, counters and reviews cover payment-risk dimensions | §4 and §12 of the profile | docs consulted 24 Sep 2026 | documented capability; Radar does not itself authorize business campaigns or refunds |
| 00I-A01 Step Functions/RDS | Wait/Task/Choice, AWS integrations, RDS and version control allow a state machine | §1–§3 and §15 of the profile | official docs consulted 24 Sep 2026 | documented capability; semantic requalification at T2 is a proposed implementation |
| 00J-A01 Panodyssey/TEMS | transparency notice, rights and portability offer provenance/interoperability signals | P1–P8, §2 and §14 of the profile | public sources and standards declared in 2026 | capability documented according to the source; H1/H2 cannot be attributed to Panodyssey/TEMS |

## Editorial corrections applied by this package

- Profile 00E-A01 v0.2 is treated as the source review of 24 September; the residual reference to v0.1 is identified for correction in the profile itself and is not reinterpreted here.
- 00E/00F retain the distinction between the original analysis of 17 September and the source update of 24 September.
- For Claude, Stripe and AWS, the consultation date is recorded; until a release, history or frozen excerpt exists, claims dependent on a live page are classified as `CAPACIDAD_DOCUMENTADA_NO_CONGELADA`.

## Evidence rule

A row authorizes only the short statement indicated. It does not authorize inferring that the product detects regime change, knows business authority, preserves an opportunity or passes a trace. Those capabilities must be presented as a proposed implementation, a synthetic fact or `NO CONCLUSION`.

## Exact routes for provenance auditing

The M/L/F/A/O/P identifiers in the table above are **internal indexes within each profile**, not external citations newly verified by 00L. Consult the primary source, section and date within the linked profile; for a publishable statement about current functionality, freeze the external page/version again. This matrix does not claim that the nine live sources were consulted again on 25 September.

| Inventory profile | Repository document |
|---|---|
| 00E-A01 | [Agent 365 v0.2](../00E_A01_MICROSOFT_AGENT_365_IMPLEMENTATION_PROFILE_v0.2_DRAFT.md) |
| 00E-A02 | [LangGraph/LangSmith v0.2](../00E_A02_LANGGRAPH_LANGSMITH_IMPLEMENTATION_PROFILE_v0.2_DRAFT.md) |
| 00F-A01 | [FIWARE/Orion-LD v0.2](../00F_A01_FIWARE_NGSI_LD_IMPLEMENTATION_PROFILE_v0.2_DRAFT.md) |
| 00F-A02 | [AWS IoT v0.1](../00F_A02_AWS_IOT_TWINMAKER_CORE_IMPLEMENTATION_PROFILE_v0.1.md) |
| 00G-A01 | [OpenAI stack v0.1](../00G_A01_OPENAI_AGENTS_STACK_IMPLEMENTATION_PROFILE_v0.1_DRAFT.md) |
| 00H-A01 | [Claude v0.4](../00H_A01_CLAUDE_AGENT_SDK_IMPLEMENTATION_PROFILE_v0.4_DRAFT.md) |
| 00H-A02 | [Stripe Radar v0.4](../00H_A02_STRIPE_RADAR_IMPLEMENTATION_PROFILE_v0.4_DRAFT.md) |
| 00I-A01 | [AWS Step Functions/RDS v0.2](../00I_A01_AWS_STEP_FUNCTIONS_RDS_IMPLEMENTATION_PROFILE_v0.2_DRAFT.md) |
| 00J-A01 | [Panodyssey/TEMS v0.1](../00J_A01_PANODYSSEY_TEMS_RIGHTS_PORTABILITY_IMPLEMENTATION_PROFILE_v0.1_DRAFT.md) |
