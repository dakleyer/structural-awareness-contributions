# CU-HIB-01 — Hibernation and Current-Context Sufficiency

**Focused discussion note · FG-TIDA Theme #23 · 14 October 2026**  
**Status:** author-side research proposal; **not** a jointly agreed China Unicom case, executed test or normative requirement.

## The practical problem

An incident-response agent A was legitimately authorized to `isolate(R)` for a declared mission and then entered hibernation. During suspension, a separately governed critical service may have become dependent on R. The agent's identity, grant and original purpose may still look valid when it resumes, but **those facts alone do not establish that exercising the same action is still appropriate under current dependencies**.

In [her 14 October answer](https://github.com/FG-TIDA/themes/issues/23#issuecomment-6164646309), [Ying Wang / Theme #23](https://github.com/FG-TIDA/themes/issues/23) explicitly calls for current-context reassessment, acknowledges partial visibility and envisages restricted authorization or reapproval as legitimate responses. [Zhao's earlier suggestion](https://github.com/FG-TIDA/themes/issues/23#issuecomment-6072991126) was to record a factual restoration condition at suspension. [Ying's subsequent clarification](https://github.com/FG-TIDA/themes/issues/23#issuecomment-6165603429) specifies the **complete two-step checkpoint: validate the declared restore condition, then derive current intent from the current context**. The Zhao anchor-only proposal and Ying's two-step sequence should not be conflated.

## R1 → R2 → R3: do not assume an outcome

| Stage | What the case is testing |
|---|---|
| **R1: freeze the problem** | A legitimate old grant and original intent do not establish the continuing applicability of `isolate(R)` after a material dependency change during hibernation. |
| **R2: fully repair and freeze the solution** | Implement and test Ying's complete checkpoint with all defensible native graph, freshness, policy, telemetry, event-subscription, source-access and authorized fallback mechanisms. A competent R2 may solve the known change completely. |
| **R3: test a further material contextual change against that genuinely frozen R2** | When the minimum **owner-required current proposition P** can no longer be sufficiently established by the R2 checking process, determine which assumption remains open and what the authorized route is. An **unavailable source or stale snapshot by itself is a known R2 family**, not proof of a new R3. Admission of any R3 requires a distinct, lawfully observable, policy-material change outside R2's effective coverage. |

**Core question for Ying — independent of which participant supplies P:**

> When an agent emerges from hibernation and the locally verifiable parts of its pre-declared restore condition are satisfied, but a material current-context proposition needed to complete validation is still **not established**, how does your two-step checkpoint represent that incomplete result, and which owner/source is responsible for targeted re-evaluation before the agent can resume the original action?

This is **not** a request to repeat the already acknowledged restricted/reauthorization outcomes; it concerns the **location, evidential meaning and bounded return path** of incomplete contextual verification. If P is required for the restore condition, step one **must not be described as fully passed** merely because the other checks succeeded.

**Optional illustration, secondary to the question:** P may depend on information held by another hibernating participant. If that participant is an AI agent whose evidential privilege is itself suspended under Theme #23, a cross-lifecycle verification dependency *might* be an admissible R3. If it is a CMDB/PIP or other infrastructure outside that lifecycle, or the only issue is old/unavailable data, classify that variant as known R2 calibration. If no distinct R3 qualifies, report **R3 NOT_ADMITTED**, without fabricating a failure or changing the source facts.

## Why ecosystem-level information might be relevant

Other independently governed participants may preserve qualified **indications of contextual movement** or different limits on their own assessments. Where scope, ownership and provenance genuinely correspond, their **non-fungible composition** could identify whether to request a characterized verification, explore a plausible but uncharacterized avenue, or preserve a residual that the present evaluator cannot resolve. That **does not authorize GO**, prove the hidden dependency or replace the owner of P. A competent native controller providing the same qualification earns full credit.

The plausibility and sufficiency conditions are already developed in [00N — *Can Ecosystem Awareness Work?*](https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/baseline/00N_FROM_MECHANISM_TO_REQUIREMENTS_SCIENTIFIC_PLAUSIBILITY_v0.7_RESEARCH_NOTE.md), grounded in the [00M mathematical interpretation](https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/baseline/00M_ABCD_AND_MATHEMATICAL_PLAUSIBILITY_v0.8_RESEARCH_NOTE.md). No new general EA defence or untested superiority claim is needed here. Experimental framing: [DDS Stage A](https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1.md) and [FG-TIDA UC-21](https://github.com/FG-TIDA/use-cases/issues/21).

**Technical backup only:** [CU-HIB-01 detailed evidence/source-suspension cases](CU_HIBERNATION_R123_CONTEXT_VERIFICATION_SOURCE_ASLEEP_v0.1.md). The detailed file is an author-side working record, including AI-assisted adversarial critique, **not independent peer review**. No comment has been sent to Ying and no scored R2/R3 trial has been run.
