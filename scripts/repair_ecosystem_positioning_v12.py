#!/usr/bin/env python3
"""Deterministically repair the two canonical Ecosystem Positioning v1.2 decks.

The operation is deliberately narrow: normalize the committed PPTX packages
through a desktop office engine, repair only the layout defects found in the
28 Sep 2026 slide-by-slide audit, preserve all hyperlink destinations, and make
only the explicitly approved wording corrections. The canonical filenames stay
unchanged so Git history remains the version lineage.
"""
from __future__ import annotations

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

REQ_REPLACEMENTS = {
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


def norm(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def slide_text(path: Path) -> str:
    prs = Presentation(path)
    return norm(" ".join(
        shape.text
        for slide in prs.slides
        for shape in slide.shapes
        if getattr(shape, "has_text_frame", False)
    ))


def link_destinations(path: Path) -> set[str]:
    """Return semantic hyperlink destinations, independent of run splitting."""
    prs = Presentation(path)
    result: set[str] = set()
    for slide in prs.slides:
        for shape in slide.shapes:
            if not getattr(shape, "has_text_frame", False):
                continue
            for paragraph in shape.text_frame.paragraphs:
                for run_ in paragraph.runs:
                    if run_.hyperlink.address:
                        result.add(run_.hyperlink.address)
    return result


def zip_slide_count(path: Path) -> int:
    with zipfile.ZipFile(path) as deck:
        bad = deck.testzip()
        if bad:
            raise RuntimeError(f"corrupt ZIP member in {path.name}: {bad}")
        return len([
            name for name in deck.namelist()
            if re.fullmatch(r"ppt/slides/slide\d+\.xml", name)
        ])


def replace_text(run_, old: str, new: str, hyperlink: str | None = None) -> bool:
    if old not in run_.text:
        return False
    run_.text = run_.text.replace(old, new)
    if hyperlink is not None:
        run_.hyperlink.address = hyperlink
    return True


def set_size(paragraph, pt: float) -> None:
    for run_ in paragraph.runs:
        run_.font.size = Pt(pt)


def set_shape_size(shape, pt: float) -> None:
    if not getattr(shape, "has_text_frame", False):
        return
    for paragraph in shape.text_frame.paragraphs:
        set_size(paragraph, pt)


def compact(paragraph) -> None:
    paragraph.space_before = Pt(0)
    paragraph.space_after = Pt(0)


def rebuild_linked_lines(paragraph, lines: list[str], *, font_pt: float) -> None:
    """Rebuild one linked paragraph with deterministic hard line breaks.

    This is idempotent: a second repair pass replaces the prior runs rather than
    appending another set of breaks.
    """
    if not paragraph.runs:
        raise RuntimeError("expected linked paragraph")
    source_runs = list(paragraph.runs)
    link = next((run_.hyperlink.address for run_ in source_runs if run_.hyperlink.address), None)
    bold = next((run_.font.bold for run_ in source_runs if run_.font.bold is not None), None)
    italic = next((run_.font.italic for run_ in source_runs if run_.font.italic is not None), None)
    paragraph.clear()
    compact(paragraph)
    for idx, text in enumerate(lines):
        if idx:
            paragraph.add_line_break()
        new_run = paragraph.add_run()
        new_run.text = text
        new_run.font.size = Pt(font_pt)
        if bold is not None:
            new_run.font.bold = bold
        if italic is not None:
            new_run.font.italic = italic
        if link:
            new_run.hyperlink.address = link
            new_run.font.underline = True
            new_run.font.color.theme_color = MSO_THEME_COLOR.HYPERLINK


def repair_cover(slide) -> None:
    """Make the shared cover robust to PowerPoint/LibreOffice font metrics."""
    for shape in slide.shapes:
        if not getattr(shape, "has_text_frame", False):
            continue
        if norm(shape.text) == "Ecosystem Positioning for Agentic Systems":
            shape.width = Inches(8.0)
            shape.height = Inches(1.46)
            tf = shape.text_frame
            tf.margin_left = 0
            tf.margin_right = 0
            tf.margin_top = 0
            tf.margin_bottom = 0
            for paragraph in tf.paragraphs:
                compact(paragraph)
                set_size(paragraph, 40.0)


def repair_architecture(path: Path) -> None:
    prs = Presentation(path)
    if len(prs.slides) != 7:
        raise RuntimeError(f"unexpected architecture slide count: {len(prs.slides)}")

    # Cover metadata and cross-renderer title sizing.
    repair_cover(prs.slides[0])
    for shape in prs.slides[0].shapes:
        if getattr(shape, "has_text_frame", False):
            for paragraph in shape.text_frame.paragraphs:
                for run_ in paragraph.runs:
                    replace_text(run_, "V1.1 · 2026-09-25", "V1.2 · 2026-09-28")

    # Slide 2: narrow process cards use explicit semantic breaks rather than
    # allowing the renderer to split identifiers in the middle of a word.
    slide = prs.slides[1]
    for idx in range(10, 17):
        shape = slide.shapes[idx]
        shape.height = Inches(0.95)
        tf = shape.text_frame
        tf.margin_left = Inches(0.035)
        tf.margin_right = Inches(0.035)
        tf.margin_top = Inches(0.02)
        tf.margin_bottom = Inches(0.02)
        tf.vertical_anchor = MSO_ANCHOR.MIDDLE
        for pi, paragraph in enumerate(tf.paragraphs):
            compact(paragraph)
            set_size(paragraph, 8.0 if pi < 2 else 7.0)
        if idx == 10:
            set_size(tf.paragraphs[0], 7.6)

    details = {
        11: ["Qualify / exchange", "ReceivedSignals"],
        13: ["Emit Δ_RA + regime", "overlay"],
        14: ["Role_effective · Type 0/1/2", "· P1/P2/P3"],
        15: ["Rank from Role_effective →", "ACC gate → re-contract /", "escalate"],
        16: ["Authority decides;", "signals ≠ commands"],
    }
    for shape_index, lines in details.items():
        rebuild_linked_lines(slide.shapes[shape_index].text_frame.paragraphs[2], lines, font_pt=7.0)

    # Slide 5: top context cards need enough vertical space under substitute
    # desktop fonts.
    slide = prs.slides[4]
    for idx in range(2, 6):
        shape = slide.shapes[idx]
        shape.height = Inches(0.84)
        tf = shape.text_frame
        tf.margin_top = Inches(0.025)
        tf.margin_bottom = Inches(0.025)
        for pi, paragraph in enumerate(tf.paragraphs):
            compact(paragraph)
            if pi >= 1:
                set_size(paragraph, 7.2)

    prs.save(path)


def repair_requirements(path: Path) -> None:
    prs = Presentation(path)
    if len(prs.slides) != 12:
        raise RuntimeError(f"unexpected requirements slide count: {len(prs.slides)}")

    # Cover.
    repair_cover(prs.slides[0])
    for shape in prs.slides[0].shapes:
        if getattr(shape, "has_text_frame", False):
            for paragraph in shape.text_frame.paragraphs:
                for run_ in paragraph.runs:
                    replace_text(run_, "V1.1 · 2026-09-25", "V1.2 · 2026-09-28")

    # Slide 4: scenario-card headings must remain whole words. A fixed 10.5 pt
    # size fits all six headings in the existing 2.92-inch title boxes under
    # both the GitHub runner and desktop-office font metrics.
    slide = prs.slides[3]
    scenario_titles = {
        "The 100 Million Token Enterprise",
        "Chaos in the Smartcity",
        "Ciber Napoleon Goes to Russia",
        "The Quiet Four Thousand",
        "The Patch That Undid the Fix",
        "The Author Pays for His Own Work",
    }
    for shape in slide.shapes:
        if getattr(shape, "has_text_frame", False) and norm(shape.text) in scenario_titles:
            shape.height = Inches(0.24)
            set_shape_size(shape, 10.5)

    # Slide 5: keep the long title on one line, prevent the 00G label from
    # colliding with its technology link, and give the two multi-line trajectory
    # headings their own vertical space before the body copy starts.
    slide = prs.slides[4]
    for shape in slide.shapes:
        if not getattr(shape, "has_text_frame", False):
            continue
        text = norm(shape.text)
        if text == "Technology used in the scenario routes and the three validation trajectories":
            shape.height = Inches(0.38)
            set_shape_size(shape, 18.5)
        elif text.startswith("00G Ciber Napoleon Goes to Russia"):
            shape.height = Inches(0.22)
            set_shape_size(shape, 9.8)
        elif text == "OpenAI Agents SDK / Agents API / Responses multi-agent stack":
            shape.top = Inches(4.08)
        elif text == "Defended / top-notch implementation":
            shape.height = Inches(0.32)
            set_shape_size(shape, 9.2)
        elif text.startswith("Strong implementation with explicit controls"):
            shape.top = Inches(5.94)
            shape.height = Inches(0.38)
            set_shape_size(shape, 8.5)
        elif text == "Frozen defended implementation under drift":
            shape.height = Inches(0.32)
            set_shape_size(shape, 9.0)
        elif text.startswith("The same defended implementation is frozen"):
            shape.top = Inches(5.94)
            shape.height = Inches(0.38)
            set_shape_size(shape, 8.3)

    # Slide 6: expand all three failure-type cards rather than squeezing the
    # explanatory text, and use one robust heading size across the row.
    slide = prs.slides[5]
    for idx in (19, 20, 23, 24, 27, 28):
        slide.shapes[idx].height = Inches(2.05)
    for idx in (21, 25, 29):
        shape = slide.shapes[idx]
        shape.height = Inches(0.38)
        set_shape_size(shape, 10.5)
    for idx in (22, 26, 30):
        shape = slide.shapes[idx]
        shape.top = Inches(4.52)
        shape.height = Inches(1.48)
        set_shape_size(shape, 8.8)
        for paragraph in shape.text_frame.paragraphs:
            compact(paragraph)

    # Slide 7: the title is intentionally one line; the previous auto-wrap put
    # “contract.” on a second line on top of the subtitle.
    slide = prs.slides[6]
    for shape in slide.shapes:
        if getattr(shape, "has_text_frame", False) and norm(shape.text) == "Six severe failure routes. Fourteen requirements. One common contract.":
            shape.height = Inches(0.42)
            set_shape_size(shape, 18.0)

    # Slide 8: six compact route buttons should remain one-line labels.
    slide = prs.slides[7]
    for shape in slide.shapes:
        if not getattr(shape, "has_text_frame", False):
            continue
        text = norm(shape.text)
        if re.fullmatch(r"00[EFGHIJ] · .+", text):
            set_shape_size(shape, 7.0)

    # Slide 9: current A23 result is a partial conformance-audit result, not an
    # all-six sufficiency claim; keep the integrated-check strip on one line.
    for shape in prs.slides[8].shapes:
        if not getattr(shape, "has_text_frame", False):
            continue
        for paragraph in shape.text_frame.paragraphs:
            for run_ in paragraph.runs:
                replace_text(run_, "conformance sufficiency", "A23 conformance audit (partial)")
        if "379/379 symbolic campaign" in shape.text:
            for paragraph in shape.text_frame.paragraphs:
                set_size(paragraph, 9.5)

    # Slide 12: align DBC labels with the current “Not a ranking” boundary.
    for shape in prs.slides[11].shapes:
        if not getattr(shape, "has_text_frame", False):
            continue
        for paragraph in shape.text_frame.paragraphs:
            for run_ in paragraph.runs:
                replace_text(run_, "PUBLIC RANKING / APPLIED VALIDATION", "APPLIED VALIDATION / EVIDENCE MATURITY")
                replace_text(
                    run_,
                    "Decision Boundary Challenge v0.2 — public ranking-by-evidence",
                    "Decision Boundary Challenge v0.2 — Not a ranking",
                    DBC_NEW,
                )
                replace_text(run_, "Public ranking · DBC v0.2", "Applied validation · DBC v0.2")

    prs.save(path)


def libreoffice_normalize(source: Path, outdir: Path) -> Path:
    run("libreoffice", "--headless", "--convert-to", "pptx", "--outdir", str(outdir), str(source))
    result = outdir / source.name
    if not result.exists():
        raise RuntimeError(f"LibreOffice did not produce {result}")
    return result


def expected_text(before: str, requirements: bool) -> str:
    value = before.replace("V1.1 · 2026-09-25", "V1.2 · 2026-09-28")
    if requirements:
        for old, new in REQ_REPLACEMENTS.items():
            value = value.replace(old, new)
    return norm(value)


def main() -> int:
    for deck in (ARCH, REQ):
        if not deck.exists():
            raise FileNotFoundError(deck)
        if zip_slide_count(deck) != EXPECTED_SLIDES[deck.name]:
            raise RuntimeError(f"unexpected source slide count: {deck.name}")

    before_text = {deck.name: slide_text(deck) for deck in (ARCH, REQ)}
    before_links = {deck.name: link_destinations(deck) for deck in (ARCH, REQ)}

    with tempfile.TemporaryDirectory(prefix="ep-pptx-repair-") as tmp:
        tmpdir = Path(tmp)

        arch_norm = libreoffice_normalize(ARCH, tmpdir)
        arch_stage = tmpdir / "architecture.normalized.pptx"
        arch_norm.rename(arch_stage)

        req_norm = libreoffice_normalize(REQ, tmpdir)
        req_stage = tmpdir / "requirements.normalized.pptx"
        req_norm.rename(req_stage)

        repair_architecture(arch_stage)
        repair_requirements(req_stage)

        if zip_slide_count(arch_stage) != 7 or zip_slide_count(req_stage) != 12:
            raise RuntimeError("repair changed slide count")

        if slide_text(arch_stage) != expected_text(before_text[ARCH.name], False):
            raise RuntimeError("unexpected architecture text change")
        if slide_text(req_stage) != expected_text(before_text[REQ.name], True):
            raise RuntimeError("unexpected requirements text change")

        if link_destinations(arch_stage) != before_links[ARCH.name]:
            raise RuntimeError("architecture hyperlink destinations changed")

        expected_req = set(before_links[REQ.name])
        if DBC_OLD in expected_req:
            expected_req.remove(DBC_OLD)
            expected_req.add(DBC_NEW)
        if link_destinations(req_stage) != expected_req:
            raise RuntimeError("requirements hyperlink destinations changed unexpectedly")

        shutil.copy2(arch_stage, ARCH)
        shutil.copy2(req_stage, REQ)

    print(f"Repaired {ARCH.relative_to(ROOT)}")
    print(f"Repaired {REQ.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
