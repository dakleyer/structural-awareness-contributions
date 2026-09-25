# 00K-A5 — P5 / 00I deterministic symbolic ablation

**Removed principle:** P5 — material-change requalification at time of use  
**Scenario:** 00I — *The Patch That Undid the Fix*  
**Status:** deterministic symbolic fixture execution; not a live system or product benchmark

## Question

Can P1/P2/P3/P4/P6 plus strong native controls keep a previously valid queued action correct after the world changes **without** reconstructing P5's invariant: compare/requalify the decision basis at use time when a material condition changes?

## Frozen branch pair

- **Continuity:** incident/config/freeze/source basis remains the same as when Patch A was qualified → must execute.
- **Stale branch:** Patch B / incident resolution / freeze / generation change makes Patch A's old basis stale → must requalify rather than execute.
- **Unavailable-current-source control:** current state cannot be established → bounded HOLD, not silent execution.

The queued Patch A object, original grant and original decision basis are identical on continuity and stale branches. The declared material difference exists in **current state at use time**.

## Tested repairs

- queue-time-only decision;
- stricter original-basis qualification (P1);
- provenance/intervention preservation without applicability reopening (P4);
- conflict visibility without applicability reopening (P6);
- native serialization only;
- deny-all;
- native generation/version compare.

## Result

The suite passes **12/12**.

The first five P5-blind repairs false-continue the stale branch or cannot discriminate it from continuity. Deny-all blocks the stale branch but fails the continuity positive control.

The native generation/version compare passes both stale and continuity branches. Under the 00K classification it is **SEMANTIC RECONSTRUCTION of P5**, because it makes the previously qualified action conditional on action-time current state/version and reopens qualification on mismatch.

No TRUE SUBSTITUTE is established by this fixture execution.

## Re-run

```bash
python -m pytest -q
```

## Boundary

This is a deterministic symbolic execution over a frozen 00I abstraction. It does not prove universal P5 necessity and it does not test AWS, Step Functions, RDS or any other product. A future repair that passes continuity + stale + unavailable-source controls without action-time requalification or an operationally equivalent current-state binding is a valid counterexample.
