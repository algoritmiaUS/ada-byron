#include <iostream>
using namespace std;

const int MAXN = 100000 + 5;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    long long a[MAXN];
    int top = 0;

    long long x;
    while (cin >> x) {
        if (x >= 0) {
            a[top++] = x;
        } else {
            long long k = -x;
            if (k >= top) top = 0;
            else top -= k;
        }
    }

    bool first = true;
    bool empty = true;

    for (int i = 0; i < top; i += 4) {
        int end = i + 4;
        if (end > top) end = top;

        // pares
        for (int j = i; j < end; j++) {
            if (a[j] % 2 == 0) {
                if (!first) cout << ' ';
                cout << a[j];
                first = false;
                empty = false;
            }
        }
        // impares
        for (int j = i; j < end; j++) {
            if (a[j] % 2 != 0) {
                if (!first) cout << ' ';
                cout << a[j];
                first = false;
                empty = false;
            }
        }
    }

    if (empty) {
        cout << "NOPROCESO";
    }

    cout << endl;

    return 0;
}
