#include <iostream>
using namespace std;

const int MAXN = 300000;

int main() {
    long long entrada[MAXN];
    int n = 0;

    while (cin >> entrada[n]) {
        n++;
    }

    int i = 0;
    while (i < n) {
        if (entrada[i] >= 0) {
            i++;
        } else {
            long long k = -entrada[i];
            if (k > i) k = i;
            int borrar_previos = k;

            int inicio_borrado = i - borrar_previos;
            int total_borrados = borrar_previos + 1; // los previos + el negativo

            // Desplazar todo lo que hay detrás del negativo
            for (int j = i + 1; j < n; j++) {
                entrada[j - total_borrados] = entrada[j];
            }

            n -= total_borrados;
            i = inicio_borrado;
        }
    }

    bool first = true;
    bool vacio = true;

    for (int p = 0; p < n; p += 4) {
        int fin = p + 4;
        if (fin > n) fin = n;

        for (int j = p; j < fin; j++) {
            if (entrada[j] % 2 == 0) {
                if (!first) cout << ' ';
                cout << entrada[j];
                first = false;
                vacio = false;
            }
        }

        for (int j = p; j < fin; j++) {
            if (entrada[j] % 2 != 0) {
                if (!first) cout << ' ';
                cout << entrada[j];
                first = false;
                vacio = false;
            }
        }
    }

    if (vacio) {
        cout << "NOPROCESO";
    }

    cout << endl;

    return 0;
}
