# CASE-EXTENSION — failure case-study extensibility registry

This package is the machine-readable companion to:

- [00K-A25 — Failure Case-Study Extensibility & Requirements-Conformance Transfer](../../00K_A25_FAILURE_CASE_STUDY_EXTENSIBILITY_AND_CONFORMANCE_TRANSFER_v0.1.md)
- [00K-A26 — Failure → Success Model Case Conversion & Three-Axis Extensibility](../../00K_A26_FAILURE_TO_SUCCESS_MODEL_CASE_AND_EXTENSIBILITY_v0.1.md)
- the six case-family profiles 00E–00J;
- the six paired Success Model Cases 00E–00J.

The validator checks structural integrity only. It does not claim that the listed domain examples have already been executed or empirically proved equivalent.

It verifies:

- exactly six active case families, 00E–00J;
- one parent scenario, one extensibility profile and one Success Model Case per family;
- all three directions: upward, downward and horizontal;
- at least one candidate in every direction;
- valid P1–P6 and S1–S14 references;
- each success case contains a minimum successful traversal, existing S/T route, success predicate, three extension directions, boundary and transfer result;
- parent/profile/success/method/source files exist.

Run:

~~~bash
python validate_extensibility.py
~~~

The logical transfer theorem is in A25; this package only checks that its declared family registry is complete and internally linked.
