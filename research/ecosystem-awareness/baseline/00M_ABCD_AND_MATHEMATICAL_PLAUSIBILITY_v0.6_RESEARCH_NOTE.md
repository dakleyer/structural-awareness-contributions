# A/B/C/D Semantics and Mathematical Plausibility of Scoped Requalification

**Research note:** v0.6, draft for external review, 2 October 2026. This note develops an **argument for mathematical plausibility** of the scoped qualification and repositioning support proposed for Ecosystem Awareness (EA) / Ecosystem Positioning (EP). It connects those operations to established mathematical structures, identifies assumptions and gives limited examples and counterexamples. It does not prove full-system consistency, engineering feasibility, economic advantage, collective convergence or operational effectiveness. No formal Technology Readiness Level (TRL) is assigned by this note.

**How to read this note:** sections 1–2 define A/B/C/D and illustrate their differences. Sections 3–6 examine the four mechanisms and their mathematical limits; section 7 assesses the strength of the argument. The definitions are proposed as a common semantic basis for EA/EP; they are not presented as an established mathematical taxonomy. No prior knowledge of the project documentation is required.

**Research question.** Under what conditions can actors combine partial metadata to recognize that an aspect has become more or less assessable, and identify a justified direction for reviewing their observation window, without assembling all source data? This note bounds that question through representations, conditions and examples; it does not provide a complete characterization.

**The claim in one paragraph.** Given declared functional meanings and legitimate scope correspondences, limits and exploration opportunities can be represented and composed without requiring a complete model of the open ecosystem. Some bounded review questions can be answered from qualified summaries; other cases can preserve uncertainty and identify a direction for review. Existing mathematics supplies representations for these tasks and their limits. Establishing useful profiles and implementations is subsequent work.

Here, **scope** means the subject and boundaries of a particular question; an **observation window** is the part a process currently examines. **Assessability** means having enough variables and a defensible method to evaluate a specified aspect. **Requalification** means revising that assessment when its grounds or context change. A **profile** specifies the use case, eligible inputs, interpretation rules, scope and assumptions under which an operation is examined. These explanations orient the reader without prescribing an implementation.

## 1. Proposed canonical definitions: four different relations to one process

Fix a **producer, functional process, question, subject/scope, capability and time**. Ask: what did that process deliver; what did it already establish about the basis and limits of its result; where does it have a credible but still uncharacterized route to explore; and what can affect it beyond its effective ability to determine? These are four *components of one qualified position*, not four mutually exclusive bins for objects, four required message fields or four probabilities. Change the process or the question and the same datum may change component. The components do not partition a closed universe or add up to 100%.

The proposed canonical vocabulary pairs A/B/C/D with **active exploitation, characterized exploitation reserve, exploration frontier and residual uncertainty beyond effective evaluation**. These names describe the position of a process. The associated exploitation, evaluation and exploration functions are defined separately in §1.7: a reserve is not an activity, and evaluating an already characterized reserve differs from exploring an uncharacterized frontier. This vocabulary is specific to the present proposal; its connection to established exploration–exploitation literature is discussed in the companion note.

| Component | Practical reading | What distinguishes it |
|---|---|---|
| **A** | Result of active exploitation | What the process actually establishes and delivers through its current activity. |
| **B** | Characterized reserve of exploitation, together with the basis and limits of A | Known support and assessable remainder: the process has defensible grounds for evaluating specified further work, even when it does not undertake it. |
| **C** | Exploration frontier | A grounded avenue that could become assessable through exploration, but whose evaluation basis has not yet been established. |
| **D** | Residual uncertainty beyond effective evaluation | Potentially material influences whose relevant effects this process has no effective route to evaluate under its current conditions; some related indicators may still be monitored. |

### 1.1 A — functional result of active exploitation

The answer, estimate, decision or other result the process actually establishes and delivers to its operative consumer for the declared question, scope and time. A may itself be a probability, confidence interval, cost estimate or capability assessment **when producing that measure is the function of this process**. A states what that result is; it does not assert that the entire ecosystem has been determined.

