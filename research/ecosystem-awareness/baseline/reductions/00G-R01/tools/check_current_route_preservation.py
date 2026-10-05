#!/usr/bin/env python3
"""Guard the R01 current-route editorial/readability pass against information loss.

The baseline is the repository state immediately before the dedicated visual and
paragraph-level readability pass. Historical/frozen material is deliberately excluded:
it must not be rewritten for presentation.

The guard allows local prose improvements while preserving structure and protected
content. It requires unchanged headings/anchors, tables, list items, fenced code,
display mathematics, link destinations and numeric tokens. Prose paragraphs must remain
one-to-one and close in length; code spans and explicit identifiers inside each paragraph
must be preserved.
"""
from __future__ import annotations

from collections import Counter
from pathlib import Path
import re
import subprocess
import sys

R01 = Path(__file__).resolve().parents[1]
REPO = R01.parents[4]
BASELINE_COMMIT = "a96f14718a3b2f307b812ae4d8fe278dffb62764"
BASELINE_BY_FILE = {
    # Active C02 material was added after the initial preservation audit.
    # Each file is compared from the commit that established the current pre-editorial content.
    "README.md": "9d644d0702022d93978a43520deb157ba2e1661e",
    "COMPUTABILITY_AND_ORACLE_PLAN.md": "42b0102bcb801cda2d21445e48c7f7e4e5dc9478",
    "STRATEGIC_WORKPLAN_AND_EXECUTION_PROMPT.md": "cfbff4801f4ba24fb4be6e17fcd8a38104fe39d8",
    "feasibility/README.md": "9a0b6024d59511af87e56764d544c69b4ffad0c5",
    "feasibility/CONTINUATION_PROMPT.md": "1ef1eab2c842299a05a6b448182bdec0a3f81c95",
    "feasibility/WORKPLAN.md": "50a0ae48b8bc9c0077119e104c0fdd997d7a2f84",
    "oracle/README.md": "a05a57ac9e3b1b883d60d7a82d1c6b4298862362",
    "oracle/SELFTEST_RECORD_v0.3.md": "7ea76588b1b7e68c5b0f560f9c0276b7fb2b0475",
    "oracle/SELFTEST_RECORD_v0.4.md": "3a8030351968edf5762c8b831e054d380fb6c03c",
    "oracle/UC4_INTEROPERABILITY_PROFILE.md": "f6d7aa5102bb63c9dc8b0bbc5751c0437b8a090d",
    "oracle/NELSON_REVIEW_REQUEST.md": "045a8a233431e8bb67cd93b3a7d5169d1c3163e3",
    "oracle/NELSON_BASELINE_IMPORT.md": "c3ed9a55dd6d5b642107ef6a0baa15320cce1b2e",
    "oracle/TOOL_BROKER_CONTRACT.md": "2cbfeaee9e533929d94e24e8ebc9dbdd8c3e4992",
    "oracle/TECHNOLOGY_ADAPTER_GUIDE.md": "e299d2fcb5be479f323969f7e8ed424bd701d095",
    "oracle/ISOLATION_CONTRACT.md": "39cd7f03fe70c7796615fd7cb4e912ba429870f8",
    "oracle/GATE_POLICY_CONTRACT.md": "a0419cde3aa06ca0a0138e026a5057100ee4699c",
    "oracle/TRACE_CONTRACT.md": "ad3db7adc9546bfd7a935b5e67b4c15be5042e75",
    "oracle/SELFTEST_RECORD_v0.7.md": "2e62f26ad41334a2cf1faf3cc913ed28678fb10b",
    "oracle/SELFTEST_RECORD_v0.9.md": "1c87399447b3769be738d1f75050db900d2c314f",
}

EXTERNAL_ROUTE_FILES = {
    "research/ecosystem-awareness/baseline/fixtures/00G-HF-ORACLE-v0.4/ESTADO_00G-R01.md":
        "13203ac89c59b8c19dd89bf50f4c5ee2aeddb8fd",
}

