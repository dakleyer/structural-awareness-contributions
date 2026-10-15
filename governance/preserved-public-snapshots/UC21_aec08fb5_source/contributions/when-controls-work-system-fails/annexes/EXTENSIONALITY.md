## Annex X

**Extensionality: family membership, extension directions and admission.** The mappings below are structural proposals, not executed results in every named domain. A new jurisdiction or sector requires its own authority and domain assumptions; resemblance alone does not admit an extension.

### 1. Why failure scenarios need an extensibility layer

A scenario such as:

- “100 million tokens”,
- “a bridge full of robotaxis”,
- “robots believe they are in Napoleonic France”,
- “4,000 refunds”,
- “a queued database rollback”, or
- “the author pays for their own work”

is deliberately memorable.

But those narrative details are not the architectural claim.

The claim concerns a smaller **failure kernel**: a set of relations among evidence, scope, authority, time, composition, residual state, capacity and decision that can appear in many different implementations.

The purpose of case-study extensibility is therefore to separate:

*minimum narrative instantiation*

from:

*structural case family*.

The minimum case makes the problem inspectable. The family tests how far the same structural problem survives controlled changes in scale and domain.

---

### 2. Three extension directions

This case uses three extension directions.

#### 2.1 Upward / vertical extension

Increase scale or organizational depth while retaining the same semantic relations.

Typical changes:

- more actors;
- more roles;
- more agents;
- nested objectives;
- additional jurisdictions/owners;
- larger dependency graphs;
- more layers of aggregation/delegation/composition.

This document uses **upward/vertical** as synonyms for increasing scale or organizational depth.

#### 2.2 Downward extension

Reduce the case to the smallest implementation that still contains the structural failure.

Typical changes:

- one team instead of an enterprise;
- one production cell instead of a city;
- one assistant plus memory instead of a multi-agent population;
- two records instead of a large registry;
- one queued action instead of a distributed workflow.

Downward extension is especially important because it distinguishes a true structural mechanism from an artefact that exists only because the story is large.

#### 2.3 Horizontal extension

Change the service/business domain while preserving the same structural relations.

The names of resources, organizations, policies and outcomes may change.

The meaning of:

- evidence sufficiency;
- unresolved state;
- authority;
- scope;
- material change;
- provenance/dependence;
- composition; and
- receiving decision

may not silently change.

---

### 3. A failure case-study family

For scenario $C$, define:

$$
Family(C)=
\langle
K_C,\sigma_C,F_C,I_C,R_C
\rangle
$$

where:

- $K_C$ — the structural failure kernel;
- $\sigma_C$ — the type of subject–proposition–decision boundary;
- $F_C$ — the family failure predicate;
- $I_C$ — the decision-material relations that must remain invariant under the mapping;
- $R_C$ — the applicable case-gate acceptance conditions.


The story-specific names, amounts, vendors, locations and technologies are **parameters**, not the kernel.

---

### 4. Admission test for an extension

A proposed extension $C'$ belongs to $Family(C)$ only if all seven tests pass.

![Admission overview: preserve the kernel, decision boundary, failure reflection, acceptance conditions, legitimate controls and finite resources; declare any new primitive. Full tests follow.](../assets/reading/admission_checklist.png)

[Open the scalable figure](../assets/reading/admission_checklist.svg). The accompanying text remains the complete reference.

#### X1 — kernel preservation

There is a mapping:

