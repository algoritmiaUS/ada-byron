#include <bits/stdc++.h>
using namespace std;

struct Edge {
    int to, cap, rev;
};

struct Dinic {
    int n;
    vector<vector<Edge>> g;
    vector<int> level, it;

    Dinic(int n) : n(n), g(n), level(n), it(n) {}

    void addEdge(int u, int v, int cap) {
        g[u].push_back({v, cap, (int)g[v].size()});
        g[v].push_back({u, 0, (int)g[u].size() - 1});
    }

    bool bfs(int s, int t) {
        fill(level.begin(), level.end(), -1);
        queue<int> q;
        level[s] = 0;
        q.push(s);

        while (!q.empty()) {
            int u = q.front();
            q.pop();

            for (const auto &e : g[u]) {
                if (e.cap > 0 && level[e.to] == -1) {
                    level[e.to] = level[u] + 1;
                    q.push(e.to);
                }
            }
        }

        return level[t] != -1;
    }

    int dfs(int u, int t, int f) {
        if (u == t) return f;

        for (int &i = it[u]; i < (int)g[u].size(); i++) {
            Edge &e = g[u][i];
            if (e.cap > 0 && level[e.to] == level[u] + 1) {
                int pushed = dfs(e.to, t, min(f, e.cap));
                if (pushed > 0) {
                    e.cap -= pushed;
                    g[e.to][e.rev].cap += pushed;
                    return pushed;
                }
            }
        }

        return 0;
    }

    int maxFlow(int s, int t) {
        int flow = 0;
        const int INF = 1e9;

        while (bfs(s, t)) {
            fill(it.begin(), it.end(), 0);
            while (true) {
                int pushed = dfs(s, t, INF);
                if (pushed == 0) break;
                flow += pushed;
            }
        }

        return flow;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;

    while (T--) {
        int N, M, K;
        cin >> N >> M >> K;

        unordered_map<string, int> roleId;
        for (int i = 0; i < K; i++) {
            string role;
            cin >> role;
            roleId[role] = i;
        }

        int limit = N / K;

        int S = 0;
        int firstPlayer = 1;
        int firstRole = 1 + M;
        int Tnode = 1 + M + K;

        Dinic dinic(Tnode + 1);

        for (int i = 0; i < M; i++) {
            dinic.addEdge(S, firstPlayer + i, 1);
        }

        for (int i = 0; i < M; i++) {
            string a, b;
            cin >> a >> b;
            dinic.addEdge(firstPlayer + i, firstRole + roleId[a], 1);
            dinic.addEdge(firstPlayer + i, firstRole + roleId[b], 1);
        }

        for (int j = 0; j < K; j++) {
            dinic.addEdge(firstRole + j, Tnode, limit);
        }

        int flow = dinic.maxFlow(S, Tnode);

        cout << (flow == M ? "YES" : "NO") << '\n';
    }

    return 0;
}