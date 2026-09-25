# 00K-TRACE — semantic/documentary traceability integrity

**Foundation semantic derivation:** [02A](../../02A_FOUNDATION_TO_OPERATIONAL_PRINCIPLE_DERIVATION_PROOF_v0.1.md)  
**Principle↔requirement semantic traceability:** [A19](../../00K_A19_PRINCIPLE_REQUIREMENT_TRACEABILITY_AND_CONSERVATION_PROOF_v0.1.md)  
**Syntactic closure package:** [00K-CLOSURE](../00K-CLOSURE/README.md)

This package checks the structural integrity of the:

Foundation → P1–P6 → S1–S14 → scenario → harness → proof

graph.

It verifies:

- exactly P1–P6 and S1–S14 are registered;
- every S has one declared primary P;
- every P owns at least one primary S;
- the six ablation anchors are present;
- each P has a scenario, harness, corpus witness and mathematical witness; and
- every referenced repository path exists.

It deliberately does **not** duplicate the syntactic grammar/closure validator. That responsibility belongs to 00K-CLOSURE.

Run:

~~~bash
python validate_traceability.py
~~~

This meta-check is not part of the 379 symbolic ablation count.
