# R01 gate-policy contract

Working contract v0.1 · 5 October 2026.

The gate policy is frozen separately from candidate behavior, private world truth and oracle implementation. This prevents the evaluator from silently changing success criteria after observing a candidate result.

Current Stage-0 policy:
[`fixtures/stage0/gate_policy.json`](./fixtures/stage0/gate_policy.json)

## Separation

```text
private world / reference truth ─┐
candidate sealed trace ──────────┼─> evaluator
authoritative resource ledger ───┤
frozen gate policy ──────────────┘
```

The gate policy does not determine world truth. The reference methods do not decide acceptance thresholds.

## Current Stage-0 rule

A bounded result can be `PASS` only when all registered conditions relevant to the evaluated mode hold:

- completion;
- legitimate quality within epsilon of the exact bounded optimum;
- economic cost target;
- physical budget;
- deadline;
- no executed violation when execution is actually evidenced.

`INCONCLUSIVE` is preserved when a required reference or authoritative measurement is not established, or reference methods disagree. It is not converted to `FAIL` merely for convenience.

The current batch self-test is conformance-only: it cannot claim a real executed violation. The interactive path may use private environment effect evidence after the candidate trace is sealed.

## Freeze and comparability

The sidecar retains a copy of the numeric acceptance parameters for portability, but semantic admission requires it to match the frozen gate-policy file exactly. A real T03 registration pins the gate-policy hash separately.

Changing epsilon, cost target, physical budget, deadline or the disposition rules creates a different registered experiment; it is not an editorial update to an existing result.
