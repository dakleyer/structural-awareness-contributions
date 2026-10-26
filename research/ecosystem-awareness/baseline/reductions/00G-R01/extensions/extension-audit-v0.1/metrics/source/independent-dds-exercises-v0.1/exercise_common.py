"""Exercise execution support; freeze bindings are checked before runtime entry."""
from pathlib import Path
import hashlib,json,platform,time
import cryptography

def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def load_frozen(root):
    root=Path(root)
    freeze=json.loads((root/"FREEZE.json").read_text(encoding="utf-8"))
    for row in freeze["files"]:
        assert sha(root/row["path"])==row["sha256"],("frozen input mismatch",row["path"])
    assert cryptography.__version__==freeze["cryptography_version"],"Use the registered dependency version or preregister a successor"
    return json.loads((root/"RUN_CARD.json").read_text(encoding="utf-8")),freeze
def save(root,output,card,freeze,result):
    target=Path(output);target.mkdir(parents=True,exist_ok=False)
    result.update({"run_id":card["run_id"],"canonical_DDS_profile":card["canonical_DDS_profile"],
        "implementation_profile":card["implementation_profile"],"software_version":"DDS-INDEPENDENT-EXERCISES-0.1",
        "python":platform.python_version(),"cryptography_version":cryptography.__version__,
        "run_card_sha256":sha(Path(root)/"RUN_CARD.json"),"freeze_sha256":sha(Path(root)/"FREEZE.json"),
        "evidence":"same-author bounded executed fixture; no production or independent validation",
        "population_rates_established":False,"native_SPIRE_TPM_or_verifier_product_executed":False})
    with (target/"RESULTS.json").open("x",encoding="utf-8",newline="") as out:json.dump(result,out,indent=2);out.write("\n")
    print(json.dumps({"run_id":result["run_id"],"status":result["status"],"cases":len(result["cases"]),
        "assertions":result["assertions"],"outcomes":result["qualified_outcome_counts"],
        "counterexamples":result.get("diagnostic_wrong_effects",0),"result":str(target/"RESULTS.json")}))

