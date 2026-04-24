#!/usr/bin/env python3
# Nombre original del script: random.py

import sys
import random
from typing import List, Tuple

random.seed(0)


def gen_all_codes(L: int, N: int) -> List[str]:
    codes = []
    buf = ['1'] * L
    def rec(i: int):
        if i == L:
            codes.append(''.join(buf))
            return
        for d in range(1, N + 1):
            buf[i] = str(d)
            rec(i + 1)
    rec(0)
    return codes

def feedback(secret: str, guess: str, N: int) -> Tuple[int, int]:
    # (verdes, amarillas)
    L = len(secret)
    verdes = 0
    cntS = [0] * (N + 1)
    cntG = [0] * (N + 1)

    for i in range(L):
        if secret[i] == guess[i]:
            verdes += 1
        cntS[int(secret[i])] += 1
        cntG[int(guess[i])] += 1

    matches = 0
    for d in range(1, N + 1):
        matches += min(cntS[d], cntG[d])

    amarillas = matches - verdes
    return verdes, amarillas

def solve_case(L: int, N: int, Q: int) -> None:
    U = gen_all_codes(L, N)
    C = U[:]  # candidatos consistentes

    # Semibruto: guess inicial aleatorio
    guess = random.choice(C)

    for _ in range(Q):
        print(f"? {guess}", flush=True)
        line = sys.stdin.readline()
        if not line:
            sys.exit(0)
        parts = line.strip().split()
        if len(parts) != 2:
            sys.exit(0)
        v, a = map(int, parts)

        if v == L:
            print(f"! {guess}", flush=True)
            return

        # Filtrado correcto por consistencia
        C = [x for x in C if feedback(x, guess, N) == (v, a)]

        if not C:
            # No debería pasar si el juez es consistente, pero por robustez:
            C = U[:]

        # Siguiente guess: aleatorio dentro de candidatos (sin minimax)
        guess = random.choice(C)

    # Si se agotan las queries, hacemos un último intento (probablemente WA)
    print(f"! {guess}", flush=True)

def main():

    while True:
        header = sys.stdin.readline()
        if not header:
            return
        header = header.strip()
        if not header:
            continue
        if header == "0":
            return
        L, N, Q = map(int, header.split())
        solve_case(L, N, Q)

if __name__ == "__main__":
    main()