CURRENT_ROUTE_FILES = (
    "README.md",
    "Escenario-creatividad-validacion.md",
    "COMPUTABILITY_AND_ORACLE_PLAN.md",
    "DIFFERENTIAL_AND_EXPERIMENT_VALUE.md",
    "MATHEMATICAL_FEASIBILITY.md",
    "STRATEGIC_WORKPLAN_AND_EXECUTION_PROMPT.md",
    "TRACE_POLICY.md",
    "INFORMATION_PRESERVATION_AUDIT_2026-10-04.md",
    "reductions/00G-to-R01/README.md",
    "extensions/CRITERIA_AND_AUDIT.md",
    "extensions/METHODOLOGICAL_FOUNDATIONS.md",
    "extensions/hugging-face/README.md",
    "extensions/infoblox/README.md",
    "extensions/family/README.md",
    "extensions/family/KERNEL_AND_PROOF.md",
    "oracle/README.md",
    "oracle/UC4_INTEROPERABILITY_PROFILE.md",
    "oracle/NELSON_REVIEW_REQUEST.md",
    "oracle/NELSON_BASELINE_IMPORT.md",
    "oracle/TOOL_BROKER_CONTRACT.md",
    "oracle/TECHNOLOGY_ADAPTER_GUIDE.md",
    "oracle/ISOLATION_CONTRACT.md",
    "oracle/GATE_POLICY_CONTRACT.md",
    "oracle/TRACE_CONTRACT.md",
    "oracle/SELFTEST_RECORD_v0.7.md",
    "oracle/SELFTEST_RECORD_v0.9.md",
    "oracle/SELFTEST_RECORD_v0.3.md",
    "oracle/SELFTEST_RECORD_v0.4.md",
    "feasibility/README.md",
    "feasibility/WORKPLAN.md",
    "feasibility/CONTINUATION_PROMPT.md",
    "feasibility/EXTENSION_CONSISTENCY_REVIEW.md",
    "feasibility/R01_AUDIT_CONTINUITY_AND_REPAIRS.md",
    "feasibility/R01_CONDITIONED_TRILEMMA_REVIEW.md",
    "feasibility/R01_CONDITIONED_TRILEMMA_THEOREM.md",
    "feasibility/R01_TO_CONDITIONED_TRILEMMA_MAPPING.md",
    "feasibility/TECHNOLOGY_EXTENSION_PROTOCOL.md",
    "feasibility/HUMAN_ESCALATION_WHISPERING.md",
)

HEADING = re.compile(r"^(#{1,6})\s+(.+?)\s*$", re.M)
ANCHOR = re.compile(r"<a\s+[^>]*(?:id|name)=[\"']([^\"']+)[\"'][^>]*>", re.I)
MD_LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
HTML_LINK = re.compile(r"<(?:a|img)\s+[^>]*(?:href|src)=[\"']([^\"']+)", re.I)
NUMBER = re.compile(r"(?<![A-Za-z_])(?:\d+(?:\.\d+)?(?:/\d+(?:\.\d+)?)?|\d+/\d+)(?![A-Za-z_])")
IDENTIFIER = re.compile(r"\b(?:[A-Z]{2,}[A-Z0-9_-]*|[A-Za-z]+\d+[A-Za-z0-9_-]*|\d+[A-Za-z][A-Za-z0-9_-]*)\b")
LIST_LINE = re.compile(r"^\s*(?:[-*+] |\d+[.)] )")
TABLE_LINE = re.compile(r"^\s*\|.*\|\s*$")
FENCE_START = re.compile(r"^\s*(" + re.escape(chr(96) * 3) + r"+|~~~+)")
ANCHOR_ONLY = re.compile(r"^\s*<a\s+[^>]*(?:id|name)=[\"'][^\"']+[\"'][^>]*>\s*</a>\s*$", re.I)
CODE_SPAN = re.compile(chr(96) + r"([^\n]+?)" + chr(96))


def git_show(path: str) -> str:
    repo_path = str((R01 / path).relative_to(REPO))
    baseline = BASELINE_BY_FILE.get(path, BASELINE_COMMIT)
    completed = subprocess.run(
        ["git", "show", f"{baseline}:{repo_path}"],
        cwd=REPO, capture_output=True, text=True, encoding="utf-8"
    )
    if completed.returncode:
        raise RuntimeError(f"cannot read baseline {baseline}:{repo_path}: {completed.stderr.strip()}")
    return completed.stdout


def fenced_blocks(text: str) -> tuple[list[str], str]:
    lines = text.splitlines(keepends=True)
    blocks: list[str] = []
    visible: list[str] = []
    i = 0
    while i < len(lines):
        start = FENCE_START.match(lines[i])
        if not start:
            visible.append(lines[i])
            i += 1
            continue
        marker = lines[i].lstrip()[0]
        block = [lines[i]]
        i += 1
        while i < len(lines):
            block.append(lines[i])
            if lines[i].lstrip().startswith(marker * 3):
                i += 1
                break
            i += 1
        blocks.append("".join(block))
        visible.append("\n")
    return blocks, "".join(visible)


