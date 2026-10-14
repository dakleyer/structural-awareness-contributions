# China Unicom / DDS Stage A — Self-audit, findings and corrective v0.2 review

**Date:** 14 October 2026. **Audited object:** initial PR [#21](https://github.com/dakleyer/structural-awareness-contributions/pull/21) at initial head 3c129488322d836372437d6df3dede88cd30eecb and source [FG-TIDA #23](https://github.com/FG-TIDA/themes/issues/23), Ying reply 14 October 08:54:54 UTC.  
**Reviewer:** author-side technical self-audit, **not** independent peer review, China Unicom approval or executable security assurance.  
**Outcome:** v0.1 appropriately bounded and source-attributed but incomplete for scientific Challenge admission. Corrected v0.2 design prepared. **LOCAL DESIGN SIGNOFF PENDING; DDS STAGE A RESULT NOT_ESTABLISHED.**

## 1. Audit basis and exclusion

Compared the original local [CAMPAIGN](CAMPAIGN.md), [Scientific Design](SCIENTIFIC_DESIGN.md), [Interface](INTERFACE_CONTRACT.md), [Trial v0.1](PRIMARY_TRIAL_PROTOCOL_DRAFT_v0.1.md), [Sources](SOURCES_AND_CUSTODY.md), [Run Card](RUN_CARD_PREPARATION.md), [Continuation](CONTINUATION.md) and parent campaign registry against:

- [DDS Index](../../DDS_CANONICAL_METHOD_INDEX_v0.1.md) and [Stage A](../../DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1.md): Challenge object, source reference, technology extension Stage 1/2, positive/negative controls, evaluator-private truth, I/M/P/Ø, Cost/Risk/Effectiveness and claim-boundary requirements;
- [DDS Stage B](../../DDS_GATE_B_ARCHITECTURE_VERIFICATION_v0.1.md) and [Stage C](../../DDS_GATE_C_IMPLEMENTATION_PROBLEM_VALIDATION_v0.1.md): later handoff/validation rather than automatic promotion;
- [DBC](../../DECISION_BOUNDARY_CHALLENGE_v0.2.md) and [00D benchmark](../../baseline/00D_CANONICAL_ARCHITECTURE_BENCHMARK_AND_REFERENCE_SCENARIO_EVIDENCE_v0.2.md): owner-preserving authorization, source-native result, strong comparator, value preservation and burden;
- [EA IF-S v0.5](../../baseline/04_GENERAL_FUNCTIONAL_INTERFACES_AGENTIC_SECURITY_v0.5_INTEGRATED.md), [00M](../../baseline/00M_ABCD_AND_MATHEMATICAL_PLAUSIBILITY_v0.8_RESEARCH_NOTE.md), [Theme #23](https://github.com/FG-TIDA/themes/issues/23) and Ying's [14 October answer](https://github.com/FG-TIDA/themes/issues/23#issuecomment-6164646309).

No actual PDP configuration, NACL, production graph, source-approved privilege rule, real run, independent evaluator, confidential data or ITU adoption was inspected. Findings refer to **documentary design** unless expressly stated.

## 2. Findings and decisions

| ID | Priority | Audited v0.1 gap or risk | v0.2 correction | Remaining |
|---|---|---|---|---|
| **CU-F01** | High | Primary story could change criticality and dependency together, preventing causal attribution | [Challenge §1](CHALLENGE_CONTRACT_v0.2.md): S critical at T0 and T2; **only edge S→R changes**. Static [casebook](fixtures/PUBLIC_CALIBRATION_VECTORS_v0.2.json) asserts a single world delta | Owner/evaluator must confirm materiality |
| **CU-F02** | High | “Choose R3 outside B2 coverage” postfreeze risks selecting only failures favorable to EA | [Challenge §6](CHALLENGE_CONTRACT_v0.2.md): predeclare event family and blind selection, keep all outcomes and parity; separate predeclared out-of-coverage stress | Independent selection and preregistration pending |
| **CU-F03** | **Critical—OPEN** | No source-approved action-policy precedence, admissibility exceptions, risk threshold or judge for “correct restoration” | [Challenge §2](CHALLENGE_CONTRACT_v0.2.md) now labels a **LOCAL SYNTHETIC reference**; [Approval D1/D2](APPROVAL_AND_PREREGISTRATION_v0.2.md) blocks actual scoring until accepted | **BLOCKS SCIENTIFIC ADMISSION** |
| **CU-F04** | High | No full source→candidate requirement→control→owner→evidence map | [Requirements matrix](REQUIREMENTS_TRACEABILITY_v0.2.md) has 22 S/E/L/M clauses with ownership, cases and gate status | No external normative adoption inferred |
| **CU-F05** | High | No indistinguishable-world control; risk scoring detection of inaccessible truth | [Challenge §7](CHALLENGE_CONTRACT_v0.2.md), CU-C3+/C3− same participant packet with different hidden edge | Structural calibration only, no run |
| **CU-F06** | High | Comparators proposed but actual B2 configuration, access/budgets/horizon not defined; semantic vs data-access benefit could be confounded | [Challenge §6](CHALLENGE_CONTRACT_v0.2.md), [Approval D2](APPROVAL_AND_PREREGISTRATION_v0.2.md): defended B2, equal legitimate source access, generic EA, cost and freeze | **BLOCKS SCIENTIFIC ADMISSION** |
| **CU-F07** | Medium | Qualification, authorization and observed effect could be treated as one result | [Challenge §§2/5/9](CHALLENGE_CONTRACT_v0.2.md) preserves native source, EA, PDP, PEP and oversight distinctions | Native receipts not available |
| **CU-F08** | Medium | Public calibration cases unstructured and without reproducible integrity checker | [12-case synthetic JSON](fixtures/PUBLIC_CALIBRATION_VECTORS_v0.2.json) and [stdlib verifier](tools/validate_challenge.py) | Static tests are not PDP or oracle evidence |
| **CU-F09** | Medium | Zhao's suspension-time restore predicate could be misread as approved China Unicom requirement | [Challenge §0](CHALLENGE_CONTRACT_v0.2.md), [Requirements CU-R03](REQUIREMENTS_TRACEABILITY_v0.2.md), [Sources](SOURCES_AND_CUSTODY.md): separately attributed suggestion | External interpretation open |
| **CU-F10** | Medium | No accountable multi-stage approval or responsible independent owners | [D0–D3 approval dossier](APPROVAL_AND_PREREGISTRATION_v0.2.md), empty signoff record | D0 signoff and D1–D3 not obtained |
| **CU-F11** | **Open** | No named domain decision owner, consent, privacy-sharing agreement, real testbed or independent adjudicator | Recorded as blockers and roles in [Approval §3](APPROVAL_AND_PREREGISTRATION_v0.2.md), not fabricated partners | **BLOCKS EXECUTION** |
| **CU-F12** | Medium | Risk of presenting a complete *document* as completed DDS A/B/C evidence | [Challenge §10](CHALLENGE_CONTRACT_v0.2.md) and [Approval](APPROVAL_AND_PREREGISTRATION_v0.2.md) distinguish D0 design from D2 admission, D3 results and later stages | Stages still not started |
| **CU-F13** | Medium | Positive restoration and false-hold safeguards lacked machine-inspectable expectations | CU-C0/C6 plus [Requirements §2](REQUIREMENTS_TRACEABILITY_v0.2.md) | Real positive demonstration pending |
| **CU-F14** | **Open** | Source discusses confidence/aggregation but no calibrated independence/weighting or universal numeric threshold | [Challenge §§2/9](CHALLENGE_CONTRACT_v0.2.md) and [Interface §6](INTERFACE_CONTRACT.md) preserve material B/D and refuse invented scores | **BLOCKS QUANTITATIVE CLAIMS** |
| **CU-F15** | Medium | GitHub comments are mutable, without frozen reference/oracle | [Sources/Custody](SOURCES_AND_CUSTODY.md) and D2 versioning/signature duties | Independent pin and accepted source policy pending |
| **CU-F16** | Low | Reader should find audited successor first without erasing v0.1 | Additive v0.2 notices to entry/registry/PR, preserved original files | Verify final diff/index after changes |

**Corrected means a design problem now has a documented remedy; it is NOT an empirical pass.** OPEN findings remain where external semantics, rights or independent reference observations cannot be supplied by self-audit.

## 3. DDS Stage A completeness assessment

| DDS segment | Design coverage | Evidence ceiling / gap |
|---|---|---|
| Challenge / task / actor / authority / world / horizon | Documented one-decision bounded CU-HIB-01 with current entitlement and single material edge event | Source policy, materiality and numerical horizon pending |
| Stage 1 technology correspondence | Partial declared mapping from #23 lifecycle to synthetic state transitions | **Analogy only**, not formal isomorphism or R01 transfer |
| Stage 2 additional mechanisms | Proposed EA/EHD context qualification and targeted re-entry alongside complete conventional PDP | No independent non-isomorphic differential proved |
| Route / trajectory gates | CU-G gates, I/M/P/Ø with unscored M until legitimacy demonstrated | Approval and source-owner action rules pending |
| Positive / negative / uncertainty controls | 12 public synthetic cases, including W+/W−, direct graph and restricted-grant checks | None are blinded/scored/native |
| Traversals, traces, Cost/Risk/Effectiveness | Prospective record/ledger and measured fields defined | No results, budget, cost or calibrated threshold |
| Acceptance, independent oracle, falsifiers | Null hypothesis, parity, known controls and review preconditions documented | **Not frozen and not independently adjudicated** |
| Business value | Informative service continuity, unnecessary interruption and review burden | No quantified economic projection |
| Stage B verification | Explicit future frozen-specification dependency | NOT_STARTED |
| Stage C implementation validation | Explicit originating-Challenge and target-effect dependency | NOT_STARTED |

**Classification:** **Simplified DDS Stage A, preparation for internal design approval**. “Unscored” means neither zero nor pass. Merely describing a trial does not generate a scientific Stage A result.

## 4. Author-side structural QA and limitation

At casebook creation, 12 declarative static checks were performed: valid case count/IDs; no observed results; constant criticality; exactly one primary S→R edge change; distinct evaluator worlds with identical visible packets; positive full-restoration controls; refusal to grant full rights in negative vectors; authorized observation separation; rooted correlation. A reproducible [Python standard-library checker](tools/validate_challenge.py) validates the current package and registry as well.

Those checks evaluate **JSON/documentary integrity**, not a real PDP, blinded evaluation, security certification, independent reviewer or China Unicom product. Any checker output must say AUTHOR_SIDE_DOCUMENTARY_AND_SYNTHETIC_INTEGRITY, with scientific result **NOT_ESTABLISHED**. A Git commit proves byte custody, not experimental validity.

## 5. Residual risks at design approval

**Source policy legitimacy:** Our example restriction around S is compatible with the discussion, but only an authorized policy owner/evaluator can fix the actual rule, exceptions and action outcomes.

**Source access and participant fairness:** B3 cannot receive evaluator-hidden facts or extra raw data while B2 is deprived of it. EA's cost and extra query burden must be charged; good B2 parity remains a valid negative differential.

**Epistemic identifiability:** Same visible packet in different worlds cannot establish which hidden world exists; measure accurate UNKNOWN/scope/horizon management rather than fictional omniscience.

**Blinding and selection bias:** Case family and all-run accounting must be prospective; do not select a postfreeze event to defeat a known peer nor drop counterexamples.

**Consent and privacy:** Open discussion is not permission to test real China Unicom systems, process secret policy/graphs or publish partner endorsement.

**Maturity overclaim:** Design approval, source-owner confirmation, preregistration, actual experiment, independent appraisal, Stage B, Stage C and ITU adoption remain distinct.

## 6. Review disposition

| Level | Actual status |
|---|---|
| Author-side completeness for local design review | **READY_FOR_REVIEW** subject to final branch QA |
| Independent technical review | **NOT_ASSIGNED** |
| Local signoff by Iván | **PENDING** |
| External China Unicom semantic/campaign acceptance | **NOT_ESTABLISHED** |
| DDS Stage A admitted, registered and frozen | **NO — BLOCKED** |
| DDS Stage A result | **NOT_ESTABLISHED** |
| Stage B / Stage C | **NOT_STARTED** |

The legitimate next decisions are internal design signoff, an optional focused discussion with Ying and, only if source-owner semantics and independent evidence are available, a separate blinded Stage A preregistration. This self-audit does not approve its own scientific claims.


## 7. Post-correction author-side QA, 14 October 2026

After the first v0.2 dossier publication, the original synthetic casebook was challenged again for *hidden precomputation* and secondary confounding. Three additive corrections are recorded in Git history:

1. **CU-C2:** Participant data now carries the **native S→R edge-added observation** plus already established service criticality; it does not hand the PDP an already-calculated authorization verdict.
2. **CU-C7:** The separately valid observation permission now **pre-exists** at T0 and remains unchanged through the critical-edge modification; there is no concurrent unexplained new grant.
3. **CU-C10:** Human acknowledgment of task resumption is an **independent T3 input event**, not a second T2 world modification or a new privilege grant.

The static verifier was extended to check these three conditions. Author-side tool inspection (not execution of the Python helper) found **27/27 broader structural, registry, change-scope and relative-link checks passing** in the earlier audit sweep, then **9/9 targeted post-correction checks passing**. The earlier sweep checked 129 current relative documentation links at that point; the v0.2 navigation updates refer to existing tracked files. Changed PR scope was 16 files (14 dossier files and parent INDEX/REGISTRY), with Flores' campaign record untouched.

**Limit:** The standalone Python verifier is **provided but was not executed in this tooling session**; the above checks were performed using the GitHub-connected author-side structural inspection. None of the validations measured a PDP, blind oracle, independent reviewer or security effect. Final CI/integration approval remains separate from these documentary checks.

**Final disposition unchanged:** ready for an independent local design review, not signed off; external-source policy, Stage A preregistration, actual runs, Stage B and Stage C remain pending.
