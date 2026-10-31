# 00L — English translation trace, batch 01

**Date:** 31 October 2026  
**Scope:** language editions of 00L-A03, 00L-A02 and 00L-A01 only  
**Source:** the unchanged Spanish files at main commit `51fc686f45b6ef10c53b69f4c26d0e381b007ff8`  
**Status:** complete English drafts checked by the translating assistant; owner/source-review and merge remain separate. This is **not** independent external review, scientific validation, a new canonical edition or translation of the whole corpus.  
**Policy:** [agent-facing English-first translation instructions](../../../AGENTS.md) are repository-wide; the human-facing README has not been edited.

## Source-to-English document mapping

| Logical item | Original Spanish source | English language edition | Source Git blob | English Git blob |
|---|---|---|---|---|
| 00L-A03 | [Paper-trace template, Spanish](./00L_A03_PLANTILLA_TRAZA_PAPEL_v0.1.md) | [Complete English translation](./00L_A03_PAPER_TRACE_TEMPLATE_v0.1.en.md) | `145a04f1d9501c6020ff0efaaf7a99a73c3e806c` | `edcf400edc3f09c4ad3a45dac0122c22c00420d6` |
| 00L-A02 | [Fact and control sheets, Spanish](./00L_A02_FICHAS_HECHOS_CONTROLES_00E_00J_v0.1.md) | [Complete English translation](./00L_A02_COMMON_FACTS_AND_CONTROLS_00E_00J_v0.1.en.md) | `a2b396fe0ea77a3e3ed2c380fd5aaf23c9f4f358` | `d3825783b5add72b08ebb761d9f8b64b34e998df` |
| 00L-A01 | [Nine-profile source inventory, Spanish](./00L_A01_INVENTARIO_FUENTES_NUEVE_PERFILES_v0.1.md) | [Complete English translation](./00L_A01_NINE_PROFILE_SOURCE_CLAIMS_INVENTORY_v0.1.en.md) | `aee756269b119b4253e0fbd5a6a86aaf8bb23302` | `6d63592d9afc25d01f0f2b5f85a70516f0d4bf1b` |

All three original Spanish blobs were fetched again from the translation branch and found unchanged from the pinned source commit. Each new English file has an editorial metadata comment that is **not** part of the translated source body. The body is the complete ordered translation.

## Structural preservation checks

The English body counts exclude the one metadata comment and its following blank line. Counts are checks of correspondence, not evidence that semantics are correct without textual review.

| Item | Source / English body lines | Heading levels | Table rows and column counts | Inline code tokens | Relative link destinations | Bullet rows | Numeric values |
|---|---:|---|---|---|---|---|---|
| A03 | 28 / 28 | 4 headings, levels identical | 14 / 14; columns identical | 10 / 10; exact | 0 / 0 | 0 / 0 | unchanged |
| A02 | 21 / 21 | 3 headings, levels identical | 8 / 8; columns identical | 8 / 8; exact | 1 / 1; exact | 0 / 0 | unchanged in value |
| A01 | 42 / 42 | 4 headings, levels identical | 22 / 22; columns identical | 2 / 2; exact | 9 / 9; exact | 3 / 3 | unchanged |

All corresponding headings, prose lines, table rows, lists and source-dependent statements were reviewed against the Spanish originals. Link targets retain their original relative strings because the English companions are adjacent to their Spanish sources. The nine A01 profile documents and the A02 A08 target exist at the declared repository paths.

## Translation-specific semantic checks

- **A03:** The four evidence categories remain distinct: vendor/standard-published capability, reinforced design, synthetic fact and calculation on paper. Each remains explicitly **No** under permission to present it as an observed result. All nine disposition literals and the full T# plus source-limit rule remain intact.
- **A02:** All six 00E–00J decision rows, negative/positive branches, time/cost facts and local case identifiers remain distinct. The H1/H2 relationship is unchanged, and scenario controls V0–Vn are expressly not equated with H0–H2. Missing universal parameters still require the canonical case sheet or `NO CONCLUSION` and an author decision.
- **A01:** All nine product/stack profiles, source indices, versions/dates, classes, limits, evidence cautions and nine source links remain present. Documented capabilities are **not** promoted into native EA semantics, implementation proof, authorization, validated traversal or current product observations. The controlled literal classification `CAPACIDAD_DOCUMENTADA_NO_CONGELADA` remains unmodified.
- **Numerical notation:** A02's Spanish grouping `~4.000 / ~$240.000` is rendered `~4,000 / ~$240,000` using English thousands punctuation. The quantities, units, approximate status and contextual identifiers are unchanged.
- **Technical names:** source-native labels (00E–00J, Q1–Q5, M/L/F/A/O/P, H0/H1/H2, V0–Vn, R1, T1/T2, T#, U/I/G, 2/USD11, F-00H-1, INC-5521, t_act) remain source identifiers. They have not been silently redefined or normalized across DDS or case-specific namespaces.

## Review boundary and next wave

These checks comprise a full first translation pass plus a second same-agent comparison against the Spanish, read in the context of the 00L package README, EA baseline and corpus control. They do **not** constitute independent scientific or human review. No vendor documentation was reconsulted and no experiment was run; historical source claims retain their dates and limitations.

This branch changes only the agent-language instruction and these three English companions plus this trace. No Spanish original, canonical requirement, protected README, review/VNext, result, fixture, code, presentation or external-submission record is rewritten.

Subsequent documents must be selected and translated one by one under the same rule. Keep the package's existing human-facing README translation and any change of primary reading links for a later, separately reviewed integration decision.
