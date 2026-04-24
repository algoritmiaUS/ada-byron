#include <iostream>
#include <vector>
using namespace std;

bool can_partition(const vector<long long>& h, int k, long long limit) {
    int used = 1;
    long long current = 0;

    for (int i = 0; i < (int)h.size(); i++) {
        if (h[i] > limit) return false;

        if (current + h[i] <= limit) {
            current += h[i];
        } else {
            used++;
            current = h[i];
            if (used > k) return false;
        }
    }

    return true;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, k;
    while (cin >> n >> k) {
        vector<long long> h(n);
        long long left = 0, right = 0;

        for (int i = 0; i < n; i++) {
            cin >> h[i];
            if (h[i] > left) left = h[i];
            right += h[i];
        }

        while (left < right) {
            long long mid = left + (right - left) / 2;
            if (can_partition(h, k, mid)) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }

        cout << left << '\n';
    }

    return 0;
}