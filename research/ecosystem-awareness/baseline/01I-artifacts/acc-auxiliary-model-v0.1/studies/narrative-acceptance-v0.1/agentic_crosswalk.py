"""Bounded source-native agentic analogue checks for ACC narrative mechanisms.

This is an explicit *non-equivalence* bridge: AG01/02/07/08/09 are executed
from PR57's pinned source, but do NOT simulate a banana, ministry, human
distress, public attribution, or the author's original economic objective.
No agentic truth is ever supplied to the source public planner.
"""
from __future__ import annotations

import argparse
from hashlib import sha256
from importlib.util import module_from_spec, spec_from_file_location
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent

ANALOGUES = {
    "EX-BAN-01": ("AG01-QUALIFIED-NEAR-OPTIMUM", "CONDITIONAL_PHYSICAL_GAIN_AND_COORDINATION_ONLY"),
    "EX-BAN-02": ("AG01-QUALIFIED-NEAR-OPTIMUM", "MATERIAL_RESOURCE_OVERHEAD_ONLY"),
    "EX-BAN-03": ("AG07-DONOR-REFUSES", "NONFUNGIBLE_CONSENT_GATE_ONLY"),
    "EX-MIN-01": ("AG08-META-OWNER-LACKS-AUTHORITY", "INSTITUTIONAL_AUTHORITY_GATE_ONLY"),
    "EX-SOLIDAR-01": ("AG07-DONOR-REFUSES", "NONFUNGIBLE_CONSENT_GATE_ONLY"),
    "EX-SUPER-01": ("AG02-LOW-CAPABILITY-SAME-A", "SAME_CURRENT_A_DIFFERENT_PRIVATE_RESPONSE_ONLY"),
    "EX-ORANGE-01": ("AG09-MATERIAL-D-UNRESOLVED", "SHARED_OPEN_MATERIAL_GATE_ONLY"),
    "EX-LINEAR-01": ("AG01-QUALIFIED-NEAR-OPTIMUM", "DECLARED_JOINT_PROTOCOL_ONLY"),
}


def _load_source(path: Path):
    spec = spec_from_file_location("_acc_pinned_agentic_crosswalk", path)
    if spec is None or spec.loader is None:
        raise RuntimeError("source-owned agentic executable unavailable")
    module = module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def _assert_source_results(agentic, by_case: dict) -> dict:
    selected = ("AG01-QUALIFIED-NEAR-OPTIMUM",
                "AG02-LOW-CAPABILITY-SAME-A",
                "AG07-DONOR-REFUSES",
                "AG08-META-OWNER-LACKS-AUTHORITY",
                "AG09-MATERIAL-D-UNRESOLVED")
    runs = {name: agentic.run_case(by_case[name]) for name in selected}
    q = "Q_META_PROTOCOL"
    direct = "CONVENTIONAL_DIRECTED"
    peer = "CONVENTIONAL_EQUIVALENT_Q"

    good = runs["AG01-QUALIFIED-NEAR-OPTIMUM"]
    low = runs["AG02-LOW-CAPABILITY-SAME-A"]
    if good["public_A"]["current_A_total_output"] != low["public_A"]["current_A_total_output"]:
        raise AssertionError("AG01/AG02 must retain equal public current A")
    chosen = good["arms"][q]
    if chosen["plan"]["transfer"] <= 0:
        raise AssertionError("qualified source's authorized transfer disappeared")
    actual = chosen["observed_by_referee_only"]
    if actual["total_resources_same"] != good["public_A"]["total_resources"]:
        raise AssertionError("agentic source created material resources")
    if good["arms"][peer]["observed_by_referee_only"]["output"] != actual["output"]:
        raise AssertionError("the same-Q conventional peer must retain its genuine tie")
    # Only an independent post-hoc referee can compare private future responses.
    future_good = agentic.physical_response(by_case[selected[0]], 2)["output"]
    future_low = agentic.physical_response(by_case[selected[1]], 2)["output"]
    if not future_good > future_low:
        raise AssertionError("no longer a future-output witness for same current A")

    denied = runs["AG07-DONOR-REFUSES"]
    if denied["public_A"]["release_consent"] is not False:
        raise AssertionError("donor refusal premise was silently changed")
    if denied["arms"][q]["plan"]["transfer"] != 0:
        raise AssertionError("a certificate must not override donor refusal")

    unauthorized = runs["AG08-META-OWNER-LACKS-AUTHORITY"]
    if unauthorized["public_A"]["meta_owner_authority"] is not False:
        raise AssertionError("meta authority premise was silently changed")
    if unauthorized["arms"][q]["plan"]["transfer"] != 0:
        raise AssertionError("agentic coordination may not create authority")

    unknown = runs["AG09-MATERIAL-D-UNRESOLVED"]
    if unknown["public_A"]["material_D_for_joint_decision"] is not True:
        raise AssertionError("material open-frontier witness no longer present")
    if unknown["arms"][q]["plan"]["transfer"] or unknown["arms"][direct]["plan"]["transfer"]:
        raise AssertionError("material D must constrain equivalent available planners")

    return {
        "source_synthetic_cases_executed": list(selected),
        "public_current_A_AG01_AG02": good["public_A"]["current_A_total_output"],
        "physical_future_response_private_referee": {
            "AG01": future_good, "AG02": future_low,
            "use": "POST_HOC_REFEREE_ONLY_NOT_PUBLIC_PLANNER_INFORMATION",
        },
        "AG01_qualified_transfer": chosen["plan"]["transfer"],
        "AG01_qualified_output": actual["output"],
        "AG01_sameQ_peer_output": good["arms"][peer]["observed_by_referee_only"]["output"],
        "AG07_consent_blocks": True,
        "AG08_authority_blocks": True,
        "AG09_D_blocks_qualified_and_conventional": True,
    }


