#!/usr/bin/env python3
"""Repair the two canonical Ecosystem Positioning v1.2 PowerPoint decks.

This is intentionally a narrow maintenance operation:

* normalize the existing committed PPTX packages through LibreOffice Impress;
* preserve slide count, slide text and hyperlinks except for explicitly approved
  wording corrections listed below;
* fix the specific text-box geometry/wrapping defects found in the 28 Sep 2026
  slide-by-slide render audit;
* keep the same canonical v1.2 filenames so Git history remains the version
  lineage and existing public links do not break.

The script must be run from the repository checkout. It modifies only the two
v1.2 PPTX files in ``presentations/ecosystem-positioning``.
"""
from __future__ import annotations

import collections
import re
import shutil
import subprocess
import tempfile
import zipfile
from pathlib import Path

from pptx import Presentation
from pptx.enum.dml import MSO_THEME_COLOR
from pptx.enum.text import MSO_ANCHOR
from pptx.util import Inches, Pt

ROOT = Path(__file__).resolve().parents[1]
PRESENTATION_DIR = ROOT / "presentations" / "ecosystem-positioning"
ARCH = PRESENTATION_DIR / "Ecosystem_Positioning_Architecture_Implementation_Canonical_v1.2.pptx"
REQ = PRESENTATION_DIR / "Ecosystem_Positioning_Requirements_Evidence_Canonical_v1.2.pptx"

EXPECTED_SLIDES = {ARCH.name: 7, REQ.name: 12}

DBC_OLD = "https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/DECISION_BOUNDARY_CHALLENGE_v0.2.md#10-ranking-and-review-rule"
DBC_NEW = "https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/DECISION_BOUNDARY_CHALLENGE_v0.2.md#10-comparative-review-rule"

APPROVED_TEXT_REPLACEMENTS = {
    "V1.1 · 2026-09-25": "V1.2 · 2026-09-28",
    "conformance sufficiency": "A23 conformance audit (partial)",
    "PUBLIC RANKING / APPLIED VALIDATION": "APPLIED VALIDATION / EVIDENCE MATURITY",
    "Decision Boundary Challenge v0.2 — public ranking-by-evidence": "Decision Boundary Challenge v0.2 — Not a ranking",
    "Public ranking · DBC v0.2": "Applied validation · DBC v0.2",
}


