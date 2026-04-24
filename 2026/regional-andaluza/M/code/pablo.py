def solve():
    L, H = input().split()
    L = float(L)
    H = int(H)

    caps = []
    for n in range(H):
        vals = list(map(float, input().split()))
        size = n + 1
        level = []
        idx = 0
        for i in range(size):
            row = vals[idx:idx + size]
            idx += size
            level.append(row)
        caps.append(level)

    # incoming[n][f][c] = líquido total que llega a esa copa
    incoming = []
    filled = []

    for n in range(H):
        size = n + 1
        incoming.append([[0.0] * size for _ in range(size)])
        filled.append([[0.0] * size for _ in range(size)])

    incoming[0][0][0] = L

    for n in range(H):
        size = n + 1
        for f in range(size):
            for c in range(size):
                x = incoming[n][f][c]
                cap = caps[n][f][c]

                kept = min(x, cap)
                filled[n][f][c] = kept

                overflow = x - cap
                if overflow > 0 and n + 1 < H:
                    part = overflow / 4.0
                    incoming[n + 1][f][c] += part
                    incoming[n + 1][f + 1][c] += part
                    incoming[n + 1][f][c + 1] += part
                    incoming[n + 1][f + 1][c + 1] += part

    Q = int(input())
    for _ in range(Q):
        n, f, c = map(int, input().split())
        print(f"{filled[n][f][c]:.6f}")


solve()