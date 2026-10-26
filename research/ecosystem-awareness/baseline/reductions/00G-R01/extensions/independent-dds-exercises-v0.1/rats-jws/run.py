"""Local RATS role/policy consumption exercise: actual hashes/JWS, synthetic trust sources."""
from pathlib import Path
import argparse,hashlib,sys,time
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from crypto_fixture import FixtureIssuer,Rejected,verify,token_digest
from exercise_common import load_frozen,save
ROOT=Path(__file__).resolve().parent
PREDICATE="https://example.org/dds/software-sha256"

def measure(path,cost):
    cost["file_hash_reads"]+=1
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def appraise(token,key,policy,nonce,now,cost):
    e=verify(token,{"attester-key":key},"local-verifier",now,cost)
    if e.get("sub")!="case-service":raise Rejected("evidence-subject")
    if e.get("nonce")!=nonce:raise Rejected("evidence-nonce")
    if e.get("policy")!=policy["id"]:raise Rejected("evidence-policy")
    if e.get(PREDICATE)!=policy["reference"]:raise Rejected("measurement-reference")
    return e

def consume(token,key,context,cost):
    r=verify(token,{"verifier-key":key},"local-relying-party",context["now"],cost)
    cost["application_policy_checks"]+=1
    if r.get("sub")!=context["subject"] or r.get("nonce")!=context["nonce"]:raise Rejected("result-subject-or-nonce")
    if r.get("status")!="PASS":raise Rejected("result-not-pass")
    if r.get("policy")!=context["policy"]:raise Rejected("current-policy")
    if not context["grant"]:raise Rejected("grant-revoked")
    if not context["capacity"]:raise Rejected("useful-human-review-not-established")
    if not context["current_source"]:raise Rejected("current-state-unknown")
    current=measure(context["software_path"],cost)
    if current!=r[PREDICATE]:raise Rejected("current-state-does-not-match-result")
    # This source read/effect boundary is sequential within this local model.
    # It is not distributed/physical atomicity or a trusted hardware measurement.
    if not context["applied"]:raise Rejected("no-confirmed-application")
    return {"applied_software_sha256":current,"subject":context["subject"],"policy":context["policy"]}

def main(output):
    card,freeze=load_frozen(ROOT)
    attester=__import__("crypto_fixture").FixtureIssuer("attester-key");other_attester=__import__("crypto_fixture").FixtureIssuer("attester-key")
    verifier=__import__("crypto_fixture").FixtureIssuer("verifier-key");other_verifier=__import__("crypto_fixture").FixtureIssuer("verifier-key")
    good=ROOT/"fixture_good.py";bad=ROOT/"fixture_changed.py";reference=hashlib.sha256(good.read_bytes()).hexdigest()
    start=time.perf_counter();rows=[];assertions=0;counts={"I":0,"M":0,"P":0,"incomplete":0};diagnostics=0
    for case in card["cases"]:
        m=case["mutations"];now=card["reference_time"];nonce="request-"+case["id"]
        software=bad if m.get("software")=="bad" else good
        cost={"file_hash_reads":0,"signature_verifications":0,"application_policy_checks":0}
        evidence={"sub":m.get("evidence_subject","case-service"),"aud":"local-verifier","exp":now-1 if m.get("evidence_expired") else now+120,
            "nonce":m.get("evidence_nonce",nonce),"policy":m.get("evidence_policy","software-policy-v1"),PREDICATE:measure(software,cost)}
        if m.get("false_measurement"):evidence[PREDICATE]=reference
        if m.get("omit_measurement"):evidence.pop(PREDICATE)
        producer=other_attester if m.get("wrong_attester") else attester
        evidence_token=producer.issue(evidence)
        e=None;reason=None
        try:e=appraise(evidence_token,attester.public_key,{"id":"software-policy-v1","reference":reference},nonce,now,cost)
        except Rejected as exc:reason=str(exc)
        accepted=e is not None
        assert accepted==case["expected_verifier_accept"],(case["id"],reason);assertions+=1
        result_token=None;effect=None;naive_wrong=False
        if e is not None:
            result={"sub":"case-service","aud":m.get("result_audience","local-relying-party"),
                "exp":now-1 if m.get("result_expired") else now+60,"nonce":nonce,"policy":"software-policy-v1",
                PREDICATE:e[PREDICATE],"status":m.get("result_status","PASS")}
            producer=other_verifier if m.get("wrong_verifier") else verifier
            result_token=producer.issue(result)
            if m.get("change_after_appraisal"):software=bad
            context={"now":now,"subject":"case-service","nonce":nonce,"policy":m.get("receiving_policy","software-policy-v1"),
                "grant":m.get("grant_active",True),"capacity":m.get("capacity",True),
                "current_source":m.get("current_source",True),"applied":m.get("applied",True),"software_path":software}
            try:effect=consume(result_token,verifier.public_key,context,cost);reason="delivery-confirmed"
            except Rejected as exc:reason=str(exc)
            # Isolate the snapshot inference only: ordinary signature/purpose/expiry validation still applies.
            try:
                old=verify(result_token,{"verifier-key":verifier.public_key},"local-relying-party",now,{"signature_verifications":0})
                naive_allowed=old.get("status")=="PASS" and old.get("policy")==context["policy"] and context["grant"] and context["capacity"]
                actual=hashlib.sha256(software.read_bytes()).hexdigest()
                naive_wrong=naive_allowed and actual!=old[PREDICATE]
            except Rejected:pass
        delivered=effect is not None
        assert delivered==case["expected_qualified_delivery"],(case["id"],reason);assertions+=1
        actual_digest=hashlib.sha256(software.read_bytes()).hexdigest()
        wrong=effect is not None and (effect["applied_software_sha256"]!=reference or actual_digest!=reference)
        assert not wrong,case["id"];assertions+=1
        outcome="I" if delivered else "incomplete";counts[outcome]+=1;diagnostics+=int(naive_wrong)
        rows.append({"id":case["id"],"narrative":case["narrative"],"verifier_accepted":accepted,"relying_reason":reason,
            "qualified_effect":effect,"qualified_outcome":outcome,"snapshot_only_diagnostic_wrong_effect":naive_wrong,
            "work":cost,"evidence_sha256":token_digest(evidence_token),
            "attestation_result_sha256":token_digest(result_token) if result_token else None,"keys_or_compact_tokens_exported":False})
    save(ROOT,output,card,freeze,{"status":"PASS_REGISTERED_FIXTURE_ASSERTIONS","cases":rows,"assertions":assertions,
        "qualified_outcome_counts":counts,"diagnostic_wrong_effects":diagnostics,"elapsed_local_seconds":time.perf_counter()-start,
        "scope":"Own RFC9334-informed software-state/JWS local roles; actual cryptography/hashes, stipulated trust provenance, no TPM/EAT/native verifier product",
        "risk_of_false_trusted_measurements":"Current file-source query helps only under this declared local trust/source assumption",
        "external_matched_differential":"not established"})
if __name__=="__main__":
    a=argparse.ArgumentParser();a.add_argument("--output",required=True);main(a.parse_args().output)