“Active exploitation” describes using the process's current capability to produce this result; it does not restrict A to a deterministic answer or a physical action. An exploration process also delivers A when it reports findings. Its own unexplored frontier remains C.

**Recognition question:** What, precisely, did this process deliver as its result?

### 1.2 B — established basis, limits and characterized reserve

What the process already knows or can defensibly calculate **about A and the defined part left out of A**: variables and model used, coverage and support, validity conditions, known exclusions, uncertainty, confidence or error margin, feasible additional measurement, its estimated time/cost/benefit and the risk or opportunity cost of stopping.

The relevant population or question and a usable basis for these assessments are characterized, even if some possible measurements were not made. A defensible estimate can be an interval or a qualitative bound where the method supports it; B must not invent a numerical probability merely because a remainder is known.

B is the **reserve of exploitation** where further use of resources, capabilities or measurement is already assessable. It also preserves the foundations and limits of what has been delivered. Choosing not to use a characterized reserve does not turn it into C, whether the reason is cost, time, policy or another priority. Cost–benefit reasoning is possible only to the extent that its inputs are justified; it is not a compulsory numerical score for every B assertion.

**Recognition question:** Can we identify the question or excluded population and the variables/method that make its qualification or further evaluation assessable?

### 1.3 C — witnessed but uncharacterized explorable frontier

There is a reason to think a *relevant avenue of exploration exists* and that this process could start pursuing it with a plausible capability. Yet the potential targets or questions are open, and it lacks sufficient variables or a validated frame to calculate the extent, acquisition cost, feasibility, expected benefit or risk of pursuing that frontier. It may name examples, a direction and the evidence for the opportunity; it cannot claim a measured margin or enumerate the frontier. **Knowing that one could look is not knowing what one would find.**

C is the **frontier of the exploration function**: potentially evaluable, but not yet brought into a frame that supports the relevant evaluation. The process need not have calculated a reason for leaving it unexplored. In particular, “we have not investigated it” must not be rewritten as “we calculated that investigating it would not pay.” Nor must C be an inventory of known targets: a direction and grounds for beginning may be all that is available.

**Recognition question:** Is there a grounded possibility of exploration, while the basis needed for the B-type calculation is still missing?

### 1.4 D — residual uncertainty beyond effective evaluation

A potentially material condition, dependency or residual whose relevant effect this process has no effective route to evaluate with its present access, authority, method, capability and time. Some factors can be named, and some associated conditions or indicators can be observed. That does not establish a defensible assessment of their likelihood, impact or interactions for the question at hand. The full residual cannot be enumerated.

**D may be monitored without being evaluable.** Observing a change in an indicator can justify reviewing the conditions for reliance without supplying a probability or impact estimate for the underlying influence. The observation is A of the monitoring function; the unresolved effect can remain D of the affected process. A list of twenty named influences is a partial account of that residual, not a complete model of it.

D is a **relative limit of this process**, not a claim of universal unknowability. Mere inability to control a factor does not make it D: a defensible estimate of an uncontrollable risk can be A when it is the delivered result, or B when it qualifies another result. Conversely, inability to evaluate an effect does not imply that all precaution or containment is impossible.

**Recognition question:** Could this influence matter, while its relevant effect remains beyond this process's effective route to evaluation under the declared conditions?

### 1.5 Boundaries between components

**A versus B is a question about the function, not the datatype.** If a forecasting process delivers “probability 0.72 of event X” as its operative answer, that probability is A. The calibration, coverage, confidence limits, known exclusions and cost of reducing its error are B insofar as they are established for that answer. If another process delivers a yes/no verdict and attaches a justified probability of error to qualify that verdict, the verdict is A and the error assessment is B. The same is true of a cost–benefit calculation: it can be A when it is the deliverable, or B when it qualifies whether and how far to examine a different result.