def display_math_blocks(text: str) -> tuple[list[str], str]:
    parts = text.split("$$")
    if len(parts) % 2 == 0:
        return ["UNBALANCED_DISPLAY_MATH"], text
    blocks = [parts[i] for i in range(1, len(parts), 2)]
    visible = "".join(parts[i] + ("\n" if i < len(parts) - 1 else "") for i in range(0, len(parts), 2))
    return blocks, visible


def links(text: str) -> Counter[str]:
    return Counter(MD_LINK.findall(text) + HTML_LINK.findall(text))


def structural_lines(text: str) -> dict[str, object]:
    code, no_code = fenced_blocks(text)
    math, prose = display_math_blocks(no_code)
    lines = prose.splitlines()
    return {
        "headings": HEADING.findall(prose),
        "anchors": ANCHOR.findall(prose),
        "links": links(prose),
        "numbers": Counter(NUMBER.findall(prose)),
        "code_blocks": code,
        "math_blocks": math,
        "table_lines": [line for line in lines if TABLE_LINE.match(line)],
        "list_lines": [line for line in lines if LIST_LINE.match(line)],
    }


def prose_paragraphs(text: str) -> list[str]:
    _, no_code = fenced_blocks(text)
    _, no_math = display_math_blocks(no_code)
    blocks = re.split(r"\n\s*\n", no_math)
    paragraphs: list[str] = []
    for block in blocks:
        stripped = block.strip()
        if not stripped:
            continue
        lines = stripped.splitlines()
        if all(ANCHOR_ONLY.match(line) for line in lines):
            continue
        if any(HEADING.match(line) for line in lines):
            continue
        if all(TABLE_LINE.match(line) for line in lines):
            continue
        if all(LIST_LINE.match(line) for line in lines):
            continue
        if stripped.startswith("<") and stripped.endswith(">") and "\n" not in stripped:
            continue
        paragraphs.append(stripped)
    return paragraphs


def protected_paragraph_tokens(text: str) -> tuple[Counter[str], Counter[str], Counter[str]]:
    return (
        Counter(CODE_SPAN.findall(text)),
        Counter(IDENTIFIER.findall(text)),
        Counter(NUMBER.findall(text)),
    )


def main() -> int:
    errors: list[str] = []
    checked = 0
    paragraph_pairs = 0

    def check_target(label: str, current_path: Path, baseline: str) -> None:
        nonlocal checked, paragraph_pairs
        if not current_path.exists():
            errors.append(f"{label}: current file missing")
            return
        current = current_path.read_text(encoding="utf-8")
        b = structural_lines(baseline)
        current_struct = structural_lines(current)

        baseline_heading_titles = [title for _, title in b["headings"]]
        current_heading_titles = [title for _, title in current_struct["headings"]]
        if baseline_heading_titles != current_heading_titles:
            errors.append(f"{label}: heading titles/order changed")

        for key in ("anchors", "links", "numbers", "code_blocks", "math_blocks", "table_lines", "list_lines"):
            if b[key] != current_struct[key]:
                errors.append(f"{label}: protected structure changed: {key}")

        bp = prose_paragraphs(baseline)
        cp = prose_paragraphs(current)
        if len(bp) != len(cp):
            errors.append(f"{label}: prose paragraph count changed {len(bp)} -> {len(cp)}")
        else:
            for index, (before, after) in enumerate(zip(bp, cp), start=1):
                paragraph_pairs += 1
                if protected_paragraph_tokens(before) != protected_paragraph_tokens(after):
                    errors.append(f"{label}: paragraph {index} protected tokens changed")
                before_len = max(1, len(before))
                ratio = len(after) / before_len
                if not 0.80 <= ratio <= 1.20:
                    errors.append(
                        f"{label}: paragraph {index} changed length too much "
                        f"({before_len} -> {len(after)}, ratio={ratio:.3f})"
                    )
        checked += 1

    for rel in CURRENT_ROUTE_FILES:
        check_target(rel, R01 / rel, git_show(rel))

    for repo_rel, baseline_commit in EXTERNAL_ROUTE_FILES.items():
        completed = subprocess.run(
            ["git", "show", f"{baseline_commit}:{repo_rel}"],
            cwd=REPO, capture_output=True, text=True, encoding="utf-8"
        )
        if completed.returncode:
            errors.append(f"{repo_rel}: cannot read external baseline {baseline_commit}")
            continue
        check_target(repo_rel, REPO / repo_rel, completed.stdout)

    result = {
        "status": "PASS" if not errors else "FAIL",
        "baseline_commit": BASELINE_COMMIT,
        "files_checked": checked,
        "paragraph_pairs_checked": paragraph_pairs,
        "errors": errors,
    }
    print(result)
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
