# Structural Awareness Programme

> **Publication-oriented repository — currently private and under editorial preparation; not a validated method, adopted standard or institutional position**

This repository organizes a connected body of work on how technical and institutional systems understand the structure on which their decisions depend, recognize when that understanding is incomplete or no longer valid, and respond with sufficient but bounded control.

The programme is hosted in the public research context of [Tegrity.AI](https://tegrity.ai/structural-awareness-program/), a circle of The Integral Management Society. Individual workstreams have different owners, evidence sets, institutional routes and validation requirements. Their connection must not be used to transfer validation from one workstream to another.

## Programme logic

```mermaid
flowchart TD
    C[Cost of Clarity<br/>pre-commitment structural conditions]
    B[Incomplete or fragile representation<br/>missing, tacit, contradictory or undeclared conditions]
    R[Regime Awareness<br/>continued validity during operation]
    D[Regime Change Detection<br/>observable departure from the current regime]
    M[Minimum Sufficient Control<br/>bounded observation, coordination and intervention]
    O[Observed outcomes and updated structural understanding]

    C -->|unresolved conditions can create| B
    B --> R
    R --> D
    D --> M
    M --> O
    O --> C
```

This is one important causal and operational path, not a claim that every regime change begins with poor initial clarity. External shocks and endogenous dynamics can invalidate even a well-specified representation.

## Repository map

| Area | Question | Repository entry | Current status |
|---|---|---|---|
| **Cost of Clarity** | Are the information, distinctions and authority required for commitment actually available? | [`applied-research/cost-of-clarity-rup/`](./applied-research/cost-of-clarity-rup/) | Applied-research project under an EIS Estonia RUP assessment route; no funding or approval claim |
| **Regime Awareness** | Does the context supporting a decision remain valid as the system operates? | [`research/regime-awareness/`](./research/regime-awareness/) | Public research direction and field-derived candidate framework |
| **Regime Change Detection** | Is observable behaviour departing from the regime against which current assumptions were established? | [`research/regime-awareness/regime-change-qava-uv.md`](./research/regime-awareness/regime-change-qava-uv.md) | Preliminary methodological review route with QAVA–Universitat de València; no validation or institutional endorsement claim |
| **Minimum Sufficient Control** | What minimum observation, coordination and intervention capacity can maintain or recover a declared objective? | [`standards/minimum-sufficient-control/`](./standards/minimum-sufficient-control/) | Standards-oriented research input; not an adopted ITU position or recommendation |

## How the workstreams connect

### 1. Before commitment — Cost of Clarity

The first problem is whether the system or organization has represented the conditions that matter before it commits resources or establishes a decision architecture. Missing, contradictory, tacit or institutionally undeclared conditions can create structural blindness at the outset.

### 2. During operation — Regime Awareness

Even a sound initial representation can become stale. Actors, data, constraints, objectives, capacities and available interventions change. Regime Awareness asks whether the evidence and context supporting present decisions remain valid.

### 3. Detection — Regime Change Detection

The quantitative subline asks how departure from the current observable regime can be detected under finite and incomplete observation, and how that signal should be compared with simpler baselines and negative cases.

### 4. Response — Minimum Sufficient Control

Detection does not imply response capacity. Minimum Sufficient Control asks what combination of observation, coordination, interoperability and intervention is sufficient to keep a declared objective within acceptable ranges without assuming maximum data collection or centralized control.

## Evidence discipline

- Field cases provide engineering provenance, not universal validation.
- A public working paper is inspectable research, not a proven method.
- A preliminary academic review does not imply institutional endorsement.
- A programme assessment route does not imply funding or approval.
- Participation in a standards discussion does not imply adoption by the standards body.
- Similar structural patterns across domains motivate testing; they do not prove transferability.

See [`governance/CLAIM_BOUNDARIES.md`](./governance/CLAIM_BOUNDARIES.md) for the current attribution and status boundaries.

## Public corpus

- [Structural Awareness Programme](https://tegrity.ai/structural-awareness-program/)
- [Regime Awareness in Adaptive Systems](https://tegrity.ai/series/regime-awareness-in-adaptive-systems/)
- [The Cost of Clarity](https://tegrity.ai/series/cost_of_clarity/)

## Public-ready submissions and contributions

The [`submissions/`](./submissions/) library preserves the relevant documents and public discussion contributions routed to UNECE WP.5, the UN CSTD Working Group on Data Governance at All Levels, ITU-T FG-AI4SSC and ITU-T FG-TIDA. Each folder records provenance, file hashes and the exact procedural status without implying adoption or endorsement.

## Repository status and licensing

This is the curated contribution repository for material intended for possible external release. It remains private until an explicit publication decision is made. No open-source or content licence has yet been selected. Unless and until a licence is added, no permission beyond GitHub's applicable platform terms should be inferred.

---

**Ivan Abril**  
Research architecture and programme coordination.

