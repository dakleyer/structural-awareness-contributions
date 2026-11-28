"""Verify literal repair candidates without modifying source or reference results."""
from pathlib import Path
import argparse,hashlib,json,sys,tempfile,urllib.parse,urllib.request

HERE=Path(__file__).resolve().parent
def git_blob(raw):
 return hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()

def verify(snapshot_root=None):
 data=json.loads((HERE/"INTERPRETATION_REPAIR_CANDIDATES_2026-10-27.json").read_text(encoding="utf-8"))
 cards=data["cards"];sources={};events=[]
 cache=Path(tempfile.gettempdir())/"IMSV-interpretation-proposal-cache"
 for card in cards:
  key=(card["source"],card["path"],card["blob"])
  if key not in sources:
   path=Path(snapshot_root)/card["source"]/card["path"] if snapshot_root else cache/card["blob"]
   if not path.exists() and not snapshot_root:
    cache.mkdir(parents=True,exist_ok=True)
    url="https://raw.githubusercontent.com/dakleyer/structural-awareness-contributions/"+card["ref"]+"/"+urllib.parse.quote(card["path"],safe="/")
    with urllib.request.urlopen(url,timeout=30) as r:raw=r.read()
    if git_blob(raw)!=card["blob"]:raise ValueError("Source pin mismatch: "+card["id"])
    path.write_bytes(raw)
   raw=path.read_bytes()
   if git_blob(raw)!=card["blob"]:raise ValueError("Source pin mismatch: "+card["id"])
   sources[key]=raw
  raw=sources[key];text=raw.decode("utf-8")
  before=card["before"];after=card["after"]
  if text.count(before)!=1:raise ValueError("Original unit not unique: "+card["id"])
  actual_line=text[:text.index(before)].count("\n")+1
  if actual_line!=card["line"]:raise ValueError("Line mismatch: "+card["id"])
  if card["mode"]=="historical_disposition":
   new=text+"\n\n"+after
   if new[:-len("\n\n"+after)]!=text:raise ValueError("Historical preservation")
  elif card["mode"]=="retain_reference":
   if before!=after:raise ValueError("Retained theorem changed")
  else:
   new=text.replace(before,after,1)
   if new.count(after)!=1 or new.replace(after,before,1).encode("utf-8")!=raw:raise ValueError("Inverse preservation: "+card["id"])
  if before.startswith("|") and card["mode"] not in {"historical_disposition","retain_reference"}:
   if before.count("|")!=after.count("|"):raise ValueError("Table column change: "+card["id"])
  events.append({"id":card["id"],"source_blob_verified":True,"literal_unit_and_line_verified":True,"preservation_verified":True,"source_applied":False})
 # Check combinations of candidates in one source, not only isolated substitutions.
 groups={}
 for card in cards:groups.setdefault((card["source"],card["path"],card["blob"]),[]).append(card)
 for key,group in groups.items():
  original=sources[key].decode("utf-8");text=original;undo=[]
  for card in group:
   if card["mode"]=="retain_reference":continue
   if card["mode"]=="historical_disposition":
    suffix="\n\n"+card["after"];text+=suffix;undo.append(("tail",suffix,""))
   else:
    if text.count(card["before"])!=1:raise ValueError("Overlapping candidates: "+card["id"])
    text=text.replace(card["before"],card["after"],1);undo.append(("replace",card["after"],card["before"]))
  for mode,after,before in reversed(undo):
   if mode=="tail":
    if not text.endswith(after):raise ValueError("Append changed")
    text=text[:-len(after)]
   else:text=text.replace(after,before,1)
  if text!=original:raise ValueError("Combined inverse failed")
 # Finite examples explaining why the interpretation distinctions matter.
 worlds=[0,1]
 risk_constant=sum(int(0!=w) for w in worlds)/2
 risk_decoder=sum(int(w!=w) for w in worlds)/2
 if not (risk_constant==.5 and risk_decoder==0):raise AssertionError("Same information, distinct policies")
 W=list(range(4));X=lambda w:w//2;Y=lambda w:w;q=lambda w:w%2
 if not any(X(a)==X(b) and q(a)!=q(b) for a in W for b in W):raise AssertionError("Lost distinction")
 if not all(q(w)==Y(w)%2 for w in W):raise AssertionError("Retained distinction")
 # A numerical cost example is an illustration of non-implication, not measured advantage.
 gross=10;execution=1
 lifecycle_a=gross-execution-2
 lifecycle_b=gross-execution-20
 if lifecycle_a==lifecycle_b:raise AssertionError("Same execution need not equal total cost")
 return {"status":"INTERNAL_PROPOSAL_VERIFICATION","cards_verified":len(events),"source_blobs_verified":len(sources),"combined_source_groups_verified":len(groups),"source_edits_applied":0,"checks":events,"finite_examples":{"same_information_policy_risks":[risk_constant,risk_decoder],"same_execution_different_lifecycle_net":[lifecycle_a,lifecycle_b]}}

if __name__=="__main__":
 p=argparse.ArgumentParser()
 p.add_argument("--snapshot-root",type=Path)
 p.add_argument("--output",type=Path)
 a=p.parse_args();r=verify(a.snapshot_root)
 raw=(json.dumps(r,ensure_ascii=False,indent=2)+"\n").encode("utf-8")
 if a.output:
  # Exclusive creation prevents accidental overwrite of a checked-in reference.
  with a.output.open("xb") as f:f.write(raw)
 print(json.dumps({k:v for k,v in r.items() if k!="checks"},ensure_ascii=False))

