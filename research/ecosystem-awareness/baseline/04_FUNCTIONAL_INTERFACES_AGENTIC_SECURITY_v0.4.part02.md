asoning becomes Type 1\.

&nbsp;

Internal EA functions

F3, F5, F7, F9.

&nbsp;

Boundary

EA does not rerun the worker’s complete domain reasoning. It qualifies what the worker’s output justifies.

&nbsp;

## O4 — Context, Memory, State, Retrieval & Research

Generic role

Provides documents, working/long-term memory, persisted session or checkpoint state, retrieved resources, search results, vector retrieval, external research or other context used by agents. MCP resources, agent-session stores and agentic retrieval systems are current examples.

&nbsp;

Inputs to Ecosystem Awareness

\- available source/resource classes;

\- retrieved evidence identifiers and scope;

\- provenance/source relationship where available;

\- freshness/cache state;

\- session/checkpoint/persistent-state identity, version and resumability where used;

\- retrieval/search bounds and stopping criteria;

\- retrieval/search latency, compute/token, bandwidth, monetary or other resource burden where available and decision-material;

\- coverage or known exclusion information where available;

\- source-dependency/duplication indications;

\- access limitations or unavailable sources.

&nbsp;

EA outputs to this function

\- widen/narrow/redirect window request;

\- request a specific missing evidence/source class;

\- request primary-source retrieval;

\- request independent corroboration rather than more copies of the same source;

\- stop, narrow or redirect condition for unbounded or low-value search;

\- observation-budget or marginal-value bound where supported by the retrieval/research function;

\- refresh request where staleness invalidates the current frame.

&nbsp;

Internal EA functions

F2, F3, F4, F7, F9.

&nbsp;

Boundary

Retrieval increases accessible context; it does not prove that the resulting window is the ecosystem or that additional search will eliminate structural residual.

&nbsp;

## O5 — Tool / Resource Access & Action Execution

Generic role

Exposes callable tools, APIs, services, files, databases or actuators and executes actions. MCP tools and ordinary enterprise APIs are examples.

&nbsp;

Inputs to Ecosystem Awareness

\- tool/resource identity and declared function;

\- action request/result/status;

\- decision/operation and predecessor-handoff reference where the action continues a material decision;

\- read/write/reversibility and material impact characteristics where available;

\- authorization scope and relevant policy/mandate reference;

\- error/failure/partial-completion state;

\- side-effect confirmation or indeterminate execution outcome;

\- latency/availability/capacity state;

\- provenance of returned data where available.

\- shared resource-time segment and competing operation/directive reference where the action can collide with another legitimate action.

&nbsp;

EA outputs to this function

\- request to delay or restrict tool use while a specific domain is requalified;

\- request for read-only, reduced-scope or reversible operation when posture requires it;

\- request for outcome reconciliation when execution status is indeterminate;

\- containment/scope-reduction request sent to the function that actually owns enforcement.

\- where the Composition-Critical EHD Profile applies, the targeted re-entry reference and expected revalidation criterion; this is not an execution command.

&nbsp;

Internal EA functions

F1, F2 where the tool/API is an acquisition pathway, F3, F6, F7, F9.

&nbsp;

Boundary

EA does not grant tool authority. Authorization and enforcement remain separate.

&nbsp;

## O6 — Task, Message, Artifact & Inter-Agent Transport

Generic role

Carries messages, tasks, task status, artifacts, streaming updates and extensions between agents or services. A2A is a current protocol example; other transports may be used.

&nbsp;

Inputs to Ecosystem Awareness

\- message/task/artifact identity and status;

\- sender/receiver or interaction binding available at the transport layer;

\- decision/operation correlation and parent-handoff reference where the message continues or changes a material decision;

\- timestamps/freshness;

\- extension metadata carrying an EHD or external epistemic envelope;

\- delivery/update state;

\- task completion, cancellation, auth-required or other relevant lifecycle state.

&nbsp;

EA outputs to this function

\- Epistemic Envelope from F8 for transport alongside the ordinary operational result;

\- updated scope/freshness qualifiers;

\- requalification or correction signal where the transport supports amendments/status updates.

\- Composition-Critical EHD Profile fields, where material, so that the receiving function can correlate the decision basis, conflict relation or targeted re-entry without interpreting a transport identifier as sufficient semantic identity.

&nbsp;

Internal EA functions

