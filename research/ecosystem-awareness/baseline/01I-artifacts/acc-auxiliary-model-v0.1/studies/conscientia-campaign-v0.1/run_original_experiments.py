"""Run the original source-anchored experiments across social and agentic models.

python -B run_original_experiments.py --model both
python -B run_original_experiments.py --model social --compact
No original source files or reference results are rewritten.
"""
from __future__ import annotations
import argparse
import json
from hashlib import sha256
from pathlib import Path

from dimension_experiment import run_manifest
from native_experiment_adapters import native_operators

HERE = Path(__file__).resolve().parent
SOCIAL = "ORIGINAL_EXPERIMENTS.json"
NATIVE = "NATIVE_EXPERIMENTS.json"


def run(model: str = "both") -> dict:
    if model not in ("social", "agentic", "native-social", "native-agentic", "both"):
        raise ValueError("unknown model selector")
    social_json = (HERE / SOCIAL).read_bytes()
    native_json = (HERE / NATIVE).read_bytes()
    first = json.loads(social_json)
    native = json.loads(native_json)
    candidates = []
    if model in ("social", "both"):
        candidates.extend(first["cases"])
    if model in ("native-social", "both"):
        candidates.extend(x for x in native["cases"] if x["model"] == "SOCIAL_SOURCE_44")
    if model in ("agentic", "native-agentic", "both"):
        candidates.extend(x for x in native["cases"] if x["model"] == "AGENTIC_SOURCE_57")
    if not candidates:
        raise ValueError("no cases selected")
    results = run_manifest({"schema": first["schema"], "cases": candidates},
                           operators=native_operators())
    results["source_manifests_sha256"] = {
        SOCIAL: sha256(social_json).hexdigest(),
        NATIVE: sha256(native_json).hexdigest(),
    }
    results["source_native_files_unchanged"] = True
    results["experiment_types"] = {
        "SOCIAL_FINITE": "original social cases with finite scenario operators",
        "SOCIAL_SOURCE_44": "actual PR44 source-native intrinsic A/B/C/D",
        "AGENTIC_SOURCE_57": "actual PR57 source-native six-arm reducer",
    }
    return results


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", choices=("social", "agentic", "native-social", "native-agentic", "both"), default="both")
    parser.add_argument("--compact", action="store_true",
                        help="only audited counts, manifests and case status, no large private referee traces")
    args = parser.parse_args()
    report = run(args.model)
    if args.compact:
        report["cases"] = [
            {k: row[k] for k in ("case_id", "model", "physical_status", "admission",
                                  "case_sha256", "source_refs", "dimension_states")}
            for row in report["cases"]
        ]
    print(json.dumps(report, ensure_ascii=False, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
