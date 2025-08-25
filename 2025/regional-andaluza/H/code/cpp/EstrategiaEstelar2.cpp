#include <iostream>
#include <vector>
using namespace std;

using Flota = vector<vector<int>>;

// Leer el estado inicial (3 líneas con 3 enteros cada una)
Flota leer_estado() {
    Flota estado(3, vector<int>(3));
    for (int i = 0; i < 3; ++i)
        for (int j = 0; j < 3; ++j)
            cin >> estado[i][j];
    return estado;
}

void actualizar_velocidades(Flota& pos, Flota& vel) {
    for (int i = 0; i < 3; ++i) {
        for (int j = i + 1; j < 3; ++j) {
            for (int eje = 0; eje < 3; ++eje) {
                if (pos[i][eje] < pos[j][eje]) {
                    vel[i][eje] += 1;
                    vel[j][eje] -= 1;
                } else if (pos[i][eje] > pos[j][eje]) {
                    vel[i][eje] -= 1;
                    vel[j][eje] += 1;
                }
            }
        }
    }
}

void actualizar_posiciones(Flota& pos, const Flota& vel) {
    for (int i = 0; i < 3; ++i)
        for (int eje = 0; eje < 3; ++eje)
            pos[i][eje] += vel[i][eje];
}

bool estado_inicial(const Flota& pos, const Flota& vel, const Flota& pos_ini) {
    Flota zero(3, vector<int>(3, 0));
    return pos == pos_ini && vel == zero;
}

int calcular_ciclo_completo(const Flota& estado_ini) {
    Flota pos = estado_ini;
    Flota vel(3, vector<int>(3, 0));
    int pasos = 0;

    while (true) {
        actualizar_velocidades(pos, vel);
        actualizar_posiciones(pos, vel);
        pasos++;
        if (estado_inicial(pos, vel, estado_ini))
            return pasos;
    }
}

int main() {
    Flota flotas = leer_estado();
    cout << calcular_ciclo_completo(flotas) << endl;
    return 0;
}