$$
h:K_C\rightarrow K_{C'}
$$

that preserves every decision-material relation in the kernel.

Changing “bridge” to “hospital bed capacity” is allowed.

Changing “shared scarce resource” into a situation with no shared resource is not an 00F extension.

#### X2 — decision-boundary preservation

The extension has an identifiable:

$$
\sigma'(d,t)
$$

with the same structural proposition and decision dependency.

The subject may change; the role played by evidence/scope/authority/time in the final decision may not.

#### X3 — failure-predicate preservation / reflection

The terminal failure is the same **structural predicate**, not merely a similarly bad outcome.

The kernel mapping induces a trace abstraction:

$$
\alpha_h:Trace_{C'}\rightarrow Trace_C.
$$

An admitted extension must satisfy **failure reflection**:

$$
F_{C'}(\tau)\Rightarrow F_C(\alpha_h(\tau)).
$$

This prevents a superficially similar bad outcome from being counted as evidence for the family.

For example:

- downtime caused by stale queued action may be 00I;
- downtime caused only by hardware failure is not.

#### X4 — acceptance-condition preservation

Every acceptance condition material to the base kernel remains applicable under the mapped roles.

The abstraction must preserve conformance:

$$
Conf_{C'}(R_C,\tau)
\Rightarrow
Conf_C(R_C,\alpha_h(\tau)).
$$

An extension may make additional existing case conditions material. It may not weaken inherited acceptance conditions and still claim to be the same family.

#### X5 — positive-control preservation

A family includes the legitimate counterpart needed to prevent shortcut solutions.

Examples:

- 00G must accept genuine regime change rather than reject every new frame;
- 00H must accept genuinely authorized campaigns and preserve genuine findings;
- 00J must accept legitimate transfer/independent creation rather than block all downstream rights claims.

#### X6 — finite resource and response declaration

Scale may change, but finite decision resources remain explicit: deadline/response horizon, observation or review capacity, relevant cost/burden and fallback. Upward extension does not grant unlimited time, evidence, humans or compute.

#### X7 — no hidden new primitive

If the proposed variant needs a new decision-material relationship or operation that cannot be represented in the base kernel and acceptance conditions, it is a **case-family extension candidate**, not yet an admitted member. Record the proposed addition explicitly; do not hide it by renaming the original roles.

Such a variant may require a separate case before its results can be combined with this family.

---

### 5. Membership is independent of success

The admission test is not:

> “the requirements work, therefore this is the same case.”

That would be circular.

Membership is established from:

- the structural kernel;
- decision boundary;
- relation mapping;
- requirement applicability; and
- positive/negative control semantics

**before** scoring a candidate implementation.

A gate-conforming implementation may therefore pass or fail the extension test empirically; its outcome does not determine family membership.

---

### 8. Six case-study families

| Family | Minimum instantiation | Structural kernel | Extensibility profile |
|---|---|---|---|
| **00E** | Meridian / 100M-token enterprise strategy | lossy qualification compression + bounded/unbounded uncertainty mismanagement compounded through a composed decision chain | [00E profile](EXTENSIONALITY.md#extension-s1) |
| **00F** | Aurora City / Central Bridge | locally justified postures become incompatible over a shared decision/resource after heterogeneous windows or frame drift | [00F profile](EXTENSIONALITY.md#extension-s2) |
| **00G** | Bar-to-Napoleon | repeated/correlated claims are promoted into independent support or authority and displace a still-valid mission/frame | [00G profile](EXTENSIONALITY.md#extension-s3) |
| **00H** | Quiet Four Thousand | a genuine material opportunity exceeds current authority; system must preserve the finding without unauthorized execution | [00H profile](EXTENSIONALITY.md#extension-s4) |
| **00I** | Patch That Undid the Fix | decision correct at qualification time becomes stale before actuation while technical reach/authorization remains valid | [00I profile](EXTENSIONALITY.md#extension-s5) |
| **00J** | Author Pays for Their Own Work | a valid narrow provenance statement is promoted through broken lineage/correlation into a stronger unsupported downstream enforcement proposition | [00J profile](EXTENSIONALITY.md#extension-s6) |

---

### 9. First-pass family status

The six profiles distinguish three statuses.

#### Strong structural extension

The mapping to the kernel is direct enough to treat the variant as an in-family design case without changing the failure semantics.

This still does not make it an executed benchmark result.

#### Candidate extension

The analogy is plausible but one or more mappings need a frozen fixture or additional source/owner definition before admission.

#### Out-of-family neighbour

The situation may be important but lacks one of the kernel relations. It should not be used as evidence that the present family generalizes.

---

### 11. Next evidentiary step

The current profiles are a **first-pass structural generalization**.

For each family:

1. freeze one or more nontrivial extensions;
2. map the same acceptance conditions to the new roles;
3. preserve matched facts, authority, evidence and resource limits across the selected three-route experiment;
4. observe the family failure predicate and legitimate-activity controls;
5. record the tested configuration, branch outcomes and limits;
6. retain any extension that escapes the kernel as a boundary finding, rather than forcing it into the family.


Family membership, a passing finite experiment and a universal guarantee are different claims. This contribution defines admission and tests; it does not supply a universal prevention theorem.


<a id="extension-s1"></a>

### X — Family S1

| | |
|---|---|
| **Family** | Compounded Epistemic Collapse under Lossy Qualification |
| **Minimum instantiation** | [00E — 100 Million Tokens / Meridian](scenarios/S1.md#annex-s1) |
| **Status** | first-pass structural family profile; extensions unexecuted unless separately recorded |

> **Family claim.** The 100-million-token number, banking/insurance sectors and Meridian organization are fixture parameters. The structural case is a composed decision system in which decision-relevant qualification is lost or mismanaged across recursive handoffs, causing Type-2 false closure and/or Type-1 determination expansion that compound instead of cancelling.

#### 1. Minimum case and kernel

The Meridian fixture combines four positions:

- in-window false certainty after lossy compression;
- in-window repeated search/HOLD/human escalation;
- out-of-window possibility promoted into strategy before sufficient determination;
- out-of-window residual turned into unlimited search/paralysis.

The minimum kernel is:

$$
K_E=
\langle
lossy\ handoff,\;
bounded\ decision\ window,\;
unresolved/residual\ state,\;
finite\ capacity,\;
composed\ downstream\ decision
\rangle.
$$

The terminal family predicate $F_E$ is present when a material downstream decision relies on a composed representation in which qualification loss and/or unbounded determination produces unsupported closure, terminal paralysis, or both.


#### 2. Inherited case acceptance criteria

The extension retains the S1 framing, source qualification, reviewer capacity, option-admission, bounded inquiry and final-composition gates. Additional scale must not weaken those acceptance criteria.

#### 3. Upward / vertical extensibility

**Strong structural extensions:**

- a larger enterprise with dozens or hundreds of specialist agents and several aggregation tiers;
- a conglomerate combining finance, operations, legal, cyber, supply-chain and strategy agents;
- a public-sector or multinational planning network where local reports are compressed into increasingly high-level decision products;
- multiple human review layers whose capacity becomes part of the determination bottleneck.

The case remains 00E if more layers amplify the same qualification-loss / bounded-capacity problem rather than introducing an unrelated failure.

The exact token count may scale from thousands to billions; “100 million tokens” is not the family boundary.

#### 4. Downward extensibility

**Strong structural extensions:**

- two specialist agents feeding one decision agent;
- one LLM summarizer feeding one human reviewer;
- one assistant that repeatedly compresses earlier qualified research into short summaries and later reasons only from those summaries;
- one analyst + one automated control queue where missing qualification causes repeated search or forced binary closure.

A minimum downward fixture needs only:

1. a source state containing materially distinct alternatives/qualification;
2. a many-to-one handoff that can discard them;
3. a later decision for which the discarded distinction can matter;
4. finite time/capacity.

If those four relations disappear, the variant is not an 00E case merely because an LLM is involved.

#### 5. Horizontal extensibility

**Strong structural candidates:**

- cyber incident triage and remediation planning;
- scientific/R&D portfolio selection;
- procurement and supplier-risk review;
- legal/compliance analysis;
- healthcare operations or public-service planning **only at the architectural decision-flow level**, without assuming domain-specific clinical/legal correctness;
- software delivery/operations where several local diagnostics are compressed into one release or rollback decision.

The domain changes; the kernel remains recursive qualification loss plus bounded/unbounded determination pressure.

#### 6. Boundary / falsifier

Out of family:

- a single wrong answer with no downstream composition or qualification loss;
- pure hallucination with no relevant handoff or determination process;
- simple resource exhaustion unrelated to unresolved decision state;
- a failure caused solely by malicious data when the qualifying architecture otherwise preserves the kernel state.


<a id="extension-s2"></a>

### X — Family S2

| | |
|---|---|
| **Family** | Systemic Divergence under Heterogeneous Local Windows and Shared Capacity |
| **Minimum instantiation** | [00F — The City That Stopped Safely](scenarios/S2.md#annex-s2) |
| **Status** | first-pass structural family profile |

> **Family claim.** Robotaxis, buses, emergency vehicles and Central Bridge are the minimum mobility scene. The structural case is that locally justified postures derived from heterogeneous windows become mutually incompatible over one material shared resource/decision surface while local safety/correctness can remain intact; R2 additionally introduces an admitted frame change.

#### 1. Kernel

$$
K_F=
\langle
multiple\ independently\ governed\ actors,\;
heterogeneous\ windows,\;
shared\ scarce\ resource,\;
frame\ compatibility\ and\ admitted\ context\ change,\;
locally\ defensible\ postures,\;
composition\ dependency
\rangle.
$$

The family failure $F_F$ occurs when locally acceptable postures jointly consume or block the same resource/mission in an incompatible way because the shared decision surface is not sufficiently requalified.


#### 2. Inherited case acceptance criteria

The extension retains the S2 gates for the shared resource, source changes, plan compatibility, responsible response, targeted observation and bounded resolution.

#### 3. Upward / vertical extensibility

**Strong extensions:**

- several corridors, municipalities or jurisdictions;
- regional logistics + emergency + public/private mobility systems;
- shared urban infrastructure with nested resource owners and multiple legitimate vetoes;
- multi-site industrial or cloud infrastructure where local controllers compete for shared capacity.

Scale may increase dramatically so long as the core remains **local validity + shared-resource incompatibility**, not centralized controller failure.

#### 4. Downward extensibility

**Strong extensions:**

- one factory production cell where safety, maintenance and production controllers make different locally valid claims over one machine/time slot;
- one warehouse intersection shared by autonomous forklifts, picking agents and human safety control;
- one cloud cluster where deployment, incident response, backup and capacity controllers make incompatible local allocations;
- one hospital operating-resource scheduling problem at the level of beds/rooms/staff availability, provided the case is treated as resource/authority composition rather than clinical judgement.

The smallest fixture needs two independently justified postures and one shared material resource whose simultaneous use is incompatible.

#### 5. Horizontal extensibility

**Strong candidates:**

- logistics hubs and loading windows;
- compute/GPU capacity allocation;
- factory-machine scheduling;
- appointment/room/staff allocation;
- energy or charging capacity;
- shared maintenance windows.

The bridge is not essential. **Non-fungible shared capacity under heterogeneous local frames** is.

#### 6. Boundary

Out of family:

- ordinary congestion with no divergent decision frames;
- one controller making a bad routing decision;
- collision-avoidance failure itself;
- failures where all actors share one current authoritative resource state and simply violate it.


<a id="extension-s3"></a>

### X — Family S3

| | |
|---|---|
| **Family** | Collective False-Context Convergence and Mission/Role Drift |
| **Minimum instantiation** | [00G — Bar-to-Napoleon Cascade](scenarios/S3.md#annex-s3) |
| **Status** | first-pass structural family profile |

> **Family claim.** “Robots in a bar think they are in Napoleonic France” is a mnemonic. The structural case is that repeated or correlated claims are mistaken for independent evidence/applicable authority and displace a still-valid objective/frame, while a correct system must remain able to accept a genuinely supported and authorized frame change.

#### 1. Kernel

$$
K_G=
\langle
bound\ objective/frame,\;
incoming\ claim,\;
repetition/correlation,\;
source\ dependence,\;
authority/applicability,\;
receiving\ decision,\;
possible\ role/mission\ drift
\rangle.
$$

Family failure $F_G$:

1. one unsupported/inapplicable frame gains operational force through repetition, recency, apparent consensus or authority laundering; and
2. the bound objective/role is displaced without sufficient independent evidence and applicable transition authority.

The paired positive control is mandatory: a genuine independently supported, authorized material frame change must be accepted.


#### 2. Inherited case acceptance criteria

The extension retains the S3 gates and the distinction among message count, source independence, sender identity, proposition truth, applicable authority, objective/role version and legitimate reassessment.

#### 3. Upward / vertical extensibility

**Strong extensions:**

- large multi-agent organizations in which one claim propagates across several agent groups;
- agent marketplaces or federated systems where repeated derived claims appear as independent support;
- enterprise knowledge networks in which summarizers, assistants and planners recursively cite each other;
- social-agent simulations or coordinated autonomous services where effective roles drift away from bound roles.

The graph can grow; the claim/source/authority distinction may not disappear.

#### 4. Downward extensibility — conversational LLMs

This is the important reduction.

A **single conversational LLM can be an 00G extension** when the conversation contains the same structural relations:

1. a bound task/objective or externally checkable frame exists;
2. a user/system/tool assertion introduces an unsupported alternative frame;
3. the model's own repeated paraphrases, memory summaries or prior assistant outputs are later treated as if they were additional corroboration;
4. provenance/dependence on the original assertion is lost or flattened;
5. the assistant's effective role/task drifts accordingly.

This includes a useful class of **sycophantic multi-turn conversations**.

Example pattern:

~~~text
user assertion
  ↓
assistant agrees / restates
  ↓
memory or summary retains the restatement without source dependence
  ↓
later turn sees several mutually reinforcing statements
  ↓
assistant treats repetition as stronger support
  ↓
task/frame drifts
~~~

This is structurally close to 00G.

However:

> a one-turn answer that merely agrees with a user is **not automatically 00G**.

Without repeated/composed evidence, source-dependence loss or task/frame displacement, it may be an unsupported-answer error or ordinary model sycophancy, but it has not yet instantiated the full 00G kernel.

That boundary is deliberate: 00G is a **systemic propagation/composition case**, not a claim that every sycophantic response is the Napoleon cascade.

#### 5. Horizontal extensibility

**Strong candidates:**

- customer-support assistants that progressively adopt an unsupported account state;
- enterprise research assistants whose own summaries recursively become “sources”;
- coding/operations agents that inherit an incorrect incident frame and reinterpret subsequent evidence around it;
- tutoring or advisory assistants where repeated user/assistant assertions displace the stated task criteria;
- multi-agent debate/review systems where derived agreement is counted as independent corroboration.

The exact content can be mundane. No Napoleon, war or robots are required.

#### 6. Boundary

Out of family:

- one hallucinated fact with no propagation;
- an explicitly authorized mission change;
- genuine independent evidence causing the system to update;
- simple recency effects where no receiving decision or persistent objective is displaced.


<a id="extension-s4"></a>

### X — Family S4

| | |
|---|---|
| **Family** | Material Opportunity Beyond Current Authority / Preservation–Execution Separation |
| **Minimum instantiation** | [00H — The Quiet Four Thousand](scenarios/S4.md#annex-s4) |
| **Status** | first-pass structural family profile |

> **Family claim.** Four thousand refunds are not the family boundary. The structural case begins when a participant legitimately discovers a material opportunity/problem outside its current action mandate. The system must preserve and route the finding without converting usefulness, technical reachability or valid leaf authority into unauthorized broader execution.

#### 1. Dual kernel

00H has two complementary base failures.

##### H-A — authority overreach

$$
qualified\ finding
+
technical\ reachability
+
beneficial\ intent
\not\Rightarrow
authority.
$$

##### H-P — preservation loss

$$
qualified\ finding
+
no\ current\ action\ authority
\not\Rightarrow
discard.
$$

The hardening adds a composition form:

$$
valid\ leaf\ grants
\not\Rightarrow
valid\ common\ root/campaign\ authority.
$$

Family failure is:

$$
F_H=F_{overreach}\lor F_{discard}.
$$


#### 2. Inherited case acceptance criteria

The extension retains the S4 finding-preservation and authority gates. A genuinely authorized campaign must remain possible; genuinely independent cases must remain independent.

#### 3. Upward / vertical extensibility

**Strong extensions:**

- millions of accounts/resources instead of 4,000;
- several teams/agents each holding valid leaf authority beneath one possible common campaign;
- multi-company/BPO/platform chains where routing authority and business-effect authority belong to different principals;
- nested delegation chains where local grants are valid but aggregate effect requires a separate root decision.

The decisive question remains whether the composed action set is covered by legitimate current authority and whether the material finding survives when it is not.

#### 4. Downward extensibility

The case can shrink to **two objects**.

Example:

- agent is authorized to remediate asset/account A;
- it discovers the same issue on B;
- B is technically reachable;
- B action is beneficial;
- B is outside current mandate.

The first unauthorized cross-object action already instantiates H-A.

Likewise, if the agent resolves A and closes the task while the material B finding disappears despite a reporting duty, H-P is instantiated.

No campaign or adversary is required.

#### 5. Horizontal extensibility

**Strong candidates:**

- IT remediation: agent fixes one assigned server and discovers the same vulnerability across a fleet;
- cloud-cost optimization: one workload is in scope, a broad savings opportunity is discovered elsewhere;
- procurement: buyer/agent identifies a portfolio-wide pricing anomaly but owns only one purchase/order;
- identity/access administration: one assigned entitlement review exposes a larger pattern but does not authorize mass revocation;
- customer-service, billing, insurance-claims or warranty remediation where local authority is narrower than discovered population effect.

The domain must retain the distinction among **discovery, preservation, authority transition and execution**.

#### 6. Boundary

Out of family:

- the actor already has valid broad authority;
- the finding is not materially established;
- the only problem is fraud detection or technical capability;
- the system lacks any identifiable owner to whom the finding could be preserved/routed — that may require a different governance case.


<a id="extension-s5"></a>

### X — Family S5

| | |
|---|---|
| **Family** | Semantic TOCTOU / Stale Decision-Basis Reuse |
| **Minimum instantiation** | [00I — The Patch That Undid the Fix](scenarios/S5.md#annex-s5) |
| **Status** | first-pass structural family profile |

> **Family claim.** PostgreSQL, rollback and a 40-minute queue are fixture parameters. The family is any system in which an action is correctly qualified at $t_0$, remains technically executable, but a material part of the decision basis changes before $t_1$ and the old determination is reused without sufficient requalification.

#### 1. Kernel

$$
K_I=
\langle
qualified\ action@t_0,\;
deferred\ actuation,\;
material\ basis,\;
change@t_1,\;
technical\ validity\ survives,\;
action-time\ reliance
\rangle.
$$

Failure:

$$
F_I=
changed(material\ basis,t_0,t_1)
\land
execute(old\ determination,t_1)
\land
\neg requalify.
$$


#### 2. Inherited case acceptance criteria

The extension retains the S5 authority, diagnosis, current evidence, freshness, intervening changes, response and check-to-act binding criteria. A second controller or human changing the target remains part of the declared fixture.

#### 3. Upward / vertical extensibility

**Strong extensions:**

- many queued changes across a distributed deployment;
- approval chains spanning several systems and owners;
- orchestration across application, infrastructure, data and policy controllers;
- long-lived plans containing many individually authorized actions whose bases can change independently.

The larger graph is still 00I if the key error is reuse of an earlier determination after material change.

#### 4. Downward extensibility

**Strong minimal forms:**

- one scheduled script;
- one delayed API call;
- one cron job;
- one pending configuration change;
- one pre-approved payment/order/access change;
- one maintenance work order.

Only two times and one material state variable are required.

Example:

> a maintenance order is valid in the morning; the machine is repaired by another route before afternoon; the old work order remains signed and executes anyway.

That is 00I even without LLMs or multi-agent orchestration.

#### 5. Horizontal extensibility

**Strong candidates:**

- software deployment/rollback;
- cloud/infrastructure configuration;
- industrial maintenance;
- access provisioning/revocation;
- scheduled financial/operational transactions;
- logistics dispatch or inventory moves;
- policy enforcement where an earlier eligibility/approval fact expires before actuation.

The domain changes. The semantics “qualified then, stale now” do not.

#### 6. Boundary

Out of family:

- the original decision was already wrong at $t_0$;
- the action never had a material delay;
- only the credential expired and no semantic state changed;
- the action fails technically rather than because its decision basis became stale.


<a id="extension-s6"></a>

### X — Family S6

| | |
|---|---|
| **Family** | Provenance-Scope Inversion into Unsupported Downstream Decision |
| **Minimum instantiation** | [00J — The Author Pays for Their Own Work](scenarios/S6.md#annex-s6) |
| **Status** | first-pass structural family profile |

> **Family claim.** Copyright/payment is one vivid enforcement consequence. The structural case is that a valid record proving proposition $q$ is promoted through broken lineage, correlation or authority substitution into a stronger proposition $q^+$ that the record does not establish, and $q^+$ controls a downstream decision.

#### 1. Kernel

$$
K_J=
\langle
valid\ narrow\ record,\;
source/lineage\ relation,\;
downstream\ transformation,\;
stronger\ proposition,\;
receiving\ enforcement/decision
\rangle.
$$

Failure:

$$
F_J=
valid(record,q)
\land
use(record,q^+)
\land
q\not\Rightarrow q^+
\land
decision(q^+).
$$

Replication/correlation and absent authority can harden the case but are not required for the minimum semantic inversion.


#### 2. Inherited case acceptance criteria

The extension retains the S6 access, source dependence, claim authority, correlated-copy and enforcement gates. Legitimate transfer and independent creation remain required controls; universal blocking is not a valid pass.

#### 3. Upward / vertical extensibility

**Strong extensions:**

- many content/rights registries and marketplaces;
- multi-stage publisher → model/provider → catalogue → licensing/enforcement chains;
- replicated metadata across several organizations;
- multiple rights principals, territories, purposes and policy versions;
- long provenance graphs where many authentic records derive from one upstream claim.

The graph may grow while each record remains locally valid.

#### 4. Downward extensibility

The family can shrink to:

1. one source object $W$;
2. one derived object $D$;
3. one valid generation/provenance record;
4. one downstream claim;
5. one decision that treats the record as proof of a stronger proposition.

A single transformation and one bad proposition jump is enough.

No large registry or multi-agent system is necessary.

#### 5. Horizontal extensibility

##### Strong rights/provenance extensions

- software/open-source licence lineage;
- dataset licensing / permitted-use lineage;
- media/content syndication;
- model/artifact provenance where a technical generation record is confused with ownership or permitted downstream use;
- supply-chain documentation where a record valid for origin/version is promoted into an unsupported entitlement or enforcement claim.

##### Broader candidate neighbour

A similar pattern can appear when:

- an attestation proves “component X passed test Y”;
- a receiver promotes that into “system Z is safe/authorized for action A”.

This is structurally close, but admission as 00J requires the same **proposition-scope inversion through lineage**. If the issue is purely current authority with no provenance/proposition promotion, the authority case S4 may be the cleaner family.

#### 6. Boundary

Out of family:

- a forged record whose problem is authenticity rather than proposition scope;
- a simple copyright disagreement with no machine-readable evidence promotion;
- a valid broader right that actually entails the final decision;
- a false claim created directly with no relevant provenance/lineage transformation.


### X — Extension admission record

Before execution, record the base family; proposed domain and scale; mapped actors, evidence, authority, time and receiving decision; retained kernel; failure predicate and trace abstraction; all X1–X7 decisions and supporting reasons; applicable gates and legitimate-activity control; jurisdiction/domain assumptions; finite resources and deadline; selected technology/route; and admitted change domain if R2 is selected. Mark the variant **admitted**, **candidate pending facts**, or **out of family**, independently of its later outcome. A passing experiment transfers only to the tested configuration and envelope.


