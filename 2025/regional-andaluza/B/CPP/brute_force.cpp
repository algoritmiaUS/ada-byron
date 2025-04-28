#include <iostream>
#include <vector>
#include <string>
using namespace std;

bool startsWith(const string& code, const string& prefix) {
    if (prefix.size() > code.size()) return false;
    for (size_t i = 0; i < prefix.size(); ++i) {
        if (code[i] != prefix[i]) return false;
    }
    return true;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int caseNum = 1;
    string line;

    while (getline(cin, line)) {
        if (line.empty()) break;

        size_t space_pos = line.find(' ');
        int N = stoi(line.substr(0, space_pos));
        int Q = stoi(line.substr(space_pos + 1));

        vector<string> codes(N);
        for (int i = 0; i < N; ++i) {
            getline(cin, codes[i]);
        }

        cout << "Case " << caseNum++ << ":\n";

        for (int i = 0; i < Q; ++i) {
            string prefix;
            getline(cin, prefix);
            int count = 0;
            for (const string& code : codes) {
                if (startsWith(code, prefix)) count++;
            }
            cout << count << "\n";
        }
    }

    return 0;
}
