import math

c_e, g = 2.0, 3.0

def R_exec(L):
    return c_e + g * L

print('D1. Human per-decision escalation under a human-time deadline')
print('   decisions needed = d - j ; decisions available = floor(T_h / tau_h)')
for T_h, tau_h in [(480, 5), (480, 15), (480, 30)]:
    avail = T_h // tau_h
    print(f'   deadline {T_h} min, {tau_h} min per decision -> {avail} decisions; chains up to L = {avail} (j=0, eps=0) can be certified; longer chains are infeasible whatever the money budget')

print()
print('D2. Human reads the whole map: cost h0 + h1*L (reading time grows with chain length)')
print('   overhead share of execution cost, h0=2, c_e=2, g=3')
for h1 in (0.1, 0.5, 1.0):
    row = []
    for L in (4, 16, 64, 256):
        over = 2 + h1 * L
        row.append(f'L={L}: {over / R_exec(L):.1%}')
    print(f'   h1={h1}: ' + '   '.join(row) + f'   limit h1/g = {h1 / g:.1%}')

print()
print('D3. Shared verification across n agents with a common binding (results reused through a store)')
d, c = 32, 1.0
print(f'   d={d} bits needed per agent, c={c} per bit, R_exec({d})={R_exec(d)}')
for n in (1, 2, 4, 8, 16, 32, 64):
    per = c * d / n
    print(f'   n={n:<3} per-agent information cost = {per:6.2f}   share of R_exec = {per / R_exec(d):6.1%}')
print('   with distinct bindings per agent (no common facts) the per-agent cost stays', c * d)

print()
print('D4. When is escalation worth it? expected-cost rule per layer')
print('   blind: g + W/2   (violation costs W, probability 1/2)   escalate: g + h')
for h in (1, 3, 6, 12):
    for W in (4, 10, 100):
        print(f'   h={h:<3} W={W:<4} -> escalate iff h <= W/2: {h <= W / 2}')
