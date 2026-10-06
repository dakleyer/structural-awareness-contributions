"""Review-only CTv1 import contract; not installed in any R01 harness."""
import collections.abc,copy,hashlib,importlib.util,json,pathlib
ROOT=pathlib.Path(__file__).resolve().parent
BASE=ROOT/"sources/research/ecosystem-awareness/baseline"
EXCLUDED={"run_id","wall_clock_timestamp","host_process_id","temporary_output_path"}
PATHS={"repository_path","file_path","artifact_path","source_path"}
class ImportRejected(ValueError): pass
def validate(trace,rules):
    if not isinstance(trace,collections.abc.Mapping): raise ImportRejected("ROOT_NOT_OBJECT")
    if not isinstance(rules,dict): raise ImportRejected("INVALID_SET_RULES")
    if any(not isinstance(k,tuple) or not all(type(x) is str for x in k) or type(v) is not str or not v for k,v in rules.items()):
        raise ImportRejected("INVALID_SET_RULES")
    prepared=dict(trace)
    prepared["canonicalization_version"]="CTv1"
    visited=set()
    def walk(value,path=()):
        if value is None or type(value) in (str,bool,int): return
        if type(value) is dict:
            if any(type(k) is not str for k in value): raise ImportRejected("NON_STRING_KEY")
            for k,child in value.items():
                if k in EXCLUDED: continue
                if k in PATHS and child is not None:
                    if type(child) is not str: raise ImportRejected("PATH_NOT_STRING")
                    raw=child.replace("\\","/")
                    if raw.startswith("/") or (len(raw)>=2 and raw[1]==":") or ".." in pathlib.PurePosixPath(raw).parts:
                        raise ImportRejected("UNSAFE_PATH")
                walk(child,path+(k,))
            return
        if type(value) is list:
            if path in rules:
                visited.add(path)
                key=rules[path]
                if any(type(x) is not dict or key not in x for x in value): raise ImportRejected("MISSING_STABLE_KEY")
                ids=[x[key] for x in value]
                if any(type(x) is not str or not x for x in ids): raise ImportRejected("STABLE_KEY_NOT_STRING")
                if len(ids)!=len(set(ids)): raise ImportRejected("DUPLICATE_STABLE_KEY")
            for x in value: walk(x,path+("[]",))
            return
        raise ImportRejected("VALUE_OUTSIDE_IMPORT_PROFILE")
    walk(prepared)
    if visited!=set(rules): raise ImportRejected("SET_RULE_PATH_NOT_PRESENT")
def import_trace(helper,trace,rules=None):
    rules={} if rules is None else rules
    try: validate(trace,rules)
    except ImportRejected as exc:
        return {"status":"REJECTED_INPUT","reason":str(exc),"bytes":None}
    try: raw=helper.canonical_trace_bytes(trace,set_like_rules=rules)
    except Exception as exc:
        return {"status":"SERIALIZER_ERROR","reason":type(exc).__name__,"bytes":None}
    return {"status":"CANONICALIZED","reason":None,"bytes":raw}
