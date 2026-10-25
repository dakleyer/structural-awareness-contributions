#!/usr/bin/env python3
"""Check repository-local documentation routes and core presentation content.

Historical snapshots are excluded from link checks: their links retain their
original relative paths as evidence of the published state at that time.
"""
from __future__ import annotations

import re
import sys
import urllib.parse
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MARKDOWN_LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
HTML_LINK = re.compile(r"<(?:a|img)\s+[^>]*(?:href|src)=[\"']([^\"']+)", re.I)
EXTERNAL = ("#", "http:", "https:", "mailto:", "data:", "javascript:", "//")

ARCHITECTURE = ROOT / "architectural-contributions/ecosystem-positioning/README.md"
REQUIRED_SECTIONS = {
    "# The corpus spine": 1100,
    "# The shared epistemic position": 600,
    "# The mechanisms of the positioning cycle": 1800,
    "# Architecture and interfaces — three levels": 800,
    "# Architecture-validation use cases": 700,
    "# From scenarios to executable fixtures": 700,
    "# Benchmark — comparison, not marketing": 900,
    "### Technical proof map": 1100,
}
REQUIRED_REFERENCES = (
    "04_GENERAL_FUNCTIONAL_INTERFACES_AGENTIC_SECURITY_v0.5_INTEGRATED.md",
    "05_FG_TIDA_IDEAL_CROSS_THEME_INTERFACE_CONTRACTS_v0.4.part01.md",
    "05A_FG_TIDA_CURRENT_STATE_CONFORMANCE_BRIDGE_v0.1.md",
    "SCENARIO_READER_GUIDE_2026-09-25.md",
)
PRESENTATIONS = {
    "Ecosystem_Positioning_Architecture_Implementation_Canonical_v1.2.pptx": (7, 10000),
    "Ecosystem_Positioning_Requirements_Evidence_Canonical_v1.2.pptx": (12, 12000),
}


