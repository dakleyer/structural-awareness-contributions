# DDS Gate A — VNext

**Owning source:** [DDS Gate A — Specification Discovery / Challenge–Trajectory Profile v0.1](./DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1.md)  
**DDS method router:** [DDS Canonical Method Index v0.1](./DDS_CANONICAL_METHOD_INDEX_v0.1.md)  
**Current review date:** 7 October 2026.  
**Status:** current Gate-A review ledger only. Historical incorporated proposals have been removed from this VNext because Git history already preserves them.

## 1. Current Gate-A state

Gate A is now explicitly separated from the complete DDS method.

The live Gate-A source currently provides:

- canonical identity as **DDS Gate A — Specification Discovery**;
- explicit A/B/C gate taxonomy for a reader entering this file;
- distinction between **DDS Gates** and local **trajectory gates**;
- full versus **Simplified DDS Gate A** coverage semantics;
- Challenge and bounded reduction;
- blind evaluator/private-map discipline;
- technology/configuration mapping;
- Stage 1 technology–problem extension/isomorphism profiling;
- Stage 2 non-isomorphic mechanism study;
- I/M/P/Ø route/outcome semantics;
- Type-0/1/2 and M-admission diagnostics where admitted;
- Cost/Risk/Effectiveness accounting;
- acceptance and optional Business Value projection;
- proportionality and material-assumption checks;
- reduced coverage / delivery separation;
- current R01, extension and HEW research relationships;
- evidence/claim boundary;
- minimum Gate-A citation block;
- explicit Gate-A entry, exit and handoff contract to Gate B.

The latest reader-orientation/handoff incorporation is commit `27938fa70a82c2fa07f79c60eed34ab4c2d9f267`.

### Conservation check for that incorporation

The Gate-A clarification commit added **125 lines and deleted 0 lines**. No prior Gate-A scientific text, mathematics, result, threshold, evidence record or source relationship was removed by that change.

## 2. Incorporated — no longer pending

The following items are incorporated in the live Gate-A source and are intentionally **not repeated as before/after proposals in this VNext**:

- canonical-boundary / meaning-of-canonical clarification;
- reduced-coverage and delivery clarification 0.1.2;
- Stage 1 extension/isomorphism + Stage 2 non-isomorphic-mechanism clarification 0.1.3;
- HEW / executed-companion evidence parity;
- proportionality clarification 0.1.4;
- material-assumption check;
- bibliography / research-basis route;
- scoped-study completion route;
- Type-0/1/2, M-admission and blind-reference refinements already present in Gate A;
- split from one monolithic DDS file into Index + Gate A + Gate B + Gate C;
- Gate-A reader taxonomy and scope boundary;
- Gate-A entry/exit package and Gate-B handoff contract.

Their detailed historical text remains available in Git history. They are not active work items.

## 3. Pending Gate-A changes

There is **no pending scientific rewrite of Gate A** after the 7 October incorporation.

One structural item remains intentionally deferred:

### GA-P01 — relocate the cross-gate profile registry after corpus taxonomy

**Current location:** Gate A §11, `Current profile mapping`.  
**Current state:** retained with an explicit migration warning.  
**Reason to defer:** the table predates the three-gate split and mixes Gate-A examples with DBC/00D/support/component roles. Rewriting it before the corpus-wide taxonomy would guess classifications that have not yet been applied to the active profiles.

**Later action, during taxonomy phase:**

1. move the authoritative cross-gate profile/support registry to the DDS Canonical Method Index;
2. classify active artefacts as Gate A / Gate B / Gate C / support / infrastructure;
3. keep in Gate A only Gate-A examples plus a link to the canonical registry;
4. do not rewrite frozen historical results merely to apply the new taxonomy.

**Status:** PENDING — intentionally blocked on corpus taxonomy, not on Gate-A science.

## 4. Not Gate-A work — do not accumulate here

The following belong to other owners and must not turn this VNext into another monolithic DDS backlog:

| Work | Owning source / phase |
|---|---|
| Common cross-gate conservation, proportionality and profile-identity rules | DDS Canonical Method Index |
| Gate-B contract evolution and 00I/S5 architecture-verification pilot | DDS Gate B |
| Gate-C contract evolution and C11/T03 real-implementation validation route | DDS Gate C |
| Product-profile labels such as Simplified DDS Gate A | corpus taxonomy phase |
| DBC / 00D role normalization | corpus taxonomy phase |
| R01 / HEW / 00L / Stage-0 classification labels | corpus taxonomy phase |
| Oracle README and local gate-policy namespace cleanup | Oracle/corpus taxonomy phase |
| WORKPLAN / VISUAL_GUIDE migration | corpus taxonomy phase |

Future substantive changes to the Index, Gate B or Gate C should use their own owning review/VNext rather than being appended here.

## 5. Gate-A review checks before any future incorporation

Any future Gate-A change should pass all of these:

1. **Object check:** the object under test is still a candidate specification/mechanism/control profile, not architecture realization or product validation.
2. **Reference check:** the authoritative reference remains the frozen Challenge / Gate-A acceptance and falsifier contract.
3. **Namespace check:** DDS Gate A/B/C is not confused with trajectory gates, gate policy, Stage-0/Stage-1 or C02/C11/T03.
4. **Evidence check:** evidence mode does not silently change Gate identity.
5. **Conservation check:** no frozen result, hash, theorem or historical evidence is strengthened or erased.
6. **Coverage check:** a Simplified Gate-A profile declares selected and omitted surfaces.
7. **Handoff check:** any Gate-B-ready result identifies a sufficiently frozen Gate-A specification package.
8. **No-zombie check:** once a proposed change is incorporated, remove it from this VNext; Git history is the archive.

## 6. Current decision

**Gate A is ready for the next phase without another canonical rewrite.**

The next repository-wide task is **corpus taxonomy and surgical referencing**: identify each active testing artefact as DDS Gate A/B/C or support/infrastructure, and add the corresponding full/Simplified classification without modifying frozen evidence.

Until that phase reaches Gate A §11, GA-P01 is the only pending item in this VNext.
