import sys

def solve():
    input = sys.stdin.readline  # entrada rápida
    case_number = 1

    while True:
        line = input()
        if not line:
            break
        line = line.strip()
        if not line:
            continue

        try:
            N, Q = map(int, line.split())
        except ValueError:
            continue

        codigos = [input().strip() for _ in range(N)]
        print(f"Case {case_number}:")

        for _ in range(Q):
            prefijo = input().strip()
            contador = sum(1 for codigo in codigos if codigo.startswith(prefijo))
            print(contador)

        case_number += 1

if __name__ == "__main__":
    solve()