**B versus C is the decisive boundary.** A known set of candidates that the process could assess, with a defensible account of the variables, sampling frame, effort and possible gains or losses, remains B when it elects not to assess them all. The decision to stop does not move that known, calculable remainder into C. C begins where that account is unavailable: the process has some basis to say that there may be more to explore, but does not yet know the population or have the variables needed to estimate its cost, feasibility, yield or risk. A rough number unsupported by such a basis does not turn C into B. Conversely, B can record a known omission without a made-up numerical error margin. It must state which part is characterized and which estimates are actually defensible.

**C versus D is a question about a route to evaluation.** C has a grounded route to explore toward evaluation, although its result and full effort are unknown. D covers material influence whose relevant effect lies beyond this process's effective evaluation routes. Access is one possible barrier; method, capability, authority and time can also matter. Merely observing an associated indicator does not establish such a route. The process's inability to quantify that exposure is part of the boundary, not a probability to be filled in. A new capability, participant, mandate or time horizon can move *a specified aspect* from D to C, B or A; it does not make the remaining D disappear. An item whose scope and capability boundary have not even been established stays **without an established A/B/C/D role** (UNKNOWN), rather than being forced into C or D. This differs from not knowing what kind of producer or interface supplied the assertion; see §3.1.

A producer may report B without C, a partially witnessed D without enumerating all of D, or only A. Silence and an empty list prove neither absence nor completeness. No component's name authorizes the receiver to manufacture a value that the producer has not established.

### 1.6 The same phenomenon can have different roles for different actors

A/B/C/D qualifies an assertion in a process, not a phenomenon once and for all. The same question about the same place may be C for an actor with an unexplored route, B for another with a characterized assessment reserve, and the subject of an A delivered by a specialist. For an actor lacking any effective route to evaluate its relevant effect, it may remain D. Different aspects of one phenomenon can also carry different roles within one process. A defensible interval for one aspect belongs to A or B according to its function; it does not quantify every open aspect of that phenomenon.

This asymmetry is an opportunity for composition: one actor's qualified basis may fill a specific gap in another's exploration. But the source's role is preserved, and the receiver must establish its own qualification. Shared subject matter alone does not transfer capability, access, authority or validity. Monitoring and disclosure alone do not promote D into A.

### 1.7 Exploitation, evaluation and exploration: distinct functions

**The exploitation function** uses established capabilities and an existing frame to carry out the current activity and deliver its operative result, A. “Active” describes what is actually being done, rather than everything the process could do. Exploitation means applying an established capability; it does not require commercial benefit or impose a resource-allocation policy.

**The evaluation function** applies a sufficiently established question, variables and method to assess a characterized aspect or option. Within the B reserve, it may evaluate a further measurement, qualify the result already delivered, or assess whether to activate a known capability. The evaluation can remain unperformed even when its method and relevant effort are already characterized. Its eventual result is A of that evaluation process; when used to qualify another process's result, it can play a B role there. Evaluation does not mean that every outcome is already known or certain.

**The exploration function** investigates a grounded but uncharacterized avenue in C to discover relevant targets, variables, methods or opportunities and develop a basis for evaluation. It need not start from an enumerable candidate population or a defensible estimate of expected benefit. A bounded exploratory step can have a known budget while its wider frontier remains C. Learning enough to characterize one aspect may bring that aspect into B; producing a finding yields A of the exploring process. Neither operation exhausts the open frontier.

The practical distinction is therefore **evaluating within an established frame versus exploring toward a frame not yet established**. An activity may contain both functions; each claim must identify which aspect is already evaluable and which still needs exploration. Monitoring indicators associated with D is also possible, but is not by itself exploration capable of evaluating the unresolved effect.

A diminishing B reserve can be a reason to explore C. So can a new opportunity, changed conditions or another participant's expressed need. Exhaustion is neither required nor a sufficient instruction to explore: the actor's commitments, capability and available resources still govern what it undertakes.

