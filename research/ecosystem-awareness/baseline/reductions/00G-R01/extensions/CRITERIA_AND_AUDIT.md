<a id="criterio-común-y-revisión-de-las-tres-extensiones-de-r01"></a>
# Common criterion and review of the three R01 extensions

Version 0.1 · 2 October 2026 · Internal author review assisted by AI

[R01 and extensions table](../README.md#extensiones) · [Hugging Face](./hugging-face/README.md) · [Infoblox](./infoblox/README.md) · [Constructed family](./family/README.md) · [Methodological foundations](./METHODOLOGICAL_FOUNDATIONS.md) · [Reproducible verification](./verify_audit.py) · [Report](./audit_results.json) · [Editorial review](./EDITORIAL_REVIEW.md)

<a id="1-base-fijada-y-objeto-de-la-revisión"></a>
## 1 Fixed base and object of the review

The base is **R01 v0.6**, full text in [commit 114ac132](https://github.com/dakleyer/structural-awareness-contributions/blob/114ac132bc2be4e7008001fe505bf5bd4c36c515/research/ecosystem-awareness/baseline/reductions/00G-R01/Escenario-creatividad-validacion.md), blob `3261a625975e303e12c484bc9c273d7f8819b099`. The documents, proofs, code and results of the three packages published in [commit cbb69f1](https://github.com/dakleyer/structural-awareness-contributions/commit/cbb69f1d673c7844610fdde01fb78a3394497bb0) were reviewed, alongside the audit observations supplied by the author. Neither independence nor a complete reading by the writer of those observations was established; their text declares a partial review.

“Extension” designates a **proposed relation**, whose object and scope must be made explicit. The three case records are evaluated under the same contract, although they do not pursue the same real object:

- **Historical:** map a documented trajectory or episode; it may also contain constructed models inspired by it.
- **Technological:** realize a problem with concrete components and interfaces; a proposed model does not establish its activation in a deployment.
- **Constructed:** specify a synthetic class or instance through declared relations; a construction by transport proves formal existence, not adequacy of an external system.

The H/L/W family is a design framework, not a third technology. Its H is a constructed scenario inspired by questions from the Hugging Face case. The historical HF case record retains an additional obligation of correspondence with its sources; it is neither the same object nor a second historical case.

<a id="historical-and-constructed-scope"></a>
### Historical motivation and constructed failure modes

The objective shared by the extensions is to investigate selected failure modes with R01-compatible features. Complete reconstruction of motivating incidents, including exact reproduction of the Hugging Face incident investigated by METR and Redwood, is outside that shared objective. The modeled mechanism is not identified as the historical cause; the mechanisms may differ. The Infoblox profile is a proposed technological setting, not an assertion that METR investigated it or that a vendor defect occurred.

| Claim | Evidence required | Limit of the conclusion |
|---|---|---|
| Selected conceptual parallel | Explicit matching features and differences | Motivates a test; does not establish formal membership or historical causation. |
| Preservation of a constructed kernel or bound | Applicable correspondence contract, policy class and proof obligations | Establishes the declared formal property, not an equivalence with the entire historical incident. |
| Result of a bounded pilot | Recorded implementation, conditions, traces and uncertainty | Concerns the tested model and scope, not all causes of the motivating incident. |
| Correspondence with a historical episode or causal claim | Separate source-grounded evidence for the declared episode or mechanism | Must not be inferred merely from a similar synthetic outcome. |

An absent R01 failure can weaken the tested hypothesis or proposed applicability; it does not imply that a reported incident did not occur or exclude other causes. Likewise, a present R01 failure does not establish that it caused the historical outcome. A verified synthetic correspondence remains valid only within its contract. References below to historical admission or pending correspondence concern their declared external object or property; they do not make complete incident reconstruction the objective. These distinctions supplement the existing evidence states and leave every proof and admission obligation intact.

<a id="2-contrato-común-de-correspondencia"></a>
## 2 Common correspondence contract

For an effective base `B_{θ*}` and a declared target E, the following are identified:

1. **World representation F and typed kernel bijections h:** operations, relations, facts, parameters and their dependencies, including all groups of R01 §2.13. A table of names does not prove those bijections.
2. **Trajectory projection α:** recovers sequence, queries, observations, decisions, effects and resources. If E adds variables, α need not be invertible over all E. An inverse on the kernel and a lifting of base trajectories are required; not a false bijection with the additional details.
3. **Preservation of information and dynamics:** enabled operations, transition law and available views; no decisive datum may disappear under projection. Changes to topology, permissions or policy require explicit counterparts.
4. **Semantic preservation:** Adm, J, admissible optimum, thresholds and endings of the same task; improvements, abstention and incompleteness are included. Technical acceptance and authorization remain distinct.
5. **Accounting:** all events and their timing; consistent normalizations of units, budget and horizon. Aggregate queries and sufficient certificates are admitted with their effective costs.
6. **Positive and falsifier:** a comparable legitimate alternative that may continue and a modification breaking some transfer condition.

The [sufficient criterion E1–E7 in the mathematical note](./family/KERNEL_AND_PROOF.md#41-obligaciones-e1e7) formalizes that contract for a parameterized kernel. Specific admission to 00G additionally requires C-V-G and A25 X1–X7. Preserving a fragment of R01 does not complete that admission.

**Common admission rule.** E1–E7 fixes the declared complete preservation; a partial correspondence, informational lemma or one-way simulation establishes only its property and scope. That threshold does not change between case records. The proof of a bound in Infoblox is not equated with complete isomorphism, and the formal H/L/W construction is not equated with a verified domain integration. Cases not completing the obligations retain their partial or pending status.

**Two separate claims.** Preserving the kernel with radius `3R_e` or cheaper review allows comparison with the effective configuration `θ*`. It does not automatically preserve the performance of `θ`. Transporting an upper success bound to the target requires simulating **every policy in the target class** in the base, without more information or greater resources, with the same distribution, optimum and success thresholds. A new sufficient capability may resolve the case and invalidate the earlier bound.

<a id="3-estados-de-evidencia-comunes"></a>
## 3 Common evidence states

Claims are recorded with their scope, not a cumulative maturity score. EV1 and EV2 may coexist; an EV4 trial does not by itself prove EV5. Independent review is another property.

| Code | Evidence established | What it does not establish by itself |
|---|---|---|
| EV0 | Proposed argument or correspondence. | Demonstrated preservation or implementation. |
| EV1 | Mathematical proof under declared hypotheses and class. | That an external system satisfies the hypotheses. |
| EV2 | Executed verification of an identified instance or finite grid. | All parameters, sample independence or agent effectiveness. |
| EV3 | Domain implementation with checked interfaces and configuration. | Performance with agents or historical correspondence. |
| EV4 | Execution with agents under a declared protocol and measurement. | Admission to the complete family or independent validation. |
| EV5 | Admission of the specific external object through the complete applicable contract. | Reproduction of an entire incident or a universal guarantee. |

Incident sources have their own executions; they do **not** turn our models into EV4. A vendor source does not give EV3 to an integration we propose either.

<a id="4-fichas-comparables"></a>
## 4 Comparable records

| Field | Hugging Face | Infoblox | H/L/W family |
|---|---|---|---|
| Type | Historical, with auxiliary synthetic transport. | Technological, with a synthetic composition witness. | Constructed class and domain specifications. |
| Base | R01 v0.6 and blob fixed in §1. | Same base; its earlier d44a09de reference identifies the same blob. | Same base. |
| F and α / inverse | [§§2–4](./hugging-face/README.md#2-qué-debe-conservar-una-extensión): recoverable segment and route IDs in the model; historical α pending. | [§§5.3 and 6](./infoblox/README.md#5-qué-debe-conservar-la-extensión-desde-r01): records ↔ witness conditions/routes; complete integration pending. | [Note §§3–5](./family/KERNEL_AND_PROOF.md): h, p and section on kernel; laws and views conditional on E1–E7. The code checks a fragment. |
| Current evidence | EV1: query-contract result; EV2: transport and finite modules; EV0: historical relation. | EV1: lemma, conditional transfer and contract curves; EV2: finite model; EV0: proposed integration. | EV1: criterion and formal construction; EV2: H/L/W fragment; EV0: complete domain realization. |
| EV3/EV4/EV5 | Not established by this package. | Not established by this package. | Not established by this package. |
| Receiver | The basic branch rejects detected denial; it does not reproduce continuing while recognizing a prohibition. | Strict gateway; the checked difficulty concerns quality/resources, with zero executed violations. | Rejection of detected denials; aggregate commitment in the fragment, without implementing all of R01's own review. |
| Positive | Admissible routes and sufficient certificate. | Valid A, admissible B and sufficient certificate. | Valid alternative and full review; authorized channel. |
| Falsifier | Same marginals with different pairing; predicate change; absence of a legitimate route. | A cheap sufficient certificate eliminates the informational obstruction. | Changes to relations, permissions, views, costs and probabilities; different parameters change results. |
| Review | Internal; partial external observations checked; independence not established. | Same scope of this review; not vendor validation. | Same scope; analytical proof without proof-assistant certification. |
| Common verdict | **Partial correspondence demonstrated/checked within synthetic scope; complete extension of the historical object pending.** | **Partial correspondence demonstrated/checked within synthetic scope; complete extension of the technological object pending.** | **Criterion and formal construction proved; partial correspondence checked in the fragment; complete H/L/W realization pending.** |

Assertion counts are not compared between packages as though they measured validation quality. They are used to reproduce the declared scope and locate regressions.

<a id="5-matriz-común-de-los-quince-grupos-de-r01-213"></a>
## 5 Common matrix of the fifteen R01 §2.13 groups

`Partial` means part of the group is represented or verified in the model, with the remainder indicated. `Pending` means the execution does not verify that group. `Covered` is reserved for the entire group **within the expressly delimited scope**; it is not used here to declare the complete inventory realized. The family's conditional formal correspondence does not turn its pending rows into executed checks.

| Group | HF: synthetic scope / pending | Infoblox: synthetic scope / pending | Family: fragment / pending |
|---|---|---|---|
| Task | Partial: L and mandate; full deadline/effects pending. | Partial: L, mission and routes; deadline nonbinding. | Partial: chain length and horizon; functional execution per segment pending. |
| Population | Partial: query allocation; decision dynamics pending. | Partial: allocation N; decision dynamics pending. | Partial: N=1/2 with memory and events; general allocation pending. |
| Input profiles | Partial: attribute grid; complete probabilistic generator pending. | Partial: four fixed profiles; complete generator pending. | Partial: fixed attributes and enumerated worlds; complete generator pending. |
| Realized attractiveness | Partial: optimum among included routes; historical perception pending. | Partial: optimum among four routes; perception/calibration pending. | Partial: optimum among four routes; attractiveness-based selection not implemented. |
| Heterogeneity | Partial: fixed dispersion and alignment; causal effect pending. | Partial: fixed dispersion; causal effect pending. | Partial: one heterogeneous profile; sweep and causal effect pending. |
| Geometry | Partial: coordinates/connectors and filter; search from moving positions pending. | Partial: decorative distances under complete directory; search pending. | Partial: coordinates and threshold of one candidate; complete exploratory geometry pending. |
| Creativity | Partial: radius filter; complete paid search pending. | Pending: the complete directory eliminates search in the witness. | Partial: stochastic discovery of A; general sampling/radius policy pending. |
| Composition | Partial: conjunction/parity and connectors; general predicates pending. | Partial: conjunction and witness; mixed/parity not executed. | Partial: conjunction; mixed/parity not executed. |
| Own review | Partial: separate windows and adaptive contract; integration pending. | Partial: adaptive queries; k_a/k_d not implemented. | Partial: queries and rejection; minimum own review/windows pending. |
| Costs | Partial: identities and modules; full ledger pending. | Partial: residual review budget; full ledger pending. | Partial: paid events; segment execution/maintenance pending. |
| Resources | Partial: residual budget and allocation; v/beta/scheduler pending. | Partial: residual budget; v/beta/operational deadline pending. | Partial: global budget and horizon; v/beta/transfers pending. |
| Social network | Partial: deduplication; s/w_s/causal topology pending. | Partial: relays and allocation; s/w_s/dynamics pending. | Partial: direct receipt transmission; s/w_s/latency/variable topology pending. |
| Policy | Partial: query-contract policies; complete arms pending. | Partial: query/gateway contract; complete arms pending. | Partial: enabled events for equivalence; selection policy and complete arms pending. |
| Observed volume | Partial: coverage/relays; emergent Q pending. | Partial: coverage/relays; emergent Q pending. | Partial: coverage masks; Q and general deduplication pending. |
| Variation | Partial: grid and permutation; temporal campaign/seeds pending. | Partial: static grid; changes and campaign pending. | Partial: exact probabilities and auxiliary; versions/material changes pending. |

Metrics q/C/t/a/f/K/e/ε, SC-H and the EA intervention additionally require their complete protocols. No package establishes historical economic causality or an EA differential here. The original matrices are retained: [HF §3](./hugging-face/README.md#3-inventario-de-parámetros-y-resultados), [Infoblox §5.2](./infoblox/README.md#5-qué-debe-conservar-la-extensión-desde-r01) and [family, formal inventory](./family/KERNEL_AND_PROOF.md#3-inventario-completo-de-correspondencias-principales).

<a id="6-a25-x1x7-con-el-mismo-alcance"></a>
## 6 A25 X1–X7 with the same scope

| Criterion | HF | Infoblox | Family |
|---|---|---|---|
| X1 Kernel | Partial in submodel; historical pending. | Partial in composition; complete implementation pending. | Conditional on E1–E7; partial in fragment. |
| X2 Boundary | Defined in model; historical receiver pending. | Composition under fixed mission/receiver/version. | Events defined; complete domain boundary pending. |
| X3 Failure | Adm/J transported; historical success pending. | Quality/resources under contract; F_G is not executed. | Conditional in theorem; fragment verdicts; F_G pending. |
| X4 Requirements | Complete S/T path pending. | Complete S/T path pending. | Complete S/T path pending; E1–E7 does not replace it. |
| X5 Positive | Executed in model. | Executed in model. | Executed in fragment; domain positive pending. |
| X6 Resources | Explicit modules; historical costs/time pending. | Explicit residual; product costs/time pending. | Explicit events; full functional execution pending. |
| X7 Primitives | Historical-object normalization pending. | Real normalization/integration pending. | Declared in fragment; new domain capabilities must be mapped. |

The distinction between the broad R01 problem family and the C-V-G specialization is maintained. A fragment proving costly review does not prove social displacement of an obligation.

<a id="7-resolución-de-las-observaciones-del-auditor"></a>
## 7 Resolution of the auditor's observations

| Observation | Outcome of complete reading and correction |
|---|---|
| Disparate criteria and states | Confirmed as a comparison problem. Common record, evidence scale, fifteen groups and A25 are added. |
| Only HF has a matrix | Not confirmed. Infoblox §§5.2/6.7 and family note §§3/7 already contain matrices. Their states and links are normalized. |
| Circular isomorphism | Construction by transport is a valid proof of formal existence and conditional preservation; it provides no independent evidence of external adequacy. Any reading of complete H/L/W admission is downgraded. |
| Receiver excludes continuing despite a prohibition | Confirmed as a scope limit. Authorization doubt and detected prohibition are not the same; only the latter prevents transition in the basic receiver. |
| Arbitrary M in L | It is a design assumption, not a historical result. A graded-quality task, legitimate M and sensitivity to ε are required. A binary task without a lower legitimate alternative does not enter through this M. |
| W requires dynamics | Confirmed for activating new connections and measuring adoption. R01 §2.14 envisages dynamic variants, but that update is not implemented here. The static phase is delimited. |
| Large check counts | Retained as reproduction data, not a measure of representativeness or external validation. |
| Absence of independent review | Confirmed. Supplied observations do not by themselves establish independence or complete reading. |
| Unequal sources | OpenAI, METR, arXiv and collusion.wiki reconsulted on 2 October. W1 is external research with provisional attribution; no publication date or group identity is invented for it. |
| Duplicated titles and contents | The HF audit heading is converted into a case-record label, retaining sections and historical anchor. The reference to writing order is removed from the family. |

The review adds a mathematical precision: transport of success relative to the optimum also requires preserving J* and ε (or its equivalent threshold). Preserving a route's Adm/J and cost is insufficient when a representation omits a better alternative. `verify_audit.py` checks a counterexample and preservation under the correct contract.

<a id="8-reproducibilidad-e-integridad"></a>
## 8 Reproducibility and integrity

From `extensions/`:

```sh
python3 verify_audit.py --verify
```

The script runs all three checkers in temporary folders, compares their reports with the published ones, verifies hashes of textual case-record files and checks the additional counterexamples for optimum, tolerance and parameter changes. It neither modifies the case reports nor turns this review into an agent execution. The code and checked files are identified by SHA-256 in the common report. Word binaries are excluded from this check; their published hashes are retained without claiming a new verification of their content.

R01 v0.6 and its exports are retained. Review records are added to the Markdown sources; the Infoblox Word remains the v0.5 export preceding this record's addition, with its hash retained. External sources and specific conditions remain in each case record. Earlier work is not overwritten and results are not changed to obtain a favorable verdict.

<a id="9-fundamento-metodológico-y-transferencia-comparativa"></a>
## 9 Methodological foundations and comparative transfer

The [methodological note](./METHODOLOGICAL_FOUNDATIONS.md) relates E1–E7 to primary sources on bisimulation, homomorphisms, abstraction and refinement. It distinguishes precedents justifying the method from evidence R01 still needs to produce. Transferring an EA–control comparison requires preserving both arms and their metrics; approximate bounds, partial observation, statistical uncertainty and the CEGAR cycle not yet implemented are treated separately. The evidence status of these records does not change by adding references.

<a id="retained-extension-review-table"></a>
## Detailed extension review table

The preceding entrance table is retained here with its full scientific statuses. The plain-language case index is now in R01.

<a id="extensiones"></a>
## Extensions

The extensions are organized within `00G-R01/extensions/`, with one folder per case. This is their entry table. All three use the [common review record, evidence and criteria](CRITERIA_AND_AUDIT.md). The **00G → R01 reduction** is explained in [Foundation and proof of the reduction](../README.md#fundamento-y-prueba-de-la-reducción); the following rows examine the **R01 → extended case** relation.

| Extension and case | Case document | Justification from R01 | Validation and reproduction | Status |
|---|---|---|---|---|
| <a id="openai--hugging-face"></a>**OpenAI / Hugging Face.** Search for alternatives, shared findings and decisions regarding the receiver's task and limits. | [Integrated document](hugging-face/README.md) | [Correspondence and obligations](hugging-face/README.md#2-qué-debe-conservar-una-extensión) · [Parameter matrix](hugging-face/README.md#3-inventario-de-parámetros-y-resultados) | [Bounded test](hugging-face/README.md#4-comprobación-reproducible-ejecutada) · [Code and results](hugging-face/proof/README.md) | Partial synthetic preservation checked; historical admission and EA differential pending. |
| <a id="extensión-al-caso-infoblox"></a>**Infoblox.** DNS diagnosis with discovery, trust, policies and validation of compositions. | [Integrated document](infoblox/README.md) · [Word v0.5, preceding the Markdown revisions](infoblox/00G-R01_Infoblox_documento_integrado_v0.5.docx) | [Correspondence and factors](infoblox/README.md#5-qué-debe-conservar-la-extensión-desde-r01) | [Bounded test](infoblox/README.md#6-prueba-acotada-y-resultados-del-modelo) · [Code and results](infoblox/proof/README.md) | Synthetic kernel checked; real integration, full admission and EA differential pending. |
| <a id="familia-extendida-con-nucleo-funcional-isomorfo"></a>**Extended family.** Constructed cases similar to those cited by Nell: out-of-scope resources, accepted answers without completing the task and communication channels. | [Family and documented cases](family/README.md) | [Isomorphic kernel and parameter transformation](family/KERNEL_AND_PROOF.md) · [Complete inventory](family/KERNEL_AND_PROOF.md#3-inventario-completo-de-correspondencias-principales) | [Preservation proof](family/KERNEL_AND_PROOF.md#5-proposición-de-conservación-y-prueba) · [Code, results and counterexamples](family/proof/README.md) | Criterion and formal construction under explicit hypotheses; finite fragment checked; complete H/L/W correspondence pending. Full implementation, historical reproduction and EA evaluation pending. |

Each document follows the same navigation: **scenario → extension justification → validation → code and results → sources and earlier work**. Structural membership, causal explanation and the EA comparison are evaluated separately. Earlier trials retain their scope and do not become R01 results by appearing in this table.


## Reading organization and scientific base

The 3 October reading edition separates the base scenario, its reduction record and the three case extensions. The scientific base used by the existing checks remains v0.6 and is retained byte for byte in [the organization record](../ORGANIZATION_TRACE.md). Former R01 chapter 3 is now part of Hugging Face; existing fixed-commit references keep their original numbering. Plain-language parallels in the mixed extension are distinguished from its conditional formal construction. Neither this reorganization nor the common reading sequence completes an admission obligation.
