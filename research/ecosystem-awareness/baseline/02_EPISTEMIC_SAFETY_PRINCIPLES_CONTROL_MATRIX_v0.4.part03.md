r many parts of a problem while each worker still emits a locally collapsed closure. Large coverage is not equivalent to ecosystem determination.

&nbsp;

## E0-I — received in-window Type 0 qualification

&nbsp;

Most orchestration patterns can receive another agent’s failure or indeterminate result, but they do not necessarily distinguish whether that signal represents a structural determination limit or simply incomplete effort. A receiver that silently relabels the source’s condition changes the epistemic meaning of the signal.

&nbsp;

## E1-I — received in-window Type 1 qualification

&nbsp;

Human handoff, retry, evaluator and recursive-agent patterns often propagate unresolved work states. The missing control is frequently whether the receiver knows that the source is in a bounded determination process or an open-ended HOLD/search condition. Propagating the latter as a stable fact can spread Type 1 through the ecosystem.

&nbsp;

## E2-I — received in-window Type 2 qualification

&nbsp;

Multi-agent messaging, summaries, voting, debate and layered aggregation are exposed here. If a source transmits PASS, NORMAL, a confidence number or a recommendation without the uncertainty needed to interpret it, the receiver can inherit Type 2 even while faithfully processing the message it received.

&nbsp;

## E0-O — received out-of-window Type 0 qualification

&nbsp;

A source may report uncertainty only over what it actually observed. Unless the source also qualifies the limits of its observation window, the receiver does not know how much of the reported uncertainty refers to in-window state and how much says anything about structural residual. “My uncertainty is 0.3” is not an ecosystem-level statement unless its scope justifies that interpretation.

&nbsp;

## E1-O — received out-of-window Type 1 qualification

&nbsp;

Discovery and research agents can emit open-ended concerns, candidate unknowns or requests for further search. The receiver must distinguish a bounded missing-context signal from an architecture whose own exploration is unbounded. Otherwise search expansion propagates across agents.

&nbsp;

## E2-O — received out-of-window Type 2 qualification

&nbsp;

This is one of the central ecosystem composition risks. A source-specific conclusion can become ecosystem truth when the receiver does not preserve the source’s window, coverage, exclusions or dependency context. Authentication, successful task completion or consensus do not by themselves repair this epistemic collapse.

&nbsp;

# Architectural gravity of common agentic patterns

&nbsp;

Orchestrator-worker / sectioning architectures gravitate toward Pole C by increasing coverage and decomposing the world into many bounded tasks. Their characteristic composition risk is O2/E2-O when local closures are aggregated without preserving scope and uncertainty. More workers can increase breadth without creating second opinions about the same proposition.

&nbsp;

Voting, debate and ensemble architectures attempt same-scope corroboration and can be valuable against individual error. Their composition risk is correlated Type 2: agreement is not independent evidence when agents share models, data, prompts, upstream sources or influence each other’s reasoning.

&nbsp;

Human-in-the-loop and approval architectures gravitate from Pole B toward Pole A by adding human determination capacity. They are strong controls when the human receives a sufficiently qualified state and escalation is bounded. They do not correct an upstream Type 2 world model merely because a human approves a decision presented inside that world model.

&nbsp;

RAG, tool-use, search and research-agent architectures gravitate from Pole C toward Pole A by bringing potentially knowable state into the window. They are powerful window-expansion mechanisms, but require O1 stopping rules and O2 scope qualification. Retrieved context remains a selected window, not the ecosystem.

&nbsp;

Evaluator, critic and self-reflection architectures gravitate from Pole B toward Pole A by attempting to resolve known weaknesses against explicit criteria. They can improve local correctness while leaving upstream coverage errors untouched if the evaluator operates on the same collapsed representation.

&nbsp;

Guardrail and policy architectures principally constrain action rather than epistemic state. They can reduce the consequences of a wrong world model without correcting that model. Good action safety therefore does not imply good Ecosystem Awareness.

&nbsp;

Brainstorming, planning and alternative-generation architectures deliberately emphasize Pole C. Their value is exploration. Their failure mode appears when generated possibilities are promoted to facts, commitments or strategic options without a subsequent determination step that actually brings them into a qualified window.

&nbsp;

Conservative safety, risk-aversion and residual-awareness architectures emphasize Pole D. They are useful when structural residual matters, but can produce O1/Type 1 if “we can never know everything” becomes a permanent veto rather than an acknowledged residual under bounded closure.

&nbsp;

Layered aggregation and mixture-style architectures are composition-sensitive across all twelve surfaces. Each layer can improve performance while also making an upstream epistemic collapse harder to reconstruct if the next layer receives only compressed conclusions.

&nbsp;

# General Law of Epistemic Composition

&nbsp;

For every material decision domain d, the epistemic state E(d) \= \[A\_d, B\_d, C\_d, D\_d\] is scope-bound. Epistemic states, controls and corrections are non-fungible across domains.

&nbsp;

General law:

&nbsp;

An ecosystem composition is epistemically valid only if it preserves the epistemic category and scope of each material input, and any claimed compensation or correction acts on the same domain or on a materially coupled dependency whose relationship to that domain is explicitly established.

&nbsp;

Equivalently, a control applied in domain d2 does not cancel an epistemic error in domain d1 merely because both contribute to the same final decision.

&nbsp;

Type2(d1) \+ Type1-control(d2) \!= balanced(d1,d2)

&nbsp;

Type2(d1) \+ exploration(d3) \!= corrected(d1)

&nbsp;

Type2(d1) \+ human-approval(d4) \!= validated(d1)

&nbsp;

A cross-domain control can reduce risk in d1 only when it directly requalifies d1 or a material dependency through which d1 is being inferred.

