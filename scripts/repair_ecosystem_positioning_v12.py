#!/usr/bin/env python3
"""Deterministically repair the two canonical Ecosystem Positioning v1.2 decks.

The maintenance operation is intentionally narrow: normalize each committed
PPTX through a desktop office engine, repair only the layout defects found in
the 28 Sep 2026 slide-by-slide audit, preserve all hyperlink destinations, and
make only the explicitly listed wording corrections. Existing filenames stay
unchanged so public links and Git history remain the version lineage.
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
    """Return semantic hyperlink destinations, independent of run splitting.

    A visual hard line break can legitimately turn one hyperlink run into two
    runs pointing to the same target. Destination-set equality therefore tests
    that no route is lost without treating that visual repair as a link change.
    """
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


def compact(paragraph) -> None:
    paragraph.space_before = Pt(0)
    paragraph.space_after = Pt(0)


def split_linked_detail(paragraph, lines: list[str], font_pt: float = 7.0) -> None:
    if not paragraph.runs:
        raise RuntimeError("expected linked process-detail run")
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

    # Cover: correct the displayed v1.2 revision/date only.
    for shape in prs.slides[0].shapes:
        if getattr(shape, "has_text_frame", False):
            for paragraph in shape.text_frame.paragraphs:
                for run_ in paragraph.runs:
                    replace_text(run_, "V1.1 · 2026-09-25", "V1.2 · 2026-09-28")

    # Slide 2: narrow process cards previously broke identifiers mid-word.
    slide = prs.slides[1]
    for idx in range(10, 17):  # human shapes 11..17
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
        split_linked_detail(slide.shapes[shape_index].text_frame.paragraphs[2], lines)

    # Slide 5: top context cards previously spilled below their containers.
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

    for shape in prs.slides[0].shapes:
        if getattr(shape, "has_text_frame", False):
            for paragraph in shape.text_frame.paragraphs:
                for run_ in paragraph.runs:
                    replace_text(run_, "V1.1 · 2026-09-25", "V1.2 · 2026-09-28")

    # Slide 6: prevent Type-1 heading breaking inside "uncertainty".
    for shape in prs.slides[5].shapes:
        if getattr(shape, "has_text_frame", False):
            for paragraph in shape.text_frame.paragraphs:
                if paragraph.text.startswith("TYPE 1 · Unbounded unresolved uncertainty"):
                    set_size(paragraph, 12.0)

    # Slide 9: use the current bounded A23 claim and keep the integrated-check
    # strip on one line.
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

        # Preserve every unique destination. Extra runs created by explicit line
        # breaks may repeat the same destination and are intentionally ignored.
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
