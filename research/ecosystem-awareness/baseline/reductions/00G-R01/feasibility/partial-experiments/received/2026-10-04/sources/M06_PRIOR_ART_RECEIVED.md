# R01 M06 — Prior Art and Counterexamples for the Trilemma Results

Oct 4, 2026 · @Ivan

## 1. Verdict

Lemma 1 is not new: it is the counting bound of group testing, which has the same form as the lemma, and what R01 may add lies in how that bound is used, not in the bound. A search over five families of prior art found the lemma, its expected-cost form and its noisy-probe form already in the group-testing literature, found close relatives but no identical statement for the trilemma itself, and found real counterexample candidates for two of the assumptions. This is a search result, not a proof of novelty or of its absence.

**What is known.**

- **The counting bound.** For group testing the probability of success with T tests is at most 2^T divided by the number of candidate defective sets. That is the same inequality as Lemma 1 with B(s) bits purchasable and b\* bits required. Its proof is the same inverse-image counting argument. The authors call the underlying log-binomial threshold folklore and say the exponential decay below it is new in their 2013 paper.
- **The expected-cost form.** The same paper gives a bound on the expected number of tests of at least log2 of the number of candidate sets minus 2, which answers assumption A6 for expected-cost budgets.
- **The noisy-probe form.** In group testing a noisy test cannot beat the capacity of the equivalent noisy channel, which is the statement that cheaper-but-noisier probes only rescale the cost per bit.
- **Adaptivity.** In group testing, adaptivity gains a constant factor in the number of tests, which is the same shape as invariant 9 of the annex.

**What the search found for the other results.**

- **The trilemma as stated** (three arms, a hard budget, an irreversible violation, a technology interface) has relatives in three families, none identical: costly information acquisition, safe exploration, and runtime policy enforcement for agents.
- **The staleness result** has a clear qualitative literature on time-of-check to time-of-use failures in agents. The first-order refresh estimate was not found and is an elementary union bound.
- **The annex mapping** onto smolagents, LangGraph and the OpenAI SDK was not found elsewhere. It is an empirical contribution still to be measured.

**Two findings that change the work.**

1. **The family F\_L is the dense worst case.** Group testing shows that when only K of N items are hidden defectives, the information needed is about the log of the number of K-subsets, close to K log(N/K), not N. Real binding rules usually forbid few compositions. If the same holds for R01's bindings, the band width scales with K log(N/K), which is Tier 2 for constant K, not Tier 3. A sparse family is needed.
2. **Fusing the check with the use is a documented pattern.** The TOCTOU work for agents proposes tool-fusing, which makes check and use atomic. That is the nearest real counterpart of the Tier 0 stack, and the annex was too quick to say no framework offers it: the pattern exists, and the cost moves to whoever builds the fused tool.

## 2. Search method

The search covered five families, chosen because each is the home of one part of the R01 argument, and it counted a result as a match only when the statement, not just the topic, was the same. It was done through a web search engine on 4 October 2026, and only one source was read in full, so the verdicts are those of a first pass.

| Family | Why it was searched | Queries, in substance |
| --- | --- | --- |
| Group testing and information-theoretic search | The counting argument of Lemma 1 | Lower bounds on the number of tests, adaptive and non-adaptive |
| Costly information acquisition | The cost of information against the commitment to act | Pandora's box, optimal search with inspection costs |
| Safe exploration | Irreversible violations and exploration | Safe exploration in Markov decision processes, ergodicity, constrained MDPs |
| Runtime policy enforcement for agents | The barrier and the verification interface | Privilege control and policy enforcement before tool calls in LLM agents |
| Time-of-check to time-of-use in agents | The staleness result of the annex | Stale authorization and re-validation in LLM agents |

**Match grades.**

| Grade | Meaning |
| --- | --- |
| Same | The statement is the same up to renaming of objects, and the proof technique matches |
| Partial | The setting or the technique matches, and an element of the R01 statement is missing from the source |
| Relative | The source addresses a neighboring problem and gives no statement that implies the R01 one |
| None found | No source in the search addresses it, which is not evidence that none exists |

**Reading depth.** The group-testing paper that states the counting bound was read in full, including its proof. Every other source was read as search-result excerpts, titles or abstracts. The sources are listed in section 7, with the depth of each.

