#!/usr/bin/env python3
"""Finalize residual cross-renderer layout defects in the two canonical EP v1.2 decks.

This post-repair pass is intentionally geometry-only. It fixes defects confirmed
by slide-by-slide rendering on 28 Sep 2026, while asserting that slide text and
hyperlink destinations remain unchanged.
"""
from __future__ import annotations

import re
import zipfile
from pathlib import Path

from pptx import Presentation
from pptx.util import Inches, Pt

ROOT = Path(__file__).resolve().parents[1]
PRESENTATION_DIR = ROOT / "presentations" / "ecosystem-positioning"
ARCH = PRESENTATION_DIR / "Ecosystem_Positioning_Architecture_Implementation_Canonical_v1.2.pptx"
REQ = PRESENTATION_DIR / "Ecosystem_Positioning_Requirements_Evidence_Canonical_v1.2.pptx"


def norm(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def all_text(path: Path) -> str:
    prs = Presentation(path)
    return norm(" ".join(
        shape.text
        for slide in prs.slides
        for shape in slide.shapes
        if getattr(shape, "has_text_frame", False)
    ))


def links(path: Path) -> set[str]:
    prs = Presentation(path)
    result: set[str] = set()
    for slide in prs.slides:
        for shape in slide.shapes:
            if not getattr(shape, "has_text_frame", False):
                continue
            for paragraph in shape.text_frame.paragraphs:
                for run in paragraph.runs:
                    if run.hyperlink.address:
                        result.add(run.hyperlink.address)
    return result


def compact_and_size(shape, pt: float) -> None:
    for paragraph in shape.text_frame.paragraphs:
        paragraph.space_before = Pt(0)
        paragraph.space_after = Pt(0)
        for run in paragraph.runs:
            run.font.size = Pt(pt)


def unique_text_shape(slide, text: str):
    matches = [
        shape for shape in slide.shapes
        if getattr(shape, "has_text_frame", False) and norm(shape.text) == text
    ]
    if len(matches) != 1:
        raise RuntimeError(f"expected exactly one shape for {text!r}, found {len(matches)}")
    return matches[0]


def validate_zip(path: Path, expected_slides: int) -> None:
    with zipfile.ZipFile(path) as zf:
        bad = zf.testzip()
        if bad:
            raise RuntimeError(f"corrupt ZIP member in {path.name}: {bad}")
        slides = [n for n in zf.namelist() if re.fullmatch(r"ppt/slides/slide\d+\.xml", n)]
        if len(slides) != expected_slides:
            raise RuntimeError(f"unexpected slide count in {path.name}: {len(slides)}")


def finalize_architecture(path: Path) -> None:
    prs = Presentation(path)
    if len(prs.slides) != 7:
        raise RuntimeError(f"unexpected architecture slide count: {len(prs.slides)}")
    slide = prs.slides[2]

    # Slide 3: the citizenship qualifier wrapped into a box too shallow for
    # desktop-office font metrics, clipping its second line.
    shape = unique_text_shape(slide, "Defines admissible conditions — not each trajectory")
    shape.left = Inches(0.96)
    shape.top = Inches(3.535)
    shape.width = Inches(2.66)
    shape.height = Inches(0.22)
    compact_and_size(shape, 6.6)

    # Slide 3: the MSCA explanatory sentence also wrapped to two lines but its
    # original text box was one-line high, making the final word appear clipped.
    shape = unique_text_shape(slide, "Control sufficiency; never creates authority.")
    shape.top = Inches(4.75)
    shape.height = Inches(0.31)
    compact_and_size(shape, 8.0)

    prs.save(path)


def finalize_requirements(path: Path) -> None:
    prs = Presentation(path)
    if len(prs.slides) != 12:
        raise RuntimeError(f"unexpected requirements slide count: {len(prs.slides)}")
    slide = prs.slides[5]

    # Slide 6: keep the complete TYPE 1 heading on one line so renderers do not
    # split "uncertainty" in the middle of the word.
    shape = unique_text_shape(slide, "TYPE 1 · Unbounded unresolved uncertainty")
    shape.left = Inches(4.90)
    shape.width = Inches(3.59)
    shape.height = Inches(0.32)
    compact_and_size(shape, 9.5)

    prs.save(path)


def main() -> int:
    for path, count in ((ARCH, 7), (REQ, 12)):
        validate_zip(path, count)

    before_text = {p.name: all_text(p) for p in (ARCH, REQ)}
    before_links = {p.name: links(p) for p in (ARCH, REQ)}

    finalize_architecture(ARCH)
    finalize_requirements(REQ)

    for path, count in ((ARCH, 7), (REQ, 12)):
        validate_zip(path, count)
        if all_text(path) != before_text[path.name]:
            raise RuntimeError(f"unexpected text change in {path.name}")
        if links(path) != before_links[path.name]:
            raise RuntimeError(f"unexpected hyperlink change in {path.name}")

    print(f"Finalized residual layout: {ARCH.relative_to(ROOT)}")
    print(f"Finalized residual layout: {REQ.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
