## Appendix D Executed adversarial traceability audit

29 September 2026. Audit update 0.4. This appendix adds new executions and a stricter assessment of the earlier evidence. The preceding draft 0.3 text, including Appendix C, is preserved. Where an earlier passage describes the audit as limited to a certificate replay, this appendix supplies the expanded status. The canonical hypotheses, principles and sufficiency interpretation are unchanged.

### D1 Assessment and scope

The new work strengthens the executable support for selected principle implementations and identifies failures outside their declared conditions. It does not establish that H1–H6 logically entail P1–P6, that the common cause has been reproduced in all six canonical families, or that the full communication thesis has achieved end-to-end sufficiency. Those distinctions determine which conclusion each test may support.

The most consequential result concerns P5. An action-time revision guard prevents stale execution in all 97,655 event words of length one through seven in the visible-change model. The same guard permits stale execution in 18,420 of 335,922 words when an actual unobserved context-change event is admitted. A separate cached-check policy fails in 1,965 of the visible-domain words. The findings make observability and enforcement at the actual execution boundary explicit conditions of this candidate mechanism.

The numbers describe exhaustive artificial model assignments or event words. They are not incident rates, independent operational samples, confidence estimates or evidence of performance in an industry. Several variants reuse the same inputs; their counts must not be added into a headline number of independent tests.

### D2 Audit design and circularity controls

The protocol was written and hashed locally before the new candidate code was implemented. It declares finite input domains, expected invariants, deliberately broken variants and adverse results that must be retained. This is a local design record, not external preregistration. The work remains an author-side audit with no independent reviewer.

Candidate mechanisms and evaluators are separate modules. The evaluator imports no candidate function or principle predicate. P1 compares a compact evidence carrier against enumeration of compatible worlds. P2 compares a scheduler against replay of charged events. P4 compares propagated permissions against original issuer records. P5 compares the candidate's observed revision against the actual event history. P6 compares propagated provenance against backward traversal of raw source edges. P3 uses eight expectations fixed in the protocol, including a safe alternative and inconsistent qualification.

This separation reduces implementation coupling. It cannot remove the semantic assumptions shared by the author of both sides. P1 and P4, for example, still implement intentionally corresponding notions of support and delegated scope. Their agreement is bounded consistency evidence, not empirical confirmation of those notions. Independent domain review is still required to establish that the encoded facts and outcomes faithfully represent each canonical case.

Mutation controls deliberately promote narrow evidence, spend the response reserve, turn unknown into permission, block every unknown, expand delegated scope, ignore revocation, discard aggregate limits, reuse a cached check and count correlated reports as independent. Every named broken variant has a retained counterexample. The P5 evaluator itself is checked against six fixed positive and negative histories; an always-safe evaluator fails four controls and an always-unsafe evaluator fails two. An always-hold candidate passes safety but fails legitimate-action continuity.

Self-review also removed a defective draft metric that compared a full-observation action label to itself. Its replacement counts observation cells containing incompatible required actions. That result is explicitly classified as a property of the representation, not proof of successful communication. The original protocol and the adverse findings remain visible.

### D3 Review of the previous formal evidence

The four preserved A23 model and certificate files were verified byte-for-byte against their Git blobs at the source snapshot. Earlier local copies contained one additional trailing newline; exact source bytes were restored before the final replay. The semantic certificate reproduces exactly after JSON normalization.

The new reduction audit derives each predicate's relevant fields from its syntax rather than trusting the certificate's field list. It accepts only pure Boolean expressions over state attributes. The derived field sets match all six published projections, and exhaustive enumeration reproduces their state, conformance and violation counts. This closes the specific field-list verification gap noted in Appendix C for these functions. It does not establish that the model includes every material real-world variable.

P1, P2 and P4 use target facts already expressed in their requirement bundles. Their zero-counterexample implications are valid results in that representation. They must be presented as logical consistency and conservation checks, not independent evidence that the corresponding empirical hypotheses are true. P3, P5 and P6 retain respectively three, three and one violating projected states. The new operational refinements neither change those original predicates nor close their full canonical interpretation.

### D4 Executed checks for the six principle links

| Check | Declared domain per variant | Qualified candidate discrepancies | Broken variant discrepancies |
| --- | --- | --- | --- |
| P1 proposition support | 189 evidence and receiving-claim combinations | 0 | Any positive evidence promoted to full support: 96 |
| P2 response capacity | 28,644 investigation, budget and response combinations | 0 | Response cost ignored: 17,566 |
| P3 unresolved disposition | 8 fixed action-specific fixtures | 0 | Unknown becomes permission: 3; all unknown blocks: 2; conflicting unknown ignored: 1 |
| P4 delegated authority | 86,016 grant-chain, revocation, cap and action combinations | 0 | Union of scopes: 6,102; revocation ignored: 4,375; aggregate cap ignored: 26 |
| P6 source dependence | 1,024 directed acyclic graphs and 10 report pairs per graph | 0 across 10,240 pairs | Distinct names treated as independence: 7,470; immediate parents only: 5,214 |

