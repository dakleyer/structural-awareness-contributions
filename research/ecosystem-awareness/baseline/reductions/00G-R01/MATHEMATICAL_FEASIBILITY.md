# R01 — Mathematical feasibility: retained scope and current route

4 October 2026. The base proof and own repairs are published in [the canonical theorem](./feasibility/R01_CONDITIONED_TRILEMMA_THEOREM.md). Do not restart M12 or repeat M03/M04 as unfinished author deliveries. Remaining independent review and source-clause fidelity belong to M16/M17. [Current queue](./feasibility/WORKPLAN.md) · [Full previous plan](./feasibility/previous-work/QUEUE_SNAPSHOT_2026-10-04.json).

## Purpose and current evidence

Determine whether a declared R01 problem and technology class has configurations where required legitimate quality, reliability, budget and deadline can be met, and configurations where they cannot. Either region may be empty within a chosen domain. Do not assume the answer before proving or measuring it.

The base scenario §§1.2–1.5 distinguishes observed failure of a finite evaluated family from impossibility for every policy in an explicit class. Its §§2.1–2.18 supply route, observation, cost and trace semantics. The [extension proposition](./extensions/family/KERNEL_AND_PROOF.md#5-proposición-de-conservación-y-prueba) preserves outcomes under E1–E7; it does not establish a negative region on its own. The [finite extension checker](./extensions/family/proof/README.md) covers a declared fragment, not the complete R01 campaign.

00M §6.3 provides the elementary information argument: identical available views cannot guarantee different correct answers for two hidden states. The current symbolic lower bounds and frontiers are in the canonical R01 v0.2 theorem; remaining independent coverage and fidelity are tracked by M16/M17. See [00M v0.8](../../00M_ABCD_AND_MATHEMATICAL_PLAUSIBILITY_v0.8_RESEARCH_NOTE.md).

## Claim to formulate before attempting a proof

Let theta identify the world distribution or declared worst-case world class, observations, allowed queries, costs, resources and fixed success thresholds. Let Pi(theta) be the explicitly allowed policy class. Each policy must use only its available history; it cannot be selected using hidden world labels.

Success e=1 retains R01 §1.4: legitimate quality within the fixed optimum tolerance, cost and deadline within limits, and no executed violation. Fix reliability p_min and, if separately required, a violation-probability ceiling delta. Define:

- Feasible region F: configurations where there exists a policy in Pi(theta) meeting all registered requirements.
- Infeasible region U: configurations where every policy in Pi(theta) fails at least one requirement.
- Unresolved region in the evidence map: configurations for which neither claim is established by the available proof or experiment.

The third category concerns our knowledge; it does not change the underlying logical definition. For infinite policy classes, a supremum at a threshold need not be attained: do not replace existence with an attained optimum without proof. If a "size" or fraction of U is reported, first fix the parameter domain and its measure or grid weights. Nonempty, positive measure and frequent under a real-world distribution are different claims.

A proposed theorem may show a nonempty U under a specified parameter inequality. It must not say every configuration is infeasible or every technology has such a region without separately proving those quantifiers. The same technology may be feasible for other problems or resources.

## Proof route to investigate

Start with finite static worlds and the declared observation contract. Construct two worlds with compatible observations but a material difference in admissibility or sufficient-quality choices. Include M, the true admissible optimum I, an attractive inadmissible reference P, and every permitted connector or mixture. Check that a common safe high-quality solution does not already resolve both worlds.

Derive the minimum additional information needed to meet the chosen reliability requirement, accounting for adaptive queries, early stopping, memory, sufficient certificates, prior knowledge and shared evidence. Then bound the charged work or latency required to obtain that information. A positive per-query cost alone proves no useful lower bound. No generic bound for all R01 predicates is asserted here.

Show separately that a legitimate sufficient-quality route physically exists and could be executed with the available execution resources. This isolates an information/validation limitation from a task that is impossible even with full information. Exhibit a feasible control using enough valid information or another declared parameter setting. Lower cost, a sufficient summary or a stronger permitted policy may eliminate the proposed region; preserve those counterexamples.

Conjunctive, parity and mixed predicates need separate arguments. A worst-case indistinguishability construction does not establish average failure under an arbitrary distribution. Randomized-policy and probabilistic-success statements must specify both randomness and quantifier order.

## Deliverables and handoff

Produce a precise proposition with assumptions, a proof or counterexample, paired feasible/infeasible witnesses where established, and a claim-to-R01 correspondence table. The executable checker in the computability workstream should reproduce finite witnesses independently. Enumeration over a finite grid establishes only that grid unless accompanied by a symbolic proof covering a larger domain.

The technology workstream may transfer the result only after checking E1–E7, policy-class coverage and resource normalization for the concrete implementation. Historical Hugging Face causation and EA superiority are separate questions.

<!-- R01_BOT_WORKPLAN_START version="0.4" role="queue-pointer" -->
M16/M17 track remaining review coverage; M13 continues technologies within the extension protocol. See [the sole active queue](./feasibility/WORKPLAN.md). Historical M01–M17 criteria remain in the register and snapshot.
<!-- R01_BOT_WORKPLAN_END -->
