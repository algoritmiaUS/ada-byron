#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int beauty(int n, const vector<int>& beauty1, const vector<int>& beauty2) {
    if (n == 1) {
        return max(beauty1[0], beauty2[0]);
    }

    vector<int> dp1(1, beauty1[0]);
    vector<int> dp2(1, beauty2[0]);

    if (n > 1) {
        dp1.push_back(dp2[0] + beauty1[1]);
        dp2.push_back(dp1[0] + beauty2[1]);
    }

    for (int i = 2; i < n; ++i) {
        dp1.push_back(beauty1[i] + max(dp2[i - 1], dp2[i - 2]));
        dp2.push_back(beauty2[i] + max(dp1[i - 1], dp1[i - 2]));
    }

    return max(dp1[n - 1], dp2[n - 1]);
}

int main() {
    int t;
    cin >> t;  // Read number of test cases
    while (t--) {
        int n;
        cin >> n;  // Read the value of n
        vector<int> list1(n), list2(n);

        // Read first list of beauty values
        for (int i = 0; i < n; ++i) {
            cin >> list1[i];
        }

        // Read second list of beauty values
        for (int i = 0; i < n; ++i) {
            cin >> list2[i];
        }

        // Call beauty function and print the result
        cout << beauty(n, list1, list2) << endl;
    }

    return 0;
}
