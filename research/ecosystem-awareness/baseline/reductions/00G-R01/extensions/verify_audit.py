"""Internal R01 extension audit: reproducibility, integrity and extra falsifiers.

Standard library only. No model/product/network calls. Run from any directory:
python3 verify_audit.py --verify (compare with recorded audit_results.json)
python3 verify_audit.py          (regenerate that common audit report)
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
BASE_DIGEST = "9848b4092b0c91cb10d4923bdfdf38e974d090655d07a6e7f3fa742ab54e6547"
CASES = {
    "hugging-face": ("check.py", "results.json"),
    "infoblox": ("proof/check.py", "proof/results.json"),
    "family": ("proof/check.py", "proof/results.json"),
}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def success(value, optimum, epsilon):
    # Quality predicate only; safety/cost/time are held satisfied in these tests.
    return value >= optimum - epsilon


def run():
    base = ROOT.parent / "Escenario-creatividad-validacion.md"
    assert digest(base) == BASE_DIGEST, "The fixed R01 base changed"
    reproduced, integrity, fingerprints, falsifiers = {}, {}, {}, {}
    with tempfile.TemporaryDirectory(prefix="r01-extension-audit-") as temporary:
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
            assert completed.returncode == 0, (case, completed.stderr)
            actual = json.loads((working / "results.json").read_text())
            expected = json.loads(expected_path.read_text())
            assert actual == expected, f"{case}: report not reproducible"
            reproduced[case] = {"status": actual["status"], "scope": actual["scope"],
                                "report_identical": True, "counts": actual["counts"]}
            fingerprints[f"{case}/{checker}"] = digest(source)
            fingerprints[f"{case}/{result}"] = digest(expected_path)
            # Load functions for boundary tests; __main__ is deliberately not run.
            if case == "family":
                family = runpy.run_path(str(source), run_name="audit_functions")

    for case in ("hugging-face", "infoblox"):
        directory = ROOT / case
        manifest = json.loads((directory / "SHA256.json").read_text())
        checks = {}
        for name, expected in manifest.items():
            file = directory / name
            if file.suffix == ".docx":
                checks[name] = "EXCLUDED_BINARY_HASH_RETAINED"
                continue
            assert file.exists() and digest(file) == expected, (case, name, "hash mismatch")
            checks[name] = "PASS"
        integrity[case] = checks
    family_manifest = json.loads((ROOT / "family/SHA256.json").read_text())
    for name, expected in family_manifest.items():
        assert digest(ROOT / "family" / name) == expected, name
    integrity["family"] = {name: "PASS" for name in family_manifest}

    # Counterexample to relative-success transfer with different reference optimum.
    value, target_best, base_best = F(2), F(2), F(3)
    assert success(value, target_best, F(0)) and not success(value, base_best, F(0))
    falsifiers["same_route_value_different_optimum"] = {
        "route_value": "2", "target_optimum": "2", "base_optimum": "3",
        "epsilon": "0", "success_in_target": True, "success_in_base": False,
    }
    # Equal optima alone do not preserve success when tolerances differ.
    assert success(F(2), F(3), F(1)) and not success(F(2), F(3), F(0))
    falsifiers["same_optimum_different_tolerance"] = {
        "route_value": "2", "optimum": "3", "tolerances": ["1", "0"]}
    # Algebraic preservation under a positive change of quality units requires
    # transforming the optimum and epsilon too, not just the observed value.
    quality_checks = 0
    for v in (F(1), F(2), F(3)):
        for best in (F(2), F(3)):
            for epsilon in (F(0), F(1, 2), F(1)):
                for scale in (F(1, 2), F(1), F(3)):
                    assert success(v, best, epsilon) == success(scale * v, scale * best, scale * epsilon)
                    quality_checks += 1
    # A legitimate M becomes quality-sufficient if epsilon includes its gap.
    assert not success(F(1), F(2), F(0)) and success(F(1), F(2), F(1))
    falsifiers["legitimate_M_is_not_always_mediocre"] = {
        "M": "1", "optimum": "2", "epsilon_0_success": False, "epsilon_1_success": True}

    # The actual family checker models aggregate commitment, not L executions.
    parameters = family["parameters"](3, F(1))
    state = (1, (0,), F(6), 0, -1)
    outcome = family["base_step"](state, ("commit", 0, 2), 3, 7, parameters)
    assert outcome == {(1, (0,), F(5), 1, 2): F(1)}
    falsifiers["family_commit_is_aggregate_and_no_minimum_review"] = {
        "L": 3, "reviewed_conditions": 0, "charge": "1", "elapsed": 1,
        "full_R01_receiver_admitted": False}

    # A homomorphism of labels is insufficient when a hidden variable changes
    # transition probabilities. This directly invokes both independent kernels.
    domain = family["build_domain"]("W", 2, 3, parameters, 0)
    starting = (0, (0,), F(6), 0, -1)
    assert family["equivalent"](starting, ("search", 0), domain, 2, 3)
    assert not family["equivalent"](starting, ("search", 0), domain, 2, 3, "hidden_influence")
    falsifiers["hidden_variable_breaks_projection"] = "rejected by transition equivalence"

    # Compulsory known-denial rejection and scope-dependent observations survive.
    known_denial = (1, (2,), F(6), 0, -1)
    denied = family["build_domain"]("H", 2, 1, parameters, 0)
    assert family["base_step"](known_denial, ("commit", 0, 2), 2, 1, parameters) is None
    assert family["domain_step"](family["encode"](known_denial, denied, 2), ("commit", 0, 2), denied) is None

    document_paths = [ROOT / "CRITERIA_AND_AUDIT.md", ROOT / "METHODOLOGICAL_FOUNDATIONS.md",
                      ROOT / "EDITORIAL_REVIEW.md", ROOT.parent / "README.md"]
    for case in CASES:
        document_paths.extend((ROOT / case).rglob("*.md"))
    for path in sorted(document_paths):
        name = "../README.md" if path == ROOT.parent / "README.md" else str(path.relative_to(ROOT))
        fingerprints[name] = digest(path)
    fingerprints["verify_audit.py"] = digest(Path(__file__))
    return {"status": "PASS", "scope": "internal reproducibility and bounded logical audit only",
            "reviewed_commit": "cbb69f1d673c7844610fdde01fb78a3394497bb0",
            "base_blob_sha": "3261a625975e303e12c484bc9c273d7f8819b099",
            "base_sha256": BASE_DIGEST, "reproduced": reproduced,
            "integrity": integrity, "additional_quality_equivalences": quality_checks,
            "falsifiers": falsifiers, "fingerprints": fingerprints,
            "independent_review": False, "full_R01_extensionality": "NOT_ESTABLISHED",
            "LLM_calls": 0, "network_calls": 0, "EA_evaluation": False}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    arguments = parser.parse_args()
    result = run()
    output = ROOT / "audit_results.json"
    if arguments.verify:
        assert json.loads(output.read_text()) == result, "Common report changed"
    else:
        output.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"status": result["status"], "cases_reproduced": list(result["reproduced"]),
                      "additional_quality_equivalences": result["additional_quality_equivalences"],
                      "falsifiers": list(result["falsifiers"]),
                      "full_R01_extensionality": result["full_R01_extensionality"]}, indent=2))