Dependency hypothesis and coupling test. The decision-relevant ecosystem is treated as open and potentially interdependent: absence of a represented dependency is not evidence of independence, and no finite dependency boundary is presumed complete. For a specific composition decision, however, compensation is allowed only when the relevant coupling is sufficiently represented to support the claimed requalification. Unknown coupling remains unknown; it neither justifies compensation nor justifies independence.

&nbsp;

A relation between domains d1 and d2 is sufficient for cross-domain requalification only if the architecture can identify a represented dependency path and state how a change in the epistemic state of d2 would alter the determination or qualification in d1. The evidential basis must be available before compensation is applied, or a newly discovered coupling must trigger explicit requalification of the earlier composition. Where coupling is not established, the composition operator preserves the scopes separately and carries the coupling as UNKNOWN where material.

&nbsp;

&nbsp;

The composition operator must therefore preserve a scope-indexed epistemic map rather than collapse participating agents into a single average confidence, uncertainty score, vote count or generic “reviewed” status.

&nbsp;

This law has six immediate consequences:

&nbsp;

1\. Coverage is not corroboration. Many agents exploring different scopes do not constitute multiple independent views of the same proposition.

&nbsp;

2\. Consensus is not determination. Agreement can be correlated, inherited or produced through mutual influence.

&nbsp;

3\. Human approval is not retroactive epistemic validation. A human can only validate what the presented representation allows the human to inspect and challenge.

&nbsp;

4\. Cross-domain caution does not compensate for cross-domain overconfidence. A conservative subsystem in one area does not neutralize false certainty elsewhere.

&nbsp;

5\. More compute does not imply a more balanced epistemic state. Compute can amplify, refine and justify an already misclassified or scope-collapsed world model.

&nbsp;

6\. Acquisition-pathway diversity is not automatically evidence diversity. Two different transports, providers or signalling routes may carry the same upstream evidence. Pathway identity and evidence lineage therefore remain separate composition variables; apparent channel diversity cannot compensate a material source-dependence condition.

&nbsp;

This is the composition-level extension of the root principle: know what you know, know what you do not know, remain aware of what could be brought into the window, and preserve the structural residual. The same four-pole discipline must hold separately for each material domain and must survive composition across agents, humans and subsystems.

&nbsp;

# Agentic epistemic decoupling — local functional coherence, global epistemic fragmentation

Human individuals and organizations are not perfectly epistemically coherent. Their stance can vary across domains, time and context. A cautious organization may still act aggressively in one market; an entrepreneurial organization may still be highly conservative in another. Human actors can therefore exhibit scope-specific epistemic positions too.

&nbsp;

Agentic systems add a different architectural risk. A role-specialized agent has no inherent requirement to harmonize its epistemic position with agents operating in other domains unless the architecture explicitly creates that requirement. The agent can remain perfectly coherent with its local objective, local prompt, local tools and local window while the composed organization becomes epistemically fragmented.

&nbsp;

This produces agentic epistemic decoupling:

&nbsp;

Functional coherence at the agent level does not imply epistemic coherence at the ecosystem level.

&nbsp;

An exploration agent may consistently privilege Pole C; a compliance or approval agent may consistently privilege Pole B; an operational agent may privilege Pole A; a risk agent may privilege Pole D. Each agent can be internally consistent and correct according to its assigned function. If their outputs are accepted as inputs by other functions without domain-scoped epistemic requalification, the resulting organization can maintain several incompatible epistemic postures simultaneously without any participant experiencing an internal contradiction.

&nbsp;

This differs from debate or explicit same-scope deliberation. When agents are asked to debate the same proposition, the architecture at least creates a mechanism that can push them toward a common position. In sectioned or functionally separated architectures, agents may respect each other’s outputs as authoritative inputs and never revisit the epistemic stance under which those outputs were produced. There is therefore no endogenous pressure toward cross-domain epistemic coherence unless such pressure is deliberately designed.

&nbsp;

The resulting organization should be described as epistemically fragmented or epistemically decoupled, not as having a single global personality. It can be simultaneously overconfident in one domain, over-escalating in another, speculative in another and structurally risk-averse in another. These positions can remain stable because each local agent is doing exactly what its role requires.

&nbsp;

## Ecosystem Awareness as epistemic re-evaluation

This gives Ecosystem Awareness an additional system-level role: epistemic re-evaluation or requalification across scopes.

&nbsp;

The purpose is not to force all agents into the same epistemic posture. Specialization is useful. The purpose is to determine, for each material domain and at material composition points, whether the four-pole position still reflects what is actually known, unknown, potentially knowable and structurally residual, and whether imported signals have preserved the scope and qualification required for their downstream use.

&nbsp;

Ecosystem Awareness therefore acts as a meta-level control over agentic specialization. It asks whether locally coherent epistemic positions remain valid when combined, whether one domain has inherited another domain’s collapsed certainty, whether a human or agent is reviewing the original uncertainty or only a compressed world model, and whether the organization has accumulated mutually incompatible epistemic postures without recognizing the inconsistency.

&nbsp;

The design implication is important: agentic epistemic incoherence may be stable rather than self-correcting. Without an explicit re-evaluation function, adding more specialized agents, more computation or more local controls can increase functional sophistication while preserving or amplifying cross-domain epistemic fragmentation.

&nbsp;

Risk/capacity implication. Specialization can also fragment observation budgets. One domain may consume excessive search and human attention while another, more ecosystem-sensitive domain operates on a narrow stale frame. Those allocations do not cancel. Ecosystem Awareness must therefore re-evaluate not only epistemic category by domain but whether awareness resources are being spent where ecosystem sensitivity and consequence justify them.

&nbsp;