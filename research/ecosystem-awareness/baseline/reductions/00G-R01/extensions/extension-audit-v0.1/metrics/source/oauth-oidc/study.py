"""Selected OAuth/OIDC DDS fixture; actual local RSA/SQLite, no native authorization service."""
import argparse,base64,collections,hashlib,importlib.metadata,json,sqlite3,sys
from pathlib import Path
from cryptography.hazmat.primitives.asymmetric import rsa,padding
from cryptography.hazmat.primitives import hashes
from cryptography.exceptions import InvalidSignature
HERE=Path(__file__).resolve().parent
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def enc(b):return base64.urlsafe_b64encode(b).rstrip(b"=").decode()
def dec(s):return base64.urlsafe_b64decode(s+"="*((-len(s))%4))
def unique(items):
    d={}
    for k,v in items:
        if k in d:raise ValueError("duplicate JSON member")
        d[k]=v
    return d
def frozen():
    c=json.loads((HERE/"RUN_CARD.json").read_text(encoding="utf-8"));f=json.loads((HERE/"FREEZE.json").read_text())
    for n,h in f["files"].items():
        if sha(HERE/n)!=h:raise RuntimeError("freeze mismatch "+n)
    if sys.version.split()[0]!=c["technology"]["python"] or sqlite3.sqlite_version!=c["technology"]["sqlite"]:raise RuntimeError("runtime mismatch")
    if importlib.metadata.version("cryptography")!=c["technology"]["cryptography"]:raise RuntimeError("crypto mismatch")
    return c
def sign(header,claims,key):
    msg=enc(json.dumps(header,separators=(",",":")).encode())+"."+enc(json.dumps(claims,separators=(",",":")).encode())
    return msg+"."+enc(key.sign(msg.encode(),padding.PKCS1v15(),hashes.SHA256()))
def validate(token,key,p,purpose,work):
    try:
        if len(token)>16000:return None,"oversized"
        a,b,c=token.split(".");h=json.loads(dec(a),object_pairs_hook=unique);x=json.loads(dec(b),object_pairs_hook=unique)
        if h.get("alg")!="RS256":return None,"algorithm"
        work["signature_verifications"]+=1
        key.verify(dec(c),(a+"."+b).encode(),padding.PKCS1v15(),hashes.SHA256())
        if x.get("iss")!=p["issuer"]:return None,"issuer"
        if not isinstance(x.get("sub"),str) or not x["sub"]:return None,"subject"
        if type(x.get("exp")) is not int or x["exp"]<=p["now"]:return None,"expired"
        if purpose=="login":
            if h.get("typ")!="JWT" or x.get("aud")!=p["client"] or x.get("nonce")!=p["nonce"]:return None,"login-binding"
        else:
            if h.get("typ","").lower() not in ["at+jwt","application/at+jwt"]:return None,"token-purpose"
            if x.get("aud")!=p["resource"]:return None,"resource-audience"
            if p["scope"] not in x.get("scope","").split():return None,"scope"
        return x,"valid"
    except (ValueError,TypeError,KeyError,InvalidSignature):return None,"signature-or-parse"
def apply(db,claims,p,ctx,work):
    work["application_policy_checks"]+=1
    if claims["exp"]<=ctx["use_time"] or not ctx["current_grant"] or claims.get("tenant")!=p["tenant"]:return False
    work["operational_sql_statements"]+=1
    db.execute("insert or ignore into effects values(?,?)",(ctx["operation"],claims["sub"]));db.commit()
    return True
def adjudicate(effect_count,identity_return,case,authoritative):
    if effect_count:
        if not authoritative or effect_count!=1 or case["purpose"]!="resource":return "P"
        return "I"
    if identity_return and case["purpose"]=="login" and authoritative:return "M"
    return "Ø"
