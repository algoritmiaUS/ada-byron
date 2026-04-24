#include <iostream>
#include <string>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int T;
    cin >> T;

    while (T--) {
        int C;
        string s;
        cin >> C >> s;

        int ocupacion = 0;
        bool valido = true;

        for (int i = 0; i < (int)s.size(); i++) {
            if (s[i] == 'E') {
                ocupacion++;
                if (ocupacion > C) {
                    valido = false;
                    break;
                }
            } else { // 'S'
                ocupacion--;
                if (ocupacion < 0) {
                    valido = false;
                    break;
                }
            }
        }

        if (ocupacion != 0) {
            valido = false;
        }

        if (valido) {
            cout << "VALIDO\n";
        } else {
            cout << "INVALIDO\n";
        }
    }

    return 0;
}