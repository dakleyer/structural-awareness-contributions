# CASE-EXTENSION — failure case-study extensibility registry

This package is the machine-readable companion to:

- [00K-A25 — Failure Case-Study Extensibility & Requirements-Conformance Transfer](../../00K_A25_FAILURE_CASE_STUDY_EXTENSIBILITY_AND_CONFORMANCE_TRANSFER_v0.1.md)
- the six case-family profiles 00E–00J.

The validator checks structural integrity only. It does not claim that the listed domain examples have already been executed or empirically proved equivalent.

It verifies:

- exactly six active case families, 00E–00J;
- one parent scenario and one extensibility profile per family;
- all three directions: upward, downward and horizontal;
- at least one candidate in every direction;
- valid P1–P6 and S1–S14 references;
- parent/profile/method/source files exist.

Run:

~~~bash
python validate_extensibility.py
~~~

The logical transfer theorem is in A25; this package only checks that its declared family registry is complete and internally linked.
