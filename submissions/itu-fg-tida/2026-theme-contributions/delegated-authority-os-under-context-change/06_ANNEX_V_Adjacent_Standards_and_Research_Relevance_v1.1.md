# Annex V — Adjacent Standards and Research Relevance

- **Version:** 1.1 (31 August 2026)
- **Parent case:** [TIDA — Delegated Authority OS under Context Change v0.6](01_TIDA_Delegated_Authority_OS_under_Context_Change_v0.6.md)
- **Status:** Public pre-freeze working annex; not an adopted FG-TIDA deliverable.

Working note. The base case should be frozen early enough to remain usable. Adjacent groups should not continuously redesign that base. After the first stable version exists, however, the same case can become a shared stress-test substrate: another group may test its architecture against an existing challenge, propose a controlled variant, or add a clearly bounded challenge relevant to its mandate. Such extensions should be versioned and should not silently alter the frozen facts.

| Adjacent work | Why it intersects | Possible controlled use of the case |
| --- | --- | --- |
| ITU-T FG-AI4SSC / SG20 [R2] | AI-enabled smart-city systems, IoT and digital-twin integration, city-scale coordination, interfaces and interoperable operation. | Most direct domain extension: add city-orchestration, capacity, mobility, digital-twin or service-integration conditions while keeping the TIDA identity and authority core stable. |
| ITU-T SG17 [R1, R3] | Security, trust and identity management. SG17 is the parent study group for FG-TIDA and covers identity, security architectures and conformance. | Use the case to expose security and identity assumptions that may need later formalization, conformance or cross-study-group coordination. |
| IETF OAuth WG [R4] | The active charter includes complex delegation for automated agents acting for users across administrative domains; Token Exchange and Rich Authorization Requests provide stable baselines. | Stress-test whether token and delegation mechanisms can express bounded authority, subdelegation, action-time applicability and multi-domain constraints in the frozen facts. |
| OpenID AuthZEN [R5] | Authorization API 1.0 standardizes the interface between policy decision and policy enforcement points using subject, action, resource and context information. | Test whether a current operative authority determination can be requested and enforced without collapsing policy, evidence, grant and decision into one object. |
| IETF WIMSE WG [R6] | Active work addresses workload identity, least privilege and context propagation across multiple systems and trust domains, including multi-hop transactions. | Test continuity of caller, workload and execution context across agent-service chains while preserving the distinction between identity and authority. |
| IETF SCITT WG [R7] | Active work on supply-chain integrity, transparency and trust provides an architectural precedent for signed statements, provenance and verifiable receipts. | Test provenance and evidence challenges: what must be recorded, how historical facts remain verifiable, and how evidence supports — but does not replace — an authority determination. |
| W3C DID WG [R8] | DID Core v1.0 is a stable identifier baseline; DID v1.1 is current candidate work on decentralized identifiers, resolution and interoperability. | Test identity, representation and cross-domain resolution without forcing the case to adopt DIDs as the only identity mechanism. |
| W3C Verifiable Credentials WG [R9] | The Verifiable Credentials 2.0 Recommendation family provides privacy-respecting, machine-verifiable credentials, claims and integrity mechanisms. | Test whether role, mandate, status or evidence claims can be represented and selectively disclosed while preserving the case's privacy constraints. |
| ISO/IEC JTC 1/SC 42 [R10] | Cross-sector AI standardization includes management systems, trustworthiness, risk and impact assessment. | Use selected variants as assessment and stress-test examples; SC 42 criteria can assess the system without redefining the TIDA-specific core. |
| FIPA legacy specifications [R11] | The archived FIPA Agent Management and ACL specifications remain historical reference points for agent identity, management, communication and interoperability. | Use only as a legacy comparison point for roles, platforms, communication and lifecycle assumptions; do not present FIPA as an active collaboration route. |

Controlled-extension rule. Freeze the base facts first; then allow versioned extension packs. A group may (a) apply its solution to an existing challenge, (b) add a bounded variant that changes actors or conditions but preserves the base concepts, or (c) propose a new challenge with an explicit mandate mapping. The original frozen case remains unchanged, so results stay comparable across groups and over time.

Boundary. This annex identifies possible future interfaces only. It does not imply participation, endorsement or adoption by any external group, and it should not delay the initial FG-TIDA pre-freeze or freeze cycle.

Reference-control note (verified 31 August 2026). The entries below are controlled comparison points, not dependencies imposed on the case. Stable publications and active work in progress are distinguished explicitly; Internet-Drafts and group work must be rechecked before any external use.

Controlled references and status

[R1] [ITU-T FG-TIDA Terms of Reference](https://www.itu.int/md/T25-SG17-260601-TD-PLEN-0295), TD 295-PLEN, 16 June 2026; parent group: ITU-T SG17.

[R2] [ITU-T FG-AI4SSC Terms of Reference](https://www.itu.int/en/ITU-T/focusgroups/ai4ssc/Documents/Terms-of-Reference-FG-AI4SSC.pdf), 2026; and [ITU-T SG20 mandate/work programme](https://www.itu.int/itu-t/workprog/wp_block.aspx?isn=9689), study period 2025–2028.

[R3] [ITU-T SG17 mandate](https://www.itu.int/en/ITU-T/about/groups/2025-2028/Pages/sg17.aspx), study period 2025–2028.

[R4] [IETF OAuth Working Group charter](https://datatracker.ietf.org/wg/oauth/about/) (charter-ietf-oauth-06, active); [RFC 8693, OAuth 2.0 Token Exchange](https://datatracker.ietf.org/doc/html/rfc8693) (January 2020); [RFC 9396, OAuth 2.0 Rich Authorization Requests](https://datatracker.ietf.org/doc/html/rfc9396) (May 2023).

[R5] [OpenID AuthZEN Authorization API 1.0](https://openid.net/specs/authorization-api-1_0.html), Final Specification, January 2026.

[R6] [IETF WIMSE Working Group charter](https://datatracker.ietf.org/doc/charter-ietf-wimse/) (charter-ietf-wimse-01, active); [WIMSE Architecture](https://datatracker.ietf.org/doc/draft-ietf-wimse-arch/) (draft-ietf-wimse-arch-08, Internet-Draft; work in progress).

[R7] [IETF SCITT Working Group charter](https://datatracker.ietf.org/doc/charter-ietf-scitt/01/) (charter-ietf-scitt-01, active); [SCITT Architecture](https://datatracker.ietf.org/doc/draft-ietf-scitt-architecture/) (draft-ietf-scitt-architecture-22, publication processing status checked 31 August 2026).

[R8] [W3C Decentralized Identifiers (DIDs) v1.0](https://www.w3.org/TR/did-core/), Recommendation, 19 July 2022; [DID Core v1.1](https://www.w3.org/TR/did-1.1/), Candidate Recommendation Snapshot, 5 March 2026.

[R9] [W3C Verifiable Credentials Data Model v2.0](https://www.w3.org/TR/vc-data-model-2.0/) and [Verifiable Credential Data Integrity 1.0](https://www.w3.org/TR/vc-data-integrity/), Recommendations, 15 May 2025.

[R10] [ISO/IEC JTC 1/SC 42 scope and catalogue](https://www.iso.org/committee/6794475.html); ISO/IEC 42001:2023 (AI management system) and ISO/IEC 42005:2025 (AI system impact assessment).

[R11] [FIPA Agent Management Specification](https://www.fipa.org/specs/fipa00023/) SC00023K, standard, 18 March 2004; [FIPA ACL Message Structure Specification](https://www.fipa.org/specs/fipa00061/) SC00061G, standard, 2002. Legacy archive; no active FIPA work is claimed.
