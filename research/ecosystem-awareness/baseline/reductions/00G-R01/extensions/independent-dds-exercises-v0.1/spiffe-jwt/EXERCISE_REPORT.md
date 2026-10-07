# SPIFFE independent DDS exercise — JWT-SVID and receiving application

Document version0.1 ·6 October2026 ·Codex, same fixture author.

The current method entry point is the [DDS Canonical Method Index](../../../../../../DDS_CANONICAL_METHOD_INDEX_v0.1.md). This report is incorporated as a **Simplified DDS Gate-A** technology-specific implementation instance under the [Gate-A challenge–trajectory contract](../../../../../../DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1.md), not another DDS method. Its frozen Run Card retains the pre-split DDS identity used at execution time. Its binary fixture assertions do not establish Gate-B architecture verification, Gate-C deployment/population acceptance, representative sampling or a success probability.

[Run Card](./RUN_CARD.json) · [frozen source/data](./FREEZE.json) · [actual result](./runs/2026-10-06-01/RESULTS.json). Cryptography50.0.1 is the pinned installed dependency. R01 mathematical0.1/virtual0.3 and the prior HEW runs remain unchanged. No source-native theorem is inherited by these different laws.

## Challenge and exact configuration

An industrial batch receiver must authenticate a workload for its intended endpoint, then apply only a currently authorized tenant/purpose operation. A valid credential is useful origin evidence; it is not a human availability source or a mission grant.

Selected profile: JWT-SVID compact JWS, RS256 signatures, local admitted trust-domain key bundles, audience/expiry and selected subject checks. Actual RSA2048 signatures and verification run through cryptography50.0.1. This is our implementation of a selected specification profile, not execution of SPIRE, Workload API/node attestation, an official SDK or full SPIFFE conformance. X.509, federation, transport encryption, streaming updates and every supported signature suite remain outside executed coverage.

## Scenarios, gates and outcomes

The25 frozen cases cover valid single/multiple audience, wrong/missing audience, expiry, missing expiry, wrong signer/key, unsupported selected algorithm, unsupported JOSE header, duplicate JSON, invalid/foreign subject, altered signature, current application grant/tenant/purpose, valid identity of a different sender, retired/rotated keys, not-before, oversized token, duplicate operation and missing human capacity. Every case has a narrative and expected control results fixed before execution.

Bundle lookup uses unverified identity data only to select an admitted local trust source; acceptance requires the actual signature and claim checks. Remote key headers never trigger a network call. Application policy separately checks the legitimate sender/tenant/purpose/current grant and useful review availability. Idempotent operation handling is an application control, not a new SPIFFE wire claim.

All75 fixture assertions pass. Qualified receiving outcomes are4 I and21 incomplete, with0 P. These are designed positive/negative cases;4/25 is not an estimated deployment success rate.

A deliberate identity-only misuse would wrongly act in5 cases despite genuine identity success. It is not a strong SPIFFE comparator; proper application authorization/capacity use can already close those cases. No extra-architecture differential is established.

## Cost and business boundary

The trace counts actual signature checks and application-policy calls. Fixture generation created25 synthetic tokens and3 ephemeral RSA key pairs; those setup/generation counts are reconstructed from the executed driver and are not individually timed or priced. Local elapsed time starts after key provisioning. Production enrollment, issuer/key lifecycle, native workload attestation, communication, maintenance, trust administration, reviewer sourcing and staffing remain unscored. Unscored means not measured, not free.

Potential bounded value: authenticated provenance plus legitimate controlled delivery. Limits: trusted issuer meaning, app policy, source truth, current authority/capacity and all actual effect paths. Signature success does not prove the sender's message is true or that a human can intervene.

Private signing keys and compact tokens remain in memory. Results contain token digests and scoped outcomes only. The clock is explicitly fixed in the Run Card; credentials are synthetic exercise material, not live workload access.

Primary source: [pinned JWT-SVID standard](https://github.com/spiffe/spiffe/blob/f97c46dfd0ff0d4e412cce5c73846a9ca32a99a2/standards/JWT-SVID.md). Strict duplicate-member rejection and RS256-only selection are fixture implementation choices; not every SPIFFE implementation is required to use this exact parser/profile.
