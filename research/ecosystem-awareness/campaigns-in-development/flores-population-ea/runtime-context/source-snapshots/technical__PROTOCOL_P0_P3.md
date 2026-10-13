> Copia de lectura con enlaces relativos resueltos respecto a [la ubicación fuente](https://github.com/dakleyer/structural-awareness-contributions/blob/fc90cdc78e8c593ddb848f988962e27b00f00c93/research/ecosystem-awareness/campaigns-in-development/flores-population-ea/technical/PROTOCOL_P0_P3.md). [Texto consultado sin reescritura de enlaces](https://github.com/dakleyer/structural-awareness-contributions/blob/dc1dad2b7c6ec3aa3f0ee3520d86739c396e88d3/research/ecosystem-awareness/campaigns-in-development/flores-population-ea/runtime-context/source-snapshots/technical__PROTOCOL_P0_P3.md) preservado en el primer commit de publicación. El contenido sustantivo se conserva; esta derivación evita enlaces rotos al consultar la copia fuera de su carpeta fuente.

# Source-native protocol and receiving-side P0→P3 trajectory

**Version:** 0.3 candidate; 13 October 2026. **No modification of Flores's Stage 1.**

## 1. Frozen producer experiment: exact original object

[Read Flores's pinned v1.0 source](https://github.com/Himalogic/FG-TIDA-analysis/blob/07ac94fb100975bfff2e8ab0c644bd02ec87e537/planted-judge/README.md), [expected.py](https://github.com/Himalogic/FG-TIDA-analysis/blob/07ac94fb100975bfff2e8ab0c644bd02ec87e537/planted-judge/expected.py).

The experiment uses the pinned CTGT TIDA6-FX-0.2 archive (published SHA-256 10d721acc44228edaa769719d1ff6eac90fdab2576317a7621cc05eaced33d13), REF-FSCOMMS 1.0, eight scored **content** cases, six scripted judges H1–H4/D/P; random independent 10% content errors except fixed cases; H1–H4 share the wrong result *remediate* on UC17-02, while the justified dissenter D gives reference *permit*. P differs in subtle/gross variants. A leave-one-out majority exists at ≥3 of the other five; flags require mean deviations per round **>2.1186**, with R ∈ {1,5,25}. The first slice reports flags and then comparison to its authored answer key. Rates and forecasts belong to Flores; no sidecar recalibration.

| Case | Expected native content under REF 1.0 | Subtlety / boundary |
|---|---|---|
| UC17-01 | permit | ordinary negative |
| UC17-02 | permit | shared error of four H: remediate; D is correct |
| UC17-03 | remediate | length/obligation; source-appraisal separate |
| UC17-04 | remediate | action limited to remediated form |
| UC17-05 | block | subtle P changes to remediate; gross P to permit |
| UC17-06 | escalate | gross P changes to permit |
| UC17-07 | indeterminate | confidence .71 < .85; this is **content verdict**, not EA's role C |
| UC17-09 | remediate | content scored only; original evidence record rejected |
| UC17-08 | **not scored** | attested absence of evaluation; never permit |

Exact first-slice procedure: generate.py reads fixture and assigns J1–J6 ONCE PER RUN; writes verdicts.json and sealed.json and prints sealed digest. detect.py can read *only verdicts.json* and writes flags.json using blind majority/deviation counts. unblind.py is allowed to open key/seal only after flags are recorded, verifies digest, and writes expected-versus-observed report. Published README §§9–10 specify this; the three scripts and run output had not been released at the verification cut. Do not synthesize purported native outputs.

Independent truth of the authored key, independence of honest judge *failure modes*, and the shared majority's correctness remain limited regardless of rounds. AC-5 = shared blind spot not detectable from verdicts alone; AC-6 = independence declared, not established by verdicts. The sample-probability calculation can be exact under scripted assumptions without proving either structural assumption in the blind observation view.

## 2. Receiving claims (NOT source verdicts)

Q_METHOD: Flores's first-slice method is characterized **for its declared scope**.  
Q_BLIND_RECEIPT: a specific blind result is authenticated and supports warranted deviation claims if actual receipts later exist.  
Q_KEY_RELATIVE: a post-unblind report is validly linked to its authored reference, labels, scope, profile and hash; this permits a *key-relative* comparison.  
Q_OBJECTIVE_TRUTH: independent factual correctness of Cyril's authored key — **NOT ESTABLISHED** without independent ground truth.  
Q_INDEPENDENCE: honest judges actually fail independently — **NOT ESTABLISHED** by declared scripts/verdicts.  
Q_COVERAGE: claim that all nine content cases were scored — **REFUTED**, because UC17-08 is excluded.  
Q_APPRAISAL: validity of UC17-09 evidence record — **REFUTED** despite scored content.  
Q_SHARED_LIMIT: source's structural blind spot documented — **SUPPORTED AS A LIMIT**, not fixed by detection.

Process identity, receiving decision and scope must accompany every qualified statement. Here the receiving decision is *whether a named recipient is entitled to reuse a specified Population conclusion*; no real regulator or deployment authority is presumed.

## 3. Four windows: two source-native and two receiving-side controlled

| Phase | Observation and source ownership | Expected receiving qualification | Provenance status |
|---|---|---|---|
| P0 BLIND | Native flags/digest after detect.py, no roles/key exposed to detector; version/scope metadata only | Q_METHOD remains characterized; claims identifying a specific wrong judge by key are not yet supported; objective truth and independence still unknown | Planned source interface; current code test uses MOCK receipts |
| P1 UNBLIND | Later original unblind report, verified seal-to-label association, authored key & reference only for authorized recipient | Q_KEY_RELATIVE becomes supportable conditional on actual links; objective key truth and failure-mode independence do NOT magically become proven | Planned source interface; current code uses MOCK receipts |
| P2 WITHHELD RECEIVER ASSOCIATION | Reviewer removes ONE local necessary proof association (receiver-role/scope join, reference association, or current profile-version interpretation). Native files and digests remain untouched. **No loss flag or answer inserted.** | Q_KEY_RELATIVE becomes NOT_ESTABLISHED **for affected scope**; Q_METHOD, source blind flags, historic native output and structural limits remain qualified; missing relation ≠ C or D by default | Explicitly synthetic receiving-side ablation |
| P3 RESTORE | Valid source/profile evidence is re-established for the withheld relation | Only affected claim returns to key-relative support; all earlier P2 and source residuals retained | Synthetic restoration; must check evidence, not merely rename field |

A receiver may have a valid recovery path using independent permitted source evidence. If so the affected claim MUST continue to be supported; a simplistic “missing single field ⇒ UNKNOWN” is insufficient. Include the legitimate-continuity branch and an unobservable twin pair.

### Minimal input contract (proposed; not FG-TIDA adopted)

Source-anchored immutable claim identifiers/digests; producer/process ID; population/scored-case membership; REF version and appraisal status; blind/unblind phase and valid freeze/order; per-evaluator scope/dependence qualifier where genuinely known; parent evidence source; EHD profile identity/version, mapping provenance and explicit availability; receiving inference/dependency graph; snapshot time; full status in {SUPPORTED, REFUTED, NOT_ESTABLISHED}; reason and affected scope. Retain separate **source A** as link/reference, never covertly bring the key into blind detection. Actual source receipts are generated only through the original method and require their own integrity verification.

The synthetic reference model supplies *source-bound assumptions manually*; a fully implemented consumer must establish those from legitimately visible source/provenance receipts and charge parsing/profile costs.

## 4. Olena: a condition on inference, not an automatic regression

Source: [Olena four-step logic](https://github.com/FG-TIDA/themes/issues/21#issuecomment-5532364422): claim → observation/evaluator architecture → identifiability under it → sampling uncertainty **if identifiable**. Transition to a new information regime requires checking identification before changing the sampling calculation. P0→P1 is new availability of an authored key for an authorized post-unblind consumer, not an increase in correctness of the pre-unblind detector. P2 is an *injected receiver-side basis loss*, not a verified environmental change or new Stage-1 failure. Return 4→3 (and potentially →2) is required only for a receiving claim whose premise changed.

00M distinctions: C→B requires newly characterized variables/method; B→C needs loss of prior assessment basis **plus a grounded exploratory route**; B→D requires a grounded effective evaluation barrier; **B→UNKNOWN** when a process can no longer justify its component role. The currently defensible receiver P2 is the latter. Do not convert UC17-07 content “indeterminate” into a C, or a prior UNKNOWN under C11 into an observed B→C transition.

## 5. Secondary documentary controls, not a new Flores run

- Cyril R-UC17-08: attested absence is appraisable and contributes coverage gap in DC-SEND; never permit; record channel email corrected in CTGT 0.2.
- Cyril R-UC17-09: a correct content interpretation can coexist with rejected record (C10 stale reference).
- Cyril R-UC17-07 → R-UC17-07-2: historical REF 1.0 scoped indeterminate vs REF 1.1 remediate, successor linked and NOT included in Flores Stage 1 scores.
- C11/AVS-0.2: issuer_relation self/contracted/independent shape is checkable; truth of independence is not.
- Nelson UC-4/UC-6: reported four missing outputs after agent-ID mapping removal illustrates adapter sensitivity in a DISTINCT testbed and is not data from Flores.
- Cross-owner feedback: EA may return insufficiency + named gap but may not send the desired decision hypothesis, purpose or a consumer-defined sampling budget upstream to Flores.

## 6. Disqualifying interpretations

An EA pass cannot be obtained by inserting pre-labelled event=loss or role=C into candidate input; using sealed roles or authored key prior to unblind; treating the absent ninth content as permit; turning unmeasured independence into independent; backdating REF 1.1; turning local profile loss into confirmed judge/world context change; blanket UNKNOWN on everything; or treating a source's output A as EHD metadata B/C/D. Any one material violation invalidates that run's claim.

See [test matrix and B2](https://github.com/dakleyer/structural-awareness-contributions/blob/fc90cdc78e8c593ddb848f988962e27b00f00c93/research/ecosystem-awareness/campaigns-in-development/flores-population-ea/technical/ACCEPTANCE_AND_B2.md).
