# R01 trace-layer policy

4 October 2026 · Documentary preservation policy

[R01 current entry](./README.md) · [Current work register](./feasibility/WORKPLAN_STATUS.json) · [Version-aware verifier](./extensions/verify_audit_v2.py)

## Purpose

R01 preserves earlier editions for auditability without treating every preserved trace, proof guide or experiment as part of the current research route. Historical evidence is retained; active scientific obligations are governed only by the current README, workplan/status register and the explicitly designated current references.

## One current route, historical layers retained

At any time R01 has one current documentary route. Earlier trace layers remain immutable evidence of what an earlier edition contained and how a later edition was derived. They do not create parallel queues, reactivate superseded experiments or become current merely because a later document links to them for provenance.

A new trace layer is justified only when a material reorganization or preservation boundary must be recorded—for example, splitting a document, relocating a canonical entry, or preserving a prior edition before a structural transformation. Ordinary wording changes, new research notes or routine status updates do not require another preservation layer.

## Successor rule

When a successor trace is necessary:

1. it identifies the exact predecessor edition or commit;
2. it preserves the predecessor bytes or hashes required for the stated recovery claim;
3. it states which assertions are historical and which, if any, describe the current edition;
4. it does not rewrite predecessor hashes to make a current file appear unchanged;
5. it declares whether it supersedes a prior trace for current navigation/integrity purposes; and
6. the root README and version-aware verifier are updated so only one integrity route is presented as current.

Superseded traces remain available as historical records. They are not recursively revalidated as if every old "current file" assertion still described the latest reading edition.

## Current integrity rule

The current gate is `extensions/verify_audit_v2.py --verify`.

It distinguishes:

- substantive checker/result reproduction;
- embedded historical-snapshot integrity;
- a frozen baseline of known documentary drift from historical manifests/traces; and
- any new, unrecorded documentary drift.

Known drift is explicit and finite. A new documentary mismatch outside that baseline is a failure until reviewed and either repaired or deliberately admitted by an explicit update to the baseline. Historical manifests and `audit_results.json` remain immutable evidence and are not regenerated to manufacture PASS.

## Historical experimental material

Files retained for provenance—including the three `extensions/*/proof/README.md` guides and superseded feasibility/experiment records—may still contain historically correct commands, terminology or pending items from their edition. Unless the root README or current work register explicitly re-admits them, they are outside the current canonical route and do not constitute active research obligations.

Scientific gaps that remain active are named in the current register. As of this policy, M16 independent coverage, M17 source-clause fidelity and P08 version-aware integrity remain governed there.
