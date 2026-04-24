#include <iostream>
#include <vector>
#include <cassert>

using namespace std;

struct TwoSatSolver {
    int n_vars;
    int n_vertices;
    vector<vector<int>> adj, adj_t;
    vector<bool> used;
    vector<int> order, comp;
    vector<bool> assignment;

    TwoSatSolver(int _n_vars) : n_vars(_n_vars), n_vertices(2 * n_vars), adj(n_vertices), adj_t(n_vertices), used(n_vertices), order(), comp(n_vertices, -1), assignment(n_vars) {
        order.reserve(n_vertices);
    }
    
    void dfs1(int v) {
        used[v] = true;
        for (int u : adj[v]) {
            if (!used[u])
                dfs1(u);
        }
        order.push_back(v);
    }
    
    void dfs2(int v, int cl) {
        comp[v] = cl;
        for (int u : adj_t[v]) {
            if (comp[u] == -1)
                dfs2(u, cl);
        }
    }
    
    bool solve_2SAT() {
        order.clear();
        used.assign(n_vertices, false);
        for (int i = 0; i < n_vertices; ++i) {
            if (!used[i])
                dfs1(i);
        }
        comp.assign(n_vertices, -1);
        for (int i = 0, j = 0; i < n_vertices; ++i) {
            int v = order[n_vertices - i - 1];
            if (comp[v] == -1)
                dfs2(v, j++);
        }
        assignment.assign(n_vars, false);
        for (int i = 0; i < n_vertices; i += 2) {
            if (comp[i] == comp[i + 1])
                return false;
            assignment[i / 2] = comp[i] > comp[i + 1];
        }
        return true;
    }
    
    void add_disjunction(int a, bool na, int b, bool nb) {
        a = 2 * a ^ na;
        b = 2 * b ^ nb;
        int neg_a = a ^ 1;
        int neg_b = b ^ 1;
        adj[neg_a].push_back(b);
        adj[neg_b].push_back(a);
        adj_t[b].push_back(neg_a);
        adj_t[a].push_back(neg_b);
    }
};

struct Show {
    vector<int> dusts;
    int unstable_count = 0;
    int neutral_count = 0;
};

void solve_season() {
    int M;
    cin >> M;
    
    int P, I, N;
    cin >> P >> I >> N;
    
    vector<int> dust_type(P + 1, 0);
    for (int i = 0; i < I; ++i) {
        int id; cin >> id;
        dust_type[id] = 1;
    }
    for (int i = 0; i < N; ++i) {
        int id; cin >> id;
        dust_type[id] = 2;
    }
    
    vector<Show> showA(M), showB(M);
    for (int i = 0; i < M; ++i) {
        int m; cin >> m;
        for (int j = 0; j < m; ++j) {
            int d; cin >> d;
            showA[i].dusts.push_back(d);
            if (dust_type[d] == 1) showA[i].unstable_count++;
            if (dust_type[d] == 2) showA[i].neutral_count++;
        }
        
        int k; cin >> k;
        for (int j = 0; j < k; ++j) {
            int d; cin >> d;
            showB[i].dusts.push_back(d);
            if (dust_type[d] == 1) showB[i].unstable_count++;
            if (dust_type[d] == 2) showB[i].neutral_count++;
        }
    }
    
    auto check = [&](int K) {
        if (K <= 0) return true;
        
        TwoSatSolver solver(K);
        vector<vector<pair<int, bool>>> dust_used(P + 1);
        
        for (int i = 0; i < K; ++i) {
            for (int d : showA[i].dusts) dust_used[d].push_back({i, true});
            for (int d : showB[i].dusts) dust_used[d].push_back({i, false});
            
            int uA = showA[i].unstable_count;
            int uB = showB[i].unstable_count;
            
            if (i < K - 1) {
                int nA_next = showA[i + 1].neutral_count;
                int nB_next = showB[i + 1].neutral_count;
                
                if (nA_next < uA) solver.add_disjunction(i, true, i + 1, true);
                if (nB_next < uA) solver.add_disjunction(i, true, i + 1, false);
                
                if (nA_next < uB) solver.add_disjunction(i, false, i + 1, true);
                if (nB_next < uB) solver.add_disjunction(i, false, i + 1, false);
            }
        }
        
        for (int d = 1; d <= P; ++d) {
            if (dust_used[d].size() > 1) {
                for (size_t x = 0; x < dust_used[d].size(); ++x) {
                    for (size_t y = x + 1; y < dust_used[d].size(); ++y) {
                        auto [week1, isA1] = dust_used[d][x];
                        auto [week2, isA2] = dust_used[d][y];
                        
                        solver.add_disjunction(week1, isA1, week2, isA2);
                    }
                }
            }
        }
        
        return solver.solve_2SAT();
    };
    
    int low = 1, high = M, ans = 0;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (check(mid)) {
            ans = mid;
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }
    
    cout << ans << endl;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int T;
    if (cin >> T) {
        while (T--) {
            solve_season();
        }
    }
    return 0;
}