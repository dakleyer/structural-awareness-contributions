# 00K-FORMAL/full-cube — P1–P6 full-cube realizability certificate

This package is the executable companion to [00K-A22](../../../00K_A22_FULL_CUBE_BOOLEAN_DIAGNOSTIC_MINIMALITY_v0.1.md).

It is a **meta-proof package**, not part of the 379 symbolic ablation campaign.

The model uses one common decision substrate:

- one action and shared time axis;
- shared evidence/provenance records;
- shared authority record;
- shared material-condition record;
- one unresolved inquiry object used jointly by P2 and P3.

It enumerates every one of the \(2^6=64\) requested P1–P6 signatures and verifies that the lower-level constructor realizes that exact signature.

Run:

~~~bash
python -m unittest -v
~~~

Expected:

~~~text
Ran 68 tests
OK
~~~

The extra four tests verify:

1. all 64 signatures are distinct and realized;
2. the counting lower bound \(2^m\ge64\Rightarrow m\ge6\);
3. the one-conjunction counterexample showing this is **not** unrestricted axiom-basis minimality;
4. P2 and P3 are computed from the same unresolved inquiry object rather than stored as independent truth flags.
