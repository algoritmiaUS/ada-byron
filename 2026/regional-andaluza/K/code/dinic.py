from collections import deque

class Dinic:
    def __init__(self, n):
        self.n = n
        self.g = [[] for _ in range(n)]

    def add_edge(self, u, v, c):
        self.g[u].append([v, c, len(self.g[v])])
        self.g[v].append([u, 0, len(self.g[u]) - 1])

    def bfs(self, s, t):
        self.level = [-1] * self.n
        q = deque([s])
        self.level[s] = 0

        while q:
            u = q.popleft()
            for v, cap, rev in self.g[u]:
                if cap > 0 and self.level[v] == -1:
                    self.level[v] = self.level[u] + 1
                    q.append(v)

        return self.level[t] != -1

    def dfs(self, u, t, f):
        if u == t:
            return f

        while self.it[u] < len(self.g[u]):
            i = self.it[u]
            self.it[u] += 1

            v, cap, rev = self.g[u][i]
            if cap > 0 and self.level[v] == self.level[u] + 1:
                pushed = self.dfs(v, t, min(f, cap))
                if pushed > 0:
                    self.g[u][i][1] -= pushed
                    self.g[v][rev][1] += pushed
                    return pushed

        return 0

    def max_flow(self, s, t):
        flow = 0
        INF = 10**9

        while self.bfs(s, t):
            self.it = [0] * self.n
            while True:
                pushed = self.dfs(s, t, INF)
                if pushed == 0:
                    break
                flow += pushed

        return flow


def solve():
    T = int(input())

    for _ in range(T):
        N, M, K = map(int, input().split())
        roles = input().split()
        role_id = {name: i for i, name in enumerate(roles)}

        limit_role = N // K

        S = 0
        first_player = 1
        first_role = 1 + M
        Tnode = 1 + M + K

        dinic = Dinic(Tnode + 1)

        for i in range(M):
            dinic.add_edge(S, first_player + i, 1)

        for i in range(M):
            a, b = input().split()
            dinic.add_edge(first_player + i, first_role + role_id[a], 1)
            dinic.add_edge(first_player + i, first_role + role_id[b], 1)

        for j in range(K):
            dinic.add_edge(first_role + j, Tnode, limit_role)

        flow = dinic.max_flow(S, Tnode)
        print("YES" if flow == M else "NO")


solve()