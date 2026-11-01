# L-09 — Remove accidental public-label leakage without rewriting source examples

**Date:** 1 November 2026. **Status:** synthetic research correction, review draft. **Source owner:** PR #73 (G-02 measured audit); frozen author examples reside in PR #68. **Finding:** Audit #58, round 31, L-09.

## 1. Exact finding and why it matters

The source-owned Conscientia study has 12 illustrative families, each with five frozen variants. For its paired VALID_GO and FALSE_Q variants, the true private verdict is ALLOW vs BLOCK, while both source Q statements claim ALLOW. In six families, VALID_GO has a public A baseline ALLOW and FALSE_Q has a baseline REVIEW. In the other six, both baselines are REVIEW.

That distinction is public before any new audit. An adaptive algorithm could learn this accidental source-fixture association and appear to distinguish false Q from true Q without having inspected the source claim or acquired any independent evidence. This is a **confounder for future learned policies**, not evidence that the existing fixed G-02 arms exploit it. The source audit found that current arms do not exploit it.

## 2. Original source preserved; new counterfactual research population

This PR does **not** edit CASE_REGISTRY.json, SOURCE_REGISTER.json, campaign.py, the original five historical arms, G02_AUDIT_PROTOCOL.json, g02_evidence_audit.py, the original reference JSON, ACC definitions, or any controlled/frozen note. Their original findings—including the original public metadata bias—remain reproducible.

The additional [L09_MATCHING_PROTOCOL.json](L09_MATCHING_PROTOCOL.json) selects the original eight source-owned G-02 instrument regimes and declares two counterfactual baseline actions, ALLOW and REVIEW. [l09_public_leakage.py](l09_public_leakage.py) reads the original **VALID_GO/FALSE_Q pairs for each family** and builds derived twins:

- Both twins share **all public A fields**, including identical baseline, question and scope.
- Both share the **sanitized public Q** (same issuer, scope, claim ALLOW, freshness, source metadata and source cost). The private labels CURRENT_VALID/CURRENT_BUT_FALSE both appear to the public planner only as CURRENT, by PR #73's original sanitization.
- Both twins share the **same synthetic sampling identifier and seed**. Therefore availability, declared instrument issuer, scope, authentication and freshness, **before observing a measured value**, are identical across worlds.
- The **private truth differs:** one twin has ALLOW, the other BLOCK. The original source row ID and original Q.independent_audit Boolean are kept only in the reviewer/provenance and legacy diagnostics; they never enter the new public policy.
- The measured audit SUPPORT/CONTRADICTION and direct ALLOW/BLOCK **may differ legitimately** after an instrument is queried. They are not erased in order to create an artificial tie.

A twin with truth BLOCK and a public baseline ALLOW is a deliberately derived *counterfactual* test case, **not the original FALSE_Q record**. This modelling choice is declared rather than silently rewriting what the author specified. Consent, authority, A/B/C/D, dimension semantics and the original social examples are not amended by this pairing.

## 3. Reusable leakage measurement

The reusable function [explicit_information](l09_public_leakage.py) computes from actual finite labelled records:

1. An upper bound for a **public-metadata-only Bayes classifier** (number of correctly classified binary observations when using the best possible label for each distinct public signature).
2. Shannon prior and conditional entropy, and their derived mutual information in bits, on **exactly this finite synthetic binary population**.
3. Separate information added by qualified **audit results** and qualified **conventional measurements** after reading them.

Metadata includes A/Q plus instrument provenance and availability **without the measured results**. It excludes ground truth, row/variant identity, original source audit flag and private scorer fields.

**Acceptance:** the original 24-case source subset must disclose the historical defect (metadata-only Bayes accuracy 18/24 = 75%; mutual information 0.5 bit). The newly matched population must achieve exactly 50% metadata-only Bayes accuracy and zero bits of information about the private binary truth in **every regime**, despite retaining public issuer and scope. If an accidental correlation reappears, the experiment fails, rather than suppressing its report.

Because this exact finite binary toy includes only adjudicable CURRENT B claims, it assigns no probability to open epistemic C/D and does not claim to estimate real-world source truth, audit efficacy, participant experience or confidence.

## 4. Executable experiment and falsifiers

Twelve source families × two shared baseline lanes (ALLOW/REVIEW) × two private truth twins = **48 derived case templates**, organised as **24 public-matched pairs**. Eight original G-02 instrument regimes × 64 repeated source-coupled synthetic observations × 48 templates = **24,576 paired-world evaluations** (not field experiments). Each one executes all five original **supplemental** G-02 public strategies through the unchanged source generator, planner and post-hoc scorer.

The original five historical Conscientia policies remain separately unchanged. The eight G-02 regimes include:

- Perfect synthetic audit and perfect direct measurement (information can genuinely discriminate **after acquisition**).
- Reliable audit with noisy conventional measurement, and weak audit with strong conventional measurement (advantage should reverse under conditions).
- Unavailable or wrong-scope audit (no information may appear from a non-existent/irrelevant reading).
- Blind audit and always-alarming audit (a declared auditor may add no information, even when expensive).
- An audit with the same accuracy but different prices (decisions must remain stable under price-only changes).

Tests intentionally mutate a baseline, public Q scope, instrument metadata, counterworld truth, source family identity or the manifest. The engine must reject a broken pair. The external one-question interface is exercised with a synthetic third-party family to show reusability without inventing new theory.

