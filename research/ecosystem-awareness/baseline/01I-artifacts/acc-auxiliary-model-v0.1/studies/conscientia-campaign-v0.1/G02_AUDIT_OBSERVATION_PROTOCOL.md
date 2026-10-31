# G-02 — Independent Q-audit evidence, not a Boolean declaration

**Owner:** ACC / Conscientia research campaign, source owner PR #68. **Date:** 31 October 2026. **Status:** experimental Stage A, source-preserving draft.

## 1. Original finding, source and precise boundary

[Audit #58 / G-02](https://github.com/dakleyer/structural-awareness-contributions/pull/58) found the phrase "independently audited Q" misleading. In the original frozen 60-case campaign, strategy PARTIAL_Q_AUDIT_GATED accepts B when Q.independent_audit is true. That Boolean is supplied by the fixture; there is **no separate audit observation, independent issuer measurement, error/detection mechanism, or falsifiable ability to detect bad Q**. Four of twelve false-Q claims have the Boolean true, and the original source arm consequently makes four incorrect decisions. These numbers are correct reproductions of a declared switch, **not measured quality assurance**.

This correction **does not change** CASE_REGISTRY.json, SOURCE_REGISTER.json, campaign.py, the source's five arms, 60 × five = 300 historical decisions, the frozen reference JSON, the author's original examples, 00M/00N/01K, the open C/D epistemic exterior, UC21/DDS or the agentic PR57 source. The historical strategy remains a separately labeled **legacy Boolean-flag diagnostic**. It is not promoted into a physical audit.

## 2. Added experimental mechanism and provenance

[g02_evidence_audit.py](g02_evidence_audit.py) creates **two fallible and independently sampled information channels**, both prior to action selection:

- **Audit of a particular Q proposition:** independent synthetic instrument emits SUPPORT, CONTRADICTION or INCONCLUSIVE. The generator takes independently stipulated sensitivity P(flag false Q), false-alarm rate P(flag true Q), availability, nominal issuer, scope, freshness and authentication metadata. Its outcome is **not the original independent_audit Boolean**.
- **Independent conventional observation:** a separately generated ALLOW/BLOCK/INCONCLUSIVE measurement for the same source **question**, with its own availability, accuracy, provenance and acquisition cost. The conventional comparator is **not handed the correct verdict** from the fixture as an oracle.
- A public planner may use an observation only when its **source ID differs from the Q issuer**, it has the expected type, declared attestation, scope and time window. A claimed independent issuer is not a proven audit organization or cryptographic signature. A qualified Q and a qualified audit can both be factually wrong. When evidence is absent, contradictory or not qualified, the model can return REVIEW rather than authorizing a new action.

**Important no-leak guarantee:** The original fixture status CURRENT_BUT_FALSE would reveal material incorrectness if taken literally as a public status. The new public packet maps both CURRENT_BUT_FALSE and CURRENT_VALID to CURRENT; the original false label and old audit Boolean remain only in the test environment/legacy artifact. The decision function takes public A, sanitized Q, and the two observation channels; **never** hidden ground truth, source case variant, or the historical audit Boolean. The scorer reuses the original campaign.score_private **only after all public decisions are fixed**.

Where the original truth is NOT_ADJUDICABLE (open C/D), the environment returns INCONCLUSIVE rather than sampling a fictitious adjudicable world or assigning a probability to all unknown possibilities.

## 3. Source-preserving policies and controls

The source's five strategies remain unchanged. The supplemental experiment compares five new explicit roles:

| Arm | Input and action | Scope |
|---|---|---|
| A_ONLY | Original source A baseline | legitimate no-new-observation control |
| Q_UNAUDITED_SOURCE | Original QUALIFIED_Q using sanitized current B | source baseline; the known failure remains |
| Q_WITH_AUDIT_OBSERVATION | Qualified B + separate audit observation; support may allow B's verdict, contradiction/inconclusive sends REVIEW | key repaired G-02 test |
| CONVENTIONAL_INDEPENDENT_MEASURED | An independent conventional sensor with its own errors and costs | competent, **fallible** comparison |
| BOTH_INDEPENDENT_EVIDENCE | Q + audit + direct measurement must consistently support the same decision | conservative dual-evidence control |

The **legacy** PARTIAL_Q_AUDIT_GATED is reported separately, not ranked against independent instruments as if it were equivalent. All instruments pay their declared cost when queried, even if the obtained signal is later rejected. Costs and the source's original utility parameters are **synthetic decision-model values**, not bananas, euros, real production, social welfare or a real ROI. The main report keeps incorrect ALLOW/BLOCK separate from REVIEW/abstention and legitimate ALLOW opportunities missed; zero wrong decisions from doing nothing is not a scientific win.

## 4. Design: eight regimes, real negative controls and paired random draws

[G02_AUDIT_PROTOCOL.json](G02_AUDIT_PROTOCOL.json) is the versioned manifest: **60 original source cases × 64 paired draws × eight instrument regimes = 30,720 matched case observations**, five public policies per observation. A deterministic SHA-256 random stream is defined per (seed, case ID, replicate, channel), **not per policy**, ensuring each strategy receives the same audit and conventional evidence within the case. Regimes deliberately include a flawless audit, a fallible audit with noisy conventional inspection, a weak audit with strong conventional inspection, no available audit, wrong-scope audit, blind audit with false assurance, equally reliable but more expensive audit, and an audit that flags even correct B claims.

Those regimes are **research hypotheses about hypothetical instruments**, not numerical calibration of real auditing or sensor technologies. The source has 12 families and five variants each, including VALID_GO, VALID_BLOCK, STALE, FALSE_Q and OPEN_RESIDUAL; their underlying interpretations are preserved.

**Falsification conditions:** the perfect independent audit must detect all 12 false current B variants per full replicate set; a blind audit may accept them all and be wrong; a detector with false alarms must reject some true approvals; an unavailable/wrong-scope audit must never be treated as qualified; a competent direct instrument can win. Audit cost and availability may make information acquisition uneconomic. We do not claim a universal benefit from auditing or exclusive capabilities of EA.

## 5. Evidence and review

Reproduction from the directory:

    python -B -m unittest discover -s . -p test_g02_evidence_audit.py -v
    python -B g02_evidence_audit.py --manifest G02_AUDIT_PROTOCOL.json --output /tmp/g02_summary.json
    python -B g02_evidence_audit.py --traces --output /tmp/g02_synthetic_private_trace.json

CI tests the added module, regenerates both outputs, runs source-owned campaign.verify_campaign.py, replays its 60 historical cases and the original source-owner tests. It publishes summary and private post-hoc referee samples as an artefact. SHA-256 identifiers of the source files and manifest are included. A changing source reference is **not silently accepted** as evidence of an unchanged experiment.

The result establishes only which outcomes are possible **within a stipulated toy world with measured-noisy signals**. Even a "perfect audit" regime is a deliberately designed positive control, **not evidence of a perfect third party in the world**.

### Reviewer acceptance checklist (do not mark complete automatically)

1. Confirm five source arms, 60 original cases and historical reference JSON stay byte-identical. Verify that the old flag is only in the legacy diagnostic.
2. Attempt to flip Q.independent_audit in a frozen fixture: new decisions and generated audit observations must **not** change. Attempt to flip CURRENT_BUT_FALSE to a current valid public label: public planner must not see hidden correctness.
3. Verify separate audit/issuer and conventional observation with scope, freshness, declared attestation, availability, cost on query, and **no private ground truth in public plan arguments**. Misqualified instruments cannot authorize.
4. Reproduce positive, negative, false-alarm and absent-audit cases; confirm error counts and missed justified actions **both** appear. Confirm conventional competitor can win and costs can change relative value without changing reality.
5. Check all C/D OPEN_RESIDUAL decisions remain unscored/inconclusive, not erroneously certified or silently dismissed.
6. Distinguish synthetic detector performance from empirical validity, rights/consent, and any institutional endorsement. The source native PR68 and reviewer PR58 own formal adjudication.

**Suggested audit state:** G-02 RESPONDIDO after independent replication and review of the signal-generation contract, never CERRADO merely because CI is green. A source PR may only merge with owner approval and in the correct stacked order.
