#include <iostream>
#include <string>
#include <vector>
using namespace std;

const int ALPHABET_SIZE = 10; // Solo dígitos 0-9

struct TrieNode {
    TrieNode* children[ALPHABET_SIZE];
    int count;

    TrieNode() {
        count = 0;
        for (int i = 0; i < ALPHABET_SIZE; i++)
            children[i] = nullptr;
    }
};

class Trie {
public:
    Trie() {
        root = new TrieNode();
    }

    ~Trie() {
        freeTrie(root);
    }

    void insert(const string& word) {
        TrieNode* node = root;
        for (char ch : word) {
            int index = ch - '0';
            if (node->children[index] == nullptr)
                node->children[index] = new TrieNode();
            node = node->children[index];
            node->count++;
        }
    }

    int countPrefix(const string& prefix) {
        TrieNode* node = root;
        for (char ch : prefix) {
            int index = ch - '0';
            if (node->children[index] == nullptr)
                return 0;
            node = node->children[index];
        }
        return node->count;
    }

private:
    TrieNode* root;

    void freeTrie(TrieNode* node) {
        if (!node) return;
        for (int i = 0; i < ALPHABET_SIZE; i++)
            freeTrie(node->children[i]);
        delete node;
    }
};

int main() {
    int N, Q;
    int caseNumber = 1;

    while (cin >> N >> Q) {
        Trie trie;
        string code;

        for (int i = 0; i < N; i++) {
            cin >> code;
            trie.insert(code);
        }

        cout << "Case " << caseNumber++ << ":\n";
        for (int i = 0; i < Q; i++) {
            cin >> code;
            cout << trie.countPrefix(code) << "\n";
        }
    }

    return 0;
}