def main():
    ap=argparse.ArgumentParser();ap.add_argument("--output",required=True);args=ap.parse_args();card=frozen();out=Path(args.output);out.mkdir(parents=True,exist_ok=False)
    good=rsa.generate_private_key(public_exponent=65537,key_size=2048);wrong=rsa.generate_private_key(public_exponent=65537,key_size=2048)
    results=[];p=card["parameters"]
    for case in card["cases"]:
        kind=case["kind"];is_id=kind in ["id-token","wrong-nonce"]
        claims={"iss":p["issuer"],"sub":"subject-a","aud":p["client"] if is_id else p["resource"],"exp":p["expires"],"iat":900,"jti":case["id"],"client_id":p["client"],"scope":"write","tenant":p["tenant"]}
        if is_id:claims["nonce"]=p["nonce"]
        if kind=="wrong-audience":claims["aud"]="resource-b"
        if kind=="expired":claims["exp"]=p["now"]
        if kind=="missing-scope":claims["scope"]="read"
        if kind=="wrong-nonce":claims["nonce"]="other-request"
        token=sign({"alg":"RS256","typ":"JWT" if is_id else "at+jwt","kid":"fixture"},claims,wrong if kind=="wrong-signer" else good)
        work={"signature_verifications":0,"application_policy_checks":0,"operational_sql_statements":0}
        db=sqlite3.connect(out/(case["id"]+".sqlite"));db.execute("create table effects(operation text primary key,subject text)")
        verified,reason=validate(token,good.public_key(),p,case["purpose"],work)
        ctx={"use_time":1011 if kind=="late-use" else p["now"],"current_grant":kind!="revoked-grant","operation":"operation-a"}
        identity_return=bool(verified and case["purpose"]=="login")
        if verified and case["purpose"]=="resource":
            for _ in range(2 if kind=="duplicate" else 1):apply(db,verified,p,ctx,work)
        # Post-effect evaluator queries a separate connection; participant receives no expected outcome.
        audit=sqlite3.connect(out/(case["id"]+".sqlite"));count=audit.execute("select count(*) from effects").fetchone()[0];audit.close();db.close()
        authoritative=(kind not in ["wrong-audience","expired","wrong-signer","missing-scope","revoked-grant","late-use","wrong-nonce"] and not(kind=="id-token" and case["purpose"]=="resource"))
        outcome=adjudicate(count,identity_return,case,authoritative)
        assert outcome==case["expected"],(case["id"],outcome);assert count==case["effects"]
        # Semantic misuse diagnostic only, not a matched strong OAuth/OIDC comparator.
        weak_authorization_action=kind in ["revoked-grant","late-use"] or (kind=="id-token" and case["purpose"]=="resource")
        results.append({"id":case["id"],"narrative":case["narrative"],"outcome":outcome,"actual_local_effects":count,"identity_return":identity_return,"validator_reason":reason,"work":work,"token_sha256":hashlib.sha256(token.encode()).hexdigest(),"misuse_would_act_without_required_authorization":weak_authorization_action,"keys_or_compact_tokens_exported":False})
    result={"schema":"DDS-EXTENSION-RESULT-0.1","study":card["study"],"status":"PASS_REGISTERED_LOCAL_EXPECTATIONS","case_count":len(results),"assertions":2*len(results),"outcome_counts":dict(collections.Counter(r["outcome"] for r in results)),"results":results,"python":sys.version.split()[0],"sqlite":sqlite3.sqlite_version,"cryptography":importlib.metadata.version("cryptography"),"setup":{"ephemeral_RSA_key_pairs":2,"synthetic_tokens":len(results),"setup_not_priced_or_individually_timed":True},"card_sha256":sha(HERE/"RUN_CARD.json"),"freeze_sha256":sha(HERE/"FREEZE.json"),"native_authorization_service_or_browser_flow":False,"population_estimate":False,"independent_validation":False}
    with (out/"RESULTS.json").open("x",encoding="utf-8",newline="\n") as f:json.dump(result,f,ensure_ascii=False,indent=2);f.write("\n")
    print(json.dumps({k:result[k] for k in ["study","status","case_count","assertions","outcome_counts"]},ensure_ascii=True))
if __name__=="__main__":main()

