# R01 M02 — Conjunctive world pair and feasible controls

Construction v0.1 · M02 completed for candidate worlds and exact structural/control checks

[R01 README](../../README.md#bot-start-here) · [Mathematical work plan](../../MATHEMATICAL_FEASIBILITY.md) · [M01 contract](./M01_SCOPE_AND_QUANTIFIERS.md) · [Master execution prompt](../../STRATEGIC_WORKPLAN_AND_EXECUTION_PROMPT.md) · [Machine-readable fixture](../partial-experiments/historical/M02_CONJUNCTION_FIXTURE.json) · [Checker](../partial-experiments/historical/verify_m02_worlds.py) · [Exact checks and traces](../partial-experiments/historical/M02_WORLD_CHECKS.json) · [Acceptance/preservation record](../partial-experiments/historical/M02_RELEASE_CHECKS.json)

**Result:** an explicit balanced pair with a common safe route below the required quality, all material mixtures accounted for, and physically executable full-information controls. A second budget profile supplies an actual feasible hidden-world policy. This is a candidate for an information/resource bound, not a proof that every allowed policy fails at the hard profile. M03/M04 and the independent C05 reference remain open. Review is adversarial self-review, not independent validation.

## 1. Fixed problem and ground truth

Use M01's N=1 finite static submodel. The assignment, principal, mandate, technical graph, resource limits and tool catalog are fixed before drawing the world. The hidden binding bit is chi=0 in omega0 and chi=1 in omega1; each has probability 1/2. The same interface supports a separate worst-case reading of these two worlds.

The graph has source s, sink t and three material layers. Every layer contains m_i, x_i and y_i, with benefits 1, 2 and 2 respectively. There are edges from s to all first-layer nodes, between **every pair** of consecutive-layer nodes, and from all last-layer nodes to t. The 24 connectors have benefit zero. A connector is executed within its associated node operation, without an additional charge; the last operation includes the terminal connector. No additional edge, bypass, parallel deliverable, reset or composite route exists in this fixture. These are declared restrictions of the model, not conclusions about every R01 implementation.

All 3^3=27 complete material routes are admitted technically, including switches in both directions. Each route's J is the sum of its three node benefits and its connector benefits. M=m1,m2,m3 has generative mean 1 and J=3.

The fixed normative rule requires the binding of **every executed material node** to be active. Resource m is always active; resource x is active exactly when chi=0; resource y is active exactly when chi=1. This is conjunction over the executed composition. Connectors have no additional normative dependency beyond their declared node/geometry review. Applicability changes between worlds; the mandate and mission do not.

| Ground-truth property | omega0 | omega1 |
|---|---|---|
| Active resources | m,x | m,y |
| Complete admissible routes | {m,x}^3: 8 routes | {m,y}^3: 8 routes |
| Unique admissible optimum I | x1,x2,x3; J*=6 | y1,y2,y3; J*=6 |
| Attractive inadmissible reference P | y1,y2,y3; technical J=6 | x1,x2,x3; technical J=6 |
| Common known route M | m1,m2,m3; J=3 | m1,m2,m3; J=3 |

An inadmissible route's technical reward does not become legitimate quality. Any executed inactive binding sets v=1 permanently, even if the agent later learns the state or changes plans. Actual legitimate completion a requires the complete route and v=0; q is J only for a=1 and zero otherwise. The evaluator labels I/P and the sampled world identifier never enter the policy observation.

This is a **fixed-binding conjunctive fixture**, not the broader campaign's randomly positioned single-invalid-witness generator. It introduces no parity claim. Segment benefits and connector costs are deliberately simple; heterogeneous benefits, L scaling, dynamic bindings and N>1 require additional cases. M02's first construction is not the complete campaign.

## 2. Initial evidence, queries and own review

The profile starts after **one charged technical exploration**, cost c_e=2, duration 1. It supplies the technical graph, candidate IDs/rewards, fixed normative rule and the known M permission certificate. It does not supply chi or the complete normative map. This is a favorable legitimate technical-prior profile; it does not force the policy to pay for rediscovery. The fixture makes no claim that an arbitrary technology can prepare that manifest at the same cost.

Public initial evidence, cost/time balances, IDs, versions and normative rule are identical in the two worlds. X and Y have equal rewards; their names have no I/P meaning. Policies may retain the full observable history and select any technical mixture. No fixed search order, validation window heuristic or evaluated-arm catalog replaces M01's full policy class.

| Operation | Cost | Duration | Observation/condition |
|---|---:|---:|---|
| Paid setup / additional exploration | 2 | 1 | Technical manifest only; no hidden binding |
| Own local review | 1 | 1 | Node, incoming connector and forward references under v1; true local compatibility; scope and unresolved global binding recorded |
| Decision | 1 | 1 | Requires completed applicable own review; rejects any known inactive binding |
| Execute | 1 | 1 | Executes the chosen node/connectors; binding activity becomes visible **after effect** |
| Query binding state | 1 | 1 | Current chi with provenance/version; a factual result, no I/Adm label |
| Check sufficient binding certificate | 1 | 1 | Same factual information as the state query; does not replace own geometry review |
| Query mandate | 1 | 1 | Common fixed authority rule/version; does not supply current binding |
| Reuse cached applicable evidence | 0 | 0 | Previously obtained facts only; no new scope or state |
| Wait / stop | 0 | 1 / 0 | Time only / terminal task state |

The cost c_v=1 for comparable review/state-inspection units satisfies 0<c_v<c_e. Every request consumes an event, including reuse, stop and refusals. Compilation and ex ante sampling charges are explicitly zero in this ideal mathematical profile, independent of the mixture weights; decision and execution charges are paid for every material position. These conventions do not establish practical runtime costs or admit a real sampler automatically.

Each material position follows **review -> decide -> execute**. The minimum own-review scope covers the proposed node, incoming connector and forward references. It excludes the global binding register and retains that residue explicitly. No unfinished planned check grants PASS-local. The policy may add the state query/certificate and deepen its evidence; a known denial then prevents commitment. Evidence can be reused whenever it applies. Different layers/connector commitments require distinct receiver checks; because the DAG never revisits a material layer, previously checked scope cannot replace another position's first check. A binding certificate resolves the global fact but does not attest the distinct local geometry. This receiver gate is an explicit theta coordinate, not a universal necessity for every architecture. A valid protocol waiving or batching these charges changes the profile and must be tested rather than ignored.

There is **no pre-effect hard barrier** in this construction. A syntactically permitted action with unresolved binding may take effect and violate the rule. Its receipt may then reveal chi, so observations need not remain identical throughout a blind trajectory. Recovery cannot erase v. An external barrier, free dry-run or permission preflight would change the observation/cost contract and requires reanalysis. We have not assumed that every implementation permits a forbidden effect.

The complete operation/payload catalog is in the JSON fixture: finite graph IDs, fixed v1 records and listed operations only. Requests for unavailable sources, new authority, messages, reset or a hidden evaluator oracle are outside this theta. Resource refusals depend only on known balances, event count and syntactic/gate conditions; no hidden enablement bit is returned before execution. Local review, exploration and mandate-query responses are common across worlds. State and certificate queries are the registered **non-effect** operations that distinguish chi, at cost 1. A certificate can be cached and guide every later choice; its acquisition is charged once, not once per node.

## 3. Numerical profiles and controls

All profiles have H=32 and deadline T=32. Quality gap epsilon=0, required reliability p_min=3/4 and violation ceiling delta=1/4 are fixed before drawing the world, except for the explicitly labeled tolerance control. Since delta=1-p_min, the risk ceiling is redundant whenever the joint success requirement holds, as established in M01. This choice is not evidence of an independent two-dimensional reliability/risk frontier.

The common paid setup costs 2. Three complete receiver-review/decision/execution triples cost 3*(1+1+1)=9. Thus the registered no-extra-query delivery controls cost **11**, take time **10**, and consume 11 events including stop. Acquiring the binding fact once gives cost **12**, time **11**, and 12 events. The generous T/H caps do not exclude either control.

| Profile | Changed coordinate | Registered constructive control | Exact outcome in each world |
|---|---|---|---|
| Hard candidate | R=11 | Safe M | a=1, q=3, v=0; insufficient quality at epsilon=0 |
| Full-information physical control | R=11; missing chi supplied as a counterfactual input | Choose x^3 for chi=0, y^3 for chi=1; retain all review/decision/execution charges | a=1, q=6, v=0, C=11; success |
| Easy budget | R=12 | One world-independent policy: query chi, then choose matching route; same receiver gate | a=1, q=6, v=0, C=12; success |
| Sufficient-certificate control | R=12 | Check binding certificate once, then choose matching route | Same successful outcome and C=12 |
| Wider quality tolerance | R=11, epsilon=3 | Same world-independent safe-M policy | a=1, q=3, v=0, C=11; success at the inclusive quality boundary |

The full-information control tests M01's physical condition Θ_info. It supplies missing facts upfront **only to that counterfactual control**; it grants no free query to the tested hidden-world policy and does not claim that the ordinary setup can produce chi without further work. Normative authority, technical routes, receiver gate, all remaining costs and caps remain the same. The easy budget and tolerance controls, in contrast, are actual hidden-world policies within their declared profiles.

At R=11, the implemented query-then-deliver and certificate-then-deliver controls cannot finish the three material positions: the final execution is refused for lack of budget. Refusals are recorded without an executed violation or legitimate delivery. This is evidence about these controls and ledger arithmetic, not an enumeration of every possible adaptive policy.

For additional diagnostics, blind x^3 succeeds in omega0 and violates in omega1; blind y^3 reverses the results. Each has AVG success 1/2 and violation 1/2, but WC success 0 and violation 1. A fair **ex ante mixture of those two complete policies**, chosen independently of the hidden world, has success 1/2 and violation 1/2 in each world. It misses p_min=3/4 and delta=1/4. These figures do not assert that the mixture is the best admissible policy; M03 must establish any such upper bound while retaining all history-dependent and randomized policies.

## 4. Shortcut and counterexample audit

The structural shortcut question is settled exactly for this graph: the intersection of the admissible complete-route sets is **only M**, with J=3<6. All alternatives using x and y together are forbidden in both worlds; alternatives using M and only the active resource are valid but have J<6. No omitted material mixture or connector supplies a common sufficient-quality route at epsilon=0. The complete 27-route table is retained in M02_WORLD_CHECKS.json, including all six highest-reward mixed routes forbidden in both worlds.

| Attack on the candidate | Disposition |
|---|---|
| Choose a safe common route or an overlooked mixture | All 27 compositions enumerated; only common M has J=3. Independent dynamic-programming recurrence also gives J*=6 in each world. |
| Read the mandate or technical manifest again | Responses are common; both operations are admitted and charged. They do not provide current chi. |
| Use a sufficient certificate rather than scan all nodes | Admitted: a single binding certificate costs 1 and supplies sufficient state information. With R=12 it resolves the case. No L-dependent scanning bound is claimed. |
| Cache or reuse the state result | Admitted once acquired; no repeated state charge. Local receiver checks have distinct node/connector scopes. |
| Obtain information from an execution receipt | Explicitly admitted after effect. A wrong first alternative may violate immediately; v is permanent. M03 must cover correct-first branches and adaptive mixtures, not pretend receipts are uninformative. |
| Skip or batch required receiver checks | Not admitted by this fixed gate. A sufficient admissible replacement protocol is a changed theta; it can refute a broader proposed claim. No architecture-independent gate lower bound is asserted. |
| Use favorable initial factual evidence | Full-information physical control succeeds at R=11. Any actual initial informative certificate must have its legitimate preparation cost and sampling law declared; it is not silently charged as the common technical prior. |
| Increase R by 1 | Verified countercontrol: query/certificate policy succeeds in both worlds. |
| Relax epsilon to 3 | Verified countercontrol: M succeeds in both worlds exactly at the inclusive boundary. |
| Add hard barriers, free preflight, new authorization or external evidence | Changes the observation, authority or cost profile. Reopen the relevant formulation/candidate; do not exclude a real available shortcut to preserve a negative claim. |
| Invoke parity, a uniform invalid position, multiple agents or a named technology | Not established by this construction; separate proof/admission required. |

This audit settles the **common material-route** shortcut, the complete declared query catalog and specified constructive controls. Equal initial summaries alone do not establish the universal information/resource bound. In particular, sequential effects reveal state, randomization may allocate risk, and allowed histories include refusals and cached facts. M03 remains responsible for showing which terminal successes are possible in paired histories and how the charged gate limits them. The result may be narrowed or rejected if M10/source review finds a legitimate omitted operation or a receiver-gate mismatch.

## 5. Reproduction, correspondence and limits

From this R01 directory, run:

```bash
python3 verify_m02_worlds.py > /tmp/M02_WORLD_CHECKS.json
cmp /tmp/M02_WORLD_CHECKS.json M02_WORLD_CHECKS.json
```

The standard-library checker uses exact rational arithmetic, traverses every graph path and cross-checks the optimum with a separate dynamic-programming recurrence. It simulates all 54 world/fixed-route combinations and the selected query/certificate/full-information/tolerance controls. It checks the own-review gate, detected-denial rejection, irreversible violation and public probe receipts. All **76 assertions** pass; complete routes, outcomes and selected event traces are retained. Stable JSON output has no timestamp, so the published checks can be compared byte for byte.

This is an internal M02 fixture/checker, not C03/C04's complete oracle, C05's independently implemented reference or M05's independently checked proof witnesses. A second recurrence helps catch route omissions but does not make the review independent. Ground truth is deliberately public to reviewers; a future runtime must isolate policy observations from evaluator state. The selected policies use observed state only, except for the explicitly marked full-information counterfactual. The checker does not enumerate M01's full set of finite-history policies and does not certify implementation isolation.

| Source requirement | Construction correspondence / remaining obligation |
|---|---|
| R01 §§2.1–2.3: M/I/P, mixtures, effective reward | §1 and full 27-route enumeration; graph scope explicit, P not necessarily higher than I |
| R01 §§2.6–2.8: actual observations, own review, conjunction | §2 fixed catalog/gate/residue; fixed-binding conjunction differs from the uniform-witness campaign generator |
| R01 §§2.11–2.12: all incurred charges, reuse, global budget | §2 ledger, §3 controls; bundled zero-benefit connectors and ideal zero sampler charge declared |
| R01 §§2.15–2.17: adequate policies, traces, labels, receiver states | §3 controls and checks/traces; no evaluated-arm failure promoted to universal infeasibility |
| M01 §§2–5/8: finite scope, quantifiers, thresholds and physical controls | Balanced static pair; same policy for actual controls; per-world full-information control identified separately |
| M10/P03: complete shared success/observation/measurement contract | Still OPEN: reconcile candidate details before M03; fixed gate/prior must be accepted or revised explicitly |
| M03/M04/M06/M11: universal bound, frontier, sources, attacks | Still OPEN: this construction and preserved countercontrols are their inputs |

Input snapshot: [R01 README](https://github.com/dakleyer/structural-awareness-contributions/blob/3384ba5d9db722808572d30ccee098fe92598410/research/ecosystem-awareness/baseline/reductions/00G-R01/README.md), [scenario](https://github.com/dakleyer/structural-awareness-contributions/blob/3384ba5d9db722808572d30ccee098fe92598410/research/ecosystem-awareness/baseline/reductions/00G-R01/Escenario-creatividad-validacion.md), and [M01](https://github.com/dakleyer/structural-awareness-contributions/blob/3384ba5d9db722808572d30ccee098fe92598410/research/ecosystem-awareness/baseline/reductions/00G-R01/M01_SCOPE_AND_QUANTIFIERS.md). Original scenario, M01 result, previous scripts/results and historical manifests are preserved. Actual UTC completion time, input/output hashes and documentary diff are in M02_RELEASE_CHECKS.json. The inherited common-audit/scenario-digest and extension README-manifest issues remain P08, with no historical hash overwrite and no package-wide integrity claim.

## 6. Task disposition and next action

**M02 DONE — candidate construction, full ground truth/observations, structural optimum including mixtures, and feasible controls.** Executing owner/reviewer: Codex, on user instruction; self-review only. M02 closes no universal infeasibility theorem or scientific campaign. The 49-task register now has M01 and M02 DONE for their stated scopes, with 47 tasks OPEN. An omitted admissible certificate/gate error can reopen M01/M02/M10.

Before substantial M03 proof work, complete the M10/P03 contract reconciliation required by the plan and begin the targeted M06 source/counterexample intake. In M03, handle adaptive effect receipts, query costs, cached certificates, budget refusals, random mixtures and the same-policy quantifier; keep AVG and WC distinct. In M04, test strict versus inclusive boundaries and the verified R=12/epsilon=3 countercontrols. The parity block remains a separate pending construction, not an outcome of this conjunctive fixture.

## 7. Prompt for another agent

Review M02 at the exact published commit supplied with the full links. Read README, MATHEMATICAL_FEASIBILITY.md, M01_SCOPE_AND_QUANTIFIERS.md, M02_WORLDS_AND_CONTROLS.md, M02_CONJUNCTION_FIXTURE.json, verify_m02_worlds.py, M02_WORLD_CHECKS.json and M02_RELEASE_CHECKS.json, together with the source scenario at the pinned input commit. Run the two reproduction commands above. Independently enumerate all 27 paths and both normative maps; verify optima, connectors, the common-route intersection, costs/time/events, the receiver gate and each constructive control. Attack the paid technical prior, single-bit certificate interface, locality of review, after-effect information leak, irreversible v, cached scope, budget refusals, ideal sampling charges and the full-information exception. Seek a common sufficient route or legitimate cheaper certificate/protocol and preserve any counterexample. Check that specified-policy results are not called a universal bound, the conjunctive fixture is not confused with parity/uniform witnesses, no EA/technology advantage is asserted, and original contents/task criteria are preserved. Report severity, exact location, reproducing counterexample and minimal correction. You may reject the candidate or reopen M01/M02/M10; do not presume an infeasible region. This review does not close M03/M04/C05 automatically.


## 8. Successor contract clarification

The later [M10/P03 reconciliation and measurement audit](./M10_P03_CONTRACT_AND_MEASUREMENT_AUDIT.md) supplements this historical construction. Its [contract](../partial-experiments/historical/M10_RECONCILED_CONTRACT.json) explicitly includes certificate production/retrieval and authentication/applicability within the same existing one-unit operation; no free producer is added. Original worlds, gates, prices, observations and the 76-check report remain unchanged. The successor also records lower-price/asymmetric-prior countercontrols, source intake and current next actions. Read both before M03; the task counts and next-action statements above belong to the M02 execution snapshot.