F4, F8, F9.

&nbsp;

Boundary

Transport preserves and conveys information. It does not determine the truth of an epistemic statement.

&nbsp;

# 5\. Trust & Security Plane interfaces

&nbsp;

## IF-S1 — Identity, Authentication & Principal Binding

Generic role

Establishes who/what is interacting and, where relevant, the binding between agent/runtime/interacting system and the human or organization behind it. Authentication proves control of credentials; legal or operational principal binding may be a separate function.

&nbsp;

Inputs to Ecosystem Awareness

\- authenticated subject/agent/service identifier;

\- principal/binding claim when available;

\- authentication assurance/context;

\- credential validity/freshness/revocation status;

\- binding scope and validity interval;

\- identity/binding evidence provenance;

\- unknown or contested identity/binding state.

&nbsp;

EA outputs to this function

\- request for refreshed identity/binding evidence when material;

\- explicit treatment of identity/binding state as unknown or insufficient for the affected domain;

\- requalification request when a previously valid binding is stale, changed or contradicted.

&nbsp;

Internal EA functions

F1, F3, F4, F6, F7.

&nbsp;

Boundary

Identity is evidence about the actor/binding; it does not predict behaviour and does not by itself establish authority, conformance or ecosystem truth.

&nbsp;

## IF-S2 — Provenance of Authority, Delegation & Authorization

Generic role

Specifies where authority originated, the grant/mandate, scope, limits, conditions, delegation chain, version and revocation/standing. This aligns closely with FG-TIDA Theme \#5 and with ordinary authorization systems.

&nbsp;

Inputs to Ecosystem Awareness

\- principal/grantor and grantee identifiers;

\- authority/grant identifier;

\- mandate/action scope;

\- limits and conditions;

\- applicable authority/mandate reference for a competing directive, including any source-owned exception, veto or precedence rule where one exists;

\- delegation/redelegation chain where material;

\- policy/reference version linked to the grant;

\- validity/revocation state;

\- authority provenance and standing;

\- contested, absent or fuzzy authority state;

\- authority capacity actually reachable for current intervention where relevant.

&nbsp;

EA outputs to this function

\- request to refresh/resolve authority state;

\- indication that authority uncertainty is binding for the current domain;

\- request to narrow action scope to the currently qualified mandate;

\- requalification trigger when the grant/reference/standing materially changes.

&nbsp;

Internal EA functions

F1, F3, F6, F7, F9.

&nbsp;

Boundary

EA consumes authority state. It does not originate a grant or decide legal standing.

&nbsp;

## IF-S3 — Remote Attestation & Runtime / Interaction Assurance

Generic role

Produces evidence about runtime, code/data/policy/model/harness or interaction state; a verifier appraises that evidence and produces an Attestation Result for a relying party. RFC 9334 RATS provides the canonical Evidence → Verifier → Attestation Result architecture. Current FG-TIDA Theme \#22 explores its agentic extension.

&nbsp;

Inputs to Ecosystem Awareness

\- Attestation Result, not necessarily raw private evidence;

\- attested subject/interaction and scope;

\- verifier/issuer identity;

\- appraisal result and relevant claims;

\- reference/policy identifiers and versions where material;

\- freshness/nonce/replay status;

\- appraisal relationship such as self/contracted/independent where available;

\- evidence/appraisal limitations;

\- no-assertion/unknown result distinct from action-side indeterminate.

&nbsp;

EA outputs to this function

\- request for re-attestation when freshness or interaction state changes;

\- request for an independent or differently rooted attestation where source dependence matters;

\- reduction of reliance when attestation scope does not cover the claim being made;

\- bounded epistemic envelope for downstream relying-party decisions.

&nbsp;

Internal EA functions

F4, F5, F6, F7, F8, F9.

&nbsp;

Boundary

A valid Attestation Result establishes what the verifier vouches for under its appraisal policy. It is evidence, not universal truth and not an authorization decision by EA.

&nbsp;

## IF-S4 — Policy / Intent Expression & Runtime Conformance

Generic role

Defines the authored policy/intent reference and evaluates an action against it at runtime. This aligns closely with FG-TIDA Theme \#6.

&nbsp;

Inputs to Ecosystem Awareness

\- named/versioned policy or intent reference;

\- provenance/authority under which the reference was authored;

\- evaluated action/task/domain;

