import random, statistics

def run(n, L, delta, tau, homogeneous, kill, rng):
    omega = [rng.randint(0, 1) for _ in range(L)]
    guesses = []
    base = [0] * L
    for i in range(n):
        guesses.append(base if homogeneous else [rng.randint(0, 1) for _ in range(L)])
    # events: (time, agent, layer, violating?)
    events = []
    for i in range(n):
        s = i * delta
        for l in range(L):
            viol = guesses[i][l] != omega[l]
            events.append((s + l, i, l, viol))
            if viol:
                break  # agent halts after its own violation receipt
    events.sort()
    first_violation = None
    for (t, i, l, v) in events:
        if v:
            first_violation = t
            break
    if kill and first_violation is not None:
        t_kill = first_violation + 1 + tau
    else:
        t_kill = float('inf')
    D = 0
    completed = 0
    for i in range(n):
        s = i * delta
        ok = True
        for l in range(L):
            t = s + l
            if t >= t_kill:
                ok = False
                break
            if guesses[i][l] != omega[l]:
                D += 1
                ok = False
                break
        if ok:
            completed += 1
    return D, completed, (first_violation is not None)

def expect(n, L, delta, tau, homogeneous, kill, trials=4000, seed=7):
    rng = random.Random(seed)
    Ds, Cs, Vs = [], [], []
    for _ in range(trials):
        D, C, V = run(n, L, delta, tau, homogeneous, kill, rng)
        Ds.append(D); Cs.append(C); Vs.append(1 if V else 0)
    return statistics.mean(Ds), statistics.mean(Cs), statistics.mean(Vs)

n, L = 50, 5
print(f'n={n} agents, L={L} layers, world drawn once per trial, common to all agents')
print('D = expected violating effects; any = P(at least one violation); done = expected agents finishing a legitimate route')
print()
print('No kill switch')
for hom in (True, False):
    D, C, V = expect(n, L, 0, 0, hom, False)
    print(f'  {"homogeneous guess" if hom else "independent guesses":<20} lockstep: D={D:6.2f}  any={V:.3f}  done={C:5.2f}')
print()
print('Kill switch (global halt tau steps after the first violation receipt)')
print('  guess        delta  tau   D       any    done')
for hom in (True, False):
    for delta in (0, 1, 2, 5):
        for tau in (0, 2, 5):
            D, C, V = expect(n, L, delta, tau, hom, True)
            print(f'  {"homog." if hom else "indep.":<12} {delta:<5} {tau:<5} {D:7.2f} {V:6.3f} {C:6.2f}')
print()
# sacrificial canary protocol: crowd waits; canary attempts, each violating attempt reveals one bit; crowd starts once a canary completes
def canary(L, trials=20000, seed=3):
    rng = random.Random(seed)
    viols = []
    for _ in range(trials):
        omega = [rng.randint(0, 1) for _ in range(L)]
        known = [None] * L
        v = 0
        while True:
            ok = True
            for l in range(L):
                g = known[l] if known[l] is not None else rng.randint(0, 1)
                if g != omega[l]:
                    known[l] = omega[l]
                    v += 1
                    ok = False
                    break
                known[l] = g
            if ok:
                break
        viols.append(v)
    return statistics.mean(viols)

for LL in (3, 5, 8, 12):
    print(f'sacrificial canary, L={LL}: expected violating canaries before a legitimate route exists = {canary(LL):.2f}  (L/2 = {LL/2})')
