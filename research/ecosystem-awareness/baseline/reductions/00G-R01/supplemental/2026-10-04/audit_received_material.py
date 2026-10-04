"""Additional diagnostics of received proposals; originals are not modified.
These finite counterexamples do not validate the full R01 theorem.
"""
from pathlib import Path
from fractions import Fraction as F
import ast,itertools,json,math
ROOT=Path(__file__).parent
SOURCE=ROOT/'sources'/'testA_budget.py'
# Reuse just the received definitions, without rerunning its top-level grid.
tree=ast.parse(SOURCE.read_text())
nodes=[n for n in tree.body if isinstance(n,(ast.Import,ast.ImportFrom,ast.FunctionDef)) or (isinstance(n,ast.Assign) and any(isinstance(t,ast.Tuple) for t in n.targets))]
ns={};exec(compile(ast.Module(body=nodes,type_ignores=[]),str(SOURCE),'exec'),ns)
L=2;eps=0;c=1;h=F(1,2);r=F(1,4);base=8
reported=ns['formula'](L,eps,c,float(h),float(r))[0]
lp=ns['feasible'](L,eps,c,9,float(h),float(r))
# Half the time query one local bit and guess the other; otherwise take M.
witness={'hard_budget':9,'eta':str(h),'rho':str(h*F(1,2)),'sigma':str(h*F(1,2)),
         'attempt_probability':'1/2','queries_on_attempt':1,'guessed_bits':1}
assert reported==10 and lp and h*F(1,2)==r

# Sparse proposal: a hidden K-subset and one fair forbidden orientation per binding.
# A delivery need not identify the subset. All-X serves choose(L,K) worlds.
sparse=[]
for L in (2,3,4,5,6):
 for K in range(1,min(L,3)+1):
  worlds=[(positions,bits) for positions in itertools.combinations(range(L),K) for bits in itertools.product((0,1),repeat=K)]
  # At each constrained position, X is permitted iff its hidden bit is 0.
  valid=sum(all(bit==0 for bit in bits) for _,bits in worlds)
  success=F(valid,len(worlds));claimed=F(1,len(worlds))
  assert success==F(1,2**K)
  if K<L:assert success>claimed
  sparse.append({'L':L,'K':K,'world_count':len(worlds),'all_X_compatible_worlds':valid,
                 'zero_query_legitimate_success':str(success),'exact_recovery_counting_candidate':str(claimed),
                 'counterexample_to_automatic_exact_recovery_transfer':success>claimed})
 # For K=1 a route-membership service that answers before effect is enough:
 # approve all-X; if denied, the unique constraint forbids X, so all-Y is safe.
 for positions,bits in [(p,b) for p in itertools.combinations(range(L),1) for b in itertools.product((0,1),repeat=1)]:
  choose_X=all(bit==0 for bit in bits)
  chosen_bit=0 if choose_X else 1
  assert all(chosen_bit==bit for bit in bits)

# Received noise estimate: asymptotic capacity is not a finite-block lower bound.
q=F(99,100);L=3
assert q**L>=F(3,4)
capacity=1-(-float(q)*math.log2(float(q))-float(1-q)*math.log2(float(1-q)))
assert 3/capacity>3

# No check-use window, a fresh certificate immediately before every effect:
# age is 0, so drift between past effects does not make this effect stale.
p=F(1,100);L=10;block=1
ages=[i%block for i in range(L)]
exact_stale=sum((1-(1-2*p)**a)/2 for a in ages)
received_first_order=p*L*block/2
assert exact_stale==0 and received_first_order>0

report={'kind':'same-agent finite supplementary diagnostics; not independent full proof',
 'testA_general_threshold_counterexample':{'reported_formula_budget':reported,'received_LP_feasible_at_9':bool(lp),'exact_witness':witness,'finding':'formula ignores efficacy h; received 60-point grid does not expose this case'},
 'sparse_route_vs_world_recovery':{'rows':sparse,'K1_pre_effect_route_oracle_control':'one query of all-X then choose all-X/all-Y gives eta=1,rho=0 for every world and every L in the declared K1 family','scope':'changed interface; sparse proposal as written does not inherit log choose(L,K) exact-recovery cost'},
 'noise_finite_block':{'q':'99/100','L':3,'three_query_success':str(q**3),'capacity_estimate':3/capacity,'finding':'3/capacity is a heuristic/asymptotic comparison, not a universal finite-sample lower bound; source search optimizes fixed repetition allocations only'},
 'staleness_zero_window_control':{'p':str(p),'L':L,'block_size':block,'exact_expected_stale_effects':str(exact_stale),'received_first_order':str(received_first_order),'finding':'refresh timing and drift/effect kernel must be declared; expectation yields sufficient probability control under conditions, not a necessary risk frontier'},
 'claims_unchanged':'No refutation of existing F/W theorems is asserted; these attacks concern the received additions and unjustified transfers.'}
(ROOT/'runs'/'additional_diagnostics.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'diagnostics':'PASS','formula_counterexample':reported,'feasible_witness_budget':9,'sparse_rows':len(sparse),'new_theorem_validated':False}))