**Not searched.** Metareasoning and the value of computation, Bayesian experimental design, bandits with knapsacks and fixed-budget best-arm identification, constrained partially observable MDPs, communication and query complexity of verification, proof-carrying code and certificate checking, formal runtime verification, and any literature specific to Ecosystem Awareness. Each is a possible home of a closer statement, and section 7 lists them as open.

## 3. Matrix of R01 results against prior art

Of nine results, five are known or follow from known results, one is a partial match, two have only relatives, and one has nothing in the search. Each row names the closest source and what remains different, so a reviewer can check the grade.

| # | R01 result | Closest prior art | Grade | What remains different |
| --- | --- | --- | --- | --- |
| C1 | Lemma 1: legitimate success is at most 2^(B(s) - b\*) | Baldassini, Johnson and Aldridge, Theorem 3.1: success probability is at most 2^T over the number of candidate sets; the log-binomial threshold is called folklore | Same, up to renaming | R01's transcripts include receipts that confirm a guess; success also requires quality above a threshold and no violation. The counting step is the same |
| C2 | Expected-cost version of Lemma 1 | The same paper: expected tests at least log2 of the number of candidates minus 2 | Same | Needs restating for R01's cost model, with violation as an absorbing event |
| C3 | Noisier or cheaper probes only rescale the cost per bit | The same paper and its capacity principle: a noisy group test cannot exceed the capacity of the equivalent channel | Same in spirit | R01 states it as a change of constant lambda\*, not as a capacity |
| C4 | Adaptivity does not change the scaling class | The same paper: adaptivity gains a constant factor in the number of tests | Same in spirit | R01's adaptivity includes receipts, which are informative only after a possible violation |
| C5 | The trilemma: each pair of goals is attainable and the triple is not, with a hard budget and an irreversible violation | Pandora's box (costly inspection before commitment), Moldovan and Abbeel (irreversible failures and exploration), runtime enforcement for agents | Relative | None of the three states a lower bound that couples cost, a permanent violation and delivery. Pandora's box is in expectation, with no violation. Safe exploration has no information price |
| C6 | Tier classification by the growth of the cost of b bits | Information-theoretic consequence of C1 for different alphabets and costs per query | Partial | The classification itself reads as a restatement. Its value is the mapping of real interfaces to tiers |
| C7 | Refresh count of about pL squared over 2r for a cached certificate | TOCTOU in agents: Mind the Gap (benchmark and mitigations), commit-time authorization | Relative | The literature is qualitative or empirical. The first-order estimate is an elementary union bound and was not found |
| C8 | A barrier with rejection leaves a band of width about (1 - alpha) times the execution budget | Adaptive group testing with membership queries | Same as a consequence of C1 | Its use for refused attempts in agent stacks was not found |
| C9 | Annex T mapping of three frameworks onto tiers | Policy-enforcement systems for agents (Progent, AgentSpec, PCAS) are engines, not a mapping of frameworks | None found | An empirical claim, still unmeasured |

**Reading the grades.** Where the grade is Same, R01 should cite the source and state only the adaptation. Where it is Relative or None found, the claim can stand as a candidate contribution, with the limitation that the search was shallow. No row is graded as a refutation: no source in the search contradicts a result.

## 4. Prior-art families

Group testing supplies the counting core, costly search supplies the cost-of-information frame, safe exploration supplies irreversibility, and agent policy enforcement supplies the barrier and the verification engine, but no source combines the four. The table gives what each source establishes and where it stops short for R01.

