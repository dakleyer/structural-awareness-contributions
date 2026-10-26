"""Execute a selected JWT-SVID profile with real RSA/JWS checks and a separate application."""
from pathlib import Path
from urllib.parse import urlsplit
import argparse,json,sys,time
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from crypto_fixture import FixtureIssuer,Rejected,verify,parse,token_digest
from exercise_common import load_frozen,save
ROOT=Path(__file__).resolve().parent

def identity(token,bundles,now,cost):
    if len(token)>8192:raise Rejected("token-size")
    pieces=token.split(".")
    if len(pieces)!=3:raise Rejected("compact-jws-required")
    # Unverified subject is used only to select an admitted local bundle.
    untrusted=parse(pieces[1]);sub=untrusted.get("sub")
    if not isinstance(sub,str):raise Rejected("spiffe-subject-required")
    u=urlsplit(sub)
    if u.scheme!="spiffe" or not u.netloc or u.query or u.fragment or "@" in u.netloc or ":" in u.netloc:
        raise Rejected("invalid-selected-spiffe-id")
    if u.netloc not in bundles:raise Rejected("untrusted-domain")
    claims=verify(token,bundles[u.netloc],"batch-service",now,cost)
    if claims["sub"]!=sub:raise Rejected("subject-instability")
    return claims

def qualified_receiver(claims,context,effects,cost):
    cost["application_policy_checks"]+=1
    if claims["sub"]!=context["sender"]:return "sender-mismatch"
    g=context["grant"]
    if not g["active"]:return "grant-revoked"
    if g["tenant"]!=context["tenant"]:return "tenant-mismatch"
    if g["purpose"]!=context["purpose"]:return "purpose-mismatch"
    if not context["capacity"]:return "useful-review-unavailable"
    operation=context["operation"]
    if operation not in effects:effects[operation]={"tenant":context["tenant"],"purpose":context["purpose"],"action":"apply-batch"}
    return "delivery-confirmed"

def main(output):
    card,freeze=load_frozen(ROOT);trusted=FixtureIssuer();untrusted=FixtureIssuer();rotated=FixtureIssuer("fixture-rotated")
    start=time.perf_counter();rows=[];assertions=0;counts={"I":0,"M":0,"P":0,"incomplete":0};diagnostics=0
    for case in card["cases"]:
        m=case["mutations"];claims=dict(card["claim_base"]);claims.update(m.get("claims",{}))
        for key in m.get("remove_claims",[]):claims.pop(key,None)
        issuer=rotated if m.get("rotated_key") else (untrusted if m.get("wrong_signer") else trusted)
        raw=None
        if m.get("duplicate_claims"):
            raw=json.dumps(claims,separators=(",",":"))[:-1]+',"exp":1791299000}'
        token=issuer.issue(claims,m.get("headers"),raw)
        if m.get("tamper_signature"):
            a,b,c=token.split(".");token=a+"."+b+"."+("A" if c[0]!="A" else "B")+c[1:]
        if m.get("oversized"):token="x"*8193
        keys={trusted.kid:trusted.public_key}
        if m.get("retired_key"):keys={}
        if m.get("rotated_key"):keys={rotated.kid:rotated.public_key}
        cost={"signature_verifications":0,"application_policy_checks":0}
        result=None;reason=None
        try:result=identity(token,{"example.org":keys},m.get("now",card["reference_time"]),cost)
        except Rejected as exc:reason=str(exc)
        accepted=result is not None
        assert accepted==case["expected_identity_accept"],(case["id"],reason);assertions+=1
        context={"sender":"spiffe://example.org/batch/client","tenant":"tenant-A","purpose":"batch-remediation",
            "capacity":m.get("capacity",True),"operation":case["id"],
            "grant":{"active":m.get("grant_active",True),"tenant":m.get("grant_tenant","tenant-A"),"purpose":m.get("grant_purpose","batch-remediation")}}
        effects={}
        if accepted:
            reason=qualified_receiver(result,context,effects,cost)
            if m.get("replay"):qualified_receiver(result,context,effects,cost)
        delivered=bool(effects)
        assert delivered==case["expected_qualified_delivery"],case["id"];assertions+=1
        assert len(effects)<=1,"replay caused duplicate actuation";assertions+=1
        outcome="I" if delivered else "incomplete";counts[outcome]+=1
        # Deliberate misuse diagnostic: successful identity is treated as complete permission/capacity.
        misuse_wrong=accepted and not case["expected_qualified_delivery"]
        diagnostics+=int(misuse_wrong)
        rows.append({"id":case["id"],"narrative":case["narrative"],"identity_accepted":accepted,
            "receiving_reason":reason,"effects":list(effects.values()),"qualified_outcome":outcome,
            "identity_only_misuse_wrong_effect":misuse_wrong,"work":cost,"compact_token_sha256":token_digest(token),
            "secret_or_compact_token_exported":False})
    save(ROOT,output,card,freeze,{"status":"PASS_REGISTERED_FIXTURE_ASSERTIONS","cases":rows,"assertions":assertions,
        "qualified_outcome_counts":counts,"diagnostic_wrong_effects":diagnostics,
        "diagnostic_is_not_a_strong_SPIFFE_comparator":True,"elapsed_local_seconds":time.perf_counter()-start,
        "scope":"Own selected RS256 JWT-SVID/app validation fixture using cryptography, no native SPIRE/Workload API execution",
        "external_matched_differential":"not established"})
if __name__=="__main__":
    a=argparse.ArgumentParser();a.add_argument("--output",required=True);main(a.parse_args().output)

