# Visual Guide — Structural / Ecosystem Awareness Corpus

> **Navigation aid — not a normative source.** This page visualizes the current public reading routes and ownership boundaries of the corpus as of 24 September 2026. The linked source documents remain authoritative for semantics, status, evidence and scope. A diagram never upgrades a working proposal, frozen source, application package or unexecuted test into validation.

## 1. How the programme accumulates

Use this map when the repository feels like many parallel documents. The programme is cumulative: later architecture and test work builds on earlier explanatory, foundational and engineering layers without deleting them.

```mermaid
flowchart TB
    FN["Field Notes / Research Series<br/>Cost of Clarity · Human Intelligence Debt<br/>Attribution Gap · Informational Friction · Regime Awareness"]
    ENG["Field Practice / Engineering<br/>Phylons · xSeil · Mobility OS"]
    F["01 Foundation<br/>bounded representation · open residual"]
    P["02 Principles & Control Matrix<br/>epistemic handling rules"]
    R["00 Requirements<br/>S1–S14 · T1–T4 · H1–H6 · KPIs"]
    A["Architecture<br/>Topology · 03 Functions · 04 General Interfaces"]
    I["Integration annexes<br/>01B / 01C / 01D · 01H / 01I / 01J"]
    V["Validation & reference scenarios<br/>UC-EA-01…04 · 00E · 00F · 00G v0.4 · 00H v0.5 · 00I v0.5"]
    B["Benchmark & evidence<br/>00D · B0–B3 · EA-H1–EA-H4"]
    T["Test programme<br/>A01 · A03 · fixtures · pre-registration"]
    EP["Ecosystem Positioning<br/>EA + RA + MSCA"]
    APP["Application packages<br/>FG-TIDA · standards/source cases"]

    FN --> F
    ENG --> F
    F --> P --> R --> A --> I --> V --> B --> T
    I --> EP
    V --> EP
    B --> EP
    EP --> APP
```

**Read:** [Structural Awareness root](../../README.md) → [EA canonical corpus](./baseline/README.md).

---

## 2. Architectural ownership at a glance

Ecosystem Positioning composes three technical gates. It does not absorb their semantic ownership, and governance remains outside the technical components.

```mermaid
flowchart TB
    SA["Structural Awareness Programme"]
    EP["Ecosystem Positioning<br/>participant-local situational core"]
    EA["Ecosystem Awareness<br/>decision-scoped epistemic qualification"]
    RA["Regime Awareness<br/>continued validity of the operating frame"]
    MSCA["MSCA<br/>control sufficiency · Cartography · Operation/Repositioning"]
    SIG["01J Ecosystem Signalling<br/>qualified boundary crossing"]
    ACC["01I ACC<br/>admissible participation conditions"]
    GOV["Human / institutional governance<br/>authority · objectives · final decision rights"]

    SA --> EP
    EP --> EA
    EP --> RA
    EP --> MSCA
    SIG -. "ReceivedSignals / qualified profiles" .-> EA
    SIG -. "qualified signals" .-> RA
    SIG -. "repositioning / authority profiles" .-> MSCA
    ACC -. "normative constraints" .-> MSCA
    MSCA -. "RepositionIntent / request" .-> GOV
    GOV -. "AuthorityResponse / decision" .-> MSCA
```

**Ownership rule:** signal ≠ command; opportunity ≠ permission; architecture ≠ authority.

**Read:** [Ecosystem Positioning](../../architectural-contributions/ecosystem-positioning/README.md) · [EA](./README.md) · [RA](../regime-awareness/README.md) · [MSCA](../../standards/minimum-sufficient-control/README.md).

---

## 3. Current positioning cycle

This is the current cross-corpus operating order. It shows where the major owners sit; it is not a mandatory transport protocol.

