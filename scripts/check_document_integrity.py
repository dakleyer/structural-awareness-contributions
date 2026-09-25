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
    "Ecosystem_Positioning_Canonical.pptx": (17, 20000),
    "Ecosystem_Positioning_Architecture_Implementation_Canonical_v1.1.pptx": (8, 10000),
    "Ecosystem_Positioning_Requirements_Evidence_Canonical_v1.1.pptx": (12, 12000),
}


def main() -> int:
    errors: list[str] = []
    checked_links = 0
    for source in ROOT.rglob("*.md"):
        if ".git" in source.parts or "preserved-public-snapshots" in source.parts:
            continue
        body = source.read_text(encoding="utf-8")
        for raw in MARKDOWN_LINK.findall(body) + HTML_LINK.findall(body):
            target = raw.split(" ")[0].strip("<>")
            if not target or target.startswith(EXTERNAL):
                continue
            route = urllib.parse.unquote(target.split("#", 1)[0].split("?", 1)[0])
            checked_links += 1
            if not (source.parent / route).resolve().exists():
                errors.append(f"missing link: {source.relative_to(ROOT)} -> {target}")

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
          f"{len(REQUIRED_SECTIONS)} architecture sections, {len(PRESENTATIONS)} decks)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