\- conformance verdict such as permit, remediate, block, escalate or indeterminate;

\- scope examined for indeterminate;

\- confidence/threshold semantics where used;

\- issuing evaluator/engine identity;

\- issuer relationship to evaluated party where available;

\- freshness/tamper-evidence of the verdict;

\- competing intents/directives, their shared decision or resource-time reference, and the source-owned priority/precedence basis where material;

\- attested absence of evaluation where no evaluation occurred.

&nbsp;

EA outputs to this function

\- request for re-evaluation under a refreshed/current reference;

\- request to preserve indeterminate instead of forcing a binary verdict;

\- indication that verdict scope is insufficient for the system-level claim;

\- request for independent evaluation where the current evaluator is not sufficient for the affected domain.

&nbsp;

Internal EA functions

F3, F4, F5, F6, F7, F9.

&nbsp;

Boundary

A conformance verdict answers whether observed/action behaviour conforms to a reference. It does not establish that the reference was legitimate, that the world model was complete or that the system-level composition is determined.

&nbsp;

## IF-S5 — Evidence Appraisal & Verifier-Side Failure Semantics

Generic role

Checks whether evidence/records/claims are entitled to be relied upon and produces explicit appraisal or rejection outcomes. This aligns with RATS appraisal and FG-TIDA Theme \#7 / the appraisal half incorporated into Theme \#6.

&nbsp;

Inputs to Ecosystem Awareness

\- appraisal result;

\- rejection/failure class;

\- checks performed or profile/version;

\- subject/record/claim appraised;

\- freshness/replay/integrity result;

\- issuer/relationship/authorization-scope checks where applicable;

\- absence/null semantics where applicable;

\- limitations or checks not performed.

&nbsp;

EA outputs to this function

\- request to appraise a particular upstream claim or evidence class;

\- request for a different appraisal profile where the current one does not cover the epistemic question;

\- preservation of appraisal failure as evidence-side uncertainty rather than silently mapping it to an action verdict.

&nbsp;

Internal EA functions

F3, F4, F5, F7.

&nbsp;

Boundary

Evidence-side failure and action-side indeterminate remain different semantic categories.

&nbsp;

## IF-S6 — Human Oversight & Intervention Capacity

Generic role

Manages escalation, qualified reviewers, human authority, decision rights, intervention records, bounded mandates and return-to-operation conditions. This aligns closely with FG-TIDA Theme \#16.

&nbsp;

Inputs to Ecosystem Awareness

\- human-capacity state: available, binding, unavailable or implementation-equivalent;

\- required reviewer/role and authority;

\- response deadline/window;

\- current escalation/HOLD/intervention state;

\- human decision and scope;

\- intervention mandate/validity where applicable;

\- evidence considered and evidence sufficiency/limitations;

\- intervention outcome/reconciliation state;

\- return-to-operation/revalidation state.

&nbsp;

EA outputs to this function

\- targeted request for human review only for the affected domain;

\- required information/scope that the reviewer must see for the requested epistemic question;

\- indication that human capacity is itself insufficient/unavailable;

\- stop/escalation boundary when repeated human requests become Type 1;

\- system-level posture and requalification requirement for intervention-path selection.

&nbsp;

Internal EA functions

F1, F2 where the human channel is an acquisition pathway, F3, F5, F6, F7, F9.

&nbsp;

Boundary

Human oversight owns human capacity and intervention. EA consumes human-capacity state as one dependency among many. Human approval does not retroactively validate an upstream world model. Repeated escalation, review and evidence requests also consume finite human attention in the extended human-agent system; EA may therefore identify the human channel itself as capacity-binding or Type-1-amplifying without taking ownership of the human decision.

&nbsp;

## IF-S7 — Observability, Telemetry, Evaluation & Drift

Generic role

Emits traces, metrics, logs, operation/tool/model telemetry, anomaly/drift measurements and evaluation results. OpenTelemetry provides current cross-vendor semantic conventions for agent invocation, model calls, retrieval and tool execution.

&nbsp;

Inputs to Ecosystem Awareness

\- observed operation/task/tool/model identifiers;

\- timestamps/duration/status/error state;

\- instrumentation/measurement coverage and observation burden or latency where available;

\- telemetry/evaluation metric and semantics;

\- drift/anomaly indicators;

\- model/runtime/tool version changes;

\- source/measurement method;

\- observation period/population/scope;

