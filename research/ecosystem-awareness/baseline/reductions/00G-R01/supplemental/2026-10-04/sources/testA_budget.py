import itertools, math
from scipy.optimize import linprog

g, c_e = 3.0, 2.0

def vectors(L):
    # per-layer actions: m (safe, gain 1), b (blind, gain 2, violates w.p. 1/2), q (query then match, gain 2, no violation)
    return itertools.product('mbq', repeat=L)

def stats(vec, L, eps_int, c):
    n_m = vec.count('m'); n_b = vec.count('b'); n_q = vec.count('q')
    cost = c_e + g * L + c * n_q
    eta = 1.0 if n_m <= eps_int else 0.0        # technical delivery
    rho = 1.0 - 0.5 ** n_b                       # P(any violation)
    return cost, eta, rho

def feasible(L, eps_int, c, R, e, r):
    vs = [stats(v, L, eps_int, c) for v in vectors(L)]
    vs = [s for s in vs if s[0] <= R + 1e-9]
    if not vs:
        return False
    # exists a mixture w with sum w*eta >= e and sum w*rho <= r
    n = len(vs)
    A = [[-s[1] for s in vs], [s[2] for s in vs]]
    b = [-e, r]
    res = linprog([0]*n, A_ub=A, b_ub=b, A_eq=[[1]*n], b_eq=[1], bounds=[(0, 1)]*n, method='highs')
    return res.status == 0

def min_budget(L, eps_int, c, e, r):
    R = c_e + g * L
    top = R + c * L + 1
    while R <= top:
        if feasible(L, eps_int, c, R, e, r):
            return R
        R += 0.25
    return None

def formula(L, eps_int, c, e, r):
    d = L - eps_int
    j = 0 if r <= 0 else math.floor(math.log2(1.0 / (1.0 - r)) + 1e-12) if r < 1 else d
    # largest j with 2^-j >= 1 - r and also e - r <= 2^-j
    j = 0
    while j + 1 <= d and (0.5 ** (j + 1)) >= (1 - r) - 1e-12:
        j += 1
    return c_e + g * L + c * max(d - j, 0), d, j

print('c_e=2 g=3, thresholds e,r vary; c = cost per bit')
rows = []
for (e, r) in [(7/8, 1/8), (1.0, 0.5), (1.0, 0.75)]:
    for c in [1.0, 2.0]:
        for L in [2, 3, 4, 5, 6]:
            for eps in [0, 1]:
                if eps >= L:
                    continue
                lp = min_budget(L, eps, c, e, r)
                fm, d, j = formula(L, eps, c, e, r)
                rows.append((e, r, c, L, eps, lp, fm))
bad = [x for x in rows if x[5] is None or abs(x[5] - x[6]) > 0.25]
print('cases', len(rows), 'mismatches', len(bad))
for x in bad[:10]:
    print(x)
print('sample rows (e,r,c,L,eps,LP,formula):')
for x in rows[:6]:
    print(x)
