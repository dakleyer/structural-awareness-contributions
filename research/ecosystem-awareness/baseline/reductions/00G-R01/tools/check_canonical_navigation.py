#!/usr/bin/env python3
"""Check local links and anchors from the current R01 entry documents.

This intentionally checks the current canonical entry surface rather than every
historical snapshot. Historical proof guides and previous-work records are preserved
for provenance and are outside this navigation gate.
"""
from __future__ import annotations

from pathlib import Path
import re
import sys
import urllib.parse

R01 = Path(__file__).resolve().parents[1]
REPO = R01.parents[4]

ENTRY_DOCS = (
    R01 / "README.md",
    R01 / "extensions/hugging-face/README.md",
    R01 / "extensions/infoblox/README.md",
    R01 / "extensions/family/README.md",
)

MARKDOWN_LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
HTML_LINK = re.compile(r"<(?:a|img)\s+[^>]*(?:href|src)=[\"']([^\"']+)", re.I)
EXPLICIT_ANCHOR = re.compile(r"<a\s+[^>]*(?:id|name)=[\"']([^\"']+)[\"'][^>]*>", re.I)
HEADING = re.compile(r"^(#{1,6})\s+(.+?)\s*$", re.M)
EXTERNAL_PREFIXES = ("http:", "https:", "mailto:", "data:", "javascript:", "//")


def githubish_slug(text: str) -> str:
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"[\x60*_~]", "", text)
    text = text.strip().lower()
    chars = []
    for ch in text:
        if ch.isalnum() or ch in (" ", "-", "_"):
            chars.append(ch)
    slug = "".join(chars)
    slug = re.sub(r"\s+", "-", slug)
    slug = re.sub(r"-{2,}", "-", slug)
    return slug.strip("-")


def anchors(path: Path) -> set[str]:
    if path.suffix.lower() != ".md":
        return set()
    body = path.read_text(encoding="utf-8")
    found = set(EXPLICIT_ANCHOR.findall(body))
    duplicate_count: dict[str, int] = {}
    for _, heading in HEADING.findall(body):
        base = githubish_slug(heading)
        if not base:
            continue
        count = duplicate_count.get(base, 0)
        found.add(base if count == 0 else f"{base}-{count}")
        duplicate_count[base] = count + 1
    return found


def parse_target(raw: str) -> tuple[str, str]:
    target = raw.strip().strip("<>")
    if " " in target and not target.startswith(("http://", "https://")):
        target = target.split(" ", 1)[0]
    path_part, sep, fragment = target.partition("#")
    path_part = urllib.parse.unquote(path_part.split("?", 1)[0])
    fragment = urllib.parse.unquote(fragment) if sep else ""
    return path_part, fragment


def main() -> int:
    errors: list[str] = []
    checked_links = 0
    checked_anchors = 0
    anchor_cache: dict[Path, set[str]] = {}

    for source in ENTRY_DOCS:
        if not source.exists():
            errors.append(f"missing entry document: {source.relative_to(REPO)}")
            continue
        body = source.read_text(encoding="utf-8")
        for raw in MARKDOWN_LINK.findall(body) + HTML_LINK.findall(body):
            target = raw.strip().strip("<>")
            if not target or target.startswith(EXTERNAL_PREFIXES):
                continue
            path_part, fragment = parse_target(raw)
            target_path = source if not path_part else (source.parent / path_part).resolve()
            checked_links += 1
            if not target_path.exists():
                errors.append(
                    f"missing local target: {source.relative_to(REPO)} -> {raw}"
                )
                continue
            if fragment and target_path.suffix.lower() == ".md":
                checked_anchors += 1
                if target_path not in anchor_cache:
                    anchor_cache[target_path] = anchors(target_path)
                if fragment not in anchor_cache[target_path]:
                    errors.append(
                        f"missing anchor: {source.relative_to(REPO)} -> {raw}"
                    )

    if errors:
        print({
            "status": "FAIL",
            "checked_links": checked_links,
            "checked_anchors": checked_anchors,
            "errors": errors,
        })
        return 1

    print({
        "status": "PASS",
        "checked_links": checked_links,
        "checked_anchors": checked_anchors,
        "entry_documents": [str(p.relative_to(R01)) for p in ENTRY_DOCS],
    })
    return 0


if __name__ == "__main__":
    sys.exit(main())
