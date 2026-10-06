"""Prospective bounded completion checks; original study files are read-only."""
from pathlib import Path
from copy import deepcopy
from fractions import Fraction as F
import argparse,hashlib,importlib.util,json,sys,platform
import cryptography

HERE=Path(__file__).resolve().parent
def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def load_module(name,path):
 spec=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
def main(source,output):
 root=Path(source).resolve();target=Path(output).resolve()
 if target.exists():raise FileExistsError("Fresh output required")
 frozen=json.loads((HERE/"FREEZE.json").read_text(encoding="utf-8"))
 for row in frozen["own_files"]:assert sha(HERE/row["path"])==row["sha256"],row["path"]
 card=json.loads((HERE/"BOUNDARY_RUN_CARD.json").read_text(encoding="utf-8"))
 for row in card["source_files"]:
  p=(root/row["path"]).resolve();p.relative_to(root);data=p.read_bytes()
  assert hashlib.sha1(("blob "+str(len(data))+"\0").encode()+data).hexdigest()==row["git_blob"],row["path"]
 assert cryptography.__version__==card["required_cryptography_version"]
 target.mkdir(parents=True)
 sys.path.insert(0,str(root/"dds-hew-v0.1"));sys.path.insert(0,str(root/"independent-dds-exercises-v0.1"))
 from hew_runtime import Runtime
 from hew_oracle import judge as hew_judge
 from crypto_fixture import FixtureIssuer,Rejected,token_digest
 out={"run_id":"DDS-COMPLETION-BOUNDARIES-20261006-01","evidence_mode":"same-author analytical/local model boundary checks","population_rates_established":False,"native_or_human_execution":False,"original_results_rescored":False,"source_commit":card["source_commit"],"card_sha256":sha(HERE/"BOUNDARY_RUN_CARD.json"),"freeze_sha256":sha(HERE/"FREEZE.json"),"python":platform.python_version(),"cryptography":cryptography.__version__}
 try:
  spec=card["analytical"];a,beta=F(spec["a"]),F(spec["beta"]);p,delta=F(spec["p"]),F(spec["delta"])
  ar=[]
  for qv,expected in zip(spec["q_values"],spec["expected_acceptance"]):
   q=F(qv);s=(1-a)*q+a*beta;r=(1-a)*(1-q)*beta
   accepted=spec["cost"]<=spec["b"] and s>=p and r<=delta
   assert accepted==expected
   ar.append({"q":qv,"s":str(s),"r":str(r),"cost":40,"cost_inside":True,"effectiveness_inside":s>=p,"risk_inside":r<=delta,"accepted":accepted})
  out["analytical"]={"cases":ar,"q_effectiveness_boundary":str((p-a*beta)/(1-a)),"q_risk_boundary":str(1-delta/((1-a)*beta)),"scope":spec["transfer"]}
  hc=json.loads((root/"dds-hew-v0.1/RUN_CARD.json").read_text(encoding="utf-8"));original=hc["scenarios"][0];hr=[]
  for case in card["hew_cases"]:
   public=deepcopy(original["public_cases"][0]);oid="COMPLETION-"+case["id"]
   public["operation_id"]=oid;public["scenario_id"]=oid;public["command_id"]="command-"+oid
   public["evidence"]["case"]=oid;public["grant"]["case"]=oid;public["semantic_contract"]["operation_id"]=oid
   public["gate_latency"]=case["gate_latency"];public["source_preparation_work"]=case["source_preparation_work"]
   db=target/(case["id"]+".sqlite");runtime=Runtime(db)
   try:
    runtime.provision_authority(oid,public["grant"]);result=runtime.run_case(public)
    verdict=hew_judge(db,public,original["private_worlds"][0],result)
    assert verdict["sufficient_delivery"]==case["expected_delivery"]
    assert not verdict["violation_observed"]
    hr.append({"id":case["id"],"input_gate_latency":public["gate_latency"],"source_preparation_work":public["source_preparation_work"],"sufficient_delivery":verdict["sufficient_delivery"],"work":verdict["work_units"],"controller_reasons":result["reasons"],"applied_at":result.get("applied_at"),"delivery_at":result.get("delivery_at"),"events":runtime.events(),"oracle_verdict":verdict})
   finally:runtime.close()
  out["hew"]=hr
  st=load_module("completion_stpa",root/"independent-dds-exercises-v0.1/stamp-stpa/run.py");sr=[]
  world={"pump_running":True,"maintenance":True,"critical_supply":False,"backup":True,"authority":True,"sensor_current":True,"stop_applied":True,"allow_defer":True}
  for case in card["stpa_cases"]:
   view={k:world[k] for k in ("pump_running","maintenance","critical_supply","backup","authority","sensor_current","allow_defer")}
   if case["false_running_observation"]:view["pump_running"]=False
   plant=st.Plant(world);calls=[0]
   def feedback():calls[0]+=1;return plant.stop_and_observe()
   commands=st.decide(view,feedback);verdict=st.judge(world,commands)
   assert verdict["outcome"]==case["expected_outcome"]
   sr.append({"id":case["id"],"outcome":verdict["outcome"],"hazards":verdict["hazards"],"commands":commands,"actual_plant_callback_calls":calls[0],"diagnostic":case.get("diagnostic")})
  out["stamp_stpa"]=sr
  sp=load_module("completion_spiffe",root/"independent-dds-exercises-v0.1/spiffe-jwt/run.py");sc=json.loads((root/"independent-dds-exercises-v0.1/spiffe-jwt/RUN_CARD.json").read_text(encoding="utf-8"));issuer=FixtureIssuer();claims=deepcopy(sc["claim_base"]);token=issuer.issue(claims);ss=[]
  for case in card["spiffe_cases"]:
   work={"signature_verifications":0,"application_policy_checks":0};validated=None;reason=None;now=sc["reference_time"]+case["validation_time_offset"]
   try:validated=sp.identity(token,{"example.org":{issuer.kid:issuer.public_key}},now,work)
   except Rejected as error:reason=str(error)
   if "expected_identity_accept" in case:assert (validated is not None)==case["expected_identity_accept"]
   effects={}
   if validated is not None:
    context={"sender":claims["sub"],"tenant":"tenant-A","purpose":"batch-remediation","capacity":True,"operation":case["id"],"grant":{"active":True,"tenant":"tenant-A","purpose":"batch-remediation"},"now":sc["reference_time"]+case.get("application_time_offset",case["validation_time_offset"])}
    reason=sp.qualified_receiver(validated,context,effects,work)
   if "expected_receiver_effect" in case:assert bool(effects)==case["expected_receiver_effect"]
   ss.append({"id":case["id"],"identity_accepted":validated is not None,"validation_time":now,"application_time":sc["reference_time"]+case.get("application_time_offset",case["validation_time_offset"]),"expiration":claims["exp"],"in_memory_effect_returned":bool(effects),"reason":reason,"work":work,"compact_token_digest":token_digest(token),"diagnostic":case.get("diagnostic")})
  out["spiffe_jwt"]=ss
  ra=load_module("completion_rats",root/"independent-dds-exercises-v0.1/rats-jws/run.py");rc=json.loads((root/"independent-dds-exercises-v0.1/rats-jws/RUN_CARD.json").read_text(encoding="utf-8"));rr=[]
  good=(root/"independent-dds-exercises-v0.1/rats-jws/fixture_good.py").read_bytes();bad=(root/"independent-dds-exercises-v0.1/rats-jws/fixture_changed.py").read_bytes()
  original_measure=ra.measure
  for case in card["rats_cases"]:
   path=target/(case["id"]+".py")
   with path.open("xb") as file:file.write(good)
   reference=hashlib.sha256(good).hexdigest();now=rc["reference_time"];nonce="completion-"+case["id"];work={"file_hash_reads":0,"signature_verifications":0,"application_policy_checks":0}
   attester=FixtureIssuer("attester-key");verifier=FixtureIssuer("verifier-key")
   evidence={"sub":"case-service","aud":"local-verifier","exp":now+120,"nonce":nonce,"policy":"software-policy-v1",ra.PREDICATE:original_measure(path,work)}
   evidence_token=attester.issue(evidence);appraised=ra.appraise(evidence_token,attester.public_key,{"id":"software-policy-v1","reference":reference},nonce,now,work)
   result={"sub":"case-service","aud":"local-relying-party","exp":now+60,"nonce":nonce,"policy":"software-policy-v1",ra.PREDICATE:appraised[ra.PREDICATE],"status":"PASS"}
   result_token=verifier.issue(result);observations=[]
   def read_then_maybe_change(file,counter):
    measured=original_measure(file,counter);observations.append(measured)
    if case["mutate_after_read"]:Path(file).write_bytes(bad)
    return measured
   ra.measure=read_then_maybe_change
   context={"now":now,"subject":"case-service","nonce":nonce,"policy":"software-policy-v1","grant":True,"capacity":True,"current_source":True,"applied":True,"software_path":path}
   try:effect=ra.consume(result_token,verifier.public_key,context,work)
   finally:ra.measure=original_measure
   actual=hashlib.sha256(path.read_bytes()).hexdigest();matches=actual==effect["applied_software_sha256"]
   assert bool(effect)==case["expected_return"] and matches==case["expected_file_matches_return"]
   rr.append({"id":case["id"],"qualified_return":bool(effect),"source_digest_at_read":observations[0],"actual_source_digest_after_return":actual,"file_matches_return":matches,"work":work,"application_confirmation":"fixture Boolean; no external actuation executed","instrumentation": "read-then-mutate callback" if case["mutate_after_read"] else "unchanged read callback","diagnostic":case.get("diagnostic")})
  out["rats_jws"]=rr;out["status"]="PASS_PREREGISTERED_BOUNDARY_EXPECTATIONS";out["boundary_case_count"]=len(ar)+len(hr)+len(sr)+len(ss)+len(rr)
  with (target/"RESULTS.json").open("x",encoding="utf-8") as file:json.dump(out,file,indent=2);file.write("\n")
  print(json.dumps({"status":out["status"],"cases":out["boundary_case_count"],"q_boundary":out["analytical"]["q_effectiveness_boundary"],"hew":[[r["id"],r["sufficient_delivery"],r["work"]] for r in hr],"stpa":[[r["id"],r["outcome"]] for r in sr],"rats_race_retained":rr[-1]["file_matches_return"] is False}))
 except Exception as error:
  with (target/"FAILED_ATTEMPT.json").open("x",encoding="utf-8") as file:json.dump({"status":"FAILED_BOUNDARY_ATTEMPT","error":repr(error),"partial_results":out},file,indent=2)
  raise
if __name__=="__main__":
 parser=argparse.ArgumentParser();parser.add_argument("--source-root",default=str(HERE.parent));parser.add_argument("--output",required=True);args=parser.parse_args();main(args.source_root,args.output)

