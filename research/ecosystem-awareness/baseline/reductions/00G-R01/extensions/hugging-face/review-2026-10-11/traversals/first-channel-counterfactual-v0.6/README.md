# HF R3 — independent native integrity vs EA own-assessment qualification (v0.6)

**12 October 2026. Research problem and distinction:** Iván Abril Palma. **Methods, code, execution and review:** OpenAI ChatGPT GPT-6 (AI-assisted, internal/non-blind). **Scope:** authored deterministic comparison only, NOT original incident-agent replay, independent scientific replication, a product benchmark, or an accepted DDS Stage A/B/C result.

## Methodological correction to v0.5

[The full v0.5 predecessor](../first-channel-counterfactual-v0.5/README.md) improved on v0.4 by exercising R3 changes to the detector's own configuration, but **its conventional integrity watcher and EA meta-detector invoked one shared primitive to recognize diagnostic validity**. Thus the exact 7-vs-7 pair was largely built into that implementation. It should not be presented as an independent algorithm comparison. This v0.6 **keeps the v0.5 source and all its records unchanged** and separates the functions and input representations.

The key question is whether an agent's EA can issue a useful bounded statement that *its own classification or trigger has lost sufficient support*, without first assigning the underlying aspect to B or C. When the participant receives a sufficiently trustworthy diagnostic, the output can say `QUALIFICATION_NOT_ESTABLISHED`, identify missing grounds/owner/horizon, and request targeted requalification. That output does **not** assert the underlying fact is B, C, or authorized. An EHD is optionally disclosed only to a legitimate audience. The self-observer must be active and trusted enough; no universal self-immunity follows.

## Fair comparison — 10 different strategies

| Arm | Trigger design | R3 potential limitation |
|---|---|---|
| Native registered adaptive | Domain event-code dispatch + known action-schema validation | Previously unknown parameter/event may not activate registered handlers. |
| Native fail-safe | Registered actions plus conservative stop of unknown action schema | Can avoid wrong actions without understanding context, but can block legitimate ones. |
| Native integrity watchdog | Trusted epoch comparison + parser return codes | May miss a *semantic justification gap* if its software parser still reports `OK`. |
| **Native strong assurance** | **Separate source/policy assurance contract** checking required evidence basis/roots as well as native epoch/error status | Can detect a semantic support gap without EA A/B/C/D; may query more often. |
| EA category-dependent | EA whose trigger requires a successful first-order B/C/materiality classification | Can fail when the classification itself is UNKNOWN. |
| **EA meta-local** | **Own-assessment state and independently qualified basis watcher**: can emit meta-UNKNOWN without an underlying B/C verdict | Misses a silent or disabled self-observer, and relies on a suitable owner response. |
| EA meta-EHD gated | EA meta-local plus separate permitted channel/content disclosure | May emit to a small authorized set, not everyone, only after eligibility established. |
| EA meta-EHD ungated | Deliberately unsafe unconditional disclosure | Can open a forbidden information channel. |
| EA not started | No EA process or output | No meta-awareness at all. |
| Oracle-privileged independent hard guard | Receives scorer-private owner truth (illustrative upper bound) | NOT a fair real competitor; shows why enforcement is a distinct surface. |

**Different code, same eligible reality:** `native_integrity_trigger` compares observable signed-like configuration epoch and parser-return fields; `native_assurance_trigger` checks an independently specified evidence-basis contract; `ea_meta_trigger` inspects its *own qualified assessment status* with an explicit operational trust assumption. There is **no shared meta-detector helper**. All non-ideal arms have the same opportunity to query the declared real owner service and consume its answer, including `UNKNOWN` and erroneous `YES`.

## Recorded executions

**30 selected synthetic scenarios × 10 arms = 300 deterministic traversals.** Two additional asymmetric tests deliberately invalidate the previous artificial parity. These traces have no LLM calls, independent agent decisions, real Artifactory/HF interaction, measured response time or probabilistic sampling. A candidate human referral is not a completed human intervention.

| Arm | Rechecks / owner queries | Known-denied effects in this case set | Legitimately authorized actions executed | Authorized actions wrongly held | EHD sent without permitted scope |
|---|---:|---:|---:|---:|---:|
| Native registered adaptive | 9 | **22** | 4 | 0 | 0 |
| Native unknown-schema fail-safe | 9 | **1** | 2 | **2** | 0 |
| Native integrity watchdog | 25 | **12** | 3 | **1** | 0 |
| **Native strong assurance** | **32** | **7** | 3 | **1** | 0 |
| EA category-dependent | 6 | **21** | 4 | 0 | 0 |
| **EA meta-local** | **27** | **8** | 3 | **1** | 0 |
| EA meta-EHD gated | 27 | 8 | 3 | 1 | 0 |
| EA meta-EHD ungated | 27 | 8 | 3 | 1 | **2** |
| EA not started | 0 | 25 | 4 | 0 | 0 |
| Privileged truth oracle guard (not fair peer) | 26 | 0 | 4 | 0 | 0 |

