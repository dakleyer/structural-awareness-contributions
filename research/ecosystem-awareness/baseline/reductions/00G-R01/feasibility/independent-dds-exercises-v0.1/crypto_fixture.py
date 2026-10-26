"""Actual local RSA/JWS operations; fixture keys and compact tokens stay in memory."""
import base64,hashlib,json
from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding,rsa

class Rejected(ValueError): pass

def b64(x):return base64.urlsafe_b64encode(x).rstrip(b"=").decode("ascii")
def unb64(x):
    if not isinstance(x,str) or any(c not in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_" for c in x):
        raise Rejected("invalid-base64url")
    try:return base64.urlsafe_b64decode(x+"="*((-len(x))%4))
    except Exception as exc:raise Rejected("invalid-base64url") from exc

def no_duplicates(pairs):
    result={}
    for k,v in pairs:
        if k in result:raise Rejected("duplicate-json-member")
        result[k]=v
    return result

def parse(x):
    try:
        obj=json.loads(unb64(x),object_pairs_hook=no_duplicates)
        if not isinstance(obj,dict):raise Rejected("object-required")
        return obj
    except (UnicodeError,ValueError) as exc:
        if isinstance(exc,Rejected):raise
        raise Rejected("invalid-json") from exc

class FixtureIssuer:
    def __init__(self,kid="fixture-key"):
        self.kid=kid
        self._private=rsa.generate_private_key(public_exponent=65537,key_size=2048)
        self.public_key=self._private.public_key()
    def issue(self,claims,headers=None,raw_claims=None):
        head={"alg":"RS256","kid":self.kid,"typ":"JWT"}
        if headers is not None:head.update(headers)
        h=b64(json.dumps(head,separators=(",",":"),sort_keys=True).encode())
        p=b64(raw_claims.encode() if raw_claims is not None else json.dumps(claims,separators=(",",":"),sort_keys=True).encode())
        signed=(h+"."+p).encode()
        signature=self._private.sign(signed,padding.PKCS1v15(),hashes.SHA256())
        return h+"."+p+"."+b64(signature)

def verify(token,keys,audience,now,counter):
    if not isinstance(token,str) or len(token)>8192:raise Rejected("token-size")
    segments=token.split(".")
    if len(segments)!=3:raise Rejected("compact-jws-required")
    h,p,s=segments
    head=parse(h)
    if set(head)-{"alg","kid","typ"}:raise Rejected("unsupported-header")
    if head.get("alg")!="RS256":raise Rejected("algorithm-outside-selected-rs256-profile")
    if head.get("typ") not in (None,"JWT","JOSE"):raise Rejected("invalid-typ")
    kid=head.get("kid")
    if kid not in keys:raise Rejected("unknown-key")
    counter["signature_verifications"]+=1
    try:keys[kid].verify(unb64(s),(h+"."+p).encode(),padding.PKCS1v15(),hashes.SHA256())
    except (InvalidSignature,ValueError) as exc:raise Rejected("invalid-signature") from exc
    claims=parse(p)
    exp=claims.get("exp")
    if isinstance(exp,bool) or not isinstance(exp,(int,float)):raise Rejected("expiration-required")
    if now>=exp:raise Rejected("expired")
    nbf=claims.get("nbf")
    if nbf is not None and (isinstance(nbf,bool) or not isinstance(nbf,(int,float)) or now<nbf):raise Rejected("not-yet-valid")
    aud=claims.get("aud")
    if not ((isinstance(aud,str) and aud==audience) or
            (isinstance(aud,list) and aud and all(isinstance(x,str) for x in aud) and audience in aud)):
        raise Rejected("audience-required-or-mismatch")
    return claims

def token_digest(token):return hashlib.sha256(token.encode()).hexdigest()

