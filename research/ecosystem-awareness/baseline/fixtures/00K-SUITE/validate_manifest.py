"""Validate the 00K execution-lock manifest.

This is a meta-integrity check. It is not counted in the 208 ablation tests.
"""

from __future__ import annotations

import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
MANIFEST = HERE / "principle_manifest.json"


def main() -> int:
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))

    principles = data["principles"]
    ids = [p["id"] for p in principles]
    if ids != ["P1", "P2", "P3", "P4", "P5", "P6"]:
        raise SystemExit(f"principle order/coverage mismatch: {ids}")

    core = sum(int(p["expected_tests"]) for p in principles)
    supplemental = sum(int(x["expected_tests"]) for x in data["supplemental_fixtures"])
    total = core + supplemental

    if core != data["core_expected_tests"] or core != 175:
        raise SystemExit(f"core count mismatch: computed={core}, declared={data['core_expected_tests']}")

    if supplemental != data["supplemental_expected_tests"] or supplemental != 33:
        raise SystemExit(f"supplemental count mismatch: {supplemental}")

    if total != data["campaign_expected_tests"] or total != 208:
        raise SystemExit(f"campaign count mismatch: {total}")

    for p in principles:
        if not p["invariant"].strip():
            raise SystemExit(f"{p['id']} has empty invariant")
        if not p["negative_control"].strip() or not p["positive_control"].strip():
            raise SystemExit(f"{p['id']} has incomplete branch lock")
        fixture = (HERE / p["core_fixture"]).resolve()
        if not fixture.is_dir():
            raise SystemExit(f"{p['id']} fixture missing: {fixture}")

    for s in data["supplemental_fixtures"]:
        fixture = (HERE / s["path"]).resolve()
        if not fixture.is_dir():
            raise SystemExit(f"supplemental fixture missing: {fixture}")

    print("00K execution-lock manifest: PASS")
    print("principles: 6/6")
    print(f"core: {core}")
    print(f"supplemental: {supplemental}")
    print(f"campaign: {total}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