# Owner-reviewed historical source quotations. Contexts are raw UTF-8 text;
# match their complete section and exact line counts, never a whole directory.
SOURCE_QUOTATION_CONTEXTS = (
    {'source': 'research/ecosystem-awareness/baseline/04_GENERAL_FUNCTIONAL_INTERFACES_AGENTIC_SECURITY_VNEXT_REVIEW_AND_DELTA_v0.1_DRAFT.md', 'context': "# First scoped judgement: input-contract custody status\r\n\r\nSealed 2026-10-14T21:19:32.094094+00:00. Phase A; whole source/receiver cohort incomplete.\r\n\r\nThe current Markdown contains dated semantic amendments. The preserved approved Word and original Markdown retain the previous contract, so the current literal unchanged-reproduction claim requires clarification. The complete original body text is accounted comparatively, but Word rendering remains unread. This is a custody correction, not reversal of the current B/C amendment.\r\n\r\nCurrent location: research/ecosystem-awareness/baseline/04_INPUT_INTERFACE_CONTRACT/04_INPUT_INTERFACE_CONTRACT_v0.4.md; blob de6c58c62ad70b3182085333106b41b63a9fef18. Each before passage occurs exactly once.\r\n\r\nComplete current before, line 1:\r\n\r\n```html\r\n<!-- Approved v0.4 Word body reproduced below in document order. -->\r\n```\r\n\r\nComplete proposed after:\r\n\r\n```html\r\n<!-- Preserved approved v0.4 Word body forms the historical base; the current Markdown includes the explicitly dated semantic amendments identified below. -->\r\n```\r\n\r\nComplete current before, line 17:\r\n\r\n**Conservación:** a continuación se reproduce íntegro el cuerpo del Word aprobado, en español, con sus tablas y diagrama. Sus declaraciones de estado corresponden a la revisión previa a esta publicación. Esta publicación añade rutas y un registro en el delta; no atribuye ejecuciones ni cierra incompatibilidades. El [manifiesto](./PUBLICATION_MANIFEST.json) identifica los archivos y el snapshot de origen. Los nombres de los campos del ejemplo de transporte son ilustrativos.\r\n\r\nComplete proposed after:\r\n\r\n**Conservación:** el Word aprobado, en español, con sus tablas y diagrama, se conserva íntegro como fuente histórica. El Markdown actual parte de ese cuerpo y contiene las enmiendas semánticas fechadas e identificadas en esta página; por ello no es una reproducción literal inalterada del Word. Las declaraciones de estado del cuerpo histórico corresponden a la revisión previa a su publicación. El [manifiesto](./PUBLICATION_MANIFEST.json) identifica los archivos originales y el snapshot de origen; sus hashes describen esa publicación histórica y no certifican las modificaciones posteriores del Markdown. Se conservan las rutas y el registro del delta. No se atribuyen ejecuciones ni se cierran incompatibilidades. Los nombres de los campos del ejemplo de transporte son ilustrativos.\r\n\r\nImpact Medium; risk Low; effort Low. Preserve original assets and the dated manifest unchanged. Benefit: honest authentication and navigation between original publication and current amendments. Cost: two local status edits; no regeneration. Acceptance: unique literal matches, original hashes preserved, current amendment/field IDs/links preserved, no execution or incompatibility-closure claim. Ivan’s named wave/passages GO is required; nothing applied.\r\n\r\nThe JSON freezes exact identities, supporting original/current clauses and contemporaneous reading/exposure records. A later A23 audit execution-record exposure is disclosed there; it contributes no input-contract evidence.\r\n\n\n</details>\n\n\n## Unified restoration candidates 15 October 2026\n\nThe [independent unified plan](https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1_VNext.md#unified-restoration-plan-15-october-2026) re-evaluates these existing proposals against their current sources and receivers. The passages below are complete current preparations, pending their stated decision gates. Earlier alternatives and audits remain visible.\n\n\n### Existing candidate 101\n\nCurrent Markdown itself contains explicit dated semantic amendments; unchanged-reproduction comment is misleading. Preserve Word/graphics/manifest bytes.\n\n**Impact / risk / effort:** Bajo / Bajo / Bajo. **State:** Pending named exact Ivan GO; additional gates in plan apply\n\n**Source:** [research/ecosystem-awareness/baseline/04_INPUT_INTERFACE_CONTRACT/04_INPUT_INTERFACE_CONTRACT_v0.4.md](https://github.com/dakleyer/structural-awareness-contributions/blob/89273f548f6b5ed8f7e0576040f615b5653ffaf6/research/ecosystem-awareness/baseline/04_INPUT_INTERFACE_CONTRACT/04_INPUT_INTERFACE_CONTRACT_v0.4.md), blob `de6c58c62ad70b3182085333106b41b63a9fef18`. Dependencies: preserve original Word, historical MD, diagram and manifest bytes with original hashes; retain current semantic amendment and actual field IDs/source anchors; resolve final existing owner and return routes after source baseline; no new owner collection; Ivan named wave/passages GO before incorporation; Companion proposal 102; publish the two custody descriptions consistently.\n\n**Text before — complete current passage (1).**\n\n``````text\n<!-- Approved v0.4 Word body reproduced below in document order. -->\n``````\n\n**Text after — complete proposal.**\n\n``````text\n<!-- Preserved approved v0.4 Word body forms the historical base; the current Markdown includes the explicitly dated semantic amendments identified below. -->\n``````\n\nThis is the same pending proposal, with its unified-review assessment, rather than another action under an alias. The complete earlier record remains above. Apply only an explicitly selected pair/wave; preserve every other source byte and its recorded freezes, evidence and results. [Joint plan and acceptance checks](https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1_VNext.md#unified-restoration-plan-15-october-2026).\n\n\n### Existing candidate 102\n\nCurrent dated amendment and historical manifest require an honest original-vs-current custody explanation; no reversal of B/C correction or rendered-parity assertion.\n\n**Impact / risk / effort:** Medio / Bajo / Bajo. **State:** Pending named exact Ivan GO; additional gates in plan apply\n\n**Source:** [research/ecosystem-awareness/baseline/04_INPUT_INTERFACE_CONTRACT/04_INPUT_INTERFACE_CONTRACT_v0.4.md](https://github.com/dakleyer/structural-awareness-contributions/blob/89273f548f6b5ed8f7e0576040f615b5653ffaf6/research/ecosystem-awareness/baseline/04_INPUT_INTERFACE_CONTRACT/04_INPUT_INTERFACE_CONTRACT_v0.4.md), blob `de6c58c62ad70b3182085333106b41b63a9fef18`. Dependencies: preserve original Word, historical MD, diagram and manifest bytes with original hashes; retain current semantic amendment and actual field IDs/source anchors; resolve final existing owner and return routes after source baseline; no new owner collection; Ivan named wave/passages GO before incorporation; Companion proposal 101; publish the two custody descriptions consistently.\n\n**Text before — complete current passage (1).**\n\n``````text\n**Conservación:** a continuación se reproduce íntegro el cuerpo del Word aprobado, en español, con sus tablas y diagrama. Sus declaraciones de estado corresponden a la revisión previa a esta publicación. Esta publicación añade rutas y un registro en el delta; no atribuye ejecuciones ni cierra incompatibilidades. El [manifiesto](./PUBLICATION_MANIFEST.json) identifica los archivos y el snapshot de origen. Los nombres de los campos del ejemplo de transporte son ilustrativos.\n``````\n\n**Text after — complete proposal.**\n\n``````text\n**Conservación:** el Word aprobado, en español, con sus tablas y diagrama, se conserva íntegro como fuente histórica. El Markdown actual parte de ese cuerpo y contiene las enmiendas semánticas fechadas e identificadas en esta página; por ello no es una reproducción literal inalterada del Word. Las declaraciones de estado del cuerpo histórico corresponden a la revisión previa a su publicación. El [manifiesto](./PUBLICATION_MANIFEST.json) identifica los archivos originales y el snapshot de origen; sus hashes describen esa publicación histórica y no certifican las modificaciones posteriores del Markdown. Se conservan las rutas y el registro del delta. No se atribuyen ejecuciones ni se cierran incompatibilidades. Los nombres de los campos del ejemplo de transporte son ilustrativos.\n``````\n\nThis is the same pending proposal, with its unified-review assessment, rather than another action under an alias. The complete earlier record remains above. Apply only an explicitly selected pair/wave; preserve every other source byte and its recorded freezes, evidence and results. [Joint plan and acceptance checks](https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1_VNext.md#unified-restoration-plan-15-october-2026).\n\n\n## Literal plan check 15 October 2026\n\nReview by Codex AI assistant, 15 October 2026, against published main `0aa9718afb40ba917ce21a45f20b4dfd7e73d925`. This is a new reading by the same assistant, not an additional independent auditor.\n\n**Pairs checked here: 101,102.** Both complete old/new publication descriptions match the source. Their joint proposed meaning distinguishes the preserved Word/manifest/diagram edition from dated living Markdown amendments. Neither pair changes those binaries or recalculates the historical manifest. Both remain one companion decision after edition/return-route reconciliation.\n\nComplete old and proposed blocks remain above; they were not replaced by this receipt. The [joint plan check](https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1_VNext.md#literal-plan-check-15-october-2026) records the selected92variant,33pairs across ten existing VNext, the48-file custody scope and the actual conditions still open. Published review is complete; source incorporation remains pending its named decision.\n\n\n### Application 101 — 15 October 2026\n\n**Applied; removed from the pending queue.** Iván authorised incorporation of the reviewed literal plan. Applied 1 complete literal replacement to `research/ecosystem-awareness/baseline/04_INPUT_INTERFACE_CONTRACT/04_INPUT_INTERFACE_CONTRACT_v0.4.md`; resulting source blob `1bbc76f673d79e3b5bb52117aeeb3d68af0d5387`. Each step has an exact inverse: every byte outside its approved old/new unit is identical. The complete earlier before/after and audit remain application history, not pending work. No campaign, run, result or code was changed.\n\n\n### Application 102 — 15 October 2026\n\n**Applied; removed from the pending queue.** Iván authorised incorporation of the reviewed literal plan. Applied 1 complete literal replacement to `research/ecosystem-awareness/baseline/04_INPUT_INTERFACE_CONTRACT/04_INPUT_INTERFACE_CONTRACT_v0.4.md`; resulting source blob `407a009999326cd051cb26e003ad78f8cf8e3162`. Each step has an exact inverse: every byte outside its approved old/new unit is identical. The complete earlier before/after and audit remain application history, not pending work. No campaign, run, result or code was changed.\n\n\n**Verified application commits — 06_attribution_and_editions:** [101](https://github.com/dakleyer/structural-awareness-contributions/commit/b6a4ba78bb7b5135dcdc7da71fd6d1821f54963c), [102](https://github.com/dakleyer/structural-awareness-contributions/commit/29c1d0da83c333348787944540ca99462515c03b).\n\n\n## Owner authorised application complete 15 October 2026\n\n**Applied and verified:** 101, 102. Iván authorised the reviewed plan on15 October2026. The current proposal queue for these items is empty; the older audits and complete old/new pairs remain their dated application history.\n\nThe source and actual step commits are recorded in the application receipts above. Every approved replacement preserved all other source bytes; the source/output check was repeated against the final composed main tree. [Joint application record](https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1_VNext.md#owner-authorised-application-complete-15-october-2026).\n\n\n## Execution reaudit 15 October 2026\n\nRe-read101/102 with the current semantic amendment and original publication description. The two caption changes do not replace the original Word, diagram, frozen Markdown or manifest, and do not promote v0.4 over current integration ownership. The actual approved pair replay and full source-prefix/suffix comparison pass; every earlier literal block in this owning VNext remains present. The applied state is now also correct in the effective registry and CSV. [Joint execution re-audit](https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1_VNext.md#execution-reaudit-15-october-2026).\n\n\n## Historical interface reception — 15 October 2026\n\nReviewer A read the complete 1,869-line 04 v0.5 body and compared all three current v0.4 bodies line by line, reading their differing blocks. All 78 historical units received clause-specific judgments. Renaming S1–S13 to IF-S1–IF-S13 preserves thirteen interface families, O1–O6 and F1–F9 while separating interface labels from requirements and DAOS challenges. Identity, authority, attestation, appraisal, capacity, privacy, records, population and response retain their owners. Theme numbers remain in v0.4 and 05/05A; their removal from the general body does not remove those functions.\n\nThe fourth EHD element survives: current line 99 accepts a source-bound reference only if the receiving profile can resolve and interpret it at decision time. An unavailable, stale or insufficiently bound reference retains UNKNOWN and cannot support uses needing the value. The line 9 notice still leaves H06 open for input contracts and EHD/F9 uses; historical reception does not settle that substantive tension.\n\nCurrent A/B/C/D corrections retain result/basis, characterised reserve, uncharacterised exploration and effective evaluation barrier, together with provenance/process/question/scope/time. Earlier definitions remain lineage, without automatic theorem or empirical transfer. ICR conditions are retained and strengthened: maintainer-declared materiality is identified; route and aggregations are declared before execution; later-discovered aggregation is a mapping defect. A distinct mapping reviewer and a material objection still block sufficiency. Nondeterministic tests retain distribution/dispersion; the original three classes remain alongside adversarial assertion. A simulated boundary is not independent interoperability.\n\nCompeting intents retain the same decision/resource-time binding and owner precedence. Continuity/re-entry remains conditional and creates no universal hierarchy, O7, IF-S14 or actuation authority. IF-S2 at line 758 directly says EA consumes authority and neither originates grants nor decides legal standing, reinforcing the Charter receiver chain. No source restoration follows. The [03 owner](03_FUNCTIONAL_VNext.md#historical-functional-architecture-reception--15-october-2026) and [Foundation owner](01_FOUNDATIONAL_VNext.md#continued-foundation-and-charter-lineage-reception--15-october-2026) record both relationships.\n\n\n\n## Historical interface custody and semantic reception — 15 October 2026\n\nD read the complete 1,038-line current input contract, its 176 rows across 19 families and all 58 changed historical units. The original field IDs and row literals remain. Original Word, SVG, PNG and historical Markdown identities match the historical manifest, while the amended current text keeps its dated semantic amendment. The two objects answer different identity questions; the historical manifest is not recast as a hash for the amended current body.\n\nThe B/C corrections and custody descriptions are legitimate receiving changes. No field, option or explanatory reason from the examined unit history needs blind restoration. This retention judgement does not admit every classification or close H06/F9, the stated A-exclusion question or O2. Those remain visible in their source contracts. No programme or result was executed or altered by this reading.\n\n\n## Historical contract and review reception — 15 October 2026\n\nB's completed prose-control reading confirms the distinction between generic 04 semantics and programme-specific 05/05A mappings. The current A_ref route keeps unavailable, stale and unbound values as UNKNOWN; H06 end-to-end reconciliation remains a real requirement. Retiring applied navigation/editorial dossiers does not settle that contract question or reactivate an older alternative.\n\nThe two visible ./PUBLICATION_MANIFEST.json strings inside the preserved 101/102 input-contract before/after material are literal source-relative context. Their named source is 04_INPUT_INTERFACE_CONTRACT; operative owner links reach the current contract 407a0099 and its manifest 3934ed2b. Both actual receivers were read. Rewriting the quoted URLs would falsify the complete old/proposed passages, so no such patch is proposed. The current input-contract semantics and 176-row conditional map retain their own review limits. The [baseline consolidation](./README_VNext.md#historical-reception-and-restoration-decisions--15-october-2026) records the cross-document decision.\n", 'context_sha256': 'fa2e925aa7cf32aca58cd030768be66d3cf254d704015492b47b196a0bf5b0bf', 'links': [{'line': '**Conservación:** a continuación se reproduce íntegro el cuerpo del Word aprobado, en español, con sus tablas y diagrama. Sus declaraciones de estado corresponden a la revisión previa a esta publicación. Esta publicación añade rutas y un registro en el delta; no atribuye ejecuciones ni cierra incompatibilidades. El [manifiesto](./PUBLICATION_MANIFEST.json) identifica los archivos y el snapshot de origen. Los nombres de los campos del ejemplo de transporte son ilustrativos.', 'line_sha256': 'fcd66dc6595d3a2f0d725cb6207c8c701b013ca32c9511ceae98e3a408ee2353', 'href': './PUBLICATION_MANIFEST.json', 'receiver': 'research/ecosystem-awareness/baseline/04_INPUT_INTERFACE_CONTRACT/PUBLICATION_MANIFEST.json', 'expected_line_occurrences': 2}, {'line': '**Conservación:** el Word aprobado, en español, con sus tablas y diagrama, se conserva íntegro como fuente histórica. El Markdown actual parte de ese cuerpo y contiene las enmiendas semánticas fechadas e identificadas en esta página; por ello no es una reproducción literal inalterada del Word. Las declaraciones de estado del cuerpo histórico corresponden a la revisión previa a su publicación. El [manifiesto](./PUBLICATION_MANIFEST.json) identifica los archivos originales y el snapshot de origen; sus hashes describen esa publicación histórica y no certifican las modificaciones posteriores del Markdown. Se conservan las rutas y el registro del delta. No se atribuyen ejecuciones ni se cierran incompatibilidades. Los nombres de los campos del ejemplo de transporte son ilustrativos.', 'line_sha256': 'c638c60904273e1f658f67e86c96268266740ab317f8589b8fc4ef6584849326', 'href': './PUBLICATION_MANIFEST.json', 'receiver': 'research/ecosystem-awareness/baseline/04_INPUT_INTERFACE_CONTRACT/PUBLICATION_MANIFEST.json', 'expected_line_occurrences': 2}]},
    {'source': 'research/ecosystem-awareness/baseline/fixtures/00K-SUITE/README_VNext.md', 'context': '### Existing A22 qualification to retain\n\n> **Audit qualification — 26 September 2026:** the executable certificate realizes 64 signatures in its simplified model. It does not yet verify a lifting to all A20 background axioms B1–B11: record-derived unresolved conflict and the inquiry graph/rank are not represented as claimed by the stronger reading below. The Boolean counting bound remains valid for 64 distinguishable signatures; its application to the full declared semantic substrate is conditional on the missing bridge. Read the earlier result below with this qualification. [A13 findings](./00L_REINFORCED_PAPER_TRAVERSALS_00E_00J_v0.1/00L_A13_AUDITORIA_TRANSVERSAL_PRUEBAS_v0.1.md) · [A14 status](./00L_REINFORCED_PAPER_TRAVERSALS_00E_00J_v0.1/00L_A14_CORRECCIONES_AUDITORIA_v0.1.md).\n\nFor the quoted A22 qualification above, open [A13 findings](../../00L_REINFORCED_PAPER_TRAVERSALS_00E_00J_v0.1/00L_A13_AUDITORIA_TRANSVERSAL_PRUEBAS_v0.1.md) and [A14 corrections and status](../../00L_REINFORCED_PAPER_TRAVERSALS_00E_00J_v0.1/00L_A14_CORRECCIONES_AUDITORIA_v0.1.md). These links resolve from this review; the source-relative links inside the historical quotation are retained verbatim.\n\nThe actual simplified model carries the following complete inspected contract and P2/P3 definitions; it does not implement a derivation of conflict from records or the full inquiry graph/rank claimed by a stronger reading. The code was read, not executed.\n\n```python\n@dataclass(frozen=True)\nclass Inquiry:\n    """One shared unresolved object used by both P2 and P3."""\n    proposition: str\n    unresolved: bool\n    material_to_action: bool\n    cyclic_progress: bool\n    bounded_fallback: bool\n\n\n@dataclass\nclass Model:\n    records: Dict[str, Record]\n    used_records: FrozenSet[str]\n    asserted: FrozenSet[str]\n    explicit_unresolved: FrozenSet[str]\n    inquiry: Inquiry\n    executes: bool\n    grant_record: str\n    requalified_at_action: bool\n    counted_pairs: FrozenSet[Tuple[str, str]]\n\n    def record(self, name: str) -> Record:\n        return self.records[name]\n\n\ndef p2(m: Model) -> bool:\n    """The shared unresolved inquiry has finite progress and a bounded fallback."""\n    if not m.inquiry.unresolved:\n        return True\n    return (not m.inquiry.cyclic_progress) and m.inquiry.bounded_fallback\n\n\ndef p3(m: Model) -> bool:\n    """A material unresolved state is not promoted into execution."""\n    material_unresolved = m.inquiry.unresolved and m.inquiry.material_to_action\n    return not (material_unresolved and m.executes)\n\n\n\n```\n\n', 'context_sha256': 'ea87107ac484a8ee536ccc90f176834571bc99c467f08f5fba4ae6f9786cf536', 'links': [{'line': '> **Audit qualification — 26 September 2026:** the executable certificate realizes 64 signatures in its simplified model. It does not yet verify a lifting to all A20 background axioms B1–B11: record-derived unresolved conflict and the inquiry graph/rank are not represented as claimed by the stronger reading below. The Boolean counting bound remains valid for 64 distinguishable signatures; its application to the full declared semantic substrate is conditional on the missing bridge. Read the earlier result below with this qualification. [A13 findings](./00L_REINFORCED_PAPER_TRAVERSALS_00E_00J_v0.1/00L_A13_AUDITORIA_TRANSVERSAL_PRUEBAS_v0.1.md) · [A14 status](./00L_REINFORCED_PAPER_TRAVERSALS_00E_00J_v0.1/00L_A14_CORRECCIONES_AUDITORIA_v0.1.md).', 'line_sha256': '277f44d8de7d866b75e47874bdcb8cacdfeb373abe0b49214160446720561397', 'href': './00L_REINFORCED_PAPER_TRAVERSALS_00E_00J_v0.1/00L_A13_AUDITORIA_TRANSVERSAL_PRUEBAS_v0.1.md', 'receiver': 'research/ecosystem-awareness/baseline/00L_REINFORCED_PAPER_TRAVERSALS_00E_00J_v0.1/00L_A13_AUDITORIA_TRANSVERSAL_PRUEBAS_v0.1.md', 'expected_line_occurrences': 1}, {'line': '> **Audit qualification — 26 September 2026:** the executable certificate realizes 64 signatures in its simplified model. It does not yet verify a lifting to all A20 background axioms B1–B11: record-derived unresolved conflict and the inquiry graph/rank are not represented as claimed by the stronger reading below. The Boolean counting bound remains valid for 64 distinguishable signatures; its application to the full declared semantic substrate is conditional on the missing bridge. Read the earlier result below with this qualification. [A13 findings](./00L_REINFORCED_PAPER_TRAVERSALS_00E_00J_v0.1/00L_A13_AUDITORIA_TRANSVERSAL_PRUEBAS_v0.1.md) · [A14 status](./00L_REINFORCED_PAPER_TRAVERSALS_00E_00J_v0.1/00L_A14_CORRECCIONES_AUDITORIA_v0.1.md).', 'line_sha256': '277f44d8de7d866b75e47874bdcb8cacdfeb373abe0b49214160446720561397', 'href': './00L_REINFORCED_PAPER_TRAVERSALS_00E_00J_v0.1/00L_A14_CORRECCIONES_AUDITORIA_v0.1.md', 'receiver': 'research/ecosystem-awareness/baseline/00L_REINFORCED_PAPER_TRAVERSALS_00E_00J_v0.1/00L_A14_CORRECCIONES_AUDITORIA_v0.1.md', 'expected_line_occurrences': 1}]},
)


