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
    "README.md": "e740126897a3952927de1991f0aeae3fc46aa997",
    "COMPUTABILITY_AND_ORACLE_PLAN.md": "5ca951ceb17ecca036ed9ea37357fd8c4a5761bb",
    "feasibility/WORKPLAN.md": "2b2f3f656da5d25f79c782d7d5d60f286c5fbbc7",
    "oracle/README.md": "c7eee86425f7d3cf44c0478708252bc430222648",
    "oracle/UC4_INTEROPERABILITY_PROFILE.md": "26d1e12c9faa2636c47015a243d02a5e927f4c6a",
    "oracle/NELSON_REVIEW_REQUEST.md": "84f2283cc6c58c970fef56bd3d58c90bbce9b4ab",
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

    for rel in CURRENT_ROUTE_FILES:
        current_path = R01 / rel
        if not current_path.exists():
            errors.append(f"{rel}: current file missing")
            continue
        baseline = git_show(rel)
        current = current_path.read_text(encoding="utf-8")
        b = structural_lines(baseline)
        c = structural_lines(current)

        baseline_heading_titles = [title for _, title in b["headings"]]
        current_heading_titles = [title for _, title in c["headings"]]
        if baseline_heading_titles != current_heading_titles:
            errors.append(f"{rel}: heading titles/order changed")

        for key in ("anchors", "links", "numbers", "code_blocks", "math_blocks", "table_lines", "list_lines"):
            if b[key] != c[key]:
                errors.append(f"{rel}: protected structure changed: {key}")

        bp = prose_paragraphs(baseline)
        cp = prose_paragraphs(current)
        if len(bp) != len(cp):
            errors.append(f"{rel}: prose paragraph count changed {len(bp)} -> {len(cp)}")
        else:
            for index, (before, after) in enumerate(zip(bp, cp), start=1):
                paragraph_pairs += 1
                if protected_paragraph_tokens(before) != protected_paragraph_tokens(after):
                    errors.append(f"{rel}: paragraph {index} protected tokens changed")
                before_len = max(1, len(before))
                ratio = len(after) / before_len
                if not 0.80 <= ratio <= 1.20:
                    errors.append(
                        f"{rel}: paragraph {index} changed length too much "
                        f"({before_len} -> {len(after)}, ratio={ratio:.3f})"
                    )
        checked += 1

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