## 2. The cats: one example, four different statements

Consider a process counting cats in a room:

- **A — the result:** it counts seven cats and delivers that count to its consumer.
- **B — the established basis and known remainder:** it knows the room's defined sampling frame, which part it has not checked, which variables determine the effort of checking it and which error or opportunity estimates its model actually supports. It can rationally decide to stop after seven; the remaining known, assessable room is still B. If the omission is known but an error percentage cannot be supported, B records the omission **without** that percentage.
- **C — the open exploration route:** the same equipment could be taken outside to look for cats. There is a street and a way to begin, but no characterized street-cat population or adequate variables to estimate search cost, yield, feasibility or benefit. This does not establish that more cats are there.
- **D — the residual beyond evaluation:** a dependency affecting the count may have an effect the process has no effective route to evaluate with its current access and method. It might monitor signs of movement at a boundary without being able to evaluate their effect on the count. A closed but inspectable room is not D merely because it is closed: a characterized inspection can belong to B, and a grounded but uncharacterized exploration route to C.

Two agents each saying “I could search street Z” have *not* jointly observed a street population. Their C declarations may justify inspecting an overlapping frontier if street Z matters to a receiving decision; they do not justify “there are probably many cats” without additional qualified evidence. If exploration identifies a defined local population **and the variables needed to assess its remaining measurement**, that portion can become B for a new position; performing the measurement may produce a new A. The earlier positions remain correctly attributed to their earlier scopes and times.

“Cats on street Z” and “birds on street Z” do not become the same proposition because their location matches. A receiving frame may legitimately group them as “fauna near street Z” **only if** the declared mapping preserves the broader meaning and does not infer an unsupported cat population from a bird-related limit.

The agricultural analogy makes the practical distinction equally clear. A is the result of working the current field. B includes the characterized reserve: known plots, resources and further work whose relevant demands can be assessed. The next hill is C when there is a grounded possibility of exploring it but no established assessment of its land, effort or yield. A dependency affecting the harvest belongs to D only insofar as its relevant effect lies beyond this process's evaluation routes. A surveyor may already have a B-type basis concerning that same hill; an assessment delivered by a surveying process is its A. Whether any of that basis can legitimately help the farmer is the composition question, not an automatic consequence of sharing a location.

## 3. What the four mechanisms need from mathematics

| Proposed operation | Mathematical basis | What remains an assumption or open question |
|---|---|---|
| Recognize A/B/C/D consistently | Functional roles and qualified assertions relative to a declared process and frame. | Producer meaning, capability and evidence must be supplied; open C/D cannot be exhaustively classified. |
| Relate different actors' scopes | Typed contexts and partial maps; compatible restrictions to a common question. | Semantic correspondence must be justified; a common label or MSCA does not establish it. |
| Compose qualified summaries | Task-relative abstraction and aggregation with explicit provenance. | The abstraction must preserve what the review question needs; reduced total cost is not automatic. |
| Requalify with direction | Versioned contextual judgments, partial orders and signed comparisons of qualified quantities. | A transition needs new grounds or a changed frame; a sign is specific to a property, not a universal value of A/B/C/D. |

These are related operations, but their separate existence does not prove that arbitrary versions compose correctly. The scope, reference result, assumptions and provenance retained by one operation must suffice for the next. A missing correspondence or qualification is a mathematical limitation of that composition, not a license to invent it.

### 3.1 Common semantics and partial recognition

A datum has an A/B/C/D role only relative to its producer, function, question, scope, capability and time. A compound statement may have to be separated into several assertions before those roles can be assigned. A probability is not intrinsically B. Nor does an unused capability make an otherwise characterized omission C.

The mathematical object can be a relation between qualified assertions and these roles. A suitable profile could make selected judgments mechanically decidable. This note neither defines a universal classifier nor derives semantic truth from a finite message. UNKNOWN records lack of grounds for a judgment; it is not a fifth substantive region of the ecosystem. D includes witnessed limits and an acknowledged open residual. Lack of control alone does not place a well-characterized factor in D; the relevant limit of determination must remain explicit.

