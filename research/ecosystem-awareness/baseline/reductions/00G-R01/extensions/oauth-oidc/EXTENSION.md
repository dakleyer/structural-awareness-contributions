# OAuth/OIDC identity and resource admission — technology extension

Version0.2 ·6 October2026 · scoped own implementation profile.

[Sole DDS](../../../../../DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1.md). Base TOKEN-PURPOSE-AND-RESOURCE0.1 is an authored finite local Challenge. This is not a complete R01 kernel, browser login or native authorization-server test.

## Problem, technology and useful outcome

A tenant-a application needs one legitimate resource write. It can alternatively request an explicitly admitted local authenticated-identity return; that M result does not perform the write. The receiver must distinguish an ID Token's identity purpose from an access token's resource scope.

The selected profile uses actual compact JWS/RS256 signing and verification, fixed local issuer/key/audience/type/expiry/nonce checks, separate current grant and an actual SQLite idempotent digital effect. Python3.12.14, cryptography50.0.1 and SQLite3.53.1 are pinned. Signing keys/tokens are ephemeral exercise material; no live credentials are used or exported.

OAuth resource protection and OpenID Connect identity are established mechanisms [AUTH01–03]. Strong conventional application authorization, audience binding and resource-side idempotency receive full credit. No new authentication standard or superiority claim is introduced.

## Stage1 — technology–problem extension and isomorphism profile

**Performed within scope. Selected normative-profile and finite local correspondence; no complete native/R01 isomorphism.**

|Surface|Concrete counterpart|Unresolved transfer obligation|
|---|---|---|
|Objects/relations|Issuer, local keys, subject/client/resource, token purpose, tenant/scope and operation key|Actual issuer enrollment, organization and identity binding|
|Events/actions|Sign, verify, admit identity or write, consume at use, deduplicate|Authorization Code/PKCE, consent, discovery, transport and external actuation|
|Information|Verified claims and admitted current application context|Issuer truth, key custody and real current-grant source|
|Authority|Identity separated from audience/scope/current grant|A valid signature is not a universal mission mandate|
|Cost/time|Signature/policy/SQL counters and fixed logical clock|Tariffs, real issuer/network latency, provisioning/rotation/revocation lifecycle|
|Quality/outcome|One admitted local effect, M identity return, Ø refusal, P wrong effect|No observed production access/login or population success|
|Coverage/policies|Eleven selected paths and one written receiver|No proof for every native policy, algorithm, federation or deployment|

R01's E1–E7 require the preserved signature/relations, enablement, transition laws, views/policies, accounting/time, outcome/optimum and scoped lifting. Those are not completed for any external OAuth/OIDC deployment. Local correspondences motivate the selected test; they transfer neither R01's bounds nor standards conformance.

## Stage2 — mechanisms beyond token authenticity

**Performed within scope.**

|Mechanism|Source/invoker and validity|Cost/interaction/failure limit|
|---|---|---|
|Token-purpose/audience binding|Receiver checks admitted issuer/key plus intended client/resource|Actual verification; a client identity token does not acquire resource permission|
|Nonce/time checks|Relying party's admitted request and clock|Logical comparison; no live replay/session/clock infrastructure tested|
|Scope/current grant|Signed scope plus local authoritative application context|Policy check; source authenticity/revocation service stipulated|
|Validity at resource use|Receiver checks expiry against selected use-time|Required by this chosen access-token contract; no universal persistent-session inference|
|Resource idempotency|SQLite primary operation key|Actual writes/deduplication; remote systems must enforce their own corresponding contract|

Composition needs token meaning, receiver purpose and current permission to agree at the effect boundary. Correct identity alone leaves resource authorization unresolved. Changing purpose or admitting a different task is a changed Challenge, not proof that the original task now succeeds.

## Scenarios and material assumptions

- **AUTH-01:** A tenant-a application submits a valid signed access token for the resource and admitted write grant.
- **AUTH-02:** The same signed token names another resource audience.
- **AUTH-03:** The request arrives at the exact access-token expiration boundary.
- **AUTH-04:** The claims are signed by a key outside the admitted local issuer bundle.
- **AUTH-05:** The caller asks only for an admitted authenticated local identity result from an ID Token; no resource operation is requested.
- **AUTH-06:** A valid client ID Token is offered as permission to perform a resource write.
- **AUTH-07:** The access token is authentic but lacks the selected write scope.
- **AUTH-08:** The resource's current operation grant has been revoked despite the token remaining valid.
- **AUTH-09:** An access token validated at tick1000 is consumed at tick1011 after its expiration1010.
- **AUTH-10:** The same admitted operation is requested twice. A local resource-side idempotency key must preserve one effect.
- **AUTH-11:** An ID Token's nonce does not match the admitted relying-party request.

The [Card](./RUN_CARD.json) freezes outcomes/effect counts and the distinct login/resource meanings. The clock is1000, expiry1010 and the late-use check1011; these are synthetic logical values, not production response-time measurements. Private expected outcomes remain in the driver/adjudicator, not the receiver arguments; this same-process design is not blind or hostile-code isolation.

Issuer/key meaning, selected token schema, clock/nonce and current grant are material assumptions. Audience, exact expiry, wrong key, wrong nonce, revoked grant and delayed consumption are challenged. Real key lifecycle, native consent/flows and source/organizational validity remain unmeasured.

## Primary sources

- [AUTH01 — RFC9700 OAuth security BCP](https://www.rfc-editor.org/rfc/rfc9700.html), selected current security/recipient advice.
- [AUTH02 — OIDC Core1.0 with errata set2](https://openid.net/specs/openid-connect-core-1_0.html), selected ID-token/issuer/audience/nonce semantics.
- [AUTH03 — RFC9068 JWT access-token profile](https://www.rfc-editor.org/rfc/rfc9068.html), selected token-purpose/audience requirements.
- [DB01 — SQLite isolation](https://www.sqlite.org/isolation.html), local persistence context.

Reviewed6 October2026. These sources do not validate our fixture or establish full conformance. JWE, multi-audience processing, all algorithms, discovery, HTTP/browser security and native products are outside this selected realization. [DDS results, accounting and closure](./DDS_STUDY.md).

