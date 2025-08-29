#include <iostream>
#include <vector>
#include <numeric> // std::gcd
using namespace std;

// Leer estado inicial: 3 líneas con 3 coordenadas (x, y, z)
vector<vector<int>> leer_estado() {
    vector<vector<int>> estado(3, vector<int>(3));
    for (int i = 0; i < 3; ++i)
        for (int j = 0; j < 3; ++j)
            cin >> estado[i][j];
    return estado;
}

int mcm(int a, int b) {
    return a * b / gcd(a, b);
}

int obtener_ciclo_eje(vector<int> posiciones) {
    vector<int> posiciones_iniciales = posiciones;
    vector<int> velocidades(3, 0);
    int pasos = 0;

    while (true) {
        // Actualizar velocidades
        for (int i = 0; i < 3; ++i) {
            for (int j = i + 1; j < 3; ++j) {
                if (posiciones[i] < posiciones[j]) {
                    velocidades[i]++;
                    velocidades[j]--;
                } else if (posiciones[i] > posiciones[j]) {
                    velocidades[i]--;
                    velocidades[j]++;
                }
            }
        }

        // Actualizar posiciones
        for (int i = 0; i < 3; ++i) {
            posiciones[i] += velocidades[i];
        }

        pasos++;

        if (posiciones == posiciones_iniciales && velocidades == vector<int>{0, 0, 0}) {
            return pasos;
        }
    }
}

int calcular_dias_para_repeticion(const vector<vector<int>>& flotas) {
    vector<int> ciclos;
    for (int eje = 0; eje < 3; ++eje) {
        vector<int> posiciones;
        for (int i = 0; i < 3; ++i) {
            posiciones.push_back(flotas[i][eje]);
        }
        ciclos.push_back(obtener_ciclo_eje(posiciones));
    }

    return mcm(ciclos[0], mcm(ciclos[1], ciclos[2]));
}

int main() {
    vector<vector<int>> flotas = leer_estado();
    cout << calcular_dias_para_repeticion(flotas) << endl;
    return 0;
}
