# 00K-TRACE — Machine-readable traceability integrity

**Semantic proof:** [00K-A19](../../00K_A19_PRINCIPLE_REQUIREMENT_TRACEABILITY_AND_CONSERVATION_PROOF_v0.1.md)  
**Upstream derivation:** [02A](../../02A_FOUNDATION_TO_OPERATIONAL_PRINCIPLE_DERIVATION_PROOF_v0.1.md)

This package checks the **structural integrity** of the Foundation → P → S → scenario → harness → proof chain.

It does not decide whether a semantic mapping is intellectually correct; that argument is in 02A/A19. It prevents silent documentary drift once the mapping has been reviewed.

Run from this directory:

~~~bash
python validate_traceability.py
~~~

Expected:

~~~text
00K semantic traceability integrity: PASS
Principles: 6/6
Requirements: 14/14
Anchor routes: 6/6
~~~

This meta-check is not counted in the 379 symbolic ablation tests.
