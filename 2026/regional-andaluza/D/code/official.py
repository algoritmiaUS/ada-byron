import sys

def solve():
    n = int(sys.stdin.readline())

    dist = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    mat = [sys.stdin.readline().split() for _ in range(n)]

    speed = {
        'G': 1,
        'A': 4,
        'P': 10,
        'L': 20
    }

    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            d = dist[i][j] * 1000
            v = speed[mat[i][j]]
            cost = d / v
            edges.append((cost, i, j))

    # Kruskal
    edges.sort()

    parent = list(range(n))

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[rb] = ra
            return True
        return False

    total = 0
    for cost, u, v in edges:
        if union(u, v):
            total += cost

    print(int(total))


if __name__ == "__main__":
    solve()