| Family | Source | What it establishes | Where it stops short for R01 | Read |
| --- | --- | --- | --- | --- |
| Group testing | [The Capacity of Adaptive Group Testing](https://arxiv.org/pdf/1301.7023) (Baldassini, Johnson, Aldridge) | Success probability with T tests is at most 2^T over the number of candidate sets, for adaptive and non-adaptive designs. Expected tests at least log2 of that number minus 2. Capacity of noisy models bounded by the equivalent channel. Adaptivity gains a constant factor | Requires exact recovery of the defective set. R01 needs only b\* of L bits. No cost per test, no irreversible violation, no technology | Full text |
| Group testing, noisy | [Non-adaptive probabilistic group testing with noisy measurements](https://arxiv.org/pdf/1107.4540) | A folklore lower bound of (1 - epsilon) d log(n/d) tests, extended to noisy tests by dividing by one minus the entropy of the noise | Non-adaptive setting; same gaps as above | Excerpt |
| Costly information acquisition | [Pandora's Problem with Nonobligatory Inspection](https://arxiv.org/pdf/1905.01428), on Weitzman's 1979 model | Opening a box costs c\_i and reveals its value. The optimal policy orders boxes by a reservation value and stops when the best found value beats the rest | Expected value, not a hard cap. No violation. The prizes are independent and the question is which to open, not how many bits are needed | Excerpt |
| Safe exploration | [Safe Exploration in Markov Decision Processes](https://arxiv.org/pdf/1205.4810) (Moldovan, Abbeel) | Unrecoverable actions break the ergodicity that exploration guarantees need. Computing the set of guaranteed-safe policies is NP-hard, and an efficient approximation is safe but suboptimal | No price for information, no budget, no technology interface | Abstract |
| Agent policy enforcement | [Progent](https://arxiv.org/pdf/2504.11703) | A deterministic runtime check of every tool call against a policy, with forbid rules ahead of allow rules and a default of blocking | A barrier per call. No lower bound, and no account of how the policy facts are obtained | Excerpt |
| Agent policy enforcement | [PCAS, a policy compiler for agentic systems](https://arxiv.org/pdf/2602.16708) | A reference monitor intercepts actions before execution and evaluates policies over a dependency graph of tool calls, results and messages, deterministically and independent of the model | An engine for route-level checks, not a bound. The policy facts are the organization's | Excerpt |
| Agent policy enforcement | [ActPlane](https://arxiv.org/pdf/2606.25189) | A benchmark that tests enforcement against indirect execution paths, where a side effect moves into a subprocess or an auxiliary artifact. It reports that tool-boundary guardrails are evaluated mostly on direct calls | Empirical. It supports the coverage rule of the annex | Excerpt |
| Authority staleness | [Mind the Gap: TOCTOU in LLM-enabled agents](https://neurips.cc/virtual/2025/129110) | A benchmark of 66 tasks. Mitigations: prompt rewriting, state-integrity monitoring and tool-fusing, which reduced vulnerable trajectories from 12 to 8 percent in combination | Empirical and qualitative. No cost model and no refresh count | Abstract |
| Authority staleness | [Temporary Authority, Permanent Effects](https://www.alphaxiv.org/abs/2607.10487) | Commit-time authorization: a durable effect is authorized only if its licensing witness is fresh, causally prior, bound to the same effect and eligible at commit | A definition and a property, with no quantitative cost of keeping witnesses fresh | Abstract |

**How the counting bound maps.** In group testing the possible defective sets play the role of R01's worlds, the vector of test outcomes plays the role of the paid-answer transcript, and the proof groups the sets by the outcome vector they produce. At most 2^T vectors exist, so at most that fraction of sets can be told apart. In R01 at most 2^B(s) transcripts exist as well, but each transcript's route is legitimate on up to 2^(L - b\*) worlds and not on one, because delivery needs only b\* bits. That refinement is the standard counting step for approximate recovery. The sphere-covering and rate-distortion literature handles it, and it was not searched here. R01 should cite it once it has been read.

**What the enforcement literature changes for the annex.** PCAS and Progent are real instances of the deterministic checking engine in stack S-A of the annex. They show that a route-level or per-call check in code, before the effect, exists as a design. They do not supply the policy facts, so the annex's reading that the interface belongs to the environment stands. ActPlane's finding that enforcement is evaded through indirect paths is the coverage rule in empirical form.

## 5. Counterexample search against A1 to A8

Two assumptions meet strong candidates from the literature, A1 on the cost of information and A5 on independent uniform bits, one meets a partial candidate, A4 on irreversible violations, and one is closed by the group-testing result, A6 on hard caps. None of these refutes Lemma 1. Each changes the technology class or the family, which is how the first document said a counterexample should be read.

| ID | Assumption | Candidate from the search | Effect on the result | Verdict |
| --- | --- | --- | --- | --- |
| A1 | Information costs at least c per bit | Tool-fusing, which makes check and use atomic, proposed in the TOCTOU work for agents. PCAS, which evaluates a policy over the whole dependency graph in one deterministic check | A fused tool folds the check into the effect, which is Tier 0 for the paths it covers, and the cost moves to whoever builds the fused tool and the policy. A route-level check in code is Tier 1 in compute. A per-call check in code, as in Progent, is a per-bit probe in compute | Strong candidate. It changes the interface, and Lemma 1 is intact |
| A2 | The M permission certificate is free and the binding state costs 1 | In Progent and PCAS the permission and the binding are rules in the same policy, read from the same source | No effect on the mathematics. The asymmetry has no support in how real policies are held | Price both, or make both free, in the contract |
| A3 | A receipt reveals only the executed node's status | Not searched. ActPlane shows that side effects can move into subprocesses and auxiliary artifacts, which suggests receipts of one tool can carry or miss more than one node's status | Unknown | Open. Needs the receipt-content test of the annex |
| A4 | A violation is permanent | Commit-time authorization: a protected commit surface that blocks stale durable effects. Progent's fallback actions for a blocked call | If effects are staged and checked at commit, a violation becomes a refusal. That is a barrier at commit, Tier 3' or Tier 0 depending on whether the check and the commit are atomic | Partial candidate. It requires effects that can be staged and discarded |
| A5 | Bindings are independent uniform bits | Group testing with K hidden defectives among N items needs about log2 of the number of K-subsets, close to K log(N/K), not N | If only K of L layers carry a binding, locating them costs about log2 C(L, K) bits and settling their bits costs K, so b\* is of order K log(L/K) by the same counting argument (sketch). The band is then Tier 2 for constant K and Tier 3 only when K grows in proportion to L | Strong candidate. F\_L is the dense worst case, and a sparse family is needed |
| A6 | The budget is a hard cap per run | The same group-testing paper bounds expected tests below by log2 of the candidates minus 2 | The expected-cost reading has the same scaling, up to an additive constant, in the analogous setting | Closed in the analogue. Restate for R01's cost model, with violation as an absorbing event |
| A7 | The gate costs g per layer and is mandatory | Not searched. Progent checks every call, so the check is a per-call cost | A parameter, not a result | Open as a parameter |
| A8 | Efficacy is technical, legitimacy derived | Not a literature question | Definitional | Fixed in the contract |

**The sparse family.** Take F\_{L,K}: L layers, of which only K carry a hidden binding, and in the others both nodes are admissible. To deliver at quality of at least J\* minus epsilon without violating, a policy must find the layers where x is forbidden and the layers where y is forbidden. That is group testing with route-membership queries, so the information needed is about log2 C(L, K) plus K, and the bound of Lemma 1 applies with that b\*. Two consequences follow, both to be proved and neither yet checked.

- With K constant, the infeasible band grows like c log L, which is Tier 2, and its share of the execution budget tends to zero.
- With K proportional to L, the family returns to the Tier 3 of F\_L.

Which regime real bindings are in is an empirical question about how many compositions a real policy forbids. The annex's measurement of cost growth should therefore use both families.

## 6. What this changes in the R01 claims

R01 should stop presenting the counting bound as its own result, keep the setting and the technology mapping as candidate contributions, and add a sparse family before it says anything about how wide the trilemma band is for real bindings. Six edits follow, in order of priority.

| # | Document | Change | Why |
| --- | --- | --- | --- |
| 1 | Trilemma sketches, Lemma 1 | Label it as adapted from the group-testing counting bound (Baldassini, Johnson, Aldridge, Theorem 3.1, and the folklore log-binomial threshold). State the two differences: delivery needs only b\* bits, so each transcript serves up to 2^(L - b\*) worlds, and receipts confirm guesses | Avoids a novelty claim the literature does not support |
| 2 | Trilemma sketches, Lemma 1 | Add the expected-cost corollary, citing the expected-tests bound of the same paper | Closes assumption A6 in the analogue |
| 3 | Trilemma sketches, assumptions register | Raise A5 to a strong candidate, add the sparse family F\_{L,K}, and add the fused tool and the route-level engine as A1 candidates | These are the two places where the search changes the result |
| 4 | Trilemma sketches, tier table | Add a row for sparse bindings: Tier 2 for constant K, Tier 3 for K proportional to L. Add the fused tool as the nearest Tier 0 pattern | The tier is a function of the sparsity regime as well as of the interface |
| 5 | Annex T, sections 7 to 9 and experiment X11 | Replace the statement that no framework offers Tier 0 with the statement that no framework documentation offers it, while tool-fusing is a documented pattern. Add a stack S-F with a fused tool. Add PCAS and Progent as engines for S-A. Run X11 on both F\_L and F\_{L,K} | The annex should reflect the patterns that exist |
| 6 | R01 differential | Claim the setting that couples a hard budget, a permanent violation and a technology interface, the sparse-family analysis, and the measured constants of section 10 of the annex. Do not claim the counting bound | States what is candidate, and what is not |

**What can be claimed now, and what cannot.**

- **Can be claimed as candidate:** the coupling of the three arms in one lower-bound setting, the interface-based classification as a way of reading agent stacks, the staleness refresh estimate as an elementary result, and the empirical mapping of three frameworks.
- **Cannot be claimed:** that the counting bound is new, that Tier 3 describes real bindings, or that no framework pattern reaches Tier 0.

**Searches that would most change this document, in order.** Approximate-recovery and rate-distortion counting bounds, because they hold the partial-credit step of Lemma 1. Bandits with knapsacks and fixed-budget best-arm identification, because they couple a budget with sequential information. Constrained partially observable MDPs, because they couple a risk constraint with partial observation. Proof-carrying code and certificate-checking cost, because they are the home of Tier 1. The literature on runtime verification with monitors that return verdicts for whole traces.

## 7. Limits, review plan and sources

This is a first-pass search through a web search engine, so absence of a source says little, and the most reliable finding is the one read in full: the counting bound. The limits and the review steps below say how far each verdict can be trusted.

**Limits.**

- Only one source, the 2013 group-testing paper, was read in full. Every other source was read as search-result excerpts, an abstract or a title, so claims about them are limited to what those excerpts say.
- The search engine returns what it ranks, not what exists. A source on a subject not searched, such as metareasoning or certificate checking, could hold a closer statement.
- Match grades were assigned by one reviewer, the author of the R01 sketches, which is a conflict of interest.
- Some sources are recent preprints. Their results have not been confirmed by the author of this document, and one was seen only through an aggregator's abstract.
- The sparse family and its bound are a sketch that rests on a group-testing analogy. They are not checked.

**Review plan.**

| Step | Object | Question | Method | Pass criterion |
| --- | --- | --- | --- | --- |
| 1 | C1 to C4 | Does R01's Lemma 1 follow from the group-testing bound with the stated adaptation? | Write the explicit map from worlds, transcripts and routes to defective sets, outcome vectors and decoders, and re-derive both proofs | The map is written and the proofs agree, or the difference is named |
| 2 | C5 | Is there a source that states the trilemma, or a bound that couples budget, violation and delivery? | Search the families listed as not searched, with a second reviewer | A source is found and the grade changes, or the second reviewer confirms none found |
| 3 | A5 and the sparse family | Does the sparse bound hold for the route problem? | Prove the bound for F\_{L,K} or find the counterexample, and check it by exhaustive enumeration for small L and K | The bound is proved and checked, or narrowed |
| 4 | A1 candidates | Do the fused tool and the route-level engine change the tier in measurement? | Stacks S-A and S-F of the annex under experiment X11 | Measured growth of the overhead, per cost dimension |
| 5 | Independent grading | Would another reviewer give the same grades? | Hand the matrix and the sources to a reviewer who did not write the sketches | Disagreements are logged with the evidence |

**Sources, with the depth of reading.**

Read in full: [The Capacity of Adaptive Group Testing](https://arxiv.org/pdf/1301.7023), by Baldassini, Johnson and Aldridge.

Read as search-result excerpts: [Non-adaptive probabilistic group testing with noisy measurements](https://arxiv.org/pdf/1107.4540); [Pandora's Problem with Nonobligatory Inspection](https://arxiv.org/pdf/1905.01428); [Progent: Programmable Privilege Control for LLM Agents](https://arxiv.org/pdf/2504.11703); [Policy Compiler for Secure Agentic Systems](https://arxiv.org/pdf/2602.16708); [ActPlane](https://arxiv.org/pdf/2606.25189).

Read as abstracts: [Safe Exploration in Markov Decision Processes](https://arxiv.org/abs/1205.4810v1); [Mind the Gap: TOCTOU in LLM-Enabled Agents](https://neurips.cc/virtual/2025/129110); [Temporary Authority, Permanent Effects](https://www.alphaxiv.org/abs/2607.10487).

The companion documents are *R01 Viability as a Trilemma: Proof Sketches and Review Plan* and *R01 Annex T: How Concrete Agent Technologies Act on the Trilemma*.