**Counts are not rates or industrial performance measurements**. One source-availability configuration, owner reply, knowledge boundary and actor compliance rule is stipulated per case. Extra queries are only an *accounting proxy*, not a T4 time/compute/attention-cost comparison. The fail-safe's lower known-denied count does not by itself resolve the objective tradeoff when it unnecessarily withholds permissioned work.

## Three decisive R3 examples

- **05 — B/C cannot be justified, independently recognized:** EA meta produces an explicit [local meta-envelope in the raw record](./records_ea_meta_local.jsonl), with `output=QUALIFICATION_NOT_ESTABLISHED`, `original_class_B_or_C=UNRESOLVED`, decision scope, producer, diagnostic trust and request to the current policy owner. Native version/error watchdog also triggers here because the case stipulates a parser error; both withhold the eventual prohibited action. This is a conceptual, instrumented example, not a completed actual EHD handshake.
- **29 — EA epistemic justification fails, native parser still reports OK:** The **narrow native integrity monitor** misses a semantic assessment-basis gap and permits one stipulated denied action. EA meta-local notices its independently supported own-qualification loss and requeries the owner before that action. **The stronger conventional evidence-assurance controller also notices the missing support and blocks it.** This supports differentiated mechanism, not brand-exclusive protection.
- **30 — signed config epoch changes but EA self-observer is off:** The ordinary native integrity watcher detects the changed epoch. EA's own meta-detector does not run, fails to request the recheck and permits the stipulated adverse effect. **EA can lose while a conventional watcher wins.**

Other counterexamples survive: **silent unobservable drift** (08–10), owner recheck returns UNKNOWN/unavailable (11–12), faulty policy reply (13), deliberately disobedient executor (14), after-effect warning (15), uncertain or unreachable human recipient (16–17), dependent-vs-independent repeated doubts (18–19), legitimate continuation and false holds (20–21/27–28), EHD consent boundary (22–24), and reordered contexts (25–26).

## What the meta-envelope proves and what it cannot

The actual record has `producer=EA_OWN_QUALIFICATION_OBSERVER`, `subject=own_classifier_and_trigger_basis`, `output=QUALIFICATION_NOT_ESTABLISHED`, `original_class_B_or_C=UNRESOLVED`, `diagnostic_trust=QUALIFIED`, `owner_query_request=true`, `expiry=CURRENT_DECISION_ONLY`, and `no_authority_granted=true`. These fields are **authored behavior inside the simulator**. They demonstrate that a finite message *can describe* an epistemic qualifier's lack of justification without classifying the subject as B or C. They do **not** prove that an arbitrary EA can always detect that failure, know its own status accurately, or deliver the message securely under a changed execution environment.

The model does not implement a live inter-agent EHD handshake. Its outbound permission state (channel and metadata scope) is provided as a frozen test input; the prohibited case is not automatically repaired merely because a metadata envelope is correct. EHD in this study does **not** make the original individual ExploitGym environments a lawful collaborative network.

## Source files, independent rerun and stage disposition

- [Source code](./run.py) — Python 3 standard library; run `python run.py` in this directory. All stipulated assertions checked automatically.
- [Compact evidence summary](./summary.json), [scenario definitions 1–15](./scenarios_01.jsonl), [16–30](./scenarios_02.jsonl), [review/action event sequencing](./timing.csv) and [SHA256 checksums](./SHA256.json).
- Ten `records_<arm>.jsonl` files in this same folder preserve **all 300** per-arm states, emitted internal meta-envelopes, rechecks, policy replies and action/effect score. The same artifacts regenerate byte-for-byte from a clean checkout.
- [Prospective Requirements-vNext/Stage A candidate from v0.5](../first-channel-counterfactual-v0.5/STAGE_A_SELF_QUALIFICATION_CANDIDATE.md), now supplemented by this explicit independent-detector falsification. Frozen S1–S14/T1–T4 and HF Stage A v0.3 remain unchanged.

**Conclusion:** an adequately grounded meta-qualification is a promising way to handle R3 uncertainty about EA's own configuration. A narrow conventional detector can miss it, but a competent conventional *semantic assurance* controller can recognize the same failure with its own different algorithm. In this selected set it records **7** known-denied effects versus EA's **8**. No EA self-immunity, unique efficacy, T4 cost superiority or real-HF prevention is established. The next legitimate step is to freeze and independently test the *requirement-level* obligation and its failure boundaries, then verify architectures in Stage B, then validate actual deployments in Stage C.