P1 uses three independent Boolean propositions and positive, negative or unknown evidence. The evaluator asks whether every world consistent with that evidence supports the receiving conjunction. This supports the narrow H2-to-P1 scope-preservation obligation. It does not measure confidence calibration or prove the whole P1 treatment of open residual.

P2 uses observation durations from one to four, sequences of one to five observations, budgets from one to eight and response durations from one to three. Only budgets permitting the response itself are admitted. Reserving time prevents the response from exceeding the total budget. The result supports the finite-capacity implementation obligation associated with H1/H6 and P2. It does not compare adaptive versus fixed windows on a risk/resource frontier.

P3 includes unresolved route safety, an independently established stop action, unrelated unknown weather, missing authority and inconsistent qualification. The qualified policy permits the safe authorized alternative and preserves unresolved status for the original action. These are eight authored semantic fixtures, not exhaustive coverage of the canonical scenario families.

P4 covers three-grant chains over three atomic actions, all scope combinations, all revocation patterns, nonempty requested action sets and uniform aggregate caps of one, two or three. Three additional controls place the tighter cap at different positions in a heterogeneous chain. This tests scope preservation and a bounded aggregate mandate. Authentic issuers, tamper resistance, mandate interpretation, temporal revocation races and preservation of wider findings remain outside the model. The externally governed F-H authority premise is still required; H2/H4 do not supply it.

P6 covers all forward-edge DAGs on five nodes, so every such acyclic shape is included under a topological numbering. The candidate propagates root provenance; the evaluator independently traverses edges backwards. A shared root prevents a claim of independent corroboration. Correlated records remain usable with their qualification. Semantic source errors, unknown graph edges, cycles, confidence calibration and mission displacement are not tested.

### D5 Temporal enforcement and counterexamples

Q denotes qualification, C a visible material change, R disposition recording, K a pre-execution check, A attempted action and X an actual unobserved material change. In the visible domain there are 97,655 words of lengths one through seven over Q/C/R/K/A. Adding X creates 335,922 words. Results count words containing at least one bad execution, not the number of bad actions.

| Candidate or challenge | Words evaluated | Words with stale or unqualified execution | Words permitting some execution |
| --- | --- | --- | --- |
| Revision guard at action time with visible changes | 97,655 | 0 | 30,846 |
| Recording treated as qualification | 97,655 | 17,847 | 46,704 |
| Cached result of an earlier check | 97,655 | 1,965 | 10,831 |
| No guard | 97,655 | 56,079 | 75,811 |
| Always hold | 97,655 | 0 | 0 |
| Same revision guard with unobserved changes admitted | 335,922 | 18,420 | 85,552 |

The shortest recording counterexample is R,A: a disposition record permits execution without qualification. Q,C,R,A shows the corresponding stale-basis error after a real qualification. The cached-check counterexample is Q,K,C,A: the check passes, the world changes, and the old result still permits execution. The hidden-change counterexample is Q,X,A: the candidate receives no change signal, yet the actual basis has changed. The evaluator sees the actual change independently of the candidate's observed revision.

Positive controls include Q,A and Q,C,Q,A, both permitted by the atomic guard. Q,C,R,A is blocked. The always-hold variant demonstrates why zero failures alone does not establish sufficient response. The cached-check variant also blocks Q,A until its separate K step occurs, so its availability is not treated as equivalent to the atomic policy.

The model assumes a single decision, serialized events, fixed valid authority and successful qualification when Q occurs. It does not model the adequacy of evidence, a complete communication protocol, costs, human response or simultaneous hardware execution. The cached trace exposes a check/use race by explicit interleaving; it is not an exhaustive concurrent-system verification. The new visible-domain result is larger than Appendix C's 5,460-word model and uses a separate evaluator, but neither bounded enumeration proves arbitrary trace lengths.

### D6 A concrete limit on the minimum context map

The observation test contains four possible contexts with two binary dimensions. The transmitted map distinguishes only the first dimension, while the required action depends on the second. Each of the two observable message classes therefore contains contexts requiring incompatible actions. All four deterministic decoders of the message are wrong in two of the four contexts. If the missing dimension is included, the four observation classes each have a single required action.

This supplies a finite impossibility witness for the insufficient map. A decoder cannot recover a distinction absent from every accessible input. Permitting abstention can preserve safety, but it cannot satisfy a requirement to complete the legitimate action in both indistinguishable contexts. The result limits a declared carrier; it does not refute H4's existence claim about some other bounded carrier. The broader theorem depends on the explicit assumption that no other distinguishing signal arrives before the decision deadline.

Together with Q,X,A, this gives the thesis a precise coverage obligation: identify which material changes the selected map and observation channels can distinguish in time. Agreement between transmitted positions is insufficient when both positions omit the decisive condition.

### D7 Traceability records and the status of each hypothesis

