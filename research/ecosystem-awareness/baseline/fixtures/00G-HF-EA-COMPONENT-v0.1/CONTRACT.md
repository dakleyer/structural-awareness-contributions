# EA component v0.1 — bounded qualification contract

**Author implementation profile, 1 October 2026.** This is a finite structured-input experiment. It is not the universal 04 interface, a complete EA implementation, a learned detector, a permission issuer or a model receiver. It receives metadata about a decision basis; it does not inspect the functional inspection/sum output A of the native task.

Sources: [canonical requirements](../../00_CANONICAL_REQUIREMENTS_CHALLENGES_SUFFICIENCY_HYPOTHESES_KPIS.md), [04 general interfaces](../../04_GENERAL_FUNCTIONAL_INTERFACES_AGENTIC_SECURITY_v0.5_INTEGRATED.md), [causal protocol §6](../../00G_HF_CAUSAL_NEGATIVE_TRAVERSAL_PROTOCOL_v0.3_DRAFT.md). Invocation is on demand at any declared process point; there is no mandatory end-of-process timing. This fixture freezes one invocation per input. A population consumer may use another timing policy in a separately registered adapter.

## Input v1

`assess(view)` receives **only** a JSON-compatible observation view. The evaluator holds case IDs, expected properties and hidden world facts separately. Required top-level fields:

- `decision`: `id`, `recipient`, `task`, `resource`, `operation`, `claim`, `basis_version`; all nonempty strings. Exact equality defines scope in this profile; no inferred aliases or semantic equivalence.
- `now`: integer logical time.
- `timing`: `transport_ticks`, `response_ticks`, `last_useful_at`; nonnegative integer costs. These are declared simulation assumptions, not measured real-time latency. The signal is emitted at `now`, received at `now + transport_ticks`; useful only if the response finishes strictly before `last_useful_at` and the earliest supporting evidence expiry.
- `checks`: a list of source-native observations. Each carries `name` (`mandate`, `access` or `applicability`), `source`, full matching `decision` scope, `version`, `observed_at`, `valid_until`, and boolean or null `value`. The host supplies source identities through a trusted channel; a peer cannot set these fields by asserting a name in text. Acceptance is an explicit trust assumption, not cryptographic verification implemented here.
- `reports`: typed `report` or `instruction` records, with `id`. A report additionally carries full scope, `claim`, boolean `value`, `qualified`, `lineage_source`, unique-root labels `roots`, `observed_at`, `valid_until`. Source independence is only the declared lineage relation, not proven statistical independence. An instruction is not evidence or a grant. Missing/unqualified lineage cannot supply roots.

The candidate configuration pins one accepted source for each check (`principal-service`, `asset-service`, `applicability-service`) and the accepted lineage qualifier `lineage-service`. The evidence rule is two qualified distinct root labels for the proposition in the same decision. These are experiment-specific conventional requirements inherited in spirit from the six-cell pilot; they are **not** canonical requirements that every EA system must use. Services must make these facts available symmetrically to any comparator.

Every current record uses the half-open interval `[observed_at, valid_until)`. The candidate cannot establish whether a claimed freshness bound is truthful or whether an unseen revocation happened inside it. Missing records, wrong scope, wrong issuer, future records, expired records or incomplete root qualification provide no positive support. A fresh positive and fresh negative observation are a conflict, not a vote. Contradiction dominates a claim of sufficiency; other missing information remains explicit in the same output.

The protocol validates shape and bounds before assessment: at most 64 check records and 64 reports, 16 root labels per report. Schema errors raise `ValueError` and produce no fabricated success signal. These engineering bounds are profile choices, not a proof of minimum disclosure or sufficient capacity under arbitrary load.

## Output v1

The output retains full decision scope and basis version, per-check status/source versions, rejected or unqualified records with reasons, admitted evidence IDs/roots, missing/contradicted dimensions, directed checks and an open-residual statement.

- `basis_sufficiency`: `SUFFICIENT_WITHIN_VIEW`, `CONTRADICTED` or `UNKNOWN`.
- `posture`: `QUALIFIED_WITHIN_SCOPE`, `REQUALIFY` or `PRESERVE_UNKNOWN`; this is decision support, never execution permission.
- `evidence.status`: supported, contradicted or unknown; two positive reports from the same root cannot be counted as two roots. Negative qualified evidence remains a reason to requalify even if there are two positive roots.
- `emitted_at`, `received_at`, `last_useful_at`, `qualified_until`, `response_margin_ticks`, `timely`: scope and time limits. Late correct qualification is not operational prevention. Equality at the expiry/deadline boundary is too late under this profile.
- `authority_effect`: always `NONE`. Existing authority remains under its owner. The output does not choose the next task or stop a tool.
- `residual`: always preserves limits of the declared window, trust bindings, hidden change and lineage assumptions. No population/regime probability is emitted.

There is no previous observation in this first profile. The candidate qualifies the current view; it **cannot identify a temporal change merely from a bad current basis**. A change detector requires a later version with qualified prior state and a separately registered temporal contrast. Similarly, `SUFFICIENT_WITHIN_VIEW` is not global truth: two worlds with exactly the same view produce exactly the same output even if hidden permission differs.

## Bounded traceability and non-claims

| Requirement / condition | Executable property | Remaining gap |
|---|---|---|
| S1 | Mandate and access qualified separately against their declared sources, scope and time. | External authenticity, delegated chains, stolen credentials, authoritative completeness and effect-time enforcement. |
| S5 / S14 | Unknown and conflict remain explicit; no promotion of peer instructions to evidence/permission. | No implemented containment or human escalation; no full transition/arbitration lifecycle. |
| S9 | Root labels preserved; duplicate relays do not create extra roots. | No general multi-principal hierarchy, graph discovery or statistical independence estimator. |
| S10 | Output binds a stated decision/time and expires. | No historical context-change detector or commitment-state machine in this version. |
| T1 / T2 | Bounded qualification and explicit observability limits. | No universal material-break detection or complete owner-preserving implementation. |
| T4 | Logical transport/response margin and finite input bounds. | No real-time production calibration or demonstrated risk/resource frontier. |
| H2 / H4 | Candidate carrier exposes residual and scope without full world access. | Behavioral benefit and bounded preservation sufficiency remain untested hypotheses. H3/H5/H6 are not evaluated. |

## Acceptance and recording

`CASES.json` separates `view`, expected output properties and hidden evaluator facts. Freeze this file and contract before candidate execution. Every run verifies that commitment, pins the candidate/checker code before invoking it, and stores every actual output and comparison. Same author prepared implementation and cases; local hashes and timing do not establish external preregistration or independence.

Two hidden-world cases deliberately share identical view bytes. Passing their equality check demonstrates an information limit, not correct identification of the hidden world. Consumer controls deliberately stipulate an agent policy: signal followed, signal ignored, or conventional guard already sufficient. They test a conditional proposition in a toy decision model, not model understanding or a C3 operational pass.

The frozen C3 oracle is not modified or imported by this component. These new properties are separately labelled contract checks; they do not extend C3's 102 controls or close empirical E1/E3.
