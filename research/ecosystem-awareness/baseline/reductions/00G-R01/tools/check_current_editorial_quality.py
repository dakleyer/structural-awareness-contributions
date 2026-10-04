#!/usr/bin/env python3
"""Check presentation hygiene of current-route R01 Markdown.

This is intentionally a visual/editorial gate, not a scientific checker. Historical
snapshots and frozen evidence are outside its scope.
"""
from __future__ import annotations

import re
import sys

from check_current_route_preservation import CURRENT_ROUTE_FILES, R01

HEADING = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
TABLE = re.compile(r"^\s*\|.*\|\s*$")
TABLE_SEPARATOR_CELL = re.compile(r"^:?-{3,}:?$")
FENCE = re.compile(r"^\s*(" + re.escape(chr(96) * 3) + r"+|~~~+)")


def outside_fences(lines: list[str]) -> list[tuple[int, str]]:
    result: list[tuple[int, str]] = []
    marker: str | None = None
    for number, line in enumerate(lines, start=1):
        match = FENCE.match(line)
        if match:
            token = match.group(1)
            char = token[0]
            if marker is None:
                marker = char
            elif marker == char:
                marker = None
            continue
        if marker is None:
            result.append((number, line))
    return result


def table_blocks(lines: list[tuple[int, str]]) -> list[list[tuple[int, str]]]:
    blocks: list[list[tuple[int, str]]] = []
    current: list[tuple[int, str]] = []
    last = -2
    for number, line in lines:
        if TABLE.match(line):
            if current and number != last + 1:
                blocks.append(current)
                current = []
            current.append((number, line))
            last = number
        elif current:
            blocks.append(current)
            current = []
            last = -2
    if current:
        blocks.append(current)
    return blocks


def cells(line: str) -> list[str]:
    stripped = line.strip().strip("|")
    return [cell.strip() for cell in stripped.split("|")]


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []
    files_checked = 0
    tables_checked = 0

    for rel in CURRENT_ROUTE_FILES:
        path = R01 / rel
        text = path.read_text(encoding="utf-8")
        lines = text.splitlines()
        visible = outside_fences(lines)

        if any(line.rstrip() != line for _, line in visible):
            nums = [str(n) for n, line in visible if line.rstrip() != line][:10]
            errors.append(f"{rel}: trailing whitespace at lines {', '.join(nums)}")

        if any("\t" in line for _, line in visible):
            nums = [str(n) for n, line in visible if "\t" in line][:10]
            errors.append(f"{rel}: tab characters outside code at lines {', '.join(nums)}")

        if "\n\n\n\n" in text:
            errors.append(f"{rel}: more than two consecutive blank lines")

        headings = [(n, HEADING.match(line)) for n, line in visible if HEADING.match(line)]
        h1 = [(n, m.group(2)) for n, m in headings if len(m.group(1)) == 1]
        if len(h1) != 1:
            errors.append(f"{rel}: expected one H1, found {len(h1)}")

        previous_level: int | None = None
        for number, match in headings:
            level = len(match.group(1))
            title = match.group(2).strip()
            if not title:
                errors.append(f"{rel}: empty heading at line {number}")
            if previous_level is not None and level > previous_level + 1:
                warnings.append(
                    f"{rel}: heading jump H{previous_level}->H{level} at line {number}: {title}"
                )
            previous_level = level

        fence_state = None
        for number, line in enumerate(lines, start=1):
            match = FENCE.match(line)
            if not match:
                continue
            char = match.group(1)[0]
            if fence_state is None:
                fence_state = (char, number)
            elif fence_state[0] == char:
                fence_state = None
        if fence_state is not None:
            errors.append(f"{rel}: unclosed fenced block opened at line {fence_state[1]}")

        if text.count("$$") % 2:
            errors.append(f"{rel}: unbalanced display-math delimiter")

        for block in table_blocks(visible):
            tables_checked += 1
            widths = [len(cells(line)) for _, line in block]
            if len(set(widths)) != 1:
                errors.append(
                    f"{rel}: inconsistent table width near line {block[0][0]}: {widths}"
                )
                continue
            if len(block) < 2:
                warnings.append(f"{rel}: one-row table near line {block[0][0]}")
                continue
            sep = cells(block[1][1])
            if not all(TABLE_SEPARATOR_CELL.match(cell) for cell in sep):
                warnings.append(
                    f"{rel}: table near line {block[0][0]} has no standard separator row"
                )

        files_checked += 1

    result = {
        "status": "PASS" if not errors else "FAIL",
        "files_checked": files_checked,
        "tables_checked": tables_checked,
        "errors": errors,
        "warnings": warnings,
    }
    print(result)
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