The following records connect source premises to tested obligations. Their labels distinguish semantic derivation from research support. The authoritative H1–H6 wording remains in Appendix A. Short descriptions below do not replace it.

| Record | Upstream and hypothesis connection | Principle and requirement route | What the execution supports |
| --- | --- | --- | --- |
| L1 | F-A/F-B/F-D; H1/H2 | P1; S14 and qualified residual | Receiving-proposition preservation in the finite evidence model |
| L2 | F-C; H1/H6 | P2; S3/S4/T4 | A response reserve within the declared total budget |
| L3 | F-B; H1 | P3; S5 with S14 | Action-specific unresolved status and legitimate alternative response |
| L4 | F-D/F-G/F-H; H2/H4 mediated | P4; S1/S6/S8 | Externally defined grants remain bounded under token propagation |
| L5 | F-E; H5/H6 | P5; S10/T2/T4/S14 | Action-time currentness for observed serialized changes; explicit failure outside that domain |
| L6 | F-F/F-G; H2/H3 | P6; S9/S11 | Source-dependence preservation for the declared DAGs |
| L7 | Bounded representation; H4 | Cross-cutting carrier feasibility | Impossibility for a map that merges incompatible decision contexts |

H4 supports the carrier across the architecture; listing it in L4 does not make it exclusive to authority. Likewise, the six records are not a one-to-one assignment between six hypotheses, principles and case families. The source meanings and added objectives determine the links.

H1 still requires a matched comparison of explicit unresolved disposition against forced closure on independently defined deadlock and false-certainty outcomes. H2 requires a comparison of conditional and unqualified confidence against receiving-decision truth. H3 requires matched loss/compression and preservation or independent-source arms. The new P1/P3/P6 checks isolate mechanisms relevant to these predictions but do not estimate their effects.

H4 requires an implemented bounded envelope whose retained distinctions suffice over a declared admissible context domain and communication budget. H5 requires varying independently imposed churn and validity under a fixed observation/verification budget. H6 requires adaptive and fixed-window policies compared with the full risk/resource ledger. The new observation-limit, P5 and P2 checks respectively constrain these designs; they do not establish those three empirical claims.

For each empirical comparison, freeze the domain, comparator, effect criterion and uncertainty rule before collecting outcomes. No numeric threshold is invented here to make the present deterministic fixtures count as successful empirical trials.

### D8 Remaining causal and integration obligations

The common causal hypothesis HC retains its quantifier: for every admitted failure family, an admissible changed-context configuration exists that reproduces the independently defined failure through the proposed pathway. A constant-context failure is compatible. A failed candidate is not a refutation of an unbounded existence claim.

No new all-six causal campaign was executed in this audit. The P5 trace is relevant to 00I but has not been admitted against all its canonical case gates. The P6 graph test does not execute 00G mission displacement. The P4 chain test does not establish both required 00H outcomes, especially preservation of the wider finding. P1 and P2 likewise do not execute the full rights-portability or synthesis cases. The accompanying TRACEABILITY.md contains all six family records and their outstanding admission obligations.

The next causal campaign must pair changed and unchanged reference context with information alone, a carried map without enforcement, and a carried map with active comparison and authorized response. Preserve the same receiving decision and independently scored business outcome. Record the loss, change and reuse events separately, and intervene on the proposed pathway to distinguish causation from co-occurrence. Admit a strong conventional peer on equal information and resource terms.

HS requires a composed implementation that simultaneously preserves the qualified signal, detects covered changes, obtains legitimate authority, completes response in time and permits justified activity. Separate component passes do not imply this composition. No pipeline with those complete responsibilities was implemented here; its declared domain and business outcome oracle remain necessary work. The deliberately weakened variants and boundary challenges in this audit diagnose specific obligations, not universal necessity of the named architecture.

### D9 Reproduction and publication record

The evidence package contains the locally frozen protocol, candidate and evaluator modules, the exhaustive runner, the prior-model replay and reduction review, machine-readable results, exact-source hashes and the detailed traceability register. The preserved prior model is included so the run requires only Python 3.10 or later and its standard library. From the package directory run `python3 run_audit.py`, then `python3 replay_and_review.py`. Both commands return nonzero if a declared acceptance assertion fails.

The source snapshot is 0ca06f446bb4f037b117c1af525a0ae7ded0900b. The preceding document was published at aaf6b5eb2f1f235e78535fa71d37b9d5146de1ad. Existing scientific sources are preserved. This audit supplies additional evidence and a more precise interpretation of its strength.

[Executable evidence and traceability register](https://github.com/dakleyer/structural-awareness-contributions/tree/main/architectural-contributions/ecosystem-positioning/documents/2026-09-29/traceability_audit_v04)

The supported conclusion is that the selected operational links now have separately implemented, mutation-sensitive checks and explicit counterexamples. Their source-to-model interpretation remains reviewable, and the common causal and full response claims retain their independent test obligations.