def run(source_dir: Path) -> dict:
    src = source_dir / "agentic_reduction.py"
    fixture = source_dir / "CASES.json"
    if not src.is_file() or not fixture.is_file():
        raise FileNotFoundError("source-owned PR57 implementation/CASES.json required")
    agentic = _load_source(src)
    registry = json.loads(fixture.read_text(encoding="utf-8"))
    if registry.get("schema") != agentic.SCHEMA:
        raise ValueError("native PR57 schema mismatch")
    original_ids = [c["id"] for c in registry["cases"]]
    if len(original_ids) != len(set(original_ids)):
        raise ValueError("duplicate native case")
    native = {c["id"]: c for c in registry["cases"]}
    declared = json.loads((HERE / "MECHANISM_CASES.json").read_text(encoding="utf-8"))
    narratives = {c["case_id"] for c in declared["cases"]}
    if set(ANALOGUES) - narratives or set(a for a, _ in ANALOGUES.values()) - set(native):
        raise ValueError("crosswalk names case outside respective source registry")
    checks = _assert_source_results(agentic, native)
    correspondence = {}
    for name in sorted(narratives):
        if name in ANALOGUES:
            native_id, property_name = ANALOGUES[name]
            correspondence[name] = {
                "status": "STRUCTURAL_ANALOGUE_EXECUTED_NOT_SAME_QUESTION_REDUCTION",
                "native_case_id": native_id, "property": property_name,
            }
        else:
            correspondence[name] = {
                "status": "NO_SAME_QUESTION_AGENTIC_SOURCE_EXECUTOR",
                "native_case_id": None,
                "property": "NOT_INFERRED_FROM_PARTIAL_MULTIAGENT_PHYSICAL_MODEL",
            }
    return {
        "schema": "ACC-NARRATIVE-AGENTIC-BOUNDED-CROSSWALK-v0.1",
        "agentic_source_sha256": {
            "agentic_reduction.py": sha256(src.read_bytes()).hexdigest(),
            "CASES.json": sha256(fixture.read_bytes()).hexdigest(),
        },
        "counts": {
            "author_examples": len(narratives),
            "structural_analogues": len(ANALOGUES),
            "non_equivalent": len(narratives) - len(ANALOGUES),
            "unique_native_agentic_cases_executed": len(checks["source_synthetic_cases_executed"]),
        },
        "source_native_executed_checks": checks,
        "cases": correspondence,
        "boundary": "STRUCTURAL_ANALOGIES_ONLY_NO_NARRATIVE_SAME_QUESTION_AGENTIC_REDUCTION_OR_FIELD_EVIDENCE",
    }


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--source-dir", type=Path, required=True)
    ap.add_argument("--output", type=Path)
    args = ap.parse_args(argv)
    report = run(args.source_dir)
    payload = json.dumps(report, ensure_ascii=False, sort_keys=True, indent=2) + "\n"
    if args.output:
        args.output.write_text(payload, encoding="utf-8")
    else:
        print(payload, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
