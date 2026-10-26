# Reading conventions and working vocabulary

The main text is the complete entry point for selecting, preparing and scoring one experiment. The annexes in this directory preserve the detailed scenarios, variants, technology walkthroughs, measurement definitions and family boundaries. Their local section numbers retain the source numbering; gaps do not imply an external dependency. Labels 00E–00J mean S1–S6 respectively. Each local Q gate belongs to its scenario.

## Routes and implementation

| Term or label | Meaning in this contribution |
|---|---|
| R0 / R1 / R2 | Ordinary implementation; reinforced implementation; the same frozen reinforced implementation under an admitted observable context change. R2 is not a separately improved implementation. |
| Profile aliases | A0/A1/A2, H0/H1/H2 and I0/I1/I2 denote the same three ordered configurations where a technology profile uses those names. An L suffix is a permitted reinforcement of R1 before freeze. S3 also names robot participants R1/R2; these are actors, not experiment routes. |
| F/G in S3; U/G/I in S4 | Unsupported versus genuinely supported mission transition; unauthorized common-root campaign versus authorized campaign versus genuinely independent cases. These are fixture branches, not architectures. |

## Evidence and state

| Term or label | Meaning in this contribution |
|---|---|
| Fixture / oracle | Registered facts and inputs / the assessor’s independent ground truth and permitted outcomes. The tested system receives only its declared evidence, never the oracle. |
| HOLD / UNKNOWN / INDETERMINATE | Temporary unresolved operational status / unavailable or insufficiently established information / a conclusion that cannot yet be determined. Each needs a bounded owner, time and consequence; none automatically authorizes action. |
| NOT DECLARED / NOT ESTABLISHED / NOT APPLICABLE / NOT EXERCISED | An input was not supplied / support was not demonstrated / a condition does not apply for a stated reason / the condition was not tested. Preserve these distinctions. |
| Capability/control diagnostic | CAPABILITY_ABSENT: no applicable control; CONTROL_PRESENT_NOT_INVOKED: bypass or non-use; CONTROL_EXECUTED_FAILED: executed but wrong; CONTROL_EXECUTED_PASS: evidenced correct; NOT_OBSERVABLE: evidence unavailable. |

## Decision and action

| Term or label | Meaning in this contribution |
|---|---|
| Gate / trace / disposition | An observable acceptance condition / the record of what happened / a proposed next procedural step. None is by itself evidence that the resulting operational action was authorized or completed. |
| Qualification / requalification | Establishing whether the declared evidence, scope, authority and timing suffice for this receiving decision / checking the affected conditions again after change or uncertainty. These words prescribe no architecture. |
| EXECUTE / REASSESS (also REQUALIFY) / DENY / ESCALATE | Respectively proceed through an authorized owner; reopen the affected evidence; reject the evaluated action; refer to a legitimate owner. These are neutral trace labels, not a shared runtime API. |
| REQUEST_AUTHORITY_CHANGE / AuthorityChangeRequest | Preserve a supported proposal and ask the legitimate owner for missing authority. The request itself grants no authority. |
| CAN / KNOW / MAY / SHOULD / ACT | Technical reach; sufficient evidence; applicable permission; objective-relevant reason; actual action. One does not substitute for another. |
| Valid-continuity or positive control | A matched branch in which legitimate activity must remain possible. It prevents a deny-all pass; it is not an additional implementation route. |

## Scope and failure-position labels

| Term or label | Meaning in this contribution |
|---|---|
| U / observation window / residual | U is the bounded operational representation; the observation window selects what is actively considered for a particular decision and time. An unresolved item inside U differs from the open residual R_U beyond it. U and the active window are not interchangeable. A larger window is not automatically better. |
| Type 1 / Type 2; I1/I2/O1/O2 in S1 | Type 1: unresolved inquiry, review or HOLD exceeds useful capacity/time. Type 2: unsupported closure is treated as settled. I means within the declared evidence window; O means beyond it. These failure-position codes are distinct from AWS configuration names. |

**Scoring precedence.** The main protocol governs every profile. A partially reinforced baseline is a diagnostic failure, not proof of recurrence: first strengthen R1 and demonstrate its correction. Retain generic discovery, policy loading and adaptation during R2. Documentary expected outcomes are predictions to test, never measured product verdicts. Report gate result, actual action, legitimate-activity control, deadline and burden separately. Compression, compaction or a static scope mismatch can exercise case gates without demonstrating a material reference-context change; count a branch as an HR recurrence trial only when Annex R’s intervention conditions are independently met.


**Hypothesis identifiers:** HC and HS are the causal and functional-response hypotheses in [Annex H](HYPOTHESES.md). H1–H6 are the six research hypotheses, not technology configuration labels. HR is the corrected-baseline recurrence question in [Annex R](RECURRENCE_PROTOCOL.md). The two-by-two A–D causal trial conditions and HS component comparisons are experimental factors; they do not add a fourth technological walkthrough to R0/R1/R2.