```mermaid
flowchart LR
    OBS["Participant action / observation"]
    SIG["ReceivedSignals_i<br/>01J"]
    EA["Π_EA,i(d,t)<br/>EA / 01H"]
    CART["Cart_i / Δ_Cart,i<br/>MSCA 03"]
    RA["Δ_RA<br/>Regime Awareness / 01C"]
    OP["Role_effective drift<br/>Type 0/1/2 · P1/P2/P3<br/>MSCA 04"]
    GR["Objective-conditioned gradient<br/>rank candidate transitions"]
    GATE["Π_RP · ACC / lineage / authority gate<br/>MSCA 04"]
    OWNER["Authorized owner acts"]
    EFFECT["Execution / effects"]

    OBS --> EA
    SIG --> EA
    EA --> CART
    SIG --> CART
    CART --> RA
    EA --> RA
    SIG --> RA
    RA --> OP --> GR --> GATE
    GATE -. "request / RepositionIntent" .-> OWNER
    OWNER --> EFFECT --> OBS
    RA -. "bounded requalification request" .-> CART
```

**Read:** [EP working process](../../architectural-contributions/ecosystem-positioning/README.md#working-process) · [MSCA Composition & Control](../../standards/minimum-sufficient-control/03_MSCA_ECOSYSTEM_COMPOSITION_AND_CONTROL.md) · [MSCA Operation & Repositioning](../../standards/minimum-sufficient-control/04_CANONICAL_MSCA_OPERATION_AND_REPOSITIONING.md).

---

## 4. Requirements → evidence → execution

Use this map to distinguish **requirements**, **scenario design**, **test design** and **actual evidence**.

```mermaid
flowchart LR
    F["01 Foundation"]
    P["02 Principles"]
    R["00 Requirements<br/>S1–S14 / T1–T4 / H1–H6 / KPI"]
    C["Case / scenario<br/>UC-EA · 00E · 00F · 00G · 00H · 00I"]
    Q["Quality gate / requirement route<br/>S# → T# → H# → KPI → disposition"]
    BM["00D benchmark<br/>B0–B3 · EA-H1–EA-H4"]
    TD["A01 test/oracle design"]
    PR["Pre-registration"]
    H["A03 / harness implementation"]
    S0["Stage 0<br/>deterministic verification"]
    S1["Stage 1<br/>observable comparative execution"]
    S2["Stage 2<br/>external validation"]

    F --> P --> R --> C --> Q --> BM --> TD --> PR --> H --> S0 --> S1 --> S2
```

### Current maturity boundary

| Layer | Current state |
|---|---|
| Requirements / hypotheses / KPI protocol | **Defined and versioned** |
| 00K six-principle symbolic ablation layer | **Serious hardening complete: 346 core + 33 supplemental = 379/379 CI-reproduced symbolic tests; P1/P3/P6 retain explicit falsified naive fixtures; P4 narrowed to minimal authority qualification** |
| 00K formal independence layer | **A16 corpus-grounded relative-independence + A20 shared-substrate mathematical independence; A18 retained as lightweight sketch; model-relative, not universal cardinality minimality** |
| 00E scenario / quality plan | **Documented** |
| 00F v0.2 · [Freeze Edition](./baseline/00F_FAILURE_MODE_SMART_CITY_MOBILITY_SYSTEMIC_DIVERGENCE_v0.2_FREEZE_EDITION.md) | **“The City That Stopped Safely” — Q0–Q5 + N0/N1/Q + V0–V9 + R0/R1/R2, FIWARE/AWS profiles, source audit and zero-loss public edition; comparative execution pending** |
| 00G v0.4 | **Canonical working reference; paired false/genuine control + DBC gate namespace + KPI instrumentation + integrated OpenAI G0/G1/G2 implementation trajectories; unexecuted; 00D/W3 execution pending** |
| 00H v0.5 Draft | **Latest working candidate; "The Quiet Four Thousand" primary no-attacker case pairs helpful overreach with discovery-without-preservation; "The Refund Campaign Nobody Approved" adds the outsourced-Dispatcher V19/V20 hardening with valid leaves under an unauthorized common root; EA0 baseline expected to pass both base paths and U/G/I; W3 execution pending** |
| 00I v0.5 Draft · [Freeze Edition](./baseline/00I_FAILURE_MODE_SEMANTIC_TOCTOU_v0.5_FREEZE_EDITION.md) | **Latest working candidate; “The Patch That Undid the Fix” — OOTB → top-notch → same frozen top-notch under observable regime/source/dependency drift; zero-loss public Freeze Edition, AWS profile and inspectable skeletons published; W3 execution pending** |
| B0–B3 comparison contract | **Defined** |
| A01 test/oracle construction | **Designed** |
| A03 Q1a harness design | **Designed** |
| RS-00E-Q1a pre-registration | **Published** |
| Stage-0 descriptive execution | **Pending** |
| Observable B0–B3 comparative execution | **Pending** |
| Independent validation / replication | **Pending** |

**Coverage warning:** A01/A03 are selected fixture work, not an exhaustive testbed for all S1–S14 or all later positioning layers.

---

## 5. Reference scenarios and implementation profiles

The current technology/strong-peer profiles are not generic product reviews. They are scenario-specific implementation-trajectory analyses: four synchronized 00E/00F successors, the OpenAI trajectory integrated inside canonical 00G §17, two deliberately different 00H peers, and one AWS Step Functions/RDS trajectory for 00I.

```mermaid
flowchart TB
    E["00E<br/>100 Million Tokens"]
    F["00F v0.2<br/>The City That Stopped Safely"]
    G["00G<br/>False-Context Convergence"]
    H00["00H<br/>Batch Opportunity Beyond Authority"]
    I00["00I<br/>Semantic TOCTOU"]
    M["00E-A01<br/>Microsoft Agent 365"]
    L["00E-A02<br/>LangGraph / LangSmith"]
    FW["00F-A01<br/>FIWARE NGSI-LD / Orion-LD"]
    AWS["00F-A02<br/>AWS IoT TwinMaker / IoT Core"]
    OAI["00G §17<br/>Integrated OpenAI trajectories"]
    CLAUDE["00H-A01 v0.4<br/>Claude Agent SDK"]
    STRIPE["00H-A02 v0.4<br/>Stripe Radar + merchant authorization"]
    AWSI["00I-A01 v0.2<br/>AWS Step Functions / RDS"]
    FUT["Future explicit benchmark/profile work"]

    E --> M
    E --> L
    F --> FW
    F --> AWS
    G --> OAI
    H00 --> CLAUDE
    H00 --> STRIPE
    I00 --> AWSI
    G -. "additional profiles / matched execution pending" .-> FUT
    H00 -. "Stage-0 / matched execution pending" .-> FUT
    I00 -. "W3 fixture admission / matched execution pending" .-> FUT
```

**Read:** [00E](./baseline/00E_FAILURE_MODES_100M_TOKEN_COMPOUNDING_v0.1.md) · [00F](./baseline/00F_FAILURE_MODE_SMART_CITY_MOBILITY_SYSTEMIC_DIVERGENCE_v0.2_DRAFT.md) · [00F Freeze Edition](./baseline/00F_FAILURE_MODE_SMART_CITY_MOBILITY_SYSTEMIC_DIVERGENCE_v0.2_FREEZE_EDITION.md) · [00G](./baseline/00G_FAILURE_MODE_COLLECTIVE_FALSE_CONTEXT_CONVERGENCE_v0.4.md) · [00H](./baseline/00H_FAILURE_MODE_BATCH_OPPORTUNITY_BEYOND_AUTHORITY_v0.5_DRAFT.md) · [00H-A01 Claude](./baseline/00H_A01_CLAUDE_AGENT_SDK_IMPLEMENTATION_PROFILE_v0.4_DRAFT.md) · [00H-A02 Stripe](./baseline/00H_A02_STRIPE_RADAR_IMPLEMENTATION_PROFILE_v0.4_DRAFT.md) · [00I technical](./baseline/00I_FAILURE_MODE_SEMANTIC_TOCTOU_v0.5_DRAFT.md) · [00I Freeze Edition](./baseline/00I_FAILURE_MODE_SEMANTIC_TOCTOU_v0.5_FREEZE_EDITION.md) · [00I-A01 AWS](./baseline/00I_A01_AWS_STEP_FUNCTIONS_RDS_IMPLEMENTATION_PROFILE_v0.2_DRAFT.md).

---

## 6. Cases, validation profiles and FG-TIDA-specific tests

This map prevents three different artifact classes from being confused.

```mermaid
flowchart TB
    DAOS["DAOS parent case<br/>T0–T2 + Annexes I–V"]
    MCASE["EA ↔ DAOS model-case interface"]
    MASTER["DAOS → EA masterclass"]
    U1["UC-EA-01<br/>frame requalification"]
    U2["UC-EA-02<br/>bounded determination"]
    U3["UC-EA-03<br/>effective human oversight"]
    U4["UC-EA-04<br/>scope-indexed composition"]
    ITP["EA-ITP-01<br/>FG-TIDA-specific interoperability test"]
    RS["00E / 00F / 00G / 00H / 00I<br/>reference failure scenarios"]

    DAOS --> MCASE --> MASTER
    DAOS --> U1
    DAOS --> U2
    DAOS --> U3
    DAOS --> U4
    MASTER -. "engineering/test guide" .-> U1
    MASTER -. "engineering/test guide" .-> U2
    MASTER -. "engineering/test guide" .-> U3
    MASTER -. "engineering/test guide" .-> U4
    DAOS -. "Theme-specific application context" .-> ITP
    RS -. "separate scenario family" .-> U1
```

**Interpretation:**
- UC-EA-01…04 are **general EA Architecture-Validation Profiles**, not four FG-TIDA submissions.
- EA-ITP-01 is a **separate FG-TIDA-specific interoperability test**.
- 00E/00F/00G/00H/00I are **reference failure scenarios**, not DAOS annexes and not validation results; 00G–00I remain additive/unexecuted where their local status says so.

**Read:** [Validation reading note](./baseline/VALIDATION_PROFILE_READING_NOTE.md) · [FG-TIDA cases](./fg-tida/cases/README.md) · [Portfolio coverage map](./baseline/USE_CASE_PORTFOLIO_REQUIREMENTS_COVERAGE_MAP_v0.1.md).

---

## 7. General architecture → FG-TIDA application

Use this whenever 04, 05 and 05A are easy to confuse.

```mermaid
flowchart LR
    G04["04 General EA Interfaces<br/>programme-independent"]
    I05["05 Ideal FG-TIDA projection<br/>candidate cross-Theme contracts"]
    C05A["05A Current-State Bridge<br/>dated public-source-constrained mapping"]
    SPEC["Specification preparation<br/>v0.3 draft"]
    CHAR["Charter / WG preparation"]
    CASES["FG-TIDA cases"]
    TESTS["FG-TIDA tests"]
    PROV["FG-TIDA provenance"]
    LATER["Later general architecture<br/>01H / 01I / 01J · 00G · Gradient · MSCA Op"]
    REV["Future versioned reconciliation"]

    G04 --> I05 --> C05A
    C05A --> SPEC
    C05A --> CHAR
    C05A --> CASES
    C05A --> TESTS
    C05A --> PROV
    LATER -. "does not auto-update 05/05A" .-> REV
    REV -. "explicit dated revision only" .-> SPEC
```

**Rule:** 05A may be narrower than 05. Later general architecture does not become an FG-TIDA requirement until a dated application revision and the relevant external-owner process support it.

**Read:** [FG-TIDA package](./fg-tida/README.md) · [Interface projection](./fg-tida/interfaces/README.md) · [Specification preparation](./fg-tida/specifications/README.md). The current v0.3 preparation route also links the Decision Boundary / cross-Theme conformance profile under FG-TIDA-specific tests.

---

## 8. Which document should I open?

| Reader question | Start here | Then continue to |
|---|---|---|
| Why can the system never treat its represented world as complete? | [01 Foundational Theory](./baseline/01_FOUNDATIONAL_THEORY_v0.5_INTEGRATED.md) | 02 Principles → Topology |
| What must any candidate solution demonstrate? | [00 Requirements](./baseline/00_CANONICAL_REQUIREMENTS_CHALLENGES_SUFFICIENCY_HYPOTHESES_KPIS.md) | 00D benchmark / coverage map |
| How does EA actually work? | [Topology](./baseline/00_CANONICAL_ARCHITECTURE_TOPOLOGY.md) | 03 Functional Architecture → 04 Interfaces |
| Where can a strong system still fail? | [00E](./baseline/00E_FAILURE_MODES_100M_TOKEN_COMPOUNDING_v0.1.md) / [00F](./baseline/00F_FAILURE_MODE_SMART_CITY_MOBILITY_SYSTEMIC_DIVERGENCE_v0.2_DRAFT.md) / [00G](./baseline/00G_FAILURE_MODE_COLLECTIVE_FALSE_CONTEXT_CONVERGENCE_v0.4.md) / [00H](./baseline/00H_FAILURE_MODE_BATCH_OPPORTUNITY_BEYOND_AUTHORITY_v0.5_DRAFT.md) / [00I](./baseline/00I_FAILURE_MODE_SEMANTIC_TOCTOU_v0.5_DRAFT.md) | product profiles / benchmark |
| How is the claim falsified fairly? | [00D](./baseline/00D_CANONICAL_ARCHITECTURE_BENCHMARK_AND_REFERENCE_SCENARIO_EVIDENCE_v0.2.md) | A01 → A03 → fixture/pre-registration |
| How are Foundation → P1–P6 → S1–S14 justified, closed and tested? | [02A semantic derivation](./baseline/02A_FOUNDATION_TO_OPERATIONAL_PRINCIPLE_DERIVATION_PROOF_v0.1.md) · [02B Foundation syntax closure](./baseline/02B_FOUNDATIONAL_SYNTAX_CLOSURE_AND_P1_P6_NORMAL_FORM_PROOF_v0.1.md) · [A19 P↔S semantic traceability](./baseline/00K_A19_PRINCIPLE_REQUIREMENT_TRACEABILITY_AND_CONSERVATION_PROOF_v0.1.md) · [A21 requirement normal-form closure](./baseline/00K_A21_REQUIREMENT_BASIS_CLOSURE_AND_RELATIVE_COMPLETENESS_PROOF_v0.1.md) · [A24 P↔S information refinement](./baseline/00K_A24_PRINCIPLE_REQUIREMENT_INFORMATION_GAIN_AND_NON_EQUIVALENCE_v0.1.md) · [A25 failure case-family extensibility](./baseline/00K_A25_FAILURE_CASE_STUDY_EXTENSIBILITY_AND_CONFORMANCE_TRANSFER_v0.1.md) | [A15 Testbook](./baseline/00K_A15_COMPLETE_SIX_PRINCIPLE_ABLATION_TESTBOOK_v0.1.md) → [A16 corpus-grounded proof](./baseline/00K_A16_FORMAL_RELATIVE_INDEPENDENCE_PROOF_P1_P6_v0.1.md) → [A20 shared-substrate proof](./baseline/00K_A20_SHARED_SUBSTRATE_MATHEMATICAL_INDEPENDENCE_P1_P6_v0.1.md) → [A22 Boolean diagnostic minimality](./baseline/00K_A22_FULL_CUBE_BOOLEAN_DIAGNOSTIC_MINIMALITY_v0.1.md) → [A17 map](./baseline/00K_A17_DOCUMENTATION_REPRODUCIBILITY_AND_PROOF_MAP_v0.1.md) |
| Which cases exist and what do they cover? | [Use-Case Portfolio Coverage Map](./baseline/USE_CASE_PORTFOLIO_REQUIREMENTS_COVERAGE_MAP_v0.1.md) | Validation reading note / FG-TIDA cases |
| How does EA connect to regime change? | [RA README](../regime-awareness/README.md) | 01C → 01D |
| How does control sufficiency and repositioning work? | [MSCA README](../../standards/minimum-sufficient-control/README.md) | MSCA 00 → 03 → 02 → 04 |
| How are all three gates composed? | [Ecosystem Positioning README](../../architectural-contributions/ecosystem-positioning/README.md) | Gradient Law / EA / RA / MSCA |
| What is ideal FG-TIDA versus currently defensible FG-TIDA? | [FG-TIDA interface projection](./fg-tida/interfaces/README.md) | 05 ideal → 05A current |
| Which older wording was preserved? | [Preserved Public Snapshots](../../governance/preserved-public-snapshots/README.md) | Deep / cumulative audits |

---

## 9. Status-reading rule

A visual route does not override document status:

- **Controlled / frozen** — preserved source; no silent semantic edits.
- **Canonical working** — current reader/working semantics; versioned and evolvable.
- **Integrated working successor** — current integration that does not erase the freeze.
- **Additive annex** — useful extension, not automatically core.
- **Application package** — programme-specific projection.
- **Preserved predecessor** — retained for lineage, not current semantics.

When in doubt, follow the status declaration in the source document and cite the exact Git commit read.

---

## 10. Known future visual/test extensions

The visual guide intentionally leaves these as open work rather than pretending they are already complete:

- Requirements-vNext **review completed**: later EP concepts map to the current S1–S14 / T1–T4 / H1–H6 / KPI basis; two non-canonical clarification candidates remain;
- benchmark extension beyond EA-H1–EA-H4;
- additional fixture/testbed coverage, including S7/S8 and later positioning layers;
- future versioned reconciliation of later architecture into FG-TIDA preparation material;
- final static SVG/PNG assets for presentations after the current Markdown/Mermaid semantics stabilize.

---

## 11. Active workfront — what is being worked on next

This map is a reader shortcut to the [Living Workplan](./WORKPLAN.md). It shows dependencies, not a rigid waterfall.

```mermaid
flowchart TB
    W1["W1 Requirements review<br/>COMPLETED · no canonical change"]
    W2["W2 Benchmark vNext<br/>Extend beyond EA-H1–EA-H4"]
    W3["W3 Testbed coverage vNext<br/>S7/S8 · 00G/00H/00I · ACC · gradient · drift/repositioning"]
    W4["W4 FG-TIDA Specification vNext<br/>incorporate / inform / exclude explicitly"]

    C1["C1 Controlled parity<br/>Drive revision ↔ Git SHA"]
    C2["C2 Empirical execution<br/>Stage 0 → Stage 1 → Stage 2"]
    C3["C3 Product evidence refresh<br/>dated 2+2 profiles"]
    C4["C4 Presentation / Release<br/>deck · GitHub Release · DOI"]
    C5["C5 Coherence pass<br/>README · Visual Guide · coverage map"]

    W1 -. "traceability gate closed" .-> W2
    W1 -. "existing requirement basis" .-> W3
    W1 -. "requirements disposition" .-> W4
    W2 --> W3
    W2 -. "evidence scope" .-> W4
    W3 -. "test / conformance evidence" .-> W4

    C1 -. "source integrity" .-> W4
    C2 --> W2
    C2 --> W3
    C3 -. "implementation evidence" .-> W2

    W2 --> C5
    W3 --> C5
    W4 --> C5
    C5 -. "stable reader state" .-> C4
```

**Current strategic front:** W2 Benchmark vNext, now using the completed W1 mapping.  
**Current first empirical milestone:** RS-00E-Q1a Stage-0 descriptive execution under operative pre-registration v0.5.

**Read:** [Living Workplan](./WORKPLAN.md).

---

## 12. How a new idea enters the corpus without deleting the past

Use this change-control map when a new concept, requirement, scenario or interface appears.

```mermaid
flowchart TD
    N["New concept / evidence / case"]
    G["Gap analysis<br/>What exact problem is not already covered?"]
    O{"Existing semantic owner?"}
    M{"Fits current requirement / interface / test route<br/>without semantic distortion?"}
    C["Clarify / map in current working document<br/>with explicit traceability"]
    S["Create versioned successor or additive annex<br/>preserve predecessor"]
    T{"Needs empirical / conformance claim?"}
    D["Design comparator / fixture / falsifier<br/>pre-register where applicable"]
    E["Execute and record evidence<br/>do not promote design to result"]
    A{"Programme-specific application?"}
    P["Project into application package<br/>e.g. 05/05A/FG-TIDA<br/>without redefining general architecture"]
    R["Update routers / workplan / visual guide / coverage map"]
    H["Preserve historical public wording<br/>snapshot / predecessor / freeze"]

    N --> G --> O
    O -->|Yes| M
    O -->|No| S
    M -->|Yes| C
    M -->|No| S
    C --> T
    S --> H
    S --> T
    T -->|Yes| D --> E --> A
    T -->|No| A
    A -->|Yes| P --> R
    A -->|No| R
    C --> R
    H --> R
```

**Conservation rule:** a later clarification may change the current route, but it does not erase what an earlier dated or frozen document actually said.

**Read:** [Living Workplan](./WORKPLAN.md) · [Preserved Public Snapshots](../../governance/preserved-public-snapshots/README.md) · [Canonical Corpus Manifest](./baseline/CANONICAL_CORPUS_MANIFEST.md).