**Two independent classification questions.** Identifying the kind of producer or interface is different from establishing the A/B/C/D role of an assertion. An unfamiliar kind of producer can still supply interpretable B/C/D if its function and evidence are clear. Conversely, recognizing the producer's kind does not establish the role of every assertion it supplies. Neither absence of classification makes an assertion D.

### 3.2 Shared scope and partial maps

A common frame specifies enough of the subject, question, spatial or relational scope, time and material assumptions to interpret declarations together. Partial maps express that such interpretation is available for some declarations and not others. Cockett–Lack supplies a formal language for partiality [R1]; it does not discover a valid correspondence between two real-world concepts.

Two accounts of the same street may support a common question about fauna while remaining incompatible with a question specifically about cats. A useful scope mapping must preserve the proposition actually being considered, and explicitly identify any qualification that a broader description no longer supports. Identifying a shared scope is therefore a conditional operation, not a consequence of lexical similarity. Not knowing whether a mapping exists is also distinct from proving that no mapping exists. A finite number of declarations does not make arbitrary semantic matching decidable.

The **Minimum Sufficient Control Architecture (MSCA)** provides a reference for the objective and control dimensions under consideration. It may help anchor this comparison. Whether a particular MSCA supplies enough common meaning remains to be justified; using the same architecture does not by itself make two declarations comparable. A justified mapping can also relate one actor's C/D gap to another's characterized B reserve. Such a correspondence identifies a possible route to assessment; it is distinct from establishing that access is available, that evaluation has occurred, or that the gap is closed.

## 4. Summaries: exact sufficiency and informative incompleteness

The central question is whether a summary retains enough information for a particular review. A summary may support an exact answer, a range of possible answers, or no useful answer.

### 4.1 When a summary is sufficient for an exact answer

Use the following notation:

