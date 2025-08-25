#include <iostream>
using namespace std;

bool es_potencia_de_2(int n) {
    return (n & (n - 1)) == 0;
}

int contar_combates(int n) {
    int combates = 0;
    while (n > 1) {
        if (es_potencia_de_2(n)) {
            combates += n - 1;
            n = 1;
        } else {
            int c = n / 2;
            combates += c;
            n = c;
            if (c % 2 == 1 && c != 1) {
                n += 1; 
            }
        }
    }
    return combates;
}

int main() {
    int T, N;
    cin >> T;
    for (int i = 0; i < T; ++i) {
        cin >> N;
        cout << contar_combates(N) << endl;
    }
    return 0;
}