\- measurement confidence/limitations where available;

\- expected versus observed outcome.

&nbsp;

EA outputs to this function

\- request for additional instrumentation/measurement on a specific domain or dependency;

\- request for refreshed observation where telemetry is stale;

\- revalidation trigger when drift invalidates window or operating-frame assumptions;

\- target domains for follow-up evaluation;

\- request to increase, decrease or redirect instrumentation when observed risk/sensitivity and observation cost are materially mismatched.

&nbsp;

Internal EA functions

F2, F3, F4, F6, F7, F9.

&nbsp;

Boundary

EA interprets the epistemic significance of telemetry. It does not replace the telemetry or evaluation method.

&nbsp;

## IF-S8 — Accountability, Attribution & Verifiable Action Records

Generic role

Records at action time enough information for a later party to establish who acted, under what authority and scope, and to verify that the record/claims have not been altered. This aligns closely with FG-TIDA Theme \#1.

&nbsp;

Inputs to Ecosystem Awareness

\- actor/agent/interacting system identity;

\- action/task and timestamp;

\- decision/operation and parent-handoff reference where needed to reconstruct a composition-critical path;

\- authority/provenance reference;

\- declared scope;

\- policy/reference identifier/version where present;

\- carried conformance verdict or attested absence;

\- issuer binding, freshness and tamper-evidence for carried claims;

\- attestation linkage where present;

\- action/result/outcome and record integrity state.

&nbsp;

EA outputs to this function

\- bounded Internal/External Epistemic Statement from F8 suitable for being recorded alongside the action where required;

\- scope, posture, residual/inherited-indeterminacy markers relevant to later reconstruction;

\- request to preserve a material requalification/containment/migration decision and its basis.

\- where material, the targeted re-entry reference, review/expiry condition and observed outcome/revalidation link for the same decision/operation.

&nbsp;

Internal EA functions

F4, F5, F8, F9.

&nbsp;

Boundary

The record preserves evidence for reconstruction. It does not itself prove that every recorded claim was substantively true.

&nbsp;

## IF-S9 — External / Population-Level Evaluation

Generic role

Reads many records/measurements to determine what can be concluded at population or evaluator-family scale when single records cannot establish certain claims. This aligns with FG-TIDA Theme \#21 and parts of Theme \#18.

&nbsp;

Inputs to Ecosystem Awareness

\- assessment claim;

\- defined population;

\- observation period;

\- taxonomy/reference/policy and version;

\- per-type rate or other non-composite measurement;

\- evaluator/evaluator-family characteristics;

\- evaluator independence/diversity information where known;

\- sample size and statistical uncertainty where applicable;

\- residual indeterminacy / identifiability limit;

\- statement of what the result is and is not capable of establishing.

&nbsp;

EA outputs to this function

\- request for a population-level assessment when local records cannot resolve a materially relevant hypothesis;

\- request for a different evaluator family or independent channel where correlation matters;

\- qualified use of the population signal within F4/F5 rather than promotion to ecosystem truth.

&nbsp;

Internal EA functions

F4, F5, F6, F7.

&nbsp;

Boundary

Population size can reduce sampling uncertainty but does not automatically remove structural non-identifiability. Population-level evidence remains scope-bound.

&nbsp;

## IF-S10 — Privacy & Minimum Disclosure

Generic role

Controls what identity, authority, context, trust, behavioural, telemetry and audit information each party may learn, retain or disclose. This aligns with FG-TIDA Theme \#19 and standard privacy-preserving design.

&nbsp;

Inputs to Ecosystem Awareness

\- disclosure policy;

\- recipient/role and decision purpose;

\- permitted/forbidden attributes;

\- retention/linkability/correlation constraints;

\- selective-disclosure or pseudonymity capabilities;

\- privacy risk/criticality constraints.

&nbsp;

EA outputs to this function

\- minimum EHD/envelope field set required for the receiving decision;

\- request for a privacy-preserving substitute or coarser abstraction where full disclosure is unnecessary;

\- indication that insufficient disclosure leaves an epistemic qualifier unknown rather than authorizing inference.

&nbsp;

Internal EA functions

F1, F4, F8.

&nbsp;

Boundary

Privacy can legitimately limit what EA learns. The correct consequence is bounded uncertainty, not forced disclosure or assumed certainty.

&nbsp;

## IF-S11 — Ecosystem Signa