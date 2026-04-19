def solve():
    n = int(input())

    dist = [list(map(int, input().split())) for _ in range(n)]
    mat = [input().split() for _ in range(n)]

    factor = {
        'G': 1000,
        'A': 250,
        'P': 100,
        'L': 50
    }

    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            cost = dist[i][j] * factor[mat[i][j]]
            edges.append((cost, i, j))

    edges.sort()

    parent = list(range(n))
    size = [1] * n

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra = find(a)
        rb = find(b)
        if ra == rb:
            return False
        if size[ra] < size[rb]:
            ra, rb = rb, ra
        parent[rb] = ra
        size[ra] += size[rb]
        return True

    total = 0
    used = 0

    for cost, u, v in edges:
        if union(u, v):
            total += cost
            used += 1
            if used == n - 1:
                break

    print(total)


solve()