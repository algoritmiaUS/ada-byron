#include <bits/stdc++.h>
using namespace std;

static vector<int> buildPi(const string& p) {
    int m = (int)p.size();
    vector<int> pi(m, 0);
    for (int i = 1; i < m; i++) {
        int j = pi[i - 1];
        while (j > 0 && p[i] != p[j]) j = pi[j - 1];
        if (p[i] == p[j]) j++;
        pi[i] = j;
    }
    return pi;
}

static vector<int> kmpOccurrences(const string& s, const string& p) {
    vector<int> occ;
    vector<int> pi = buildPi(p);
    int n = (int)s.size(), m = (int)p.size();

    int j = 0;
    for (int i = 0; i < n; i++) {
        while (j > 0 && s[i] != p[j]) j = pi[j - 1];
        if (s[i] == p[j]) j++;
        if (j == m) {
            occ.push_back(i - m + 1);
            j = pi[j - 1];
        }
    }
    return occ;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string dna;
    if (!(cin >> dna)) return 0;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    string line;
    getline(cin, line);

    int k;
    cin >> k;

    // Parsear motivos
    stringstream ss(line);
    vector<string> rawPatterns;
    string pat;
    while (ss >> pat) rawPatterns.push_back(pat);

    // Eliminar duplicados conservando orden
    vector<string> patterns;
    unordered_set<string> seen;
    for (const string& x : rawPatterns) {
        if (!seen.count(x)) {
            seen.insert(x);
            patterns.push_back(x);
        }
    }

    int n = (int)dna.size();
    int m = (int)patterns.size();

    if (k > m) {
        cout << 0 << '\n';
        return 0;
    }

    // events[r] = lista de (idMotivo, inicio) de ocurrencias que terminan en r
    vector<vector<pair<int,int>>> events(n);

    for (int id = 0; id < m; id++) {
        const string& p = patterns[id];
        vector<int> occ = kmpOccurrences(dna, p);
        int len = (int)p.size();

        for (int start : occ) {
            int end = start + len - 1;
            events[end].push_back({id, start});
        }
    }

    vector<int> latestStart(m, -1);
    int answer = INT_MAX;

    for (int r = 0; r < n; r++) {
        for (auto &ev : events[r]) {
            int id = ev.first;
            int start = ev.second;
            latestStart[id] = max(latestStart[id], start);
        }

        vector<int> active;
        active.reserve(m);
        for (int x : latestStart) {
            if (x != -1) active.push_back(x);
        }

        if ((int)active.size() >= k) {
            sort(active.begin(), active.end(), greater<int>());
            int L = active[k - 1];
            answer = min(answer, r - L + 1);
        }
    }

    cout << (answer == INT_MAX ? 0 : answer) << '\n';
    return 0;
}