Crucially, the experiment must NOT declare audit superiority merely because it makes fewer wrong decisions by returning REVIEW. Wrong decisions, unresolved adjudicable cases, missed legitimate ALLOW opportunities and instrument cost remain separate, as they were in G-02.

## 5. Reviewer procedure

Read the source PR73 and source-owned PR68 before interpreting the new evidence. Then reproduce from the Conscientia campaign directory:

    python -B -m unittest discover -s . -p test_l09_public_leakage.py -v
    python -B l09_public_leakage.py --manifest L09_MATCHING_PROTOCOL.json --output /tmp/l09_public_summary.json
    python -B l09_public_leakage.py --private-samples --output /tmp/l09_private_referee_samples.json

Check these boundary conditions independently:

- Recount the six distinguishable families from **unchanged source fixtures** and confirm 18/24 historical public-metadata classification, without treating a variant name or source case ID as public evidence.
- Inspect every matched pair's **complete** public A, sanitized Q, pre-read audit/direct issuer, scope, freshness and availability. They must match across ALLOW/BLOCK twins. An unrestricted public-metadata classifier cannot beat 50% on a balanced population of such exact twins.
- Confirm the new G-02 audit and direct readings may differ only **after** observation; qualification is not proof of factual correctness or real third-party independence.
- Confirm the *original* G-02 results, five source arms and 60 case fixture are untouched. Repeat original blind/weak/perfect/no-audit controls and distinguish wrong vs unresolved vs missed opportunities.
- Confirm C/D open remain separately unscored; only the controlled binary B subpopulation is balanced. No cross-case aggregation of wellbeing, costs or experimental claims.
- Verify source input hashes and CI artefacts. Do not treat a successful CI or a finite information identity as empirical validation of human/agent behaviour or FH-C.

## 6. Results actually observed and reproduced on CI

**Original run:** [GitHub Actions 41288498924](https://github.com/dakleyer/structural-awareness-contributions/actions/runs/41288498924), 15 tests at that commit (including source-owner G-02 regressions). [Machine-readable summary and limited post-hoc private samples](https://github.com/dakleyer/structural-awareness-contributions/actions/runs/41288498924/artifacts/13076127496).

**Exact historical leak, independently derived by grouping every source A + sanitized Q visible signature:** 24 source TRUE/FALSE Q cases, equally weighted: 12 ALLOW and 12 BLOCK, original best possible public-only classification **18/24 = 75%**; conditioned finite mutual information **0.5 bit**. This does **not** mean any existing policy learned that association; it quantifies its possible exploitation.

**Matched derived protocol:** 24 pairs × 2 private outcomes × 64 draws × 8 instrument regimes = **24,576 evaluations**. For **each of the eight regimes**, the public view excluding a new measured observation has exact Bayes optimum **1/2** and **0 bits** of information about the private truth. Each regime contains 1,536 true and 1,536 false claim worlds, with exactly matching A/Q and pre-read evidence metadata. The sample count is *synthetic repeated observations on fixed author-example source conditions*, not a field sample.

The following are information metrics computed from the **actual finite synthetic output records**, and source-native G-02 counts of wrong final ALLOW/BLOCK decisions; the same source batch and error parameters apply to both true and false twins.

| Source-owned signal regime | Pre-read information (bits) | Acquired, qualified audit reading (bits) | Qualified conventional measurement (bits) | Audited Q wrong / measured conventional wrong |
|---|---:|---:|---:|---:|
| Perfect audit, perfect conventional | **0** | **1.000** | **1.000** | 0 / 0 |
| Reliable audit, noisy conventional | **0** | **0.726** | **0.029** | 81 / 1,254 |
| Weak audit, strong conventional | **0** | **0.047** | **0.704** | 1,247 / 170 |
| Audit unavailable | **0** | **0** | **0.704** | 0 / 170 |
| Audit wrong scope | **0** | **0** | **0.704** | 0 / 170 |
| Blind audit (false assurance) | **0** | **0** | **0.704** | 1,536 / 170 |
| Same reliable audit, price changed | **0** | **0.726** | **0.029** | 81 / 1,254 |
| Audit always flags claims | **0** | **0** | **0.508** | 0 / 338 |

This table deliberately reports **information acquisition** separately from **correct actions, deferrals and costs**. In the no-audit regime the audited-Q strategy has no wrong final actions but **3,072 unresolved decisions and 1,536 missed legitimate ALLOW opportunities**: no signal, no action is not an informational victory. With a perfect audit, Q claims false in 1,536 worlds are **not automatically corrected into BLOCK**; the source-native policy returns REVIEW. The perfect independent conventional measurement can decide those worlds because it measures the same question directly, a different observation capability.

The figures are a **finite experimental proof of absence of label leakage through the specified public data contract**, followed by a demonstration of conditional signal information. They do not establish real-world auditor accuracy, rule out other implementation side channels, produce empirical probabilities for C/D, nor validate FH-C.

### Additional test after initial run

A new regression verifies directly for all 24 pairs that the source A-only and unaudited-Q public policies choose the **same actions** in the two private worlds, while with a perfect qualified measurement the audit-based and conventional policies may choose different actions. The CI now also rejects an unexpected change in the pinned source PR73 commit or its six original source files. This guarantees stable questions and source ownership during review, not future automatic merge compatibility.

**Requested disposition:** when an independent reviewer reproduces the corrected experimental protocol and confirms source preservation, L-09 may be marked **RESPONDIDO**, but **not CERRADO** before the approved merge sequence. Do not replace the original examples or label the derived counterfactuals as historical outcomes.