def run(*args: str) -> None:
    proc = subprocess.run(args, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    if proc.returncode:
        raise RuntimeError(f"command failed ({proc.returncode}): {' '.join(args)}\n{proc.stdout}")


def normalize_whitespace(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def all_slide_text(path: Path) -> str:
    prs = Presentation(path)
    pieces: list[str] = []
    for slide in prs.slides:
        for shape in slide.shapes:
            if getattr(shape, "has_text_frame", False):
                pieces.append(shape.text)
    return normalize_whitespace(" ".join(pieces))


def hyperlinks(path: Path) -> collections.Counter[str]:
    prs = Presentation(path)
    result: collections.Counter[str] = collections.Counter()
    for slide in prs.slides:
        for shape in slide.shapes:
            if not getattr(shape, "has_text_frame", False):
                continue
            for paragraph in shape.text_frame.paragraphs:
                for run_ in paragraph.runs:
                    if run_.hyperlink.address:
                        result[run_.hyperlink.address] += 1
    return result


def zip_and_slide_count(path: Path) -> int:
    with zipfile.ZipFile(path) as deck:
        bad = deck.testzip()
        if bad:
            raise RuntimeError(f"corrupt ZIP member in {path.name}: {bad}")
        slides = [
            name for name in deck.namelist()
            if re.fullmatch(r"ppt/slides/slide\d+\.xml", name)
        ]
        return len(slides)


def replace_run_text(run_, old: str, new: str, *, hyperlink: str | None = None) -> bool:
    if old not in run_.text:
        return False
    run_.text = run_.text.replace(old, new)
    if hyperlink is not None:
        run_.hyperlink.address = hyperlink
    return True


def set_paragraph_size(paragraph, pt: float) -> None:
    for run_ in paragraph.runs:
        run_.font.size = Pt(pt)


def compact_paragraph(paragraph) -> None:
    paragraph.space_before = Pt(0)
    paragraph.space_after = Pt(0)


def split_linked_detail(paragraph, lines: list[str], *, font_pt: float) -> None:
    """Keep one logical detail paragraph but add explicit OOXML line breaks.

    This prevents desktop renderers from breaking identifiers such as
    ReceivedSignals, P1/P2/P3 or commands in the middle of the word.
    """
    if not paragraph.runs:
        raise RuntimeError("expected linked detail run")
    first = paragraph.runs[0]
    link = first.hyperlink.address
    first.text = lines[0]
    first.font.size = Pt(font_pt)
    for text in lines[1:]:
        paragraph.add_line_break()
        extra = paragraph.add_run()
        extra.text = text
        extra.font.size = Pt(font_pt)
        if link:
            extra.hyperlink.address = link
            extra.font.underline = True
            extra.font.color.theme_color = MSO_THEME_COLOR.HYPERLINK


def repair_architecture(path: Path) -> None:
    prs = Presentation(path)
    if len(prs.slides) != 7:
        raise RuntimeError(f"unexpected architecture slide count: {len(prs.slides)}")

    # Cover metadata only; no claim/content change.
    for shape in prs.slides[0].shapes:
        if getattr(shape, "has_text_frame", False):
            for paragraph in shape.text_frame.paragraphs:
                for run_ in paragraph.runs:
                    replace_run_text(run_, "V1.1 · 2026-09-25", "V1.2 · 2026-09-28")

    # Slide 2: the seven narrow process cards were wrapping mid-word in the
    # committed v1.2 binary. Give them a little more height and insert semantic
    # hard breaks only in the detail line; headings and hyperlinks stay intact.
    slide = prs.slides[1]
    for idx in range(10, 17):  # shapes 11..17 in human numbering
        shape = slide.shapes[idx]
        shape.height = Inches(0.95)
        tf = shape.text_frame
        tf.margin_left = Inches(0.035)
        tf.margin_right = Inches(0.035)
        tf.margin_top = Inches(0.02)
        tf.margin_bottom = Inches(0.02)
        tf.vertical_anchor = MSO_ANCHOR.MIDDLE
        for pi, paragraph in enumerate(tf.paragraphs):
            compact_paragraph(paragraph)
            set_paragraph_size(paragraph, 8.0 if pi < 2 else 7.0)
        if idx == 10:
            set_paragraph_size(tf.paragraphs[0], 7.6)

    detail_lines = {
        11: ["Qualify / exchange", "ReceivedSignals"],
        13: ["Emit Δ_RA + regime", "overlay"],
        14: ["Role_effective · Type 0/1/2", "· P1/P2/P3"],
        15: ["Rank from Role_effective →", "ACC gate → re-contract /", "escalate"],
        16: ["Authority decides;", "signals ≠ commands"],
    }
    for shape_index, lines in detail_lines.items():
        split_linked_detail(slide.shapes[shape_index].text_frame.paragraphs[2], lines, font_pt=7.0)

    # Slide 5: four upper context cards spilled below their rounded rectangles.
    slide = prs.slides[4]
    for idx in range(2, 6):  # shapes 3..6
        shape = slide.shapes[idx]
        shape.height = Inches(0.84)
        tf = shape.text_frame
        tf.margin_top = Inches(0.025)
        tf.margin_bottom = Inches(0.025)
        for pi, paragraph in enumerate(tf.paragraphs):
            compact_paragraph(paragraph)
            if pi >= 1:
                set_paragraph_size(paragraph, 7.2)

    prs.save(path)


def repair_requirements(path: Path) -> None:
    prs = Presentation(path)
    if len(prs.slides) != 12:
        raise RuntimeError(f"unexpected requirements slide count: {len(prs.slides)}")

    # Cover metadata.
    for shape in prs.slides[0].shapes:
        if getattr(shape, "has_text_frame", False):
            for paragraph in shape.text_frame.paragraphs:
                for run_ in paragraph.runs:
                    replace_run_text(run_, "V1.1 · 2026-09-25", "V1.2 · 2026-09-28")

    # Slide 6: Type-1 label broke inside "uncertainty".
    for shape in prs.slides[5].shapes:
        if not getattr(shape, "has_text_frame", False):
            continue
        for paragraph in shape.text_frame.paragraphs:
            if paragraph.text.startswith("TYPE 1 · Unbounded unresolved uncertainty"):
                set_paragraph_size(paragraph, 12.0)

    # Slide 9: current A23 result is partial/conformance-audit evidence, not an
    # all-six sufficiency claim. This wording is already the current README claim
    # boundary; the smaller bar font keeps the line inside its container.
    for shape in prs.slides[8].shapes:
        if not getattr(shape, "has_text_frame", False):
            continue
        for paragraph in shape.text_frame.paragraphs:
            for run_ in paragraph.runs:
                replace_run_text(run_, "conformance sufficiency", "A23 conformance audit (partial)")
        if "379/379 symbolic campaign" in shape.text:
            for paragraph in shape.text_frame.paragraphs:
                set_paragraph_size(paragraph, 9.5)

    # Slide 12: align the DBC labels with the current document boundary.
    for shape in prs.slides[11].shapes:
        if not getattr(shape, "has_text_frame", False):
            continue
        for paragraph in shape.text_frame.paragraphs:
            for run_ in paragraph.runs:
                replace_run_text(run_, "PUBLIC RANKING / APPLIED VALIDATION", "APPLIED VALIDATION / EVIDENCE MATURITY")
                replace_run_text(
                    run_,
                    "Decision Boundary Challenge v0.2 — public ranking-by-evidence",
                    "Decision Boundary Challenge v0.2 — Not a ranking",
                    hyperlink=DBC_NEW,
                )
                replace_run_text(run_, "Public ranking · DBC v0.2", "Applied validation · DBC v0.2")

    prs.save(path)


def normalize_with_libreoffice(source: Path, destination_dir: Path) -> Path:
    run(
        "libreoffice",
        "--headless",
        "--convert-to",
        "pptx",
        "--outdir",
        str(destination_dir),
        str(source),
    )
    converted = destination_dir / source.name
    if not converted.exists():
        raise RuntimeError(f"LibreOffice did not produce {converted}")
    return converted


def expected_text(source_text: str, *, requirements: bool) -> str:
    value = source_text
    value = value.replace("V1.1 · 2026-09-25", "V1.2 · 2026-09-28")
    if requirements:
        for old, new in APPROVED_TEXT_REPLACEMENTS.items():
            value = value.replace(old, new)
    return normalize_whitespace(value)


def main() -> int:
    for deck in (ARCH, REQ):
        if not deck.exists():
            raise FileNotFoundError(deck)
        if zip_and_slide_count(deck) != EXPECTED_SLIDES[deck.name]:
            raise RuntimeError(f"unexpected source slide count: {deck.name}")

    before_text = {deck.name: all_slide_text(deck) for deck in (ARCH, REQ)}
    before_links = {deck.name: hyperlinks(deck) for deck in (ARCH, REQ)}

    with tempfile.TemporaryDirectory(prefix="ep-pptx-normalize-") as tmp:
        tmpdir = Path(tmp)
        norm_arch = normalize_with_libreoffice(ARCH, tmpdir)
        # LibreOffice refuses to overwrite a converted file of the same name;
        # move this one out before converting the second deck.
        staged_arch = tmpdir / "architecture.normalized.pptx"
        norm_arch.rename(staged_arch)
        norm_req = normalize_with_libreoffice(REQ, tmpdir)
        staged_req = tmpdir / "requirements.normalized.pptx"
        norm_req.rename(staged_req)

        repair_architecture(staged_arch)
        repair_requirements(staged_req)

        # Structural/package checks before replacing the canonical files.
        if zip_and_slide_count(staged_arch) != EXPECTED_SLIDES[ARCH.name]:
            raise RuntimeError("architecture repair changed slide count")
        if zip_and_slide_count(staged_req) != EXPECTED_SLIDES[REQ.name]:
            raise RuntimeError("requirements repair changed slide count")

        after_text_arch = all_slide_text(staged_arch)
        after_text_req = all_slide_text(staged_req)
        if after_text_arch != expected_text(before_text[ARCH.name], requirements=False):
            raise RuntimeError("unexpected architecture text change")
        if after_text_req != expected_text(before_text[REQ.name], requirements=True):
            raise RuntimeError("unexpected requirements text change")

        # Hyperlinks must be preserved exactly, apart from the deliberately
        # renamed DBC heading anchor.
        after_links_arch = hyperlinks(staged_arch)
        if after_links_arch != before_links[ARCH.name]:
            raise RuntimeError("architecture hyperlink set changed")

        expected_req_links = before_links[REQ.name].copy()
        if expected_req_links[DBC_OLD]:
            count = expected_req_links[DBC_OLD]
            del expected_req_links[DBC_OLD]
            expected_req_links[DBC_NEW] += count
        after_links_req = hyperlinks(staged_req)
        if after_links_req != expected_req_links:
            raise RuntimeError("requirements hyperlink set changed unexpectedly")

        shutil.copy2(staged_arch, ARCH)
        shutil.copy2(staged_req, REQ)

    print(f"Repaired {ARCH.relative_to(ROOT)}")
    print(f"Repaired {REQ.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
