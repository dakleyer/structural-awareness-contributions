# Unit-safe economic evidence — implementation reception for #66

This is an implementation supplement for F-05/K-07/OP-06 in [audit #58](https://github.com/dakleyer/structural-awareness-contributions/pull/58), building on #66 at `7c9043e0`. It strengthens the evidential basis for EA's information-economy conclusions by testing **what the source information enables, physical outcomes, and acquisition costs in their own units**.

## Source architecture, preserved

[ACC author notes S1-P0205–P0223](../../model/01_NOTAS_COMPLETAS.md#s1-p0205) and [S1-P0280](../../model/01_NOTAS_COMPLETAS.md#s1-p0280) define open K, nonfungibility and evidence-based extension. [00M v0.8](../../../../00M_ABCD_AND_MATHEMATICAL_PLAUSIBILITY_v0.8_RESEARCH_NOTE.md) owns epistemic A/B/C/D; [00N v0.7](../../../../00N_FROM_MECHANISM_TO_REQUIREMENTS_SCIENTIFIC_PLAUSIBILITY_v0.7_RESEARCH_NOTE.md) owns the information/metadata opportunity. Neither is rewritten here.

| Source notation | Reading in #76 | Distinction to preserve |
| --- | --- | --- |
| E | E | Resource efficiency requires comparable outputs. |
| R, or direct/distributive D in the later example | R | Actor components stay separate; epistemic D is different. |
| C | C | Coordination; no automatic deduction from R. |
| V, or attribution A in the later example | V | Attribution; epistemic A is different. |
| K(n+1) | Evidence-justified additional dimension | Open extension, never a coefficient added for convenience. |

This is a crosswalk of existing source usage, not a decision to rename canonical letters. Returns, investment and complementarity coefficients generate a toy's data; they are not automatically new dimensions. Output and instrument price in this supplement are **measurements**, not a new assignment of economic K dimensions. Rights, capabilities and permission remain separate controls.

## Concrete repair and stronger conclusions

Use [unit_safe_envelope.py](unit_safe_envelope.py) as the review/report entry point. It executes the unchanged source-native engines and accounting, then constructs its report **only** from physical gross output and itemized information prices. Source net, net deltas, legacy winners and legacy scalar metric labels cannot enter the result. Identical numerical unit labels do not authorize dimensional compensation.

The report publishes physical gains against A, the nondominated output/price frontier and exact **equal-realized-output** price comparisons. It does not average objectives across questions or let SOURCE_PUBLIC_RECEIVER compete with the policy it selected.

The original K-01 result is now independently tested without output-minus-price arithmetic: at n=16, 128 and 256, B and directed exploration each realize output **10**. Information prices are respectively **9/4 vs 3**, **3 vs 3**, and **13/4 vs 3**. Thus B's first price advantage and the exact cost crossover remain supported entirely in the cost unit. This is a stronger basis than an assumed conversion of output into money. The frozen sources and their results remain intact.

```sh
python -B unit_safe_envelope.py --corpus-root /path/to/repository --model both
python -B -m unittest test_unit_safe_envelope test_economic_envelope -v
```

## Reviewer obligations and author decisions

1. Reproduce all **168 social regimes** and original agentic fixtures/prices. Reconcile every output, price, status and source reference with the unchanged engines.
2. Change a legacy net/winner arbitrarily: the corrected report must remain identical. Increasing output while increasing price must leave a tradeoff. Equal output permits a price comparison; matching units alone never permits compensation.
3. Verify unknown output or price is UNKNOWN, not zero; malformed/nonfinite values and inconsistent cost ledgers fail. A partial measured frontier is not a decision or a permission.
4. Review #76 as an R/C projection: its **46/92/38/4** and **13/26** counts are retained. The game does not define a participant's choice over all open K. Do not invent that choice rule or change an audit status.
5. **Escalated, unimplemented:** any mapping of physical mission output into R/E, information price or resource overhead into C, any accepted inter-dimensional tradeoff/conversion, and any change to the original source planners. The source planners retain their historical scalar assumptions. This supplement repairs their evidential report; it does not silently redesign their decision policy.
6. An equal-Q synthetic control supplies Q to both arms by construction. Its outcome is not a finding that EA's discovery, qualification or prospective requalification is dispensable. It isolates the information contribution already supplied. The canonical EA conclusions and their research direction are preserved.

Code and checks are AI-assisted implementation, not independent adjudication. No merge, canonical promotion, audit closure, external test result, document-control edit or original experiment change is requested.