def documentation_link_records(source: Path, body: str, root: Path | None = None):
    """Resolve only unique complete quoted contexts; leave live links ordinary."""
    import hashlib
    visible = navigation_text(body)
    relative = source.relative_to(root or ROOT).as_posix()
    authorized = {}
    lines = body.splitlines()
    for record in SOURCE_QUOTATION_CONTEXTS:
        if record["source"] != relative:
            continue
        context = record["context"]
        if hashlib.sha256(context.encode("utf-8")).hexdigest() != record["context_sha256"]:
            continue
        if body.count(context) != 1:
            continue
        exposed = navigation_text(context)
        if not exposed or visible.count(exposed) != 1:
            continue
        offset = visible.index(exposed)
        for link in record["links"]:
            line = link["line"]
            if hashlib.sha256(line.encode("utf-8")).hexdigest() != link["line_sha256"]:
                continue
            if lines.count(line) != link["expected_line_occurrences"]:
                continue
            if exposed.count(line) != 1:
                continue
            at = offset + exposed.index(line)
            key = (at, at + len(line), link["href"])
            authorized[key] = link["receiver"]
    matches = list(MARKDOWN_LINK.finditer(visible)) + list(HTML_LINK.finditer(visible))
    for match in matches:
        start = visible.rfind("\n", 0, match.start()) + 1
        end = visible.find("\n", match.end())
        if end < 0:
            end = len(visible)
        raw = match.group(1)
        receiver = next((target for (a, b, href), target in authorized.items()
                         if href == raw and a <= match.start() and match.end() <= b), None)
        yield raw, receiver


