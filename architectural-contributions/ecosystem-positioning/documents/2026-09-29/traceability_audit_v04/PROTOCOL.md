# Executable traceability audit protocol

Source snapshot: 0ca06f446bb4f037b117c1af525a0ae7ded0900b. Publication base: aaf6b5eb2f1f235e78535fa71d37b9d5146de1ad.

This is an author-side bounded semantic and implementation audit. It does not test commercial products or establish the six-case HC/HS claims. Freeze this protocol before running the new suite. All results, including adverse results, must be retained. No statistical frequency claim is supported by exhaustive artificial state counts.

Expected properties and domains

1. P1: three independent Boolean propositions, partial positive/negative evidence, seven nonempty conjunctive receiving claims. A claim is justified only if every world compatible with the evidence satisfies it. Candidate uses a qualification carrier; evaluator enumerates worlds. Empty or unknown evidence must not support a stronger claim. Mutant promotes any positive evidence into full support.
2. P2: unresolved investigation durations 1 to 4, lengths 1 to 5, total budgets 1 to 8, response durations 1 to 3. Admit only budgets that permit the response itself. Actual observation plus actual response must finish within the budget. Candidate schedules with a reserve; evaluator replays charged events. Mutant ignores response cost. This does not prove H6 frontier improvement.
3. P3: fixed action-specific fixtures distinguish unresolved basis, unrelated unknowns, explicit negative evidence and authorized safe alternatives. Expected dispositions are recorded independently below. A safe alternative must remain possible. No principle predicate is called by the candidate.
4. P4: three-grant chains over three atomic actions; finite scope, revocation and aggregate caps. Candidate uses propagated tokens; evaluator consults original grants at each issuer. Union-of-scope, ignored-revocation and ignored-cap mutants must have counterexamples. Unforgeability, issuer authenticity and real legal authority are outside the model.
5. P5: exhaustively enumerate event words through length seven. Visible domain alphabet Q,C,R,K,A: qualification, visible material change, disposition recording, check, action. Extended domain adds X, an actual unobserved material change. Candidate uses its observed revision; evaluator uses the event history of the actual world and execution outputs only. Test atomic guard, record-as-qualification, cached precheck, no guard, always hold and hidden-change extension. Safety passes require zero stale executions; continuity controls must also allow Q,A and Q,C,Q,A. An all-hold policy must fail the continuity control. Finding an out-of-domain counterexample bounds the claim; do not silently add observability to the original hypothesis.
6. P6: all 1,024 forward DAGs on five nodes, all ten report pairs. Candidate propagates bit provenance; evaluator traverses raw edges to causal roots. Distinct report names and distinct immediate parents must not count as independent evidence when roots overlap. Correlated evidence remains usable with its qualification; independent corroboration is the property tested.
7. H4/HS observation limit: enumerate four contexts with two binary dimensions, observe only one dimension, require opposite actions for the other. Exhibit same-message contexts with incompatible required actions. No deterministic decoder of this message can satisfy safety and continuity in both. Adding the missing observation should separate the contexts. This tests a declared representation, not every possible bounded representation.
8. Replay the earlier certificates unchanged. Inspect predicate overlap and call dependencies. A source-led implication whose conclusion is already contained in its antecedent is a consistency result, not independent empirical confirmation.

P3 frozen fixtures

| ID | Established | Unknown | Required by action | Authorized | Expected |
|---|---|---|---|---|---|
| U1 | stop | route | route | yes | hold |
| U2 | stop | route | stop | yes | act |
| U3 | stop | route | stop | no | hold |
| U4 | route | weather | route | yes | act |
| U5 | none | route | route | yes | hold |
| U6 | route, stop | none | route, stop | yes | act |
| U7 | stop | none | route | yes | hold |
| U8 | route | route | route | yes | hold |

U8 deliberately supplies inconsistent qualification and must fail closed. All eight are authored expectations, not an external validation set.

Acceptance discipline

- Safety and continuity are reported separately. Preserve shortest failing trace and full counts for each named mutant.
- Separate implementation and evaluator modules. The evaluator may not import the candidate or its predicates. The runner passes only inputs and observable outputs to the evaluator.
- Freeze protocol digest before implementation. This is a local audit record, not independent preregistration.
- Report semantic assumptions that both sides necessarily share. Code separation cannot establish independent authorship or external truth.
- Do not claim a direct H-to-P deduction where only motivation exists. Authority requires the separate F-H premise. Six hypothesis effects do not compose into HS without a separate integration argument.
