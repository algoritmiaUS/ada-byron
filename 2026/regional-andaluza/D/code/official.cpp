#include <iostream>
#include <vector>
#include <limits>
using namespace std;

long long get_speed(char c) {
    if (c == 'G') return 1;
    if (c == 'A') return 4;
    if (c == 'P') return 10;
    return 20; // 'L'
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    cin >> n;

    vector<vector<long long> > dist(n, vector<long long>(n));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> dist[i][j];
        }
    }

    vector<vector<char> > mat(n, vector<char>(n));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> mat[i][j];
        }
    }

    const long long INF = numeric_limits<long long>::max();

    vector<long long> minCost(n, INF);
    vector<bool> used(n, false);

    minCost[0] = 0;
    long long total = 0;

    for (int it = 0; it < n; it++) {
        int u = -1;

        for (int i = 0; i < n; i++) {
            if (!used[i] && (u == -1 || minCost[i] < minCost[u])) {
                u = i;
            }
        }

        used[u] = true;
        total += minCost[u];

        for (int v = 0; v < n; v++) {
            if (!used[v] && u != v) {
                long long cost = dist[u][v] * 1000LL / get_speed(mat[u][v]);
                if (cost < minCost[v]) {
                    minCost[v] = cost;
                }
            }
        }
    }

    cout << total << '\n';

    return 0;
}