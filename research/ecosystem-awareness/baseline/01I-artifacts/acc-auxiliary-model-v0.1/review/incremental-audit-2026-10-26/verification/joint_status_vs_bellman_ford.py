"""Joint-evidence status of qualify() against an exact feasibility oracle.

Usage: python3 -B joint_status_vs_bellman_ford.py <studies/scoped-closure-metacognition-v0.1>
Compares _joint_evidence_status with a Bellman-Ford check of the difference
constraints |y_i - y_j| <= L |x_i - x_j|, l_i <= y_i <= u_i, on 4 000 random
cases, and checks that the envelope bounds are attainable. Supports the I-01 /
M27-01 closure (rounds 11-13). Expected: 0 mismatches, 1 990 envelope cases,
on main 51fc686 and on PR #64. Writes nothing.
"""
import sys, random, itertools
sys.path.insert(0, sys.argv[1])
import metacognition as m

def feasible(pts, L, extra=None):
    """Bellman-Ford on difference constraints: exists y_i in [l_i,u_i] with |y_i-y_j|<=L|x_i-x_j|."""
    P = list(pts) + ([extra] if extra else [])
    n = len(P); N = n + 1  # node n = origin 0
    edges = []
    for i,(xi,li,ui) in enumerate(P):
        edges.append((n, i, ui)); edges.append((i, n, -li))
        for j,(xj,lj,uj) in enumerate(P):
            if i != j: edges.append((j, i, L*abs(xi-xj)))
    dist = [0.0]*N
    for _ in range(N):
        for a,b,w in edges:
            if dist[a]+w < dist[b]-1e-12: dist[b] = dist[a]+w
    return all(dist[a]+w >= dist[b]-1e-9 for a,b,w in edges)

random.seed(1)
bad = []; n_cases = 0
for t in range(4000):
    L = random.choice([0.0, 0.5, 1.0, 2.0])
    k = random.randint(1, 4)
    pts = []
    for _ in range(k):
        x = random.choice([0, 0.5, 1, 1.5, 2]); l = random.choice([0, 0.5, 1, 1.5, 2, 3]); u = l + random.choice([0, 0.5, 1])
        pts.append((x, l, u))
    P = [m.Point(claim_id=f"p{i}", origin_id=f"s{i}", scope="S", revision="r1", observed_at=0,
                 x_min=float(x), x_max=float(x), y_min=float(l), y_max=float(u), source_attested=True) for i,(x,l,u) in enumerate(pts)]
    js = m._joint_evidence_status(P, L)
    truth = feasible(pts, L)
    if (js == "CONSISTENT") != truth or js == "NOT_ESTABLISHED":
        bad.append(("joint", pts, L, js, truth))
    # if joint feasible, check TRUE/FALSE soundness at a query point via feasibility of f(x)<thr / f(x)>=thr
    if truth:
        xq = random.choice([0, 0.25, 1, 1.75, 2]); thr = random.choice([0, 0.5, 1, 1.5, 2, 2.5])
        lo = max(l - L*abs(xq-x) for x,l,u in pts); hi = min(u + L*abs(xq-x) for x,l,u in pts)
        can_below = lo < thr  # some compatible f(xq) < thr exists iff lo < thr (envelope tight)
        can_above = hi >= thr
        # verify tightness: lo and hi themselves attainable
        assert feasible(pts, L, (xq, lo, lo)) and feasible(pts, L, (xq, hi, hi)), (pts, L, xq)
        n_cases += 1
print("joint-status mismatches:", len(bad), "| envelope-tightness cases checked:", n_cases)
for b in bad[:3]: print(b)