def navigation_text(body: str) -> str:
    """Exclude literal fenced/inline code from rendered-link checks."""
    visible = []
    fence = None
    for line in body.splitlines(keepends=True):
        opening = re.match(r"^ {0,3}(\x60{3,}|~{3,})(.*)$", line.rstrip("\n\r"))
        if fence is None and opening:
            token = opening.group(1)
            # A backtick info string cannot contain a backtick (CommonMark).
            if token[0] == "\x60" and "\x60" in opening.group(2):
                visible.append(line)
                continue
            fence = (token[0],len(token))
            continue
        if fence is not None:
            closing = re.match(r"^ {0,3}([\x60~]{3,})[ \t]*$",line.rstrip("\n\r"))
            if closing and set(closing.group(1)) == {fence[0]} and len(closing.group(1)) >= fence[1]:
                fence = None
            continue
        visible.append(line)
    value = "".join(visible)
    # A matching backtick run bounds a CommonMark code span; unmatched runs remain prose.
    return re.sub(r"(?<!`)(`+)(?!`)([\s\S]*?)(?<!`)\1(?!`)", "", value)


def extract_targets(body: str):
    visible = navigation_text(body)
    return MARKDOWN_LINK.findall(visible) + HTML_LINK.findall(visible)


def check_document_links(root: Path):
    from historical_source_routes import qualified_routes
    qualifications, errors = qualified_routes(root, extract_targets)
    checked_links = historical_links = 0
    used = {}
    context_keys = {(record["source"], link["href"])
                    for record in SOURCE_QUOTATION_CONTEXTS for link in record["links"]}
    for source in root.rglob("*.md"):
        if ".git" in source.parts or "preserved-public-snapshots" in source.parts:
            continue
        # Keep exact quote-context bytes, including mixed line endings.
        body = source.read_bytes().decode("utf-8")
        for raw, quoted_target in documentation_link_records(source, body, root):
            target = raw.split(" ")[0].strip("<>")
            if not target or target.startswith(EXTERNAL):
                continue
            route = urllib.parse.unquote(target.split("#", 1)[0].split("?", 1)[0])
            checked_links += 1
            if (source.parent / route).resolve().exists():
                continue
            key = (source.relative_to(root).as_posix(), target)
            if key in qualifications:
                if key in context_keys and quoted_target is None:
                    errors.append(f"historical quote context changed: {key}")
                    continue
                if quoted_target is not None and (root / quoted_target).resolve() != qualifications[key]["receiver"]:
                    errors.append(f"historical quote receiver disagreement: {key}")
                    continue
                used[key] = used.get(key, 0) + 1
                historical_links += 1
                continue
            if quoted_target is not None:
                # Retain the upstream exact-context disposition for other records.
                if not (root / quoted_target).exists():
                    errors.append(f"missing quoted receiver: {key} -> {quoted_target}")
                continue
            errors.append(f"missing link: {source.relative_to(root)} -> {target}")
    for key, qualification in qualifications.items():
        if used.get(key, 0) != qualification["expected_occurrences"]:
            errors.append(f"qualified citation use changed: {key}")
    return errors, checked_links, historical_links


