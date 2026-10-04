"""Version-aware R01 audit.

Separates substantive reproduction from documentary integrity. Historical manifests and
audit_results.json are preserved. Documentary drift is reported as
STALE_HISTORICAL_MANIFESTS rather than being converted into a new historical PASS.

Standard library only. No model/product/network calls.

Run from any directory:
    python3 verify_audit_v2.py --verify
    python3 verify_audit_v2.py --write-current
"""
from fractions import Fraction as F
from pathlib import Path
import argparse
import hashlib
import json
import runpy
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parent
R01 = ROOT.parent
HISTORICAL_REPORT = ROOT / "audit_results.json"
CURRENT_REPORT = ROOT / "audit_results_current.json"

BASE_DIGEST = "856c0d8dad3b27f1f48226a7978f2288dace3cc316912de083a5ea9dbb5e4d99"
BASE_SOURCE_DIGEST = "9848b4092b0c91cb10d4923bdfdf38e974d090655d07a6e7f3fa742ab54e6547"

CASES = {
    "hugging-face": ("check.py", "results.json"),
    "infoblox": ("proof/check.py", "proof/results.json"),
    "family": ("proof/check.py", "proof/results.json"),
}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def text_digest(text):
    return hashlib.sha256(text.encode()).hexdigest()


def success(value, optimum, epsilon):
    return value >= optimum - epsilon


def hash_record(path, expected, classification="documentary"):
    if not path.exists():
        return {
            "classification": classification,
            "status": "MISSING",
            "expected_sha256": expected,
            "actual_sha256": None,
        }
    actual = digest(path)
    return {
        "classification": classification,
        "status": "PASS" if actual == expected else "STALE_HISTORICAL_MANIFEST",
        "expected_sha256": expected,
        "actual_sha256": actual,
    }


def reproduce_cases():
    reproduced = {}
    fingerprints = {}
    family = None
    with tempfile.TemporaryDirectory(prefix="r01-extension-audit-v2-") as temporary:
        for case, (checker, result) in CASES.items():
            source = ROOT / case / checker
            expected_path = ROOT / case / result
            working = Path(temporary) / case
            working.mkdir()
            shutil.copyfile(source, working / "check.py")
            shutil.copyfile(expected_path, working / "results.json")
            command = [sys.executable, str(working / "check.py")]
            if case == "family":
                command.append("--verify")
            completed = subprocess.run(command, capture_output=True, text=True, timeout=180)
            if completed.returncode != 0:
                raise AssertionError((case, completed.stderr))
            actual = json.loads((working / "results.json").read_text())
            expected = json.loads(expected_path.read_text())
            if actual != expected:
                raise AssertionError(f"{case}: report not reproducible")
            reproduced[case] = {
                "status": actual["status"],
                "scope": actual["scope"],
                "report_identical": True,
                "counts": actual["counts"],
            }
            fingerprints[f"{case}/{checker}"] = digest(source)
            fingerprints[f"{case}/{result}"] = digest(expected_path)
            if case == "family":
                family = runpy.run_path(str(source), run_name="audit_functions")
    return reproduced, fingerprints, family


