<a id="comprobación-finita-del-núcleo-de-las-extensiones-hlw"></a>
# Finite check of the H/L/W extension kernel

[Family](../README.md) · [Proposition and proof](../KERNEL_AND_PROOF.md) · [Code](./check.py) · [Results](./results.json)

<a id="qué-se-ha-ejecutado"></a>
## What has been executed

A Python 3 checker, without external dependencies, enumerates states and events of a **finite synthetic fragment**. The three encodings correspond to constructed cases H, L and W: resource permissions, semantic obligations and effect authorization. No network requests are made and no products, LLM agents or Lean are executed.

The general mathematical proof is in the linked note. This code checks witnesses for some of its obligations and counterexamples; it does not replace the pending complete implementation of R01.

<a id="dominio-enumerado"></a>
## Enumerated domain

- Two or three conditions per chain; four chains without cross-connectors. All truth combinations of candidate A's conditions.
- M and B are known admissible routes of different values. A may surpass both if admissible; C has a visible prohibition. I is calculated from admissibility and value, not fixed as a route name.
- N equal to one or two; memory of conditions reviewed by actor, evidence reception and preservation of origin.
- Effective radius 1 or 3; exploration cost 4; review 2 or 1; message, execution and waiting with cost 1; budget and horizon 6. An event consumes one time unit, except voluntary termination.
- Exploration of A with probability 1/2 when within radius; outside the radius it is not discovered. This law is a recorded synthetic assumption, not a historical measurement.
- Review per condition, evidence transmission, commitment, waiting and abstention. Detected prohibitions are rejected. A candidate without an observed prohibition may be executed under the partial-review receiver.
- An auxiliary bit with two representatives per projected state evolves between events, without influencing kernel views or transitions. The theorem covers more variables under the same conditions; the code does not enumerate 50 binary variables.

The fragment starts with known M/B and undiscovered A. Learning the initial recipes is outside the horizon; that initial condition is common to all three encodings and the base. Evidence on A is acquired and paid for during the episode. Transmission uses a fixed authorized channel. In W, that experimental channel is not the resource whose writing or use is being evaluated.

The `commit` event adjudicates a complete route as an aggregate effect with charge 1; it does not execute or charge its L segments separately. `inspect` may query any of its conditions once A is discovered: it does not implement k_a/k_d or require the minimum own review before commitment. The fragment therefore verifies encoding/transition obligations, but is not a fully admitted realization of R01's receiver and execution. These pending items are in the [common matrix](../../CRITERIA_AND_AUDIT.md#5-matriz-común-de-los-quince-grupos-de-r01-213).

<a id="cómo-evita-una-comprobación-circular"></a>
## How it avoids a circular check

`base_step` operates on discovery/review masks and the base world. `domain_step` is implemented separately over domain actors, operations and receipts; it does not call the former or obtain its output to construct its own. Successors are projected and exact probabilities compared using `Fraction`.

The domain evaluator calculates admissibility from permissions/obligations and quality from its operation values. These are compared with the base definition, alongside verification of each material relation and attribute. View equality compares the collection of views per actor, including receipt origin and scope; it does not mean each actor sees the others' private memories.

All events—enabled and disabled—are checked in each reachable fragment state. Diagnostic states with prior review and available budget are added to check review and transmission operations more broadly. Those states are counted separately and are not presented as reachable from the small-budget initial condition.

<a id="resultado-registrado"></a>
## Recorded result

The execution saved in `results.json` passed:

| Check | Count |
|---|---:|
| H/L/W domain structures | 288 |
| Reachable-state round trips | 16 104 |
| Reachable-state / event pairs | 274 572 |
| Diagnostic-state / event pairs | 172 224 |
| Indistinguishable-view pairs with different verdicts and full-review controls | 768 |
| Deliberately invalid mutations rejected | 14 |

The counts refer to checks of a model, not independent experiments or tests with 274 572 agents. Each transition comparison also examines both auxiliary-bit values. The three encodings use the same base construction; their results are not three independent empirical validations.

The mutations cover a non-bijective map, role exchange, omitted connection, false permission, altered benefit, local redistribution preserving the sum, mission change, hidden shortcut, free review, provenance laundering, omission of a denial, altered probability, influence of a hidden variable and oracle leakage.

Two positive counterexamples of regime change are included: increasing radius changes the discovery distribution; reducing review cost allows a previously unaffordable query. **Family membership does not automatically preserve the original configuration's performance.** Full review accepts the positive and rejects the negative of the constructed pair: defense failure is not imposed.

<a id="cobertura-frente-al-inventario-completo"></a>
## Coverage against the complete inventory

| Covered by this fragment | Outside this execution |
|---|---|
| Chain graph, attributes, conjunction, partial views and optimum among four routes | General graphs, other connectors, parity and mixed predicates |
| Probabilistic exploration of one candidate, two radii and two costs | Complete geometric generator, correlations, adaptive radius and search policies |
| Memory, paid queries, transmission and origin | Intensity s, weight w_s, heterogeneous latencies, versioned caches and negotiation |
| Global budget, horizon and rejection of detected denial | Allocation v, beta, transfers and full accounting by category |
| Kernel equivalence with fixed effective parameters | Parameters changing during the episode, new topology and agents ignoring a prohibition |

The complete inventory has a formal correspondence in the mathematical note; groups in the right-hand column are **not** verified by this code. The preservation proof is conditional on E1–E7 for any future implementation incorporating them.

**Common procedure:** from `00G-R01/`, run `python3 extensions/verify_audit.py --verify`. It recalculates the three checks in temporary folders, compares recorded reports and verifies textual hashes. [Criteria and scope](../../CRITERIA_AND_AUDIT.md) · [Common guide from R01](../../../README.md#reproducción-conjunta-de-las-comprobaciones).

<a id="reproducción"></a>
## Reproduction

From this folder:

```bash
python3 check.py --verify
```

The command recalculates the checks and requires exact equality with the recorded report, including the code's SHA-256 hash. To regenerate the report after a deliberate change:

```bash
python3 check.py
```

The report fixes the base specification commit and checker hash. It contains no EA results, historical prevention figures or results from the complete R01 simulator.
