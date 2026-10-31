# Agent instructions — English-first Structural Awareness corpus

> **Language policy — Iván Abril Palma, 31 October 2026.** English is the default language for new and maintained reader-facing prose in this research corpus. Translate Spanish-language research documents into complete, faithful English language editions, one document or a small verified batch at a time. **Translation is not summarization, abridgment, substantive editing, evidence review, rewriting or scientific promotion.** Do not omit, combine, simplify or expand any source statement.

This is an **agent-facing working instruction**, not an additional canonical README level. The existing human-facing `README.md` files and their protected navigation remain unchanged. The operative [document-control policy](DOCUMENT_CONTROL.md), [corpus review procedure](governance/CORPUS_REVIEW_PROCEDURE_2026-10-06.md), exact source-specific freeze records and owner decisions still govern.

## Language and source preservation

1. Write newly authored explanatory and technical prose in English, except where exact historical quotations, proper names, legally or technically controlled expressions, citations or source identifiers require another language. Preserve such expressions exactly and explain them in English when necessary.
2. Before translating, identify the logical document, current role (canonical, working, frozen, historical, evidence, review or other), exact source path, edition, pinned Git commit and blob SHA, dependencies, and any existing English edition. Do not retranslate or overwrite an already verified English edition without a documented reason.
3. Preserve the original Spanish document and its source-specific historical authority. Add a **separately identified English language edition**, clearly linked to the original, without treating it as a new scientific version, a second canonical authority, a VNext or a change to an existing test contract.
4. For documents that are frozen, signed, externally submitted, preregistered or otherwise protected, retain their bytes unchanged. Translation remains an explicitly identified derivative, subject to the same authorization boundaries for public use.

## Exact-translation contract

For each source document, translate **every** heading, paragraph, sentence, list item, table cell, note, caption and explanatory line in source order. Preserve:

- heading hierarchy, section numbering, paragraph boundaries, bullet and numbered-list structure, table dimensions, link destinations and resolvable anchors;
- equations, mathematical notation, variables, units, numerical values, thresholds, code, commands, file paths, stable IDs, version labels, dates and source citations;
- negations, qualifiers, uncertainty, counterexamples, assumptions, falsifiers, open questions, conditional statements and exact evidence maturity;
- distinctions between proposal and specification, paper calculation and symbolic execution, observed product behaviour and unexecuted tests, source authority and implemented control, research contribution and institutional adoption.

Do not change research content for fluency. If a phrase is genuinely ambiguous, preserve the closest defensible meaning in the English text and record the ambiguity **outside the translation**, for source-owner review. Do not silently resolve it by inventing detail or harmonizing an apparent cross-document inconsistency.

## Per-document review and batch acceptance

1. Read the complete source and relevant canonical definitions before translating. Use a bounded batch; a longer or higher-risk document is translated alone.
2. Produce a full source-to-English correspondence check by ordered section, paragraph, list item and table row/cell. Automated counts and hashes supplement rather than replace textual examination.
3. Independently of the first drafting pass, reread the English against the Spanish **line by line or paragraph by paragraph**. Check each claim's actor, modality, scope, condition, temporal reference, evidence status and intended result against its surrounding context and controlling sources. A second pass by the same agent is **not** an independent external review.
4. Verify retained code/math/technical tokens, identifiers, numbers, citations, reference targets, internal Markdown links and anchors. Record exceptions explicitly. Keep the full original available at its pinned Git revision.
5. Maintain a concise translation trace for every completed language edition: source and target paths, source commit/blob, target commit/blob or hash, structural comparison, semantic-review disposition, unresolved ambiguities and exact scope. A translation cannot be marked complete when source information is missing.
6. Use a focused review branch/pull request and verify public readback. Do not merge, promote to canonical, change controlled/human READMEs, alter frozen records or claim adoption without the applicable owner decision.

## Current initial translation wave

The first bounded batch comprises the Spanish `00L` documents A03, A02 and A01 under `research/ecosystem-awareness/baseline/00L_REINFORCED_PAPER_TRAVERSALS_00E_00J_v0.1/`, each as a separate English companion with source preserved. This does not establish that the whole corpus has been translated. Continue only after the first batch's structural and semantic checks are reported.

Existing English material is not a fresh translation target. In particular, [R01's earlier English translation and integrity record](research/ecosystem-awareness/baseline/reductions/00G-R01/TRANSLATION_TRACE.md) must be checked before planning any additional R01 language work.
