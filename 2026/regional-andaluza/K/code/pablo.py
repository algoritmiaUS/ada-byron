from collections import deque

class EdmondsKarp:
    def __init__(self, n):
        self.n = n
        self.cap = [[0] * n for _ in range(n)]
        self.adj = [[] for _ in range(n)]

    def add_edge(self, u, v, c):
        self.cap[u][v] += c
        self.adj[u].append(v)
        self.adj[v].append(u)

    def bfs(self, s, t, parent):
        for i in range(self.n):
            parent[i] = -1
        parent[s] = -2

        q = deque()
        q.append((s, float('inf')))

        while q:
            u, flow = q.popleft()

            for v in self.adj[u]:
                if parent[v] == -1 and self.cap[u][v] > 0:
                    parent[v] = u
                    new_flow = min(flow, self.cap[u][v])

                    if v == t:
                        return new_flow

                    q.append((v, new_flow))

        return 0

    def max_flow(self, s, t):
        flow = 0
        parent = [-1] * self.n

        while True:
            new_flow = self.bfs(s, t, parent)
            if new_flow == 0:
                break

            flow += new_flow
            v = t
            while v != s:
                u = parent[v]
                self.cap[u][v] -= new_flow
                self.cap[v][u] += new_flow
                v = u

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

        ek = EdmondsKarp(Tnode + 1)

        for i in range(M):
            ek.add_edge(S, first_player + i, 1)

        for i in range(M):
            a, b = input().split()
            ek.add_edge(first_player + i, first_role + role_id[a], 1)
            ek.add_edge(first_player + i, first_role + role_id[b], 1)

        for j in range(K):
            ek.add_edge(first_role + j, Tnode, limit_role)

        flow = ek.max_flow(S, Tnode)
        print("YES" if flow == M else "NO")


solve()