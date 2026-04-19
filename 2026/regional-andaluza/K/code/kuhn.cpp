#include <iostream>
#include <vector>
#include <string>
#include <map>

using namespace std;

// Algoritmo de Kuhn (DFS Bipartite Matching)
bool dfs(int u, vector<vector<int>>& adj, vector<int>& match, vector<bool>& vis) {
    for (int v : adj[u]) {
        if (vis[v]) continue;
        vis[v] = true;
        if (match[v] < 0 || dfs(match[v], adj, match, vis)) {
            match[v] = u;
            return true;
        }
    }
    return false;
}

void solve() {
    int n, m, k;
    cin >> n >> m >> k;
    
    map<string, int> class_id;
    for (int i = 0; i < k; ++i) {
        string c;
        cin >> c;
        class_id[c] = i;
    }
    
    int limit = n / k;
    // Grafo bipartito: M jugadores hacia K * limit slots disponibles
    vector<vector<int>> adj(m);
    for (int i = 0; i < m; ++i) {
        string c1, c2;
        cin >> c1 >> c2;
        int id1 = class_id[c1], id2 = class_id[c2];
        
        // Conectar el jugador a todos los "slots" disponibles de sus dos clases
        for(int j = 0; j < limit; j++) {
            adj[i].push_back(id1 * limit + j);
            adj[i].push_back(id2 * limit + j);
        }
    }
    
    vector<int> match(k * limit, -1);
    int assigned = 0;
    for (int i = 0; i < m; ++i) {
        vector<bool> vis(k * limit, false);
        if (dfs(i, adj, match, vis)) assigned++;
    }
    
    if (assigned == m) cout << "YES\n";
    else cout << "NO\n";
}

int main() {
    int t;
    if (cin >> t) {
        while (t--) {
            solve();
        }
    }
    return 0;
}