def run_falsifiers(family):
    falsifiers = {}
    value, target_best, base_best = F(2), F(2), F(3)
    assert success(value, target_best, F(0)) and not success(value, base_best, F(0))
    falsifiers["same_route_value_different_optimum"] = {
        "route_value": "2", "target_optimum": "2", "base_optimum": "3",
        "epsilon": "0", "success_in_target": True, "success_in_base": False,
    }

    assert success(F(2), F(3), F(1)) and not success(F(2), F(3), F(0))
    falsifiers["same_optimum_different_tolerance"] = {
        "route_value": "2", "optimum": "3", "tolerances": ["1", "0"]
    }

    quality_checks = 0
    for value in (F(1), F(2), F(3)):
        for best in (F(2), F(3)):
            for epsilon in (F(0), F(1, 2), F(1)):
                for scale in (F(1, 2), F(1), F(3)):
                    assert success(value, best, epsilon) == success(
                        scale * value, scale * best, scale * epsilon
                    )
                    quality_checks += 1

    assert not success(F(1), F(2), F(0)) and success(F(1), F(2), F(1))
    falsifiers["legitimate_M_is_not_always_mediocre"] = {
        "M": "1", "optimum": "2", "epsilon_0_success": False,
        "epsilon_1_success": True,
    }

    parameters = family["parameters"](3, F(1))
    state = (1, (0,), F(6), 0, -1)
    outcome = family["base_step"](state, ("commit", 0, 2), 3, 7, parameters)
    assert outcome == {(1, (0,), F(5), 1, 2): F(1)}
    falsifiers["family_commit_is_aggregate_and_no_minimum_review"] = {
        "L": 3, "reviewed_conditions": 0, "charge": "1", "elapsed": 1,
        "full_R01_receiver_admitted": False,
    }

    domain = family["build_domain"]("W", 2, 3, parameters, 0)
    starting = (0, (0,), F(6), 0, -1)
    assert family["equivalent"](starting, ("search", 0), domain, 2, 3)
    assert not family["equivalent"](
        starting, ("search", 0), domain, 2, 3, "hidden_influence"
    )
    falsifiers["hidden_variable_breaks_projection"] = "rejected by transition equivalence"

    known_denial = (1, (2,), F(6), 0, -1)
    denied = family["build_domain"]("H", 2, 1, parameters, 0)
    assert family["base_step"](known_denial, ("commit", 0, 2), 2, 1, parameters) is None
    assert family["domain_step"](
        family["encode"](known_denial, denied, 2), ("commit", 0, 2), denied
    ) is None
    return falsifiers, quality_checks


def check_historical_trace_integrity():
    organization = json.loads((R01 / "ORGANIZATION_TRACE.json").read_text())
    pilot = json.loads((R01 / "PILOT_OBJECTIVE_TRACE.json").read_text())
    scope = json.loads((R01 / "INCIDENT_SCOPE_TRACE.json").read_text())

    fixed_base = organization["before_files"]["Escenario-creatividad-validacion.md"]
    if text_digest(fixed_base) != BASE_DIGEST:
        raise AssertionError("Historical fixed R01 reference changed inside ORGANIZATION_TRACE.json")

    embedded_snapshots = {}
    for label, trace in (("organization", organization), ("pilot", pilot), ("scope", scope)):
        for name, before in trace.get("before_files", {}).items():
            expected = trace.get("before_sha256", {}).get(name)
            actual = text_digest(before)
            status = "PASS" if expected == actual else "CORRUPT_HISTORICAL_SNAPSHOT"
            embedded_snapshots[f"{label}:{name}"] = {
                "status": status, "expected_sha256": expected, "actual_sha256": actual,
            }

    current_trace_references = {}
    expected = pilot["predecessor_organization_trace_sha256"]
    current_trace_references["ORGANIZATION_TRACE.json -> PILOT predecessor"] = hash_record(
        R01 / "ORGANIZATION_TRACE.json", expected
    )
    for name, expected in scope.get("predecessor_trace_sha256", {}).items():
        current_trace_references[f"{name} -> INCIDENT_SCOPE predecessor"] = hash_record(
            R01 / name, expected
        )

    declared_current = {
        **organization.get("after_sha256", {}),
        **pilot.get("after_sha256", {}),
        **scope.get("after_sha256", {}),
    }
    current_edition_claims = {
        name: hash_record(R01 / name, expected)
        for name, expected in declared_current.items()
    }
    drift = [
        key for key, record in {**current_trace_references, **current_edition_claims}.items()
        if record["status"] != "PASS"
    ]
    embedded_corrupt = [
        key for key, record in embedded_snapshots.items()
        if record["status"] != "PASS"
    ]
    return {
        "embedded_historical_snapshots": embedded_snapshots,
        "embedded_snapshot_corruption": embedded_corrupt,
        "current_trace_references": current_trace_references,
        "historical_current_edition_claims": current_edition_claims,
        "status": (
            "HISTORICAL_SNAPSHOT_CORRUPT" if embedded_corrupt
            else ("CURRENT" if not drift else "STALE_HISTORICAL_MANIFESTS")
        ),
        "drift_items": drift,
    }


