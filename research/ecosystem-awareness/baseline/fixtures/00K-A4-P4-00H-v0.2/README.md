# 00K-A4 / P4–00H reviewed v0.2 package

**Status:** preserved reviewed executable package + independent verification  
**Parent test:** [00K — Six-Principle Sufficiency & Adversarial Ablation Test](../../00K_SIX_PRINCIPLE_REQUIREMENTS_MAPPING_AND_ABLATION_TEST_v0.1_DRAFT.md)  
**Scenario:** [00H — The Quiet Four Thousand](../../00H_FAILURE_MODE_BATCH_OPPORTUNITY_BEYOND_AUTHORITY_v0.5_DRAFT.md)

This folder preserves the second reviewed A4 package supplied as `00K_A4_executed_ablation.zip`.

## Exact package

[**00K_A4_executed_ablation_v0.2.zip**](./00K_A4_executed_ablation_v0.2.zip)

SHA-256:

`e7d1caf81e2534fa5b0250f8982fe16fb8e960a273803f151b9ca876dd7c4b63`

The ZIP contains the reviewed `README.md`, `ablation_A4.py` and `test_ablation_A4.py`. It was not rewritten before preservation.

## Independent execution

The supplied package was executed independently in the analysis environment:

```text
21 passed in 0.18s
```

The four-arm comparison produced the expected pattern:

```text
--- Branch U ---
1_baseline_no_lineage               -> DBC_EXECUTE
2_strongest_non_lineage_repair      -> DBC_DENY
3_A2L_semantic_reconstruction       -> DBC_REPOSITION_RECONTRACT
4_route_q_full_six_principles       -> DBC_REPOSITION_RECONTRACT

--- Branch G ---
2_strongest_non_lineage_repair      -> DBC_DENY
3_A2L_semantic_reconstruction       -> DBC_EXECUTE
4_route_q_full_six_principles       -> DBC_EXECUTE
```

The key addition relative to the first reviewed harness is that **A2-L is explicitly separate from Route Q** while still implementing the same root/delegation authority invariant. This is positive evidence for the 00K distinction between **semantic necessity** and **implementation/branding exclusivity**.

## Current active browsable harness

The active browsable harness remains [`../00K-A4-P4-00H/`](../00K-A4-P4-00H/), where the earlier reviewed source is preserved and the v0.2 changes are added without rewriting it:

- `a2l_strong_peer.py` — A2-L semantic-reconstruction peer;
- `test_ablation_A4_v02_additions.py` — NM + A2-L + four-arm comparison;
- `test_ablation_A4_extended.py` — additional U/G indistinguishability sweeps.

That composed harness has been independently reconstructed and run as **27/27** tests.

## Evidence boundary

This remains a deterministic symbolic fixture, not a live agent, payment system, Claude, Stripe, vendor or production benchmark. No TRUE SUBSTITUTE has been found in the tested repair surface; universal P4 necessity is not established.
