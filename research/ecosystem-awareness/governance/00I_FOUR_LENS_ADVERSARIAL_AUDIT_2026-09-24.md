# 00I — Four-Lens Adversarial Audit Record — 24 September 2026

| | |
|---|---|
| **Scope** | 00I Semantic TOCTOU case, AWS implementation trajectory, fixture skeletons, routing/readability and source claims |
| **Status** | Editorial/adversarial audit record · not independent validation · not execution evidence |
| **Reviewed sources** | 00I v0.4 Draft · 00I-A01 v0.2 Draft · Canonical Requirements · EA Principles · Requirements vNext · routers/workplan/visual guide · official AWS/PostgreSQL/Kubernetes/MITRE sources · GitHub/GitLab public postmortems |

> **Review-boundary note.** The four “auditors” below are four deliberately separate review lenses applied in this editorial pass. They are **not four independent external human reviewers**. Their purpose is to make disagreement surfaces and corrections explicit before W3 fixture admission.

## Audit A — EA / Requirements traceability

### Question

Does the winning quality route depend on requirements invented after seeing the scenario?

### Finding

**PASS with one clarification candidate.**

- Q0–Q5 have direct routes through the frozen S1–S14 / T1–T4 / H1–H6 system.
- Q6 check-to-act binding is strongly implied by S10/S14/T4/H5/H6 but benefits from explicit test wording.
- V11 regime/source/dependency drift remains inside S3/S10/S11/S14 → T1/T2/T4 → H5/H6, with S9/S12/S13 activated where composition/history is material.
- No S15/T5/H7 or new canonical KPI family is needed.

### Correction retained

CAND-R4 remains a **clarification candidate**, not a new requirement.

### Residual challenge

Execution may still show that Q6 can be fully operationalized without any future Requirements wording change. That outcome must remain admissible.

## Audit B — AWS / distributed-systems engineering

### Question

Is the “top-notch” peer technically credible, or does it win only because the document gives it hand-wavy atomicity?

### Initial finding — material defect

The prior description could be read as if a DynamoDB conditional/version write made the later RDS action atomic. It does not. DynamoDB can protect the broker/control record; an unrelated RDS API call can still race unless the architecture also controls writers and the check-to-act boundary.

### Correction

00I-A01 v0.2 now declares:

- application-level, not fictional native-RDS, `config_generation`;
- a **single-writer change broker** for all material `db-7` mutations in the defended test environment;
- short-lived `ExecutionLease`;
- human Patch B still originates with the DBA but is submitted through the same broker;
- direct bypass mutation is a separate failure branch, not part of the top-notch configuration;
- the worker verifies the live lease/basis before the RDS call.

### Source audit

Official AWS documentation supports the building blocks:

- Step Functions Wait/Task/Choice and AWS SDK service integrations;
- RDS pending modifications and reboot behavior;
- SSM `GetCalendarState` and multiple-calendar composition;
- Change Calendar EventBridge best-effort / timing boundary;
- DynamoDB conditional updates / optimistic version control.

### Residual challenge

The skeletons are not deploy-ready code. Concrete IAM/resource policies, Lambda/broker implementation and real RDS calls remain W3 work.

## Audit C — experimental design / falsification

### Question

Is the drift designed so the conventional peer must lose?

### Initial finding — high risk of strawman

A source-set change such as “Calendar B becomes applicable” can be trivial for a genuinely dynamic policy engine. Assuming AWS-I1 misses B would pre-decide the result.

### Correction

The implementation profile now uses a **progressive preregistered drift ladder**:

- D1 policy/source-set drift — easiest; strong dynamic peers may pass;
- D2 dependency drift;
- D3 causal/data drift;
- D4 freshness-regime drift;
- D5 adversarial relocation, admitted only after attacker/action boundaries are frozen.

The experiment stops or narrows the claim when a strong peer matches the EA route. It must not invent harder drift after observing results simply to create separation.

### Winner rule

- peer passes at equal/lower burden → no EA differential for that branch;
- peer detects but cannot recover in time while EA does → possible targeted-reentry differential;
- peer false-continues and EA correctly requalifies → support for the fixture hypothesis;
- both fail → no positive EA claim;
- EA wins only by blanket HOLD / excessive search → EA fails T4/H6;
- asymmetric oracle/API access → invalid comparison.

## Audit D — CEO / public readability

### Question

Can a non-specialist understand why the scenario matters without reading 600 lines of architecture?

### Initial finding

The technical story was sound but the reader encountered gate namespaces and product detail before a concise business interpretation. N0/N1/Q versus R0/R1/R2 could also look like two competing arm systems.

### Correction

00I v0.4 now begins with:

- business problem;
- what strong conventional engineering fixes;
- the harder regime-drift question;
- what EA is and is not being tested for;
- a fairness rule;
- a suggested executive reading path.

The case also explains:

> a valid maintenance order can become inappropriate before it is executed even though the signature on the order is still valid.

00I-A01 v0.2 adds a non-specialist technology map and a five-outcome adjudication table.

N0/N1/Q are now explicitly identified as **gate-behavior traces**; R0/R1/R2 are **implementation trajectories**.

## Public-reality / evidence audit

The scenario is fictional, but its mechanism is not represented as fictional technology behavior.

The current source boundary is:

- **MITRE CWE-367:** TOCTOU is a recognized weakness class.
- **AWS RDS:** modifications can be pending and applied later; Apply Immediately can also apply queued changes and may cause unexpected downtime; static parameter changes can require reboot.
- **PostgreSQL:** strong locks serialize many conflicting DDL operations; the case does not claim automatic simultaneous corruption.
- **Kubernetes:** `resourceVersion` / `409 Conflict` is a strong conventional example of stale-write protection and therefore a fair counterexample to any claim that version binding is uniquely EA.
- **GitHub 2018:** Orchestrator actions behaved as configured while the application tier could not support the resulting topology; a 43-second partition led to 24h11m degradation and inconsistent/out-of-date information.
- **GitLab 2017:** replication recovery involved `max_wal_senders`, restart failure due to the pre-existing `max_connections` state, and further configuration changes. The later destructive deletion was human error and is not presented as the 00I mechanism.

No cited incident is labelled as an exact historical instance of the synthetic Northwind sequence.

## Mechanical audit

Completed:

- JSON parsing for I0/I1/I2 ASL skeletons, D1 fixture and trace contract;
- state-transition reference check: no missing `Next`, `Default` or `Choice` targets;
- relative-link audit for 00I v0.4 and 00I-A01 v0.2;
- public-router / canonical README / Requirements vNext / Workplan version reconciliation;
- Visual Guide updated for 00I v0.4 and 00I-A01 v0.2.

## Current disposition

**Suitable for continued W3 preparation, not yet for an empirical claim.**

What is now strong enough:

- public failure story;
- requirements/gate traceability;
- strong conventional peer;
- adaptive drift hypothesis;
- no-predetermined-winner rules;
- public source corroboration;
- inspectable implementation skeletons.

What remains before execution:

1. concrete Lambda/broker code;
2. source adapters and policy/dependency manifest owner;
3. IAM/resource-policy freeze proving the single-writer assumption;
4. numerical freshness/lease/response thresholds;
5. deterministic oracle;
6. DBC-R# mapping;
7. preregistration commit;
8. continuity admission execution;
9. strong-peer defender review by a person/team not authoring the EA arm;
10. Stage 0 trace and only then comparative execution.

## Audit conclusion

The reviewed design is stronger after the audit because it no longer relies on either of the two easiest shortcuts:

1. **weak peer shortcut:** the top-notch conventional implementation is expected to pass the base case;
2. **magic adaptation shortcut:** the EA arm may react only to observable legitimate changes and gets no oracle or privileged source.

The remaining scientific question is therefore substantive:

> **When a previously sufficient control model becomes stale because the governing source/dependency/freshness regime changes, can the system requalify the minimum necessary decision boundary before acting — and can it do so with less false continuation or lower recovery burden than an equally resourced strong conventional peer?**
