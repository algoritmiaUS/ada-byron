#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>

using namespace std;

// Función de DP para calcular el flujo
vector<vector<double>> resolverDP(int H, double liquido, const vector<vector<double>>& caps) {
    // Inicializar DP con ceros, misma estructura que capacidades
    vector<vector<double>> dp(H);
    for (int i = 0; i < H; ++i) {
        dp[i].resize((i + 1) * (i + 1), 0.0);
    }

    // Vertido inicial
    if (H > 0) dp[0][0] = liquido;

    // Propagar líquido nivel a nivel
    for (int i = 0; i < H - 1; ++i) {
        int ladoActual = i + 1;
        int ladoSiguiente = i + 2;

        for (int r = 0; r < ladoActual; ++r) {
            for (int c = 0; c < ladoActual; ++c) {
                int idxActual = r * ladoActual + c;
                double sobrante = dp[i][idxActual] - caps[i][idxActual];

                if (sobrante > 0) {
                    double cuarto = sobrante / 4.0;
                    
                    // Índices de las 4 copas inferiores en el array aplanado
                    dp[i + 1][r * ladoSiguiente + c] += cuarto;
                    dp[i + 1][(r + 1) * ladoSiguiente + c] += cuarto;
                    dp[i + 1][r * ladoSiguiente + (c + 1)] += cuarto;
                    dp[i + 1][(r + 1) * ladoSiguiente + (c + 1)] += cuarto;
                }
            }
        }
    }
    return dp;
}

int main() {
    // Optimización de E/S estándar
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    double liquidoInicial;
    int H;

    if (!(cin >> liquidoInicial >> H)) return 0;

    // 1. Leer Capacidades (Array dentado aplanado por nivel)
    vector<vector<double>> capacidades(H);
    for (int i = 0; i < H; ++i) {
        int numCopasNivel = (i + 1) * (i + 1);
        capacidades[i].resize(numCopasNivel);
        for (int j = 0; j < numCopasNivel; ++j) {
            cin >> capacidades[i][j];
        }
    }

    // 2. Procesar con DP
    vector<vector<double>> flujoTotal = resolverDP(H, liquidoInicial, capacidades);

    // 3. Responder Consultas
    int Q;
    if (cin >> Q) {
        for (int q = 0; q < Q; ++q) {
            int nivel, fila, col;
            cin >> nivel >> fila >> col;

            int idx = fila * (nivel + 1) + col;
            // El volumen real es el mínimo entre lo que llegó y la capacidad
            double contenido = min(capacidades[nivel][idx], flujoTotal[nivel][idx]);
            
            // Usar printf para formateo rápido de precisión
            printf("%.6f\n", contenido);
        }
    }

    return 0;
}