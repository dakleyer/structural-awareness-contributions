README — Ecosystem Awareness Validation Profiles — Maintenance Freeze — 2026-09-10

&nbsp;

STATUS

Maintenance-frozen internal validation release. This release is a controlled successor to the earlier 2026-09-10 Frozen set. It applies only the six changes authorized in the Post-Freeze Minimal Maintenance Change Plan. No public FG-TIDA/GitHub artifact and no canonical architecture baseline document is modified by this maintenance release.

&nbsp;

CONTROLLING RULE

The earlier Frozen release remains preserved as historical evidence. This maintenance release supersedes only UC-EA-02, UC-EA-03 and UC-EA-04. UC-EA-01, the Validation Profile Family, EA-ITP-01 and the canonical/release baseline remain unchanged.

&nbsp;

CURRENT VALIDATION SET

&nbsp;

UC-EA-01 — Architecture-Validation Profile — Action-time Operating-Frame Requalification under Context Change — v0.3 — Frozen (unchanged)

Drive ID: 19k4fY-zu3IoRmsSuUyS0xgjqX7NhvvgoTAeZLN3ijI8

revisionId: ANLCKQlStGsiIpmk6-chrWqsaxd3heaQcGZspYjcP10UC\_L5hNl3UZT29OUDfrVDkpMq8uWsVENoay4eVxFMhllpvAhiAowNGYIiNbxt5VM

&nbsp;

UC-EA-02 — Architecture-Validation Profile — Bounded Determination under Incomplete, Conflicting or Partially Scoped Evidence — v0.6 — Maintenance Freeze

Drive ID: 1\_a1edMjJx4ozTmMn9iT23j7zYjOcX7Fmln8Zn\_Tf8Qw

revisionId: ANLCKQkeMVo62XPP2Axp9ZxSRBsypcxAv3TdIkqqP7OXaqbyM9dTtLeQu8EAQ-tJTc3mdY-uSIxrW2O2tSTaK3PH7neOZ9iUW2YrYxj-Ewo

&nbsp;

UC-EA-03 — Architecture-Validation Profile — Human Oversight under Bounded Effective Capacity and Non-curative Approval — v0.4 — Maintenance Freeze

Drive ID: 1Mhv4mUIU-S5yifmH8G0UDRdf0ItXt1aEK4kn0kAG6uY

revisionId: ANLCKQmK5qAOIQMcyFyBWqL1mkURxZ7YmzDE8hdFqfwPeIMWOq9ko8bn-33qyKbuXotk8Mn7U6HPEGCs2giz9LMda2jTAif258tNERVWwYU

&nbsp;

UC-EA-04 — Architecture-Validation Profile — Scope-indexed Composition of Locally Valid Determinations — v0.5 — Maintenance Freeze

Drive ID: 1y8wRR89mAYSgkYvsMS2ljr7V5jV1P2My1fIkonGkv1Y

revisionId: ANLCKQmPMeDp4nBuz5k\_l-Rt8YcbR7iLnnpUnPFe3Q4YP9WXwzCYcWsmhde1DIDFOIRJbdDul3P0i3TAj9\_3ouacLPYK4\_\_\_zRZstMlX7Zk

&nbsp;

DAOS / Ecosystem Awareness — Validation Profile Family & Traceability — v0.5 — Frozen (unchanged)

Drive ID: 1qjCLvOp02Lgh9hVlJae\_GZTNImenMXboEJ3fJMsqmok

revisionId: ANLCKQlDApN1bmivf8mRoewf34APYZEFH6U44Q9WyNJ-cTjD4WZcd64jiRrMoPSEhuWWabKyKp00tcIN8bidf9YoGKJctn\_DWKaP46DGMdc

&nbsp;

EA-ITP-01 — EHD / Theme \#13 Cross-Implementation Interoperability Test — v0.1 — Frozen (unchanged)

Drive ID: 1OnBzCX0TP6mtxdLjn9\_OORq0UIOdl9I\_3vkVsmRW1XA

revisionId: ANLCKQm7X12ia2wKez3hdF9dTc9iB8tMcCWDWo\_PnAbfjc1uwEG5jVQLHiFxEeW6VN4x0zdrZFkZ9bHl4JDuaSij98Esh8DSn8l9dbR\_IOk

&nbsp;

BASELINE

The exact canonical/release baseline is inherited unchanged from FREEZE\_MANIFEST — Ecosystem Awareness Validation Profiles — 2026-09-10 (Drive ID 19OLmEG9CHdR1SfFk\_FqoKp-xMdJaiudXZWkU4zYQ1eg). No Foundation, Control Matrix, Functional Architecture, Functional Interfaces, Contracts or Benchmark document is changed in this maintenance release.

&nbsp;

AUTHORIZED CHANGES APPLIED

1\. UC-EA-02 R21 converted from an obligation on an external campaign into an evidence condition on the interoperability claim.

2\. UC-EA-04 R18 replaced by the same interoperability-claim rule used in UC-EA-02, with Stage 1 retained only as the preferred current fixture, not a normative dependency.

3\. UC-EA-03 lifecycle-consumption rule moved above the EA-output heading; wording unchanged.

4\. UC-EA-04 general composition rule moved before the operational/epistemic graph boundary; boundary wording preserved and given its own label.

5\. UC-EA-02 Branch K stale hedge \`candidate F2.APQ\` reduced to \`F2.APQ\`; no other Branch K semantics changed.

6\. UC-EA-02 lineage corrected in maintenance control artifacts only: the file named v0.4 is preserved as an administrative/versioned successor whose body remained substantively equivalent to v0.3. The substantive predecessor content for the v0.5 reconciliation is therefore v0.3. The v0.4 file is not edited, deleted or renamed.

&nbsp;

MECHANICAL VERIFICATION

The common interoperability requirement was verified by exact-text matching in both UC-EA-02 v0.6 and UC-EA-04 v0.5. \`candidate F2.APQ\` returns no exact-text match in UC-EA-02 v0.6. In UC-EA-03 v0.4, the lifecycle-consumption rule occurs before \`EA outputs to the oversight function may include:\`. In UC-EA-04 v0.5, the general composition rule occurs before the \`Operational / epistemic graph boundary\` label.

&nbsp;

LINEAGE NOTE — UC-EA-02 v0.4

The preserved Drive file titled \`UC-EA-02 ... v0.4\` is not repaired retroactively. Audit comparison found its body substantively equivalent to v0.3 and internally still carrying v0.3-era labeling. Future lineage reads should therefore treat v0.4 as an administrative/versioned step and v0.3 as the substantive predecessor content for the v0.5 reconciliation, while retaining the v0.4 Drive ID/revision as historical evidence.

&nbsp;

CARRY-FORWARD — TESTBED METHOD

An older UC-EA-02 fixture-design sentence stated that fixture sets should expose observation cost, capacity and decision sensitivity sufficiently to compare fixed-broad, fixed-narrow and adaptive policies. R14 preserves the normative comparison requirement, but that fixture-construction guidance is not restored here. Carry it forward into the future testbed-method artifact. EA-ITP-01 is deliberately unchanged by this maintenance release.

&nbsp;

NO-CHANGE DECISIONS

UC-EA-01 v0.3 unchanged. Family v0.5 unchanged. Historical status-label folding is documented rather than repaired. UC-EA-03 R8/Branch G remain aligned to Lei's implementation-neutral lifecycle. UC-EA-02's deleted fixture sentence is not restored. No architecture baseline document changes. No public GitHub/FG-TIDA changes.

&nbsp;