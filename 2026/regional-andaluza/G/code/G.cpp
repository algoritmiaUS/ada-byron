#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

/**
 * Función de verificación: O(n)
 * @param cargaMax: Máxima carga que se puede asignar a una brigada.
 * @param k: Número de brigadas disponibles.
 * @param horas: Vector de horas de trabajo por tramo.
 * @return Si se pueden o no repartir todos los tramos entre 
 *         @code k brigadas a lo sumo sin superar @code cargaMax,
 */
bool esSolucion(ll cargaMax, int k, const vector<int>& horas)
{
    ll carga = 0;

    // Asignar carga de trabajo consecutivamente a las
    // brigadas sin superar cargaMax por brigada.
    for (int hi : horas)
        if ((carga += hi) > cargaMax) {
            --k;
            carga = hi;
        }

    return k > 0; // ¿Hay suficientes brigadas disponibles?
}

// Mínima carga máxima de n tramos entre k brigadas como mucho:
// O(n log(carga_total))
ll minCargaMax(int n, int k)
{
    vector<int> horas(n);
    ll inf = 0, sup = 0,
       mCM = 0;

    for (int i = 0; i < n; ++i) {
        cin >> horas[i];
        // Intervalo de la solución [inf, sup]
        inf = max(inf, (ll)horas[i]); // Máximo de horas de todos los tramos
        sup += horas[i];              // Total de horas de todos los tramos
    }
    // Búsqueda de la solución óptima
    while (inf <= sup) { // O(n log(suma horas[i]))
        ll cargaMax = inf + (sup - inf) / 2;
        if (esSolucion(cargaMax, k, horas)) {
            mCM = cargaMax; // cargaMax es solución, intentar algo menor
            sup = cargaMax - 1;
        }
        else
            inf = cargaMax + 1; // No es solución, se necesita mayor carga de trabajo
    }
    return mCM;
}

int main()
{
    int n, k;
    while (cin >> n >> k)
        cout << minCargaMax(n, k) << '\n';
    return 0;
}
