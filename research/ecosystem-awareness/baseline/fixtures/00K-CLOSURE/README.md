# 00K-CLOSURE — canonical syntactic closure integrity package

This package is the single machine-readable companion for:

- [02B — Foundational Syntax Closure & P1–P6 Normal-Form Proof](../../02B_FOUNDATIONAL_SYNTAX_CLOSURE_AND_P1_P6_NORMAL_FORM_PROOF_v0.1.md)
- [00K-A21 — Requirement Basis Closure & Relative Completeness](../../00K_A21_REQUIREMENT_BASIS_CLOSURE_AND_RELATIVE_COMPLETENESS_PROOF_v0.1.md)

It checks the declared syntax, not the truth of the semantic argument.

The validator verifies:

- A/B/C/D and Type 0/1/2 foundation vocabulary;
- six generated P1–P6 normal forms;
- fourteen S1–S14 requirement normal forms;
- complete coverage of every admitted requirement object×operator atom;
- all six P invariants represented in the requirement grammar; and
- existence of the canonical 02A/02B/A19/A21 proof files.

Run:

~~~bash
python validate_closure.py
~~~

This is a structural meta-check and is not part of the 379 symbolic ablation count.
