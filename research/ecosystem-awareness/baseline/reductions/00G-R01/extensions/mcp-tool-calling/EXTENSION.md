# MCP selected tool-call admission — technology extension

<!-- DDS terminology revision 1 (2026-10-07): Stage A/B/C only; source scientific version and evidence unchanged. -->

Version0.2 ·6 October2026 · own partial protocol/application profile.

**DDS classification:** Simplified **Stage A — Specification Discovery** under the [DDS Canonical Method Index](../../../../../DDS_CANONICAL_METHOD_INDEX_v0.1.md), using the [Stage A challenge–trajectory contract](../../../../../DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1.md). Base DECLARED-TOOL-AND-CURRENT-RESOURCE0.1 is an authored finite local Challenge. Placement under R01 is navigation, not mathematical membership; this profile is not Stage B or Stage C.

## Problem and configured technology

An admitted caller requests one set_tier write for tenant-a under the declared tool contract. A protocol name, parseable request, clientInfo label or readOnly hint is not the application's current mandate. The actual resource must enforce its admitted operation and reject unsupported inputs/authority.

Reference revision: MCP2026-07-28. This pilot serializes/parses own JSON-RPC request objects, checks selected required metadata and scalar arguments, and applies an actual local SQLite effect. Its handler records local error codes; it does not implement full JSON-RPC response-envelope conformance. No official MCP SDK, HTTP/stdio connection, OAuth transport, MCP Apps or full JSON Schema validation was executed.

The core protocol already separates required request metadata, self-reported information and tool descriptions [MCP01–03]. Correct conventional servers/hosts and resource policies receive full credit.

## Stage1 — technology–problem extension and isomorphism profile

**Performed within scope; selected request/object correspondence, no proved native/R01 isomorphism.**

|Material surface|Selected counterpart|Transfer limit|
|---|---|---|
|Objects/relations|Caller request, declared tool, typed args, catalog revision, tenant/grant and operation key|One authored tool, not all MCP objects/extensions|
|Events|Serialize/parse/validate, current resource check, write/deduplicate|No connected transport, SDK lifecycle or interoperability|
|Observations|Per-request protocol metadata, local registry and authority reads|clientInfo is self-report; a registry source is stipulated|
|Authority|Caller metadata separate from local grant and resource check|No native token issuer, user-consent or identity proof|
|Cost/time|Request bytes and actual operational SQL|Network, hosts, discovery, schema lifecycle and service times unscored|
|Quality/outcome|One admitted local write versus Ø/P|No business correctness for arbitrary tools or physical effects|
|Coverage|Nine selected paths of one handler|No every-policy or complete schema/protocol preservation|

A declared catalog revision is part of this tool's argument contract, not a new MCP core requirement. E1–E7 would require full preserved signature/enablement/laws/views/accounting/outcomes/coverage for a claimed R01 extension; those obligations are not supplied by this finite mapping. No source theorem or full-native result transfers.

## Stage2 — additional mechanisms and interactions

**Performed within scope.**

|Mechanism|Producer/consumer and validity|Burden/failure boundary|
|---|---|---|
|Selected request/schema validation|Handler consumes wire metadata and own scalar schema|Parsing/validation; does not authenticate semantic claims|
|Scope independent of self-report|Resource consumes an admitted local grant source|Actual lookup; fake admin labels never create authority|
|Current tool-contract binding|Caller/registry revision checked by application|Own contract field; stale schema can invalidate a previously prepared request|
|At-effect authorization|Resource rechecks its current grant in the local transaction|Extra SQL; real distributed issuer/state/provenance untested|
|Idempotent resource operation|Actual SQLite primary operation key|One effect across replay; arbitrary downstream services need their own enforcement|

readOnlyHint is descriptive metadata. In the selected case an authorized write occurs despite the hint; this demonstrates that the hint itself is not a no-effect barrier. It does not demonstrate malicious native-server behavior or an unauthorized action in that admitted write task.

## Scenario battery

- **MCP-01:** An admitted caller requests the declared write tool with valid typed arguments and current application authority.
- **MCP-02:** The request omits a required selected protocol metadata field.
- **MCP-03:** The caller invokes an unsupported JSON-RPC method.
- **MCP-04:** The tool arguments use a number where the selected schema requires a tenant string.
- **MCP-05:** The caller self-reports an admin-like clientInfo name but has no admitted resource grant.
- **MCP-06:** The caller relies on catalog revision1 after the selected tool contract changes to revision2.
- **MCP-07:** An authorized write tool advertises a readOnly hint. The local write still occurs under its actual contract; the hint does not enforce read-only behavior.
- **MCP-08:** The same admitted operation is submitted twice and the actual local resource must deduplicate it.
- **MCP-09:** A local grant is revoked after initial admission and before the resource effect; resource-side current checking must refuse it.

[Card](./RUN_CARD.json) fixes expected outcomes/effect counts. The handler receives request, registry and resource source, not expected outcome labels. Controlled grant/catalog changes test relevant source-at-use limits; the evaluator later inspects actual effects. The same-process fixture provides no hostile-code or blind isolation.

## Sources

- [MCP01 — Tools, revision2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/server/tools), selected schema/annotation semantics.
- [MCP02 — Basic protocol, revision2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic), selected JSON-RPC/request metadata and self-report meaning.
- [MCP03 — Authorization, revision2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization), documentary transport/resource safeguards; not executed here.
- [DB01 — SQLite isolation](https://www.sqlite.org/isolation.html), local transaction context.

Primary references reviewed6 October2026; no author/standards-body validation of this study. [DDS evidence, cost/value and closure](./DDS_STUDY.md).