| Symbol | Meaning in this section |
|---|---|
| \(\mathcal X_p\) | The modeled source states allowed by a declared profile \(p\), including its assumptions. |
| \(X,X'\) | Two possible source states in that class. |
| \(r_x\) | The answer function for a review question indexed by \(x\), specified independently of the summary. |
| \(\pi(X)\) | The combined summary of source state \(X\). |
| \(m\) | A particular summary available to the receiver. |

This class models a bounded question; it does not enumerate the open ecosystem or all of C/D. The following is an **exact task-sufficiency condition**:

\[
\pi(X)=\pi(X')\;\Longrightarrow\;r_x(X)=r_x(X')
\qquad(X,X'\in\mathcal X_p).
\]

**In words:** if two source states produce the same summary, they must give the same answer to the review question. Information discarded by the summary cannot change that answer.

Equivalently, there is a function \(g_x\) on the summary image such that \(r_x=g_x\circ\pi\). The elementary argument is that every class of source states with the same summary must have the same answer; that answer defines \(g_x\).

**This functional factorization does not establish computability, tractability, useful compression or economy.** Keeping all the data trivially satisfies it, and defining the review question from the summary would make the condition circular. The question must be fixed independently.

**Three different tasks must be distinguished:**

- **Define** the condition: state what sufficiency would mean.
- **Prove** it symbolically: show that it holds under declared assumptions. Such a proof can sometimes cover an infinite class.
- **Check** it exhaustively: evaluate every relevant case. This is possible for a finite, effectively enumerable class with computable summary and answer functions and decidable equality for both summaries and answers, but may still be prohibitively costly.

Mere enumerability of an infinite class does not give a terminating universal check. No general verification method is supplied here, and examples or tests do not establish the implication for all source states.

For a simple illustration over an infinite domain, the question “is this real number positive?” factors through its sign: numbers with the same sign give the same answer. That statement is proved symbolically without enumerating the real numbers. It illustrates the distinction between proof and exhaustive checking, not a sufficient summary for EA in general.

### 4.2 When a summary leaves several answers open

Exact sufficiency is a demanding special case. For an incomplete summary, consider the possible answers compatible with it:

\[
\Gamma_x(m)=\{r_x(X):X\in\mathcal X_p,\ \pi(X)=m\}.
\]

**In words:** \(\Gamma_x(m)\) contains all answers that the modeled source states could give while producing the available summary \(m\). This defines a set; it does not provide an algorithm for finding it.

A justified abstraction may instead supply a **sound conservative approximation** \(\widehat\Gamma_x(m)\supseteq\Gamma_x(m)\), conditional on its assumptions and source evidence. It must retain every genuinely compatible answer, but may also retain alternatives that no compatible source state would produce. Several retained answers therefore show uncertainty at the approximation level; they do not prove that each alternative is genuinely possible. EA must distinguish this approximation from the exact set.

Even without recovering the hidden answer, a review indication may report a lost bound, an unresolved overlap or an available exploration direction. If the evidence fits no admitted state, that indicates inconsistency or model inadequacy, not certainty. Establishing this inconsistency can itself require further analysis: a conservative approximation need not detect that the exact set is empty. Because it is a superset, the approximation can still contain candidate answers even when no modeled source state is compatible with the available summary. Abstract interpretation provides an established mathematical precedent [R2]; applying it soundly to EA remains a separate task.

### 4.3 What aggregation can preserve, and what it costs

A set union of attributed declarations can be **associative, commutative and idempotent**: grouping does not change the result, order does not change it, and adding the same declaration twice has no further effect. Conflicting declarations can both be retained. Deduplicating a declaration does not establish whether different declarations depend on the same original observation.

For a small failure case, actor P reports a C frontier on street Z and actor Q republishes the same lead under its own attribution. Set union can correctly retain two distinct declarations. A receiver that counts them as two independent grounds for increasing confidence has nevertheless made an evidential error: there is only one originating lead. Idempotence removes repeat insertions of the same declaration; it does not discover shared origins. Unknown source dependence must remain unknown, and neither report establishes a cat population. The failure lies in the corroboration rule, not in set union itself.

Results on Conflict-free Replicated Data Types (CRDTs) concern convergence under stated assumptions [R3]; they do not establish honest sources, upstream independence or Byzantine resilience. Exact source-lineage tracking can require increasing state.

Some statistical questions admit compact summaries with bounded error in a streaming-space model [R4], while other estimation tasks have substantial communication requirements in distributed models [R5]. These are distinct resource models; a space bound does not transfer directly into an EA communication bound. This supports the plausibility of using less than all source data **for suitable questions**, not a universal compression result for EA. Reduced transmission or storage is distinct from lower total cost: preparing, interpreting and maintaining summaries may dominate. This note does not specify transport, storage, adapters, execution budgets or a mandatory payload.

## 5. A small positive example and its boundary

Suppose two appropriately qualified declarations share a street segment, time horizon and inspection method. One supplies a defined scope of \(N=20\) doors. The other supplies a justified per-door inspection-effort bound \(c\in[2,3]\) minutes applicable to each door in that scope. Assume each door is inspected once, effort is additive, and travel/setup are explicitly excluded. Then inspection effort for those twenty doors lies in \([40,60]\) minutes. No independence assumption is needed to sum valid per-door bounds.

The example shows a narrow possibility: complementary, already available qualifications can make **one previously unassessable aspect** assessable, without sharing every source observation. It gives no cat-population estimate, expected benefit, permission to inspect or complete search cost. The street beyond those doors can remain an open C frontier. If both declarations only say “we could search this street”, neither the door count nor the effort bound follows.

The component label remains process-relative: the derived cost qualification can be B relative to the result being qualified; if producing that cost is itself the function, it is A of that function. A source value is not admissible on a metadata-only route just because someone renames it “metadata”; a route that excludes source A must justify that these are eligible qualifiers or leave that use outside its scope. This is a condition on the example's admissible inputs; the numerical calculation alone does not establish it.

An already characterized inspection can also acquire a new reason to be performed. Its owner may have left it unused because the local benefit did not justify the effort. If compatible declarations reveal its relevance to other actors' C/D gaps, the owner can reassess that option in a broader context. The option remains characterized in B while its evaluation is pending; performing that evaluation can deliver A of the evaluating function. The new demand does not establish the inspection result or a quantified collective benefit. This is a change in the grounds for using a reserve, distinct from discovering that reserve.

Thus aggregation can contribute grounds for a **partial C→B requalification** when it supplies a missing, justified assessment basis. It cannot accomplish that transition merely by accumulating C labels. The example illustrates a compatible small fragment; it is not an existence proof for every requirement of EA/EP.

## 6. Direction, requalification and repositioning

### 6.1 Changes in component role

| Movement for a specified aspect | Required grounds | Interpretation |
|---|---|---|
| C→B | A defined question and sufficient variables/method to assess that aspect become available, possibly through complementary qualified declarations. | This aspect has become assessable. Others may remain C or D. |
| B→C | The former assessment basis loses applicability; a plausible exploration route remains. | This aspect needs open exploration again. Its previous B is retained as an attributed historical record, with any correction or supersession linked to it. |
| B→UNKNOWN | The receiver no longer has sufficient grounds to assign a component role. | Missing grounds do not establish either an exploration route or a determination barrier. |
| B→D | The former assessment basis no longer applies, and an effective barrier to evaluating the material effect is established. | D requires grounds for that boundary; missing metadata alone is insufficient. |
| D→C/B/A | A changed capability, scope, authorized access or participant provides grounds for one specified aspect. | The relevant boundary changes; the unenumerated residual is not eliminated. |

These are relations between contextual judgments, not transfers of objects between four globally exhaustive sets. More evidence can invalidate an earlier model and weaken its current qualification. There is no contradiction between preserving all historical declarations and revising the current judgment. A plain accumulation of old declarations alone does not perform that revision. To make revisions interpretable, each declaration must retain its time basis and the version of its interpretation rules. An unknown version cannot be interpreted merely by resemblance to a familiar one.

### 6.2 A sign without a universal score

A sign describes an increase or decrease in a specified property; it needs comparable frames. For example, if a qualified quantity has old bound \([a,b]\) and new bound \([c,d]\), its change is enclosed by \([c-b,d-a]\). In words, subtracting the old upper bound from the new lower bound gives a lower bound on the change; subtracting the old lower bound from the new upper bound gives an upper bound. These bounds may be conservative when the two values are related.

A strictly positive lower endpoint supports an increase; a strictly negative upper endpoint supports a decrease. A bound compatible with both signs does not establish the direction. These are operations on warranted bounds, not assigned probabilities for open C or D.

Coverage, effort, dependence and assessability can move in different directions. Their changes can be represented together without a total order or one number. “C→B” can indicate increased assessability of an aspect; it does not automatically mean lower risk or higher value. A proposed widening, narrowing or redirecting of a window is a direction relative to an objective and authority frame, not a guaranteed improvement. More reports can also reflect a reporting-policy change rather than a change in the underlying environment.

EA can therefore qualify a direction of review and EP can represent a candidate MSCA position under declared semantics. Mathematical plausibility of this support does not establish an optimal target, collective convergence, autonomous healing of every failure, or permission to execute. A claim of physical regime change needs its own qualified evidence and comparison.

### 6.3 An information limit with an elementary argument

If two source states give identical available metadata and disagree on a hidden target, a deterministic function of those metadata has the same output in both states and cannot always identify the target correctly. A randomized method with the same metadata and the same internal-randomness law has the same output distribution in both states; randomization does not create the missing distinction. Additional assumptions or information can alter the question, and partial predictive value is not ruled out.

This elementary indistinguishability argument is stated here directly. Braverman et al. [R5] provides quantitative communication lower bounds for particular statistical models; it is relevant context, not the source of this generic two-state argument or an EA validation.

## 7. Strength of the argument and the next evidential level

The four operations have meaningful mathematical representations and compatible small examples. No inference of a hidden fact from its absence is needed. This supports **mathematical plausibility as an early research claim**. Plausibility is used here as an explicitly limited assessment, not a standardized mathematical proof category. Full-system consistency, correct scope matching, computable useful abstractions and net benefit remain open.

A compact organizing framework for this note is **typed contexts with partial maps and qualified abstractions**, with explicit attribution and contextual change. The cited traditions illuminate parts of it; this document has not constructed one category, a functor or an algebra that satisfies all EA/EP requirements. Their familiar names cannot substitute for the missing construction. A later formal treatment may choose a categorical organization; a working representation need not use categorical software.

This note addresses **early conceptual maturity, consistent with low-TRL research**. That describes the scope of the research argument; it is not a system-wide TRL assessment. In the cited NASA scale [R6], TRL 2 concerns a formulated concept, TRL 4 laboratory validation, and TRL 5 validation in a relevant environment; a conceptual paper alone does not establish those maturity levels for the complete technology.

**Questions for conceptual review:** Are the definitions distinguishable in the stated contexts? Are the assumed scope correspondences justified? Do the examples respect the difference between exact answers and conservative approximations? Does each cited result support only the claim assigned to it?

**For a later feasibility or validation claim**, the research would need specified producer profiles, scope compatibility cases, justified C→B transitions, loss-driven B→C transitions and matched comparisons of cost, error and deadlines. Those later evaluations are not claimed by this plausibility argument.

## References and scope of support

| Source | What it supports here | What it does not establish |
|---|---|---|
| **R1.** Cockett & Lack, *Restriction categories I: categories of partial maps*, TCS 270 (2002), 223–259. | Formal treatment of partial maps. | Correct real-world scope matching or an EA category. |
| **R2.** Cousot & Cousot, *Abstract interpretation: a unified lattice model for static analysis of programs by construction or approximation of fixpoints*, POPL (1977), 238–252. | Mathematical precedent for qualified abstractions of richer semantics. | A sound abstraction of arbitrary agent metadata, or automatic proof over every infinite domain. |
| **R3.** Shapiro et al., *Conflict-free Replicated Data Types*, SSS (2011). | Convergence conditions for appropriate replicated data types. | Truth of metadata, source independence, or Byzantine fault tolerance; the cited model assumes non-Byzantine processes. |
| **R4.** Alon, Matias & Szegedy, *The Space Complexity of Approximating the Frequency Moments*, JCSS 58 (1999), 137–147; STOC preliminary version (1996). | Task-specific savings and lower bounds for stream statistics. | Universal compact or exact composition of B/C/D. |
| **R5.** Braverman et al., *Communication Lower Bounds for Statistical Estimation Problems via a Distributed Data Processing Inequality*, STOC (2016); arXiv:1506.07216. | Quantitative error/communication tradeoffs in specified estimation models. | A direct theorem about EA or the generic indistinguishability argument above. |
| **R6.** NASA, NPR 7123.1D, Appendix E, *Technology Readiness Levels*. | Maturity terminology and evidence requirements. | A TRL award for this document or for EA/EP. |

- R1: https://cspages.ucalgary.ca/~robin/FMCS/FMCS_06/RestrictionsI.pdf
- R2: https://www.di.ens.fr/~cousot/COUSOTpapers/POPL77.shtml
- R3: https://www.lip6.fr/Marc.Shapiro/papers/2011/CRDTs_SSS-2011.pdf
- R4: https://www.tau.ac.il/~nogaa/PDFS/amsz4.pdf
- R5: https://arxiv.org/abs/1506.07216
- R6: https://nodis3.gsfc.nasa.gov/displayDir.cfm?Internal_ID=N_PR_7123_001D_&page_name=AppendixE