def load(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod);return mod
def main():
    q=load("q1a_ctv1",BASE/"fixtures/RS-00E-Q1a/canonical_trace_v1.py")
    r=load("r01_ctv1",BASE/"reductions/00G-R01/oracle/canonical_trace_v1.py")
    good=[
        ("unicode",{"label":"oráculo"},{}),
        ("nested",{"events":[{"at":1,"ok":True,"value":None}]},{}),
        ("integer",{"count":12345678901234567890},{}),
        ("decimal_string",{"cost":"1.250"},{}),
        ("excluded_metadata",{"run_id":1.1,"payload":{"host_process_id":object(),"x":1}},{}),
        ("relative_path",{"source_path":"a/b.txt"},{}),
        ("path_separators",{"repository_path":"a\\b.txt"},{}),
        ("dot_path",{"artifact_path":"./a/./b"},{}),
        ("set_order",{"items":[{"id":"b","v":2},{"id":"a","v":1}]},{("items",):"id"}),
        ("version_overwrite",{"canonicalization_version":object(),"x":1},{})
    ]
    bad=[
        ("pairs_root",[("x",1)],{},"ROOT_NOT_OBJECT"),
        ("none_root",None,{},"ROOT_NOT_OBJECT"),
        ("missing_key",{"items":[{"v":1}]},{("items",):"id"},"MISSING_STABLE_KEY"),
        ("non_object_set_item",{"items":[1]},{("items",):"id"},"MISSING_STABLE_KEY"),
        ("heterogeneous_key",{"items":[{"id":1},{"id":"a"}]},{("items",):"id"},"STABLE_KEY_NOT_STRING"),
        ("duplicate_key",{"items":[{"id":"a"},{"id":"a"}]},{("items",):"id"},"DUPLICATE_STABLE_KEY"),
        ("unused_rule",{"x":1},{("items",):"id"},"SET_RULE_PATH_NOT_PRESENT"),
        ("float",{"x":1.1},{},"VALUE_OUTSIDE_IMPORT_PROFILE"),
        ("absolute_path",{"file_path":"/tmp/a"},{},"UNSAFE_PATH"),
        ("windows_absolute",{"file_path":"C:\\a"},{},"UNSAFE_PATH"),
        ("parent_path",{"file_path":"a/../b"},{},"UNSAFE_PATH"),
        ("path_type",{"file_path":1},{},"PATH_NOT_STRING"),
        ("mixed_keys",{1:"x","a":2},{},"NON_STRING_KEY"),
        ("tuple_outside_profile",{"x":(1,2)},{},"VALUE_OUTSIDE_IMPORT_PROFILE")
    ]
    rows=[]
    for label,trace,rules in good:
        original=copy.deepcopy(trace)
        a=import_trace(q,trace,rules);b=import_trace(r,trace,rules)
        assert a["status"]==b["status"]=="CANONICALIZED" and a["bytes"]==b["bytes"],label
        # object() metadata cannot be equality-compared after deepcopy; inspect semantic fields instead.
        assert trace.keys()==original.keys() and "canonicalization_version" not in trace or label=="version_overwrite",label
        rows.append({"id":label,"status":"MATCHED_VALID_BYTES","sha256":hashlib.sha256(a["bytes"]).hexdigest()})
    for label,trace,rules,reason in bad:
        a=import_trace(q,trace,rules);b=import_trace(r,trace,rules)
        assert a==b=={"status":"REJECTED_INPUT","reason":reason,"bytes":None},(label,a,b)
        rows.append({"id":label,"status":"MATCHED_IMPORT_REJECTION","reason":reason})
    # These are deliberately independent behavioural properties of the serialization boundary.
    ordered={"events":[{"at":1},{"at":2}]}
    reordered={"events":list(reversed(ordered["events"]))}
    assert import_trace(q,ordered)["bytes"]!=import_trace(q,reordered)["bytes"]
    one={"items":[{"id":"a"},{"id":"b"}]}
    two={"items":[{"id":"b"},{"id":"a"}]}
    assert import_trace(q,one,{("items",):"id"})["bytes"]==import_trace(r,two,{("items",):"id"})["bytes"]
    assert import_trace(q,{"run_id":"a","x":1})["bytes"]==import_trace(r,{"run_id":"b","x":1})["bytes"]
    sample={"events":[{"at":1}],"canonicalization_version":"old"}
    previous=copy.deepcopy(sample)
    import_trace(q,sample);import_trace(r,sample)
    assert sample==previous
    rows.extend({"id":name,"status":"PROPERTY_VERIFIED"} for name in [
        "chronology_not_sorted","declared_set_reordering_invariant","metadata_exclusion_invariant","caller_not_mutated"])
    # Confirm the two historical helper differences without changing either implementation.
    raw_q_root=raw_r_root=None
    try:q.canonical_trace_bytes([("x",1)])
    except Exception as e:raw_q_root=type(e).__name__
    try:r.canonical_trace_bytes([("x",1)]);raw_r_root="ACCEPTED"
    except Exception as e:raw_r_root=type(e).__name__
    raw_errors=[]
    for helper in (q,r):
        try:helper.canonical_trace_bytes({"items":[{"v":1}]},set_like_rules={("items",):"id"})
        except Exception as e:raw_errors.append(type(e).__name__)
    assert raw_q_root=="CanonicalTraceError" and raw_r_root=="ACCEPTED"
    assert raw_errors==["CanonicalTraceError","KeyError"]
    result={"profile":"R01-CTv1-IMPORT-REVIEW-1","status":"BOUNDED_REVIEW_PROTOTYPE_CHECKS_PASS",
        "shared_valid_examples":len(good),"invalid_examples":len(bad),"behavioural_properties":4,
        "total_checks":len(rows),"raw_helpers_still_differ":{"pairs_root":[raw_q_root,raw_r_root],"missing_key":raw_errors},
        "rows":rows,"limits":["review prototype only; not installed/admitted","not universal conformance","no candidate campaign or scientific harness executed","same agent; no independent review"]}
    (ROOT/"CTv1_IMPORT_REVIEW_RESULT.json").write_text(json.dumps(result,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    print(json.dumps({k:v for k,v in result.items() if k not in ("rows",)},ensure_ascii=False))
if __name__=="__main__":main()