def check_extension_manifests():
    cases = {}
    documentary_mismatches = []
    substantive_mismatches = []
    substantive_files = {case: {checker, result} for case, (checker, result) in CASES.items()}

    for case in CASES:
        directory = ROOT / case
        manifest = json.loads((directory / "SHA256.json").read_text())
        checks = {}
        for name, expected in manifest.items():
            path = directory / name
            if path.suffix == ".docx":
                checks[name] = {
                    "classification": "historical_binary", "status": "NOT_RECHECKED",
                    "expected_sha256": expected, "actual_sha256": None,
                }
                continue
            classification = "substantive" if name in substantive_files[case] else "documentary"
            record = hash_record(path, expected, classification)
            checks[name] = record
            if record["status"] != "PASS":
                target = substantive_mismatches if classification == "substantive" else documentary_mismatches
                target.append(f"{case}/{name}")
        cases[case] = checks

    return {
        "cases": cases,
        "substantive_status": "PASS" if not substantive_mismatches else "FAIL",
        "substantive_mismatches": substantive_mismatches,
        "documentary_status": "CURRENT" if not documentary_mismatches else "STALE_HISTORICAL_MANIFESTS",
        "documentary_mismatches": documentary_mismatches,
    }


def run():
    reproduced, fingerprints, family = reproduce_cases()
    falsifiers, quality_checks = run_falsifiers(family)
    trace_integrity = check_historical_trace_integrity()
    manifest_integrity = check_extension_manifests()

    historical = json.loads(HISTORICAL_REPORT.read_text())
    historical_substantive_match = (
        historical.get("reproduced") == reproduced
        and historical.get("additional_quality_equivalences") == quality_checks
        and historical.get("falsifiers") == falsifiers
    )
    substantive_ok = historical_substantive_match and manifest_integrity["substantive_status"] == "PASS"

    embedded_corrupt = any(
        record["status"] != "PASS"
        for record in trace_integrity["embedded_historical_snapshots"].values()
    )
    if embedded_corrupt:
        status, combined = "FAIL", "HISTORICAL_SNAPSHOT_CORRUPT"
    elif not substantive_ok:
        status, combined = "FAIL", "SUBSTANTIVE_FAILURE"
    elif trace_integrity["status"] == "CURRENT" and manifest_integrity["documentary_status"] == "CURRENT":
        status, combined = "PASS", "SUBSTANTIVE_PASS_DOCUMENTARY_CURRENT"
    else:
        status, combined = "PASS", "SUBSTANTIVE_PASS_DOCUMENTARY_DRIFT"

    return {
        "status": status,
        "combined_status": combined,
        "scope": "substantive finite-check reproduction plus version-aware documentary integrity; no independent scientific replication or EA evaluation",
        "historical_report": "audit_results.json",
        "historical_report_preserved": True,
        "historical_substantive_match": historical_substantive_match,
        "base_sha256": BASE_DIGEST,
        "base_source_sha256": BASE_SOURCE_DIGEST,
        "reproduced": reproduced,
        "substantive_fingerprints": fingerprints,
        "additional_quality_equivalences": quality_checks,
        "falsifiers": falsifiers,
        "extension_manifest_integrity": manifest_integrity,
        "trace_integrity": trace_integrity,
        "independent_review": False,
        "full_R01_extensionality": "NOT_ESTABLISHED",
        "LLM_calls": 0,
        "network_calls": 0,
        "EA_evaluation": False,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--verify", action="store_true",
        help="Fail only if substantive reproduction or embedded historical-snapshot integrity fails; documentary drift is reported separately.",
    )
    parser.add_argument(
        "--write-current", action="store_true",
        help="Write a current dynamic report to audit_results_current.json.",
    )
    arguments = parser.parse_args()
    result = run()
    if arguments.write_current:
        CURRENT_REPORT.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({
        "status": result["status"],
        "combined_status": result["combined_status"],
        "cases_reproduced": list(result["reproduced"]),
        "historical_substantive_match": result["historical_substantive_match"],
        "extension_documentary_status": result["extension_manifest_integrity"]["documentary_status"],
        "trace_documentary_status": result["trace_integrity"]["status"],
        "substantive_mismatches": result["extension_manifest_integrity"]["substantive_mismatches"],
        "documentary_mismatches": result["extension_manifest_integrity"]["documentary_mismatches"],
        "trace_drift_items": result["trace_integrity"]["drift_items"],
        "full_R01_extensionality": result["full_R01_extensionality"],
    }, indent=2))
    if arguments.verify and result["status"] != "PASS":
        sys.exit(1)
