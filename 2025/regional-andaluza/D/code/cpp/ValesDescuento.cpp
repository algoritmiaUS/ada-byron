#include <iostream>
#include <vector>
#include <algorithm>   // make_heap, push_heap, pop_heap

using namespace std;

struct cociente {
    size_t cliente;
    int gasto;
    int divisor;
};

inline bool operator <(const cociente& a, const cociente& b)
{
    int cociente_a = a.gasto / a.divisor,
        cociente_b = b.gasto / b.divisor;
    return cociente_a < cociente_b ||
          (cociente_a == cociente_b && a.gasto < b.gasto);
}

void repartir_vales(size_t m, size_t n)
{
    vector<size_t> vales(m, 0); // Número de vales de cada cliente
    vector<cociente> mayores_cocientes;    // Montículo de máximos
    int gasto;

    // Inicialización con los gastos de los m clientes.
    for (size_t k = 0; k < m; ++k) {
        cin >> gasto;
        mayores_cocientes.push_back(cociente{k, gasto, 1});
    }
    make_heap(mayores_cocientes.begin(), mayores_cocientes.end());

    // Seleccionar los n mayores cocientes
    for (size_t i = 1; i <= n; ++i) {
        // Asignar vale al cliente con mayor cociente
        vales[mayores_cocientes[0].cliente] += 1;
        // Añadir nuevo cociente y eliminar el mayor
        mayores_cocientes[0].divisor += 1;
        mayores_cocientes.push_back(mayores_cocientes[0]);
        pop_heap(mayores_cocientes.begin(), mayores_cocientes.end());
        mayores_cocientes.pop_back();
    }

    for (int v : vales)
        cout << v << (--m ? " " : "");
    cout << '\n';
}

int main()
{
    size_t n_cli,  n_vales;
    cin >> n_cli >> n_vales;
    while (n_cli && n_vales) {
        repartir_vales(n_cli, n_vales);
        cin >> n_cli >> n_vales;
    }
}
