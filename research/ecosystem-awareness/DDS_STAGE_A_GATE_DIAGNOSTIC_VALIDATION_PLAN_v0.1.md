# DDS Stage A — Gate Diagnostic Validation Plan v0.1

**Status:** preregistered validation plan for the draft gate diagnostic profile · no completed validation claim.  
**Date:** 8 October 2026.  
**Gate profile:** [DDS Stage A Gate Diagnostic Profile v0.1 Draft](./DDS_STAGE_A_GATE_DIAGNOSTIC_PROFILE_v0.1_DRAFT.md)  
**Gate catalog:** [DDS Stage A Gate Catalog v0.1 Draft](./DDS_STAGE_A_GATE_CATALOG_v0.1_DRAFT.json)

## 1. Purpose

The gate catalog must not be promoted merely because it explains the Hugging Face audit well.

This plan freezes three materially different validation families before the catalog is revised again.

## 2. Frozen validation families

### V-A — historical / incident-derived family

**Family:** Hugging Face / METR-derived Stage A package under 00G-R01.  
**Role:** adversarial historical specification test.  
**Use:** test whether the generic catalog can express the already audited distinctions, including authority applicability, self-certified identity, self-report/effect evidence, conscious mandate displacement, positive continuity and external execution ownership.  
**Independence ceiling:** low for catalog validation because this family materially informed the design discussion. It can expose contradictions, but cannot by itself validate completeness/generalization.

### V-B — mathematical / reduced family

**Family:** 00G-R01 probabilistic reduction core.  
**Role:** check that the catalog does not assume only documentary authority incidents or conversational-agent behavior.  
**Use:** identify which gates are genuinely applicable to a mathematical/reduction profile and which must be NOT_APPLICABLE without penalty.  
**Key falsifier:** if the catalog forces irrelevant identity/authority gates into every reduction, the catalog is overfitted and must be revised.

### V-C — non-HF technology/configuration family

**Family:** 00I-A01 AWS Step Functions / RDS implementation-trajectory profile.  
**Role:** non-HF technology/configuration stress test.  
**Use:** check whether gate results can be produced from a strong conventional workflow/orchestration mechanism without translating AWS-native semantics into EA-native vocabulary.  
**Key falsifier:** if the gate model cannot distinguish “not a responsibility of this technology/profile” from “missing inside claimed scope”, the profile is not portable enough.

## 3. Frozen validation questions

For each family:

1. Which SA-G00…SA-G14 gates are applicable?
2. Can every applicable gate receive one base verdict and one level without forced semantic translation?
3. Do hard dependencies create any false blocking?
4. Does at least one gate become NOT_APPLICABLE legitimately?
5. Can a missing prerequisite be reported once as a root blocker rather than as multiple independent failures?
6. Does the Stage-B handoff remain clearly separate from the Stage-A verdict?
7. Does the profile produce a more informative result than a single overall PASS/FAIL?
8. Is any local gate needed?
9. Is any core gate redundant with another?
10. Is any gate impossible to falsify under the selected family?

## 4. Catalog-change rule

After results are produced:

- no gate ID/meaning is edited in place;
- any material gate merge/split/dependency change creates catalog v0.2;
- original V-A/V-B/V-C results remain pinned to v0.1;
- a new local gate remains local unless at least two materially different families justify promotion;
- Hugging Face-specific IDs or EA S#/T# clauses may map to core gates but never redefine them.

## 5. Promotion criterion

The gate diagnostic profile may move from “draft for validation” to a stronger working status only if:

- all three families can be represented without semantic translation;
- dependency logic does not create a known false PASS or false FAIL;
- NOT_APPLICABLE and NOT_ESTABLISHED remain distinguishable;
- at least one useful root-blocker/remediation recommendation is produced in two different families;
- no family requires a hidden aggregate score to make the result interpretable;
- limitations and any catalog revisions are published.

Until then, the gate catalog remains a draft diagnostic layer.