def main() -> int:
    errors, checked_links, historical_links = check_document_links(ROOT)

    if not ARCHITECTURE.exists():
        errors.append("missing Ecosystem Positioning architecture README")
    else:
        body = ARCHITECTURE.read_text(encoding="utf-8")
        for title, minimum in REQUIRED_SECTIONS.items():
            match = re.search(rf"(?m)^{re.escape(title)}$", body)
            if not match:
                errors.append(f"missing architecture section: {title}")
                continue
            level = len(title.split(" ", 1)[0])
            following = re.finditer(r"(?m)^(#{1,3}) ", body[match.end():])
            next_heading = next((item for item in following
                                 if len(item.group(1)) <= level), None)
            end = match.end() + next_heading.start() if next_heading else len(body)
            if end - match.end() < minimum:
                errors.append(f"architecture section unexpectedly short: {title}")
        for route in REQUIRED_REFERENCES:
            if route not in body:
                errors.append(f"missing architecture route: {route}")

    for filename, (minimum_slides, minimum_text) in PRESENTATIONS.items():
        target = ROOT / "presentations/ecosystem-positioning" / filename
        if not target.exists():
            errors.append(f"missing presentation: {filename}")
            continue
        with zipfile.ZipFile(target) as deck:
            bad_member = deck.testzip()
            if bad_member:
                errors.append(f"corrupt presentation member: {filename} -> {bad_member}")
                continue
            slides = [name for name in deck.namelist()
                      if re.fullmatch(r"ppt/slides/slide\d+\.xml", name)]
            text_size = sum(
                len(node.text or "")
                for slide in slides
                for node in ET.fromstring(deck.read(slide)).iter()
                if node.tag.endswith("}t")
            )
            if len(slides) < minimum_slides or text_size < minimum_text:
                errors.append(
                    f"presentation content unexpectedly reduced: {filename} "
                    f"({len(slides)} slides, {text_size} text characters)"
                )

    if errors:
        print("DOCUMENT INTEGRITY: FAIL")
        print("\n".join(errors))
        return 1
    print(f"DOCUMENT INTEGRITY: PASS ({checked_links} local routes, "
          f"{historical_links} qualified historical source citations, "
          f"{len(REQUIRED_SECTIONS)} architecture sections, {len(PRESENTATIONS)} canonical decks)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
