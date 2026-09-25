# 00K-A4 / P4–00H executable harness — corpus integration and execution record

**Status:** deterministic symbolic execution; **not** a live agent/product benchmark  
**Date:** 25 September 2026  
**Parent:** [00K — Six-Principle Sufficiency & Adversarial Ablation Test](../../00K_SIX_PRINCIPLE_REQUIREMENTS_MAPPING_AND_ABLATION_TEST_v0.1_DRAFT.md)  
**Paper precursor:** [00K-A03 — P4 / 00H deterministic paper execution](../../00K_A03_P4_00H_PAPER_ABLATION_EXECUTION_v0.1.md)  
**Scenario:** [00H — The Quiet Four Thousand v0.5 Draft](../../00H_FAILURE_MODE_BATCH_OPPORTUNITY_BEYOND_AUTHORITY_v0.5_DRAFT.md)

## 1. Imported reviewed harness

The original three files in this directory were supplied as the reviewed package `00K_A4_executed_ablation.zip` and were copied into the repository without redesigning their model:

- [`README.md`](./README.md)
- [`ablation_A4.py`](./ablation_A4.py)
- [`test_ablation_A4.py`](./test_ablation_A4.py)

Local SHA-256 values of the supplied files before repository insertion:

| File | SHA-256 |
|---|---|
| `README.md` | `ea440194559bb4f400a282c8157bf0402ad67181cddbaeb20b7bbfc0d57da39c` |
| `ablation_A4.py` | `d5cf72b99240444d31728dc0f421721e5ad117a6a387e256be9184c511e82172` |
| `test_ablation_A4.py` | `fcc0de21e2b217a9a4771f74e4ffca73604781ac3176458a2d77dccc09b64628` |

The source package's own claim was independently re-run before publication.

## 2. Independent local execution

Environment used for the verification run:

- Python **3.13.5**
- pytest **9.0.2**

Original reviewed suite:

```text
...........                                                              [100%]
11 passed in 0.17s
```

This confirms the package's stated **11/11** result in the current sandbox execution environment.

## 3. Additive strengthening — not a rewrite of the reviewed harness

The reviewed three-file package is left intact. One additive file was created:

- [`test_ablation_A4_extended.py`](./test_ablation_A4_extended.py)

The extended suite adds six adversarial checks:

1. **P4-blind U/G observation equivalence** — under the frozen fixture, U and G expose the same finding, leaf validity, campaign identity, timing and volume to the currently modelled P1/P5/P6/native-control surface.
2. **Rate-cap threshold sweep** — below, at and above the one-hour burst threshold, the same rate policy gives the same result on U and G.
3. **Stricter materiality sweep** — tightening a P1-style materiality threshold cannot separate U from G because the finding is identical.
4. **Leaf-freshness symmetry** — P5 can make both branches fresh or stale, but cannot distinguish their authorization state.
5. **Composition-only dilemma** — P6 can detect one campaign, but a P4-blind `DENY common campaign` rule fails G while `EXECUTE common campaign` fails U.
6. **Discriminant restoration** — with the finding/action stream held identical, adding a current root-authority relation is sufficient for the Route-Q model to separate U from G.

Combined run after adding these checks:

```text
.................                                                        [100%]
17 passed in 0.21s
```

## 4. Important audit observations

### 4.1 The original P1 rescue is named more strongly than it is coded

`ablated_rescue_P1_stricter_evidence()` in the supplied model calls the same base `check_P1_evidence_sufficiency()` used by the baseline; it does not implement a numerically stricter threshold.

This does **not** invalidate the 11-test result, but it means the original code by itself is weaker evidence for the phrase “stricter evidence sufficiency” than the README suggests.

The additive threshold-sweep test addresses that gap without modifying the reviewed source: even when the materiality threshold is moved across values below, at and above the 4,000-account finding, U and G remain indistinguishable because they share the same finding. A P1-only tightening therefore cannot solve the U/G separation problem inside this fixture.

### 4.2 Section-number drift is editorial, not semantic

The supplied README/source comments refer to “§14 Branch U / Branch G / Branch I”. In the current 00H v0.5 document, the relevant U/G/I logic is now most explicit in the gate audit and deterministic pre-execution trace (§10/§17A). The branch semantics themselves are preserved. The imported reviewed files were not silently edited merely to update this numbering.

### 4.3 What the stronger result actually says

The executable result is now stronger than “four hand-picked rescue functions failed.”

Within the **current frozen observable surface**, U and G are intentionally identical to a P4-blind deterministic decision rule: the declared material difference is current root campaign authority. Therefore a deterministic mechanism that uses only those identical observables cannot map U to block/recontract and G to execute.

