import random
from collections import Counter

random.seed(0)


def score(guess, secret):
    green = 0
    cg = Counter()
    cs = Counter()

    for x, y in zip(guess, secret):
        if x == y:
            green += 1
        else:
            cg[x] += 1
            cs[y] += 1

    yellow = 0
    for k in cg:
        yellow += min(cg[k], cs[k])

    return green, yellow


def generate_sequences(counts, L):
    res = []
    cur = []
    freq = counts[:]

    def backtrack():
        if len(cur) == L:
            res.append(tuple(cur))
            return
        for x in range(1, len(freq)):
            if freq[x] > 0:
                freq[x] -= 1
                cur.append(x)
                backtrack()
                cur.pop()
                freq[x] += 1

    backtrack()
    return res


def ask(seq):
    s = "".join(map(str, seq))
    print("?", s, flush=True)
    v, a = map(int, input().split())
    return v, a


def solve_case(L, N, Q):
    counts = [0] * (N + 1)

    # Fase 1: contar cuántas veces aparece cada número
    for d in range(1, N + 1):
        guess = [d] * L
        v, a = ask(guess)

        if v == L:
            print("!", "".join(map(str, guess)), flush=True)
            return

        counts[d] = v + a

    # Todos los candidatos compatibles con esas cantidades
    candidates = generate_sequences(counts, L)

    # Fase 2: elegir consultas aleatorias entre los candidatos posibles
    while True:
        if len(candidates) == 1:
            ans = candidates[0]
            print("!", "".join(map(str, ans)), flush=True)
            return

        guess = random.choice(candidates)
        v, a = ask(guess)

        if v == L:
            print("!", "".join(map(str, guess)), flush=True)
            return

        candidates = [s for s in candidates if score(guess, s) == (v, a)]


def solve():
    while True:
        line = input().strip()
        if line == "0":
            break

        L, N, Q = map(int, line.split())
        solve_case(L, N, Q)


solve()