def solve():
    s = input().strip()
    motifs = input().split()
    k = int(input())

    motifs = list(dict.fromkeys(motifs))

    n = len(s)
    m = len(motifs)

    starts = [[False] * m for _ in range(n)]

    for i in range(n):
        for j, w in enumerate(motifs):
            lw = len(w)
            if i + lw <= n and s[i:i+lw] == w:
                starts[i][j] = True

    ans = float('inf')

    for l in range(n):
        present = [False] * m
        count = 0

        for r in range(l, n):
            for j, w in enumerate(motifs):
                lw = len(w)
                start_pos = r - lw + 1
                if start_pos >= l and start_pos >= 0 and starts[start_pos][j]:
                    if not present[j]:
                        present[j] = True
                        count += 1

            if count >= k:
                ans = min(ans, r - l + 1)

    print(0 if ans == float('inf') else ans)

solve()