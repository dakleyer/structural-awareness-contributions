# Independent technology exercises under the single canonical DDS profile

Document version0.1 ·6 October2026 ·same author, no external independence.

The unique method source is [DDS Canonical Challenge–Trajectory Profile](../../../../../DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1.md). These are separate implementation instances, not additional canonical DDS profiles. They use different predicates, fixtures and evidence modes. Their counts are not pooled into a success rate.

| Implementation instance | Narrative cases | Registered assertions | Qualified outcomes | Misuse diagnostic |
|---|---:|---:|---|---:|
|[STAMP/STPA](./stamp-stpa/EXERCISE_REPORT.md)|10 plus64 actual contexts|306|4 I;2 M;4 incomplete;0 P|5 violating cases|
|[SPIFFE JWT-SVID](./spiffe-jwt/EXERCISE_REPORT.md)|25|75|4 I;21 incomplete;0 P|5 wrong applications|
|[RATS local software/JWS](./rats-jws/EXERCISE_REPORT.md)|20|60|2 I;18 incomplete;0 P|2 stale/false uses|

Every assertion passes, including expected refusals and retained misuse counterexamples. Acceptance is fixture/instrument acceptance, not deployment approval. M is admitted only by the STPA synthetic deferment contract; it is unevaluated in the other two profiles. No matched external comparator or technology advantage is established.

To reproduce, use Python with cryptography50.0.1 and execute each run.py with --output pointing to a new directory. Run cards and freezes precede execution. Results and source versions are immutable; changes require a registered successor. Frozen HEW/R01 results are unchanged.

The SPIFFE exercise performs actual RSA/JWS operations; it is an authored selected-profile validator, not a running SPIRE installation. The RATS exercise hashes actual local files and signs/appraises/consumes actual JWS; its sources/trust and measurement contract are synthetic, with no hardware attestation. The STPA exercise applies the four-step analysis to an executed finite control model. None supplies a real human-performance rate, full native conformance, external validation, Sponsor seal or certification.
