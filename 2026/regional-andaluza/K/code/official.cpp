 #include <bits/stdc++.h>
using namespace std;

const int INF = numeric_limits<int>::max();

int bfs(int s, int t,
        vector<int>& parent,
        vector<vector<int>>& capacity,
        vector<vector<int>>& adj){
    fill(parent.begin(), parent.end(), -1);
    parent[s] = -2;
    queue<pair<int, int>> q;
    q.push({s, INF});

    while (!q.empty()) {
        int cur = q.front().first;
        int flow = q.front().second;
        q.pop();

        for (int next : adj[cur]) {
            if (parent[next] == -1 && capacity[cur][next]) {
                parent[next] = cur;
                int new_flow = min(flow, capacity[cur][next]);
                if (next == t)
                    return new_flow;
                q.push({next, new_flow});
            }
        }
    }

    return 0;
}

int maxflow(int n, int s, int t,
    vector<vector<int>>& capacity,
    vector<vector<int>>& adj){
    int flow = 0;
    vector<int> parent(n);
    int new_flow;

    while ((new_flow = bfs(s, t, parent, capacity, adj))) {
        flow+=new_flow;
        int cur=t;
        while(cur != s){
            int prev = parent[cur];
            capacity[prev][cur] -=new_flow;
            capacity[cur][prev]+=new_flow;
            cur=prev;
        }
    }
    return flow;
}


int main(){
    int T;
    cin >> T;
    while(T--){
        int N,M,K;
        cin >> N >> M >> K;

        // Nodos:
        // 0: Source
        // 1 a M: Jugadores
        // M+1 a M+K: Clases
        // M+K+1: Sink
        int V = M + K + 2;
        int source = 0;
        int sink = V-1;

        map<string, int> class_to_id;
        for (int i = 0; i < K; ++i) {
            string class_name;
            cin >> class_name;
            class_to_id[class_name] = i + 1; // IDs del 1 al K
        }

        vector<vector<int>> capacity(V, vector<int>(V, 0));
        vector<vector<int>> adj(V);

        auto add_edge = [&](int u, int v, int cap){
            capacity[u][v] += cap;
            adj[u].push_back(v);
            adj[v].push_back(u); // para residual
        };

        // Source -> Jugadores
        for (int i = 1; i <= M; ++i) {
            add_edge(source, i, 1);
        }
        
        // Jugadores -> Clases
        for (int i = 1; i <= M; ++i) {
            string c1, c2;
            cin >> c1>> c2;

            int id1 = class_to_id[c1];
            int id2 = class_to_id[c2];

            add_edge(i, M+id1, 1);
            add_edge(i, M+id2, 1);
        }

        // Conectar Clases -> Sink
        int class_limit = N / K;
        for (int i = 1; i <= K; ++i) {
            int vol_node = M+i;
            add_edge(vol_node, sink, class_limit);
        }

        int flow = maxflow(V,source,sink,capacity, adj);

        if (flow ==M){
            cout << "YES" << endl;
        } else{
            cout << "NO" << endl;
        }

    }

    return 0;
}