This is a **fixture-level indistinguishability result**, not a universal theorem about all possible systems. A future repair may introduce another discriminating observation. If that observation passes U/G/I/NM without being operationally equivalent to a receiver-verifiable authority qualification, it is a TRUE SUBSTITUTE and falsifies the current P4-necessity claim.

## 5. Current evidence classification

| Layer | Result |
|---|---|
| 00K-A03 paper reasoning | **SEMANTIC RECONSTRUCTION / provisional P4 support** |
| Reviewed executable harness | **11/11 passed** |
| Additive adversarial strengthening | **6/6 passed** |
| Combined deterministic symbolic suite | **17/17 passed** |
| TRUE SUBSTITUTE found | **No, within the tested/documented repair surface** |
| Live runtime / product execution | **Not performed** |
| Universal P4 necessity | **Not established** |

## 6. Re-run

From this directory:

```bash
python -m pytest -q
```

The intended falsification route remains open: add a new repair that passes U, G, I and NM under matched facts/resources **without** using or reconstructing a receiver-verifiable root/campaign authority relation. Such a passing repair counts against P4 necessity.


## 7. Reviewed successor package and unified current fixture

A later reviewed successor package, again supplied as
`00K_A4_executed_ablation.zip`, was received after the original 11-test
package. It extends the same model with:

- NM checks across the ablated arms and A2-L;
- an explicit non-EA-branded A2-L strong peer;
- the four-arm comparison requested by 00K-A03 §10; and
- a summary test that no TRUE SUBSTITUTE is present among the tested repairs.

### 7.1 Successor provenance

| Artifact | SHA-256 |
|---|---|
| successor ZIP | `e7d1caf81e2534fa5b0250f8982fe16fb8e960a273803f151b9ca876dd7c4b63` |
| successor `README.md` | `266eb42543bbddc7e3f0be5b49b11575f1ab1cada41b093b02adf0c53c014da9` |
| successor `ablation_A4.py` | `6cd2f24629672e5337bdf512dc1612e704c5f7828b462de04bb8ae7c174e4f26` |
| successor `test_ablation_A4.py` | `38fc897f7eafaf5f700fcaddfd40eae20866fc2546d150027a6563b6875f97b5` |

### 7.2 Independent successor execution

The successor package was executed unmodified before corpus integration:

```text
.....................                                                    [100%]
21 passed in 0.25s
```

The printed four-arm pattern matches the paper execution:

| Arm | Branch U | Branch G | Interpretation |
|---|---|---|---|
| −P4 leaf/local baseline | EXECUTE | — | unsafe on U |
| −P4 native rate cap | DENY | DENY | blocks blindly; positive-control failure |
| A2-L semantic reconstruction | REPOSITION/RECONTRACT | EXECUTE | branch-correct; reconstructs P4 invariant |
| full six-principle Route Q | REPOSITION/RECONTRACT | EXECUTE | branch-correct |

### 7.3 Corpus-preserving integration

The already-reviewed predecessor files were not silently replaced. The current
fixture family was advanced by:

1. retaining the A2-L implementation in `a2l_strong_peer.py`;
2. adding `test_ablation_A4_v02_additions.py` for the successor-only NM,
   A2-L and four-arm checks; and
3. retaining `test_ablation_A4_extended.py` as the independent six-test
   U/G indistinguishability strengthening.

The current active corpus composition is **29 tests**: 11 reviewed predecessor tests + 10 reviewed successor additions + 6 independent U/G indistinguishability checks + 2 bounded grid checks. During integration, a duplicate successor-alignment file was removed after confirming the reviewed `test_ablation_A4_v02_additions.py` already carried those checks, and the original reviewed `ablation_A4.py` was restored byte-for-byte. A2-L remains an additive peer implementation in `a2l_strong_peer.py`.

The evidence claim remains unchanged in kind: this is a runnable symbolic fixture result, not a live agent/product test and not universal proof of P4.

## Addendum — 25 September 2026, strict 00H-MAT-1 boundary

The earlier byte-for-byte preservation statement above describes the reviewed predecessor at the time of that integration. A later additive 00L verification found that the active harness used `>= USD 10,000` whereas the scenario's frozen `00H-MAT-1` requires **more than USD 10,000**. The active `ablation_A4.py` now uses `>` for the exposure threshold; the reviewed ZIP is untouched. [00L-A10](../../00L_REINFORCED_PAPER_TRAVERSALS_00E_00J_v0.1/00L_A10_VERIFICACION_PARES_Y_PREVUELO_v0.1.md) records the failing-before/fixed-after boundary check and the limited standard-library replay. Previously published full-suite totals apply to the previous code revision; the full `pytest` suite has not been rerun after this one-operator correction in the current environment.
