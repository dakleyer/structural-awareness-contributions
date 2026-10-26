# RATS independent DDS exercise — software evidence, appraisal and consumption

Document version0.1 ·6 October2026 ·Codex, same fixture author.

The current method entry point is the [DDS Canonical Method Index](../../../../../../DDS_CANONICAL_METHOD_INDEX_v0.1.md). This report is incorporated as a **Simplified DDS Gate-A** technology-specific implementation instance under the [Gate-A challenge–trajectory contract](../../../../../../DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1.md), not another DDS method. Its frozen Run Card retains the pre-split DDS identity used at execution time. Its binary fixture assertions do not establish Gate-B architecture verification, Gate-C deployment/population acceptance, representative sampling or a success probability.

[Run Card](./RUN_CARD.json) · [frozen source/data](./FREEZE.json) · [actual result](./runs/2026-10-06-01/RESULTS.json). Cryptography50.0.1 is the pinned installed dependency. R01 mathematical0.1/virtual0.3 and the prior HEW runs remain unchanged. No source-native theorem is inherited by these different laws.

## Challenge, roles and meaning

A receiving batch decision uses evidence about a named software state. The selected local roles are Attester, Verifier and Relying Party, with distinct ephemeral signing keys and policies. Distinct keys do not establish organizational independence or hardware-backed trust.

The Attester hashes an actual fixture file; the Verifier checks its signed, scoped evidence against a fixed reference/policy/nonce; the Relying Party checks the signed result for its subject, audience, time, current policy and mission grant. A separately admitted current file-source query and confirmed local effect are required by this chosen application profile.

Wire realization: private synthetic software-state claims carried in compact JWS/RS256. It is not a standardized EAT profile, TPM/TEE measurement, native verifier product or interoperable RATS deployment. RFC9334 defines the architecture; the clock, nonce, claims, current source and application guards are declared profile choices.

## Frozen scenario battery and executed result

The20 cases cover admitted/mismatched measured software, unauthorized attester, subject/nonce/expiry/reference policy, absent measurement, untrusted verifier, result audience/time, state change after appraisal, lying trusted source, receiving-policy change, revoked grant, missing current telemetry, current-state recovery, UNKNOWN result, missing useful human capacity and lack of confirmed application.

All60 fixture assertions pass. Qualified outcomes are2 I and18 incomplete, with0 P. The scenario set intentionally emphasizes boundary conditions. It is not a population estimate of effectiveness or risk.

A snapshot-only consumption diagnostic, which still respects signature/audience/expiry/policy/grant, wrongly uses software state in2 cases: change after appraisal and false measurement by a trusted fixture source. Proper current-source controls can already be part of a conventional relying policy; no new-architecture or vendor superiority is established.

The chosen remeasurement catches these fixture faults only because the local current file-source assumption is admitted. It does not solve a compromised OS, lying physical measurement producer, every concurrent mutation or distributed atomicity. The code explicitly separates signature/policy success from current-state truth and confirmed effect.

## Cost and business interpretation

The trace records actual file-hash reads, signature verification and policy checks.4 ephemeral key pairs provision separate trusted/untrusted fixture roles; source/result signing and setup are not individually priced or timed. Local elapsed time starts after provisioning. Production measurement, reference maintenance, device/root trust, network, retries, source validity, human review, infrastructure and effect-path coordination remain unscored.

Potential bounded value: more supportable admission decisions and explicit refusal of unsupported reliance. Limits: supported predicate, actual provenance, post-observation change, current policy/grant, effect confirmation and useful deadlines. Software acceptance is not a capacity certificate.

No compact token or private key is exported. Original evidence/result are represented by hashes in the result record; rerunning creates new in-memory keys, so token digests need not match across repeats. Input/source hashes and registered assertions remain reproducible.

Primary architecture: [RFC9334](https://www.rfc-editor.org/info/rfc9334/), especially role/policy/freshness and privacy boundaries. This original local application copies no external verifier implementation.
