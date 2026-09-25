# 00K-CLOSURE — Syntactic closure integrity

This package is the machine-readable integrity companion to:

- [02B — Foundational Syntax Closure & P1–P6 Normal-Form Proof](../../02B_FOUNDATIONAL_SYNTAX_CLOSURE_AND_P1_P6_NORMAL_FORM_PROOF_v0.1.md)
- [00K-A21 — Requirement Normal-Form Closure & Relative Completeness Proof](../../00K_A21_REQUIREMENT_NORMAL_FORM_CLOSURE_AND_RELATIVE_COMPLETENESS_PROOF_v0.1.md)

It checks that every declared foundational control surface has at least one P normal form, every P is generated, all fourteen S normal forms exist exactly once, and every S has a declared primary P.

It is a structural certificate. Semantic correctness remains in 02B/A21.

Run:

~~~bash
python validate_closure.py
~~~
