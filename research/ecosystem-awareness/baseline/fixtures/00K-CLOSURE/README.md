# 00K-CLOSURE — canonical syntactic closure integrity package

> **Semantic scope of this proof record — 2 October 2026.** Current corpus meanings are defined in [00M §1 — canonical A/B/C/D definitions](../../00M_ABCD_AND_MATHEMATICAL_PLAUSIBILITY_v0.8_RESEARCH_NOTE.md#abcd-canonical). The grammar, fixtures and recorded results below retain their declared source vocabulary. Linking the current definition does not prove that a result transfers to the revised B/C boundary: that correspondence requires a separate semantic check. No formula, executed result or coverage count is changed here.

> **Audit corrections — 26 September 2026:** [A14](./../../00L_REINFORCED_PAPER_TRAVERSALS_00E_00J_v0.1/00L_A14_CORRECCIONES_AUDITORIA_v0.1.md) describes current behavior and regression evidence. Prior execution records below remain historical; current implementations and replay outputs are versioned separately.

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
