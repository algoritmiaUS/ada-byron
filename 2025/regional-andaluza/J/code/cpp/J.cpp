#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int maxCristales(int n, int m, vector<vector<int>>& grid) {
    vector<vector<int>> dp(n, vector<int>(m));
    dp[0][0] = grid[0][0];

    // Primera fila
    for (int j = 1; j < m; j++) {
        dp[0][j] = dp[0][j - 1] + grid[0][j];
    }

    // Primera columna
    for (int i = 1; i < n; i++) {
        dp[i][0] = dp[i - 1][0] + grid[i][0];
    }

    // Resto de la matriz
    for (int i = 1; i < n; i++) {
        for (int j = 1; j < m; j++) {
            dp[i][j] = grid[i][j] + max({dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]});
        }
    }

    return dp[n - 1][m - 1];
}

int main() {
    int n, m;
    while (cin >> n >> m) {
        vector<vector<int>> grid(n, vector<int>(m));
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                cin >> grid[i][j];
            }
        }
        cout << maxCristales(n, m, grid) << "\n";
    }
    return 0;
}
