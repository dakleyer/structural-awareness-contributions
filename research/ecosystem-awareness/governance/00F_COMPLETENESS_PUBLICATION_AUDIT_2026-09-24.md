# 00F — Smart-City Mobility Divergence Completeness & Publication Audit — 24 September 2026

| | |
|---|---|
| **Scenario** | [00F v0.2 — The City That Stopped Safely](../baseline/00F_FAILURE_MODE_SMART_CITY_MOBILITY_SYSTEMIC_DIVERGENCE_v0.2_DRAFT.md) |
| **Public edition** | [00F v0.2 Freeze Edition](../baseline/00F_FAILURE_MODE_SMART_CITY_MOBILITY_SYSTEMIC_DIVERGENCE_v0.2_FREEZE_EDITION.md) |
| **Technology profiles** | [FIWARE / Orion-LD](../baseline/00F_A01_FIWARE_NGSI_LD_IMPLEMENTATION_PROFILE_v0.2_DRAFT.md) · [AWS IoT TwinMaker / IoT Core](../baseline/00F_A02_AWS_IOT_TWINMAKER_CORE_IMPLEMENTATION_PROFILE_v0.2_DRAFT.md) |
| **Status** | Editorial / architecture / evidence audit · not independent validation or execution evidence |

## 1. Completeness finding

**PASS for pre-execution publication completeness.**

00F v0.2 now contains, explicitly:

- public reader story and executive paradox;
- actor/local-window model and shared decision scope;
- six-stage failure development;
- Q0–Q5 gate register and deterministic logic;
- original Route N / Route Q pair;
- N0 capability-absent / N1 bypass-or-late / Q conforming evidence routes;
- V0–V9 continuity, divergence, false-convergence, hidden-dependency, timestamp, human-capacity, oscillation, residual-coverage, regime-drift and response-margin variants;
- R0 standard / R1 top-notch / R2 frozen-top-notch-under-drift comparison;
- scenario-local hypotheses and decisive falsifiers;
- technology-neutral public corroboration with explicit “does not establish” boundaries;
- two maintained strong technology profiles;
- product-annex boundary and status limitations.

No new S15/T5/H7 or canonical KPI family is required by this pass.

## 2. Architecture / scientific-fairness audit

The most important correction relative to v0.1 is that “failure route” no longer means one undifferentiated weak comparator.

- **N0** distinguishes absence of a systemic composition capability.
- **N1** distinguishes a real control that is bypassed, incomplete or late.
- **R1 top-notch** must close valid continuity and known A/B conflict branches before adaptive claims are scored.
- **R2-peer** is allowed to adapt generically under V8; if it matches or beats R2-EA at equal/lower burden, there is no demonstrated EA differential.
- V0 prevents blanket HOLD/containment from winning.

This makes 00F comparable in scientific discipline to the later 00G–00I family without rewriting its original event.

## 3. External-source verification

The external evidence table was rechecked against official/public sources.

### NERC 2003 blackout

The NERC final report documents FirstEnergy's alarm-processor failure and loss of a major situational-awareness function; operators did not receive further alarms and relied heavily on that processor. This supports the 00F neighboring mechanism “signals/system partially present while shared situational awareness is not effectively re-established.” It does not establish a mobility analogue.

### CFTC / SEC Flash Crash

The official CFTC material describes a large automated sell program, cross-market propagation and the interrelatedness of markets amplifying the disruption. This supports the composition/system-interaction analogy only.

### SEC Knight Capital

The SEC public enforcement material confirms 212 customer orders leading to more than four million market orders/executions, hundreds of millions of shares and a loss above USD 460 million after deployment/control failures. The 00F table now points to the reader-friendly SEC public page rather than requiring the PDF order as the primary link.

### NTSB Tempe

The NTSB investigation page confirms ineffective operator oversight, automation complacency and inadequate safety-risk assessment as contributing factors. 00F uses this only for finite-human-oversight pressure; it is not presented as multi-actor systemic divergence.

### NIST digital-twin credibility

NIST's 2022 publication states that digital-twin decision support requires verification, validation and uncertainty quantification across the twin lifecycle. NISTIR 8620 (published 21 Jul 2026; updated 31 Aug 2026) identifies persistent interoperability, VVUQ, cybersecurity and trustworthiness challenges. These support the distinction between “integrated/current model” and “sufficiently credible decision basis.”

## 4. Named-technology verification

### FIWARE / Orion-LD

- Orion-LD release **1.12.0** is publicly listed as released **28 Jan 2026**.
- The Orion-LD repository explicitly states that its compliance position is not equivalent to full conformance with the latest NGSI-LD specification.
- ETSI **GS CIM 009 V1.9.1** was published **2 Jul 2025**.
- The profile correctly separates the ETSI standard version from Orion-LD's implementation/conformance boundary.

### AWS IoT TwinMaker / IoT Core

- AWS IoT TwinMaker's API Reference states the document was last published **14 Sep 2026**.
- The live AWS guide describes TwinMaker as an operational digital-twin service and carries an explicit warning that it is not intended for hazardous/critical systems that could cause serious injury/death/property/environmental damage; collected data should be evaluated for accuracy and TwinMaker is not a substitute for human safety monitoring.
- The 00F AWS profile correctly keeps physical safety actuation outside TwinMaker and treats the service as a representation/decision-support substrate.

## 5. Reader / visual audit

The v0.2 source adds five technical/public Mermaid views. The Freeze Edition adds three publication-layer visuals, for **eight total**:

1. four postures competing for Central Bridge;
2. local safety versus resource/mission failure;
3. Q0–Q5 gate flow;
4. R0/R1/R2 comparison;
5. public evidence-to-fixture map;
6. five-minute incident timeline;
7. FIWARE/AWS fair-comparison map;
8. evidence-versus-claim boundary.

The premium public title is:

> **Smart-City Mobility Chaos — The City That Stopped Safely**

The hook remains technically faithful:

> **Every vehicle can avoid a collision and the city can still fail.**

## 6. Remaining boundary before execution

Publication completeness is not W3 admission. Before empirical execution, 00F still needs:

- an admitted machine-readable fixture/oracle;
- concrete threshold values for freshness/materiality/yield/margin;
- named R1 defender configurations for FIWARE and AWS;
- exact R2 drift injection contract;
- trace schema and DBC/benchmark mapping as applicable;
- continuity admission execution;
- comparative run and independent replication.

## Conclusion

00F is now complete enough to circulate as a reference failure scenario and quality-plan design. Its strongest feature is the paradox it exposes without requiring an attacker or a failed safety controller:

> **local safety can succeed while the shared mobility mission fails.**

The remaining work is experimental, not narrative repair.
