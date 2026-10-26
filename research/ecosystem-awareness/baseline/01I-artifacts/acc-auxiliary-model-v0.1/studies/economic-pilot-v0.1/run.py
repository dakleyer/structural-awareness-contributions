"""Reproduce the frozen local toy; uses only the Python standard library."""
from pathlib import Path
import argparse
import hashlib
import json
import sys

from model import bounded_controls, run_case

ROOT = Path(__file__).resolve().parent


def load_inputs(root=ROOT):
    freeze = json.loads((root / "freeze.json").read_text(encoding="utf8"))
    for name, expected in freeze["files"].items():
        if hashlib.sha256((root / name).read_bytes()).hexdigest() != expected:
            raise ValueError("Frozen study input changed: " + name)
    return (json.loads((root / "protocol.json").read_text(encoding="utf8")),
            json.loads((root / "cases.json").read_text(encoding="utf8")),
            json.loads((root / "manual_oracle.json").read_text(encoding="utf8")), freeze)


def compare_manual(result, expected, negative=False):
    if negative:
        assert result["actions"] == expected["actions"], (result["case_id"], result["actions"])
        for field in ["operating_surplus", "full_net", "invalid_attempts"]:
            assert result[field] == expected[field], (result["case_id"], field, result[field], expected[field])
    else:
        assert result["actions"] == expected["primary_policies_expected_actions"], (result["case_id"], result["actions"])
        for field, oracle_field in [("operating_surplus", "primary_operating_surplus"), ("full_net", "primary_full_net"), ("actual_effects", "primary_actual_effects")]:
            assert result[field] == expected[oracle_field], (result["case_id"], field, result[field], expected[oracle_field])
        assert result["invalid_attempts"] == (1 if expected["expected_primary_limit"] == "FAIL_HIDDEN_COST" else 0)


def execute(root=ROOT):
    protocol, cases, oracle, freeze = load_inputs(root)
    expected = {x["case_id"]: x for x in oracle["records"]}
    assert set(expected) == {c["id"] for c in cases}
    runs = []
    for case in cases:
        for policy in protocol["policies"]:
            result = run_case(case, policy, protocol)
            compare_manual(result, expected[case["id"]])
            runs.append(result)
        if expected[case["id"]]["stale_reference_expected"]:
            result = run_case(case, "stale_reference", protocol)
            compare_manual(result, expected[case["id"]]["stale_reference_expected"], negative=True)
            runs.append(result)
    primary = [r for r in runs if r["policy"] != "stale_reference"]
    for cid in expected:
        paired = [r for r in primary if r["case_id"] == cid]
        assert paired[0]["actions"] == paired[1]["actions"]
        assert paired[0]["full_net"] == paired[1]["full_net"]
    by_key = {(r["case_id"], r["policy"]): r for r in runs}
    for policy in protocol["policies"]:
        safe, costly = by_key[("E09", policy)], by_key[("E10", policy)]
        assert safe["trace"][0]["request"]["observation_sha256"] == costly["trace"][0]["request"]["observation_sha256"]
        assert safe["scenario_outcome"] == "PASS" and costly["scenario_outcome"] == "FAIL"
    traces = [event for run in runs for event in run.pop("trace")]
    controls = bounded_controls()
    assert controls["information_incentive"]["W_hidden"] > controls["information_incentive"]["W_visible"]
    result = {"study_id": protocol["id"], "evidence_mode": "deterministic reference-model execution",
        "evidence_ceiling": protocol["evidence_ceiling"], "formal_dds_acceptance": False,
        "native_acc_implemented": False, "native_uc21_r01_executed": False,
        "manual_oracle_matches": True, "frozen_case_count": len(cases), "primary_runs": len(primary),
        "negative_control_runs": len(runs) - len(primary), "trace_events": len(traces),
        "primary_comparison": "behavior and declared full-cost ties on all listed fixtures; no EA efficacy inference",
        "cost_sensitivity": "If the qualified record costs one extra unit of preparation, its full net is one unit lower per case; no advantage is imposed",
        "known_limits": ["Both main policies fail E10 with the same misleading observation as E09", "The stale control fails T02/T03 and is not the competent comparator", "No measured human welfare, skill, compute saving or real-organization estimate"],
        "input_sha256": freeze["files"],
        "implementation_sha256": {n: hashlib.sha256((root / n).read_bytes()).hexdigest() for n in ["model.py", "run.py"]},
        "runs": runs, "separate_bounded_controls": controls}
    return result, traces


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, default=ROOT / "results")
    args = parser.parse_args()
    result, traces = execute()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    (args.output_dir / "results.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf8")
    (args.output_dir / "traces.jsonl").write_text("".join(json.dumps(t, ensure_ascii=False, sort_keys=True) + "\n" for t in traces), encoding="utf8")
    rows = ["# Resultados del primer modelo determinista", "", "El ejecutable concuerda con el recorrido manual congelado. Esta concordancia cualifica este modelo pequeño; los FAIL previstos siguen siendo fallos de escenario.", "", "| Caso | Procedimiento | Acciones | Saldo completo | Resultado del escenario |", "|---|---|---|---:|---|"]
    rows += ["| " + r["case_id"] + " | " + r["policy"] + " | " + " → ".join(r["actions"]) + " | " + str(r["full_net"]) + " | " + r["scenario_outcome"] + " |" for r in result["runs"]]
    rows += ["", "Ambos procedimientos principales empatan en estas instancias. Con una unidad adicional de preparación, el registro cualificado resulta una unidad más caro por caso. E10 conserva el límite de información: ambos ejecutan una transición realmente desfavorable. El control incompleto se mantiene separado y no fundamenta superioridad frente a un proceso convencional competente.", "", "Los controles auxiliares ilustran el incentivo de una puerta basada sólo en W, las distinciones de capacidad humana y un ahorro con servicio equivalente. No miden felicidad, habilidades o prácticas de una organización real. DDS formal y ejecución nativa UC21/R01 permanecen pendientes."]
    (args.output_dir / "RESULTS.md").write_text("\n".join(rows) + "\n", encoding="utf8")
    print(json.dumps({"manual_oracle_matches": True, "cases": result["frozen_case_count"], "primary_runs": result["primary_runs"], "negative_controls": result["negative_control_runs"], "trace_events": len(traces), "formal_dds_acceptance": False}))


if __name__ == "__main__":
    main()
