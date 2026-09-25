# 00K-TRACE — Machine-readable traceability integrity

**Semantic proof:** [00K-A19](../../00K_A19_PRINCIPLE_REQUIREMENT_TRACEABILITY_AND_CONSERVATION_PROOF_v0.1.md)  
**Upstream semantic derivation:** [02A](../../02A_FOUNDATION_TO_OPERATIONAL_PRINCIPLE_DERIVATION_PROOF_v0.1.md)  
**Foundation syntactic closure:** [02B](../../02B_FOUNDATIONAL_FAILURE_GRAMMAR_AND_PRINCIPLE_NORMAL_FORM_PROOF_v0.1.md)  
**Requirement semantic traceability:** [A19](../../00K_A19_PRINCIPLE_REQUIREMENT_TRACEABILITY_AND_CONSERVATION_PROOF_v0.1.md)  
**Requirement grammar closure:** [A21](../../00K_A21_REQUIREMENT_GRAMMAR_CLOSURE_AND_UNIQUENESS_PROOF_v0.1.md)

This package checks the **structural integrity** of the Foundation → P → S → scenario → harness → proof chain.

It does not decide whether a semantic mapping is intellectually correct; that argument is in 02A/A19. It prevents silent documentary drift once the mapping has been reviewed.

Run from this directory:

~~~bash
python validate_traceability.py
python validate_normal_forms.py
~~~

Expected:

~~~text
00K semantic traceability integrity: PASS
Principles: 6/6
Requirements: 14/14
Anchor routes: 6/6
Foundation normal forms: 6/6
Requirement normal forms: 14/14
~~~

This meta-check is not counted in the 379 symbolic ablation tests.


`normal_form_manifest.json` records the declared foundation language, admitted primitive forms, P1–P6 normal forms, requirement language and S1–S14 normal forms. `validate_normal_forms.py` checks both marginal coverage and every admitted object/operator atom.
