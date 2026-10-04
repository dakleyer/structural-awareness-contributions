# R01 ↔ Nelson UC-4 interoperability profile

Working bridge v0.1 · 4 October 2026 · source-contributor review requested before calling it UC-4-compatible.

## 1. Design intent

Nelson's UC #4 is the **primary testbed contract** for R01 integration with Theme #13. R01 should enter that testbed as a bounded imported profile, not require UC #4 to adopt an R01-native experiment format.

UC #4 Requirements 22–24 are therefore treated as the governing interoperability constraints:

- versioned adapters for imported contracts;
- frozen positive, boundary and rejection cases with machine-readable expected outcomes;
- mutually agreed, version-pinned scope with source-contributor validation and no silent maintenance obligation.

Source: https://github.com/FG-TIDA/use-cases/issues/4

Nelson's package description also separates common experiment data from adapter-specific mappings. It records question/hypothesis, controlled change, actors/trust boundaries, source versions, expected observations, resources, reproducibility and sharing. Schema 1.1.0 additionally records assessment time, determination consumed, provenance, required execution capabilities and separate technical/preparer/contributor review states.

Sources:
- https://github.com/FG-TIDA/use-cases/issues/4#issuecomment-5847245589
- https://github.com/FG-TIDA/use-cases/issues/4#issuecomment-5871266911
- revised #13 mapping package v0.4.1-r1: https://github.com/FG-TIDA/themes/issues/13#issuecomment-5900725441
- Stage-0 calibration result: https://github.com/FG-TIDA/themes/issues/13#issuecomment-5949120841

## 2. What R01 reuses unchanged in meaning

| UC-4 concept | R01 use |
|---|---|
| Experiment question / hypothesis | Identifies the bounded R01 claim or technology question; never inferred from results. |
| Controlled change | Defines exactly what differs between comparator/technology conditions. |
| Source versions | Pins R01 scenario, technology profile, imported Theme outputs and adapter versions. |
| Adapter | Preserves source-specific semantics and translates only at the declared boundary. |
| Expected outcome | Stored outside the candidate-visible view and applied only after candidate execution. |
| Assessment time | Required because R01 evidence, mandate, dependency and state applicability are time-bound. |
| Consumed determination reference | Identifies an upstream determination without allowing R01/EA to recreate that semantic authority. |
| Required capabilities | Declares what the execution environment must actually provide before a case is runnable. |
| Review states | Technical validity, preparer review and source-contributor semantic review remain distinct. |
| Positive / boundary / rejection vectors | Used directly as the minimum Stage-0 control structure. |

## 2.1 Nelson Stage-0 controls reused

Nelson reports 64 passing reference assertions in the UC-6 / Theme #13 calibration, plus deliberate applicability corruption, malformed-record isolation, deterministic replay, missing agent-ID sensitivity and case-order reversal. R01 reuses those **testbed patterns**, not the UC-6 authority semantics. The detailed source-to-R01 mapping is in [NELSON_BASELINE_IMPORT.md](./NELSON_BASELINE_IMPORT.md).

R01 additionally adds an identifier-permutation control because §2.17 explicitly requires auditing accidental hints, and a no-reference vector that must remain `INCONCLUSIVE`.

## 3. R01-only sidecar

R01 needs private information that **must not become a shared Theme #13 interface**. It is therefore kept in a sidecar referenced by the experiment/test-vector identity.

The sidecar adds only:

- private frozen-world reference and hash;
- participant-view projection and forbidden-private-field policy;
- finite operation/cost/deadline contract from R01 §§2.6, 2.11–2.12;
- exact bounded reference method(s);
- R01 task-state and candidate-state evaluation from §§2.16–2.17;
- acceptance parameters from §1.4: epsilon, economic cost target b, physical budget R and deadline T;
- separate evaluator/oracle resource ledger;
- sealed candidate-trace hash before reference evaluation.

These are evaluator/testbed concerns. They are **not Theme #13 signal fields** and are not proposed as FG-TIDA-wide vocabulary.

## 4. Semantic ownership

R01 must not turn imported determinations into locally authored truth.

```text
source owner determination
        |
        v
UC-4 versioned adapter
        |
        v
Theme #13 / EA consumer view
        |
        +--> R01 participant-visible observation
        |
        +--> private testbed record of the source/version/expected relation
```

If authority, delegation, identity, oversight capacity or another imported state changes, the adapter preserves that source meaning. R01 may evaluate whether reliance remains supported in its scenario, but actual re-determination remains with the semantic owner.

## 5. Compatibility levels

| Level | Meaning |
|---|---|
| R01-BRIDGE-DRAFT | R01 sidecar and adapter contract exist; no source-contributor review. Current status. |
| UC4-SOURCE-REVIEWED | Nelson confirms the mapping is compatible with his current experiment/testbed semantics. |
| UC4-SCHEMA-VALIDATED | The R01 profile has been packaged against a pinned UC-4 schema and passes its validator. |
| STAGE0-ADMITTED | Frozen case vectors, capabilities, reviews and expected outcomes are accepted for deterministic execution. |
| STAGE1-ADMITTED | A separately agreed federated/runtime integration exists. |

No higher level is inferred from a lower one.

## 6. Requested review points for Nelson

Before claiming UC4-SOURCE-REVIEWED, ask Nelson to correct at least these points:

1. whether R01's private evaluator fields should remain a sidecar or live under an extension object in his experiment package;
2. the preferred identity/reference mechanism linking a sidecar to a UC-4 experiment and test-vector ID;
3. whether the sealed pre-oracle candidate-trace hash should be part of the common experiment record, adapter result or external evidence manifest;
4. how he wants evaluator-only resource cost represented without contaminating the participant/comparator burden;
5. whether the current explicit statuses `PASS | FAIL | INCONCLUSIVE | INFRASTRUCTURE_ERROR` fit his expected-outcome semantics or require mapping.

Until that review, this profile deliberately avoids claiming exact UC-4 schema compatibility.
