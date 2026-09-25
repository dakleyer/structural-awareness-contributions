# 00K-FORMAL/requirement-sufficiency — S/T conformance ⇒ P1–P6

Executable companion to [00K-A23](../../../00K_A23_CANONICAL_REQUIREMENT_CONFORMANCE_SUFFICIENCY_P1_P6_v0.1.md).

This meta-proof package tests the reverse traceability direction:

\[
canonical\ requirement\ conformance \Rightarrow principle\ conformance.
\]

It is not part of the 379 symbolic ablation count.

The finite model uses shared semantic fields and computes both the P predicates and clause-level requirement/T conditions separately.

It exhaustively checks all \(2^{16}=65,536\) states for the six sufficient conformance bundles and retains negative controls showing why S14-only, S4-only and S8-only are insufficient shortcuts.

Run:

~~~bash
python -m unittest -v
~~~
