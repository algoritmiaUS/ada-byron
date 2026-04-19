#include <iostream>
using namespace std;

// Fase 1: Convierte la matriz 12x3 de decimales a matriz binaria 12x12
// Cada elemento (0-9) se expande en 4 bits
void convertirBinario(int A[12][3], int MB[12][12]) {
    for (int i = 0; i < 12; i++) {
        for (int j = 0; j < 3; j++) {
            int val = A[i][j];
            // Los 4 bits del valor, del más significativo al menos
            for (int b = 3; b >= 0; b--) {
                MB[i][j * 4 + (3 - b)] = (val >> b) & 1;
            }
        }
    }
}

// Fase 2: Rotación de la periferia de una submatriz 3x3
// La periferia en orden horario empezando por (0,0):
// (0,0),(0,1),(0,2),(1,2),(2,2),(2,1),(2,0),(1,0)
void rotarSubmatriz(int MB[12][12], int filaBase, int colBase) {
    // Extraer los 8 elementos de la periferia en orden horario
    int ri[] = {0, 0, 0, 1, 2, 2, 2, 1};
    int ci[] = {0, 1, 2, 2, 2, 1, 0, 0};

    int periferia[8];
    for (int k = 0; k < 8; k++) {
        periferia[k] = MB[filaBase + ri[k]][colBase + ci[k]];
    }

    int central = MB[filaBase + 1][colBase + 1];

    // Contar unos en la periferia
    int N = 0;
    for (int k = 0; k < 8; k++) N += periferia[k];

    if (N == 0) return; // Sin rotación

    // Rotar: derecha si central==1, izquierda si central==0
    int rotado[8];
    for (int k = 0; k < 8; k++) {
        if (central == 1) {
            // Rotación N posiciones a la derecha
            rotado[(k + N) % 8] = periferia[k];
        } else {
            // Rotación N posiciones a la izquierda
            rotado[((k - N) % 8 + 8) % 8] = periferia[k];
        }
    }

    // Escribir la periferia rotada de vuelta
    for (int k = 0; k < 8; k++) {
        MB[filaBase + ri[k]][colBase + ci[k]] = rotado[k];
    }
}

// Fase 2 completa: procesar las 16 submatrices 3x3
void transformarSubmatrices(int MB[12][12]) {
    // 4 bloques en filas x 4 bloques en columnas = 16 submatrices
    for (int bi = 0; bi < 4; bi++) {
        for (int bj = 0; bj < 4; bj++) {
            rotarSubmatriz(MB, bi * 3, bj * 3);
        }
    }
}

// Fase 3: Convertir cada columna de MB' (12 bits) a decimal
void convertirDecimal(int MB[12][12], int resultado[12]) {
    for (int j = 0; j < 12; j++) {
        int val = 0;
        for (int i = 0; i < 12; i++) {
            val = val * 2 + MB[i][j];
        }
        resultado[j] = val;
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    // Leer matriz de entrada 12x3
    int A[12][3];
    for (int i = 0; i < 12; i++)
        for (int j = 0; j < 3; j++)
            cin >> A[i][j];

    // Fase 1
    int MB[12][12] = {};
    convertirBinario(A, MB);

    // Fase 2
    transformarSubmatrices(MB);

    // Fase 3
    int resultado[12];
    convertirDecimal(MB, resultado);

    // Salida
    for (int i = 0; i < 11; i++) {
        cout << resultado[i] << " ";
    }
    cout << resultado[11] << endl;

    return 0;
}
