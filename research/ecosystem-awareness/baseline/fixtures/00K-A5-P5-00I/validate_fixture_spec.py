"""Meta-integrity agreement gate for the 00K A5 / P5 reduced fixture.

Not counted in the 47 canonical P5 checks or 379 registered 00K campaign.
It prevents silent drift between the machine-readable branch contract and the
executable serious-repair model.
"""
from __future__ import annotations

import json
from itertools import combinations
from pathlib import Path

from p5_serious_repairs import (
    B,
    FIELDS,
    Current,
    all_field_subsets,
    passes_material_grid,
    subset_compare,
)

HERE = Path(__file__).resolve().parent
SPEC = json.loads((HERE / "fixture_spec.json").read_text(encoding="utf-8"))


def expected_power_set():
    return {
        tuple(combo)
        for r in range(len(FIELDS) + 1)
        for combo in combinations(FIELDS, r)
    }


def main() -> int:
    if SPEC["schema"] != "00K-A5-P5-00I/fixture-spec/v1":
        raise SystemExit("unexpected fixture schema")

    declared_fields = tuple(SPEC["fields"])
    if declared_fields != FIELDS:
        raise SystemExit(
            f"field-order/coverage drift: spec={declared_fields}, code={FIELDS}"
        )

    basis = SPEC["basis"]
    actual_basis = {
        "generation": B.generation,
        "incident_open": B.incident_open,
        "freeze_active": B.freeze_active,
        "source_version": B.source_version,
    }
    if basis != actual_basis:
        raise SystemExit(f"basis drift: spec={basis}, code={actual_basis}")

    observed_subsets = set(all_field_subsets())
    if observed_subsets != expected_power_set() or len(observed_subsets) != 16:
        raise SystemExit("the code no longer enumerates the full 2^4 field power set")

    for name, branch in SPEC["branches"].items():
        cur = Current(**branch["current"])
        observed = subset_compare(cur, FIELDS).value
        if observed != branch["expected"]:
            raise SystemExit(
                f"{name}: expected {branch['expected']}, got {observed}"
            )

        changed = branch.get("changed_field")
        if changed in FIELDS:
            diffs = [
                field for field in FIELDS
                if getattr(cur, field) != getattr(B, field)
            ]
            if diffs != [changed]:
                raise SystemExit(
                    f"{name}: attribution drift; declared {changed}, actual {diffs}"
                )

    winners = [s for s in all_field_subsets() if passes_material_grid(s)]
    if winners != [FIELDS]:
        raise SystemExit(f"winner-set drift: {winners}")

    print("00K A5 P5 fixture-spec agreement: PASS")
    print("branches:", len(SPEC["branches"]))
    print("field subsets:", len(observed_subsets))
    print("winner:", FIELDS)
    print("meta-integrity only: not counted in 47/379")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
