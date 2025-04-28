import sys

class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, number):
        node = self.root
        for ch in number:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
            node.count += 1

    def count_prefix(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return 0
            node = node.children[ch]
        return node.count

def main():
    input = sys.stdin.readline
    case_number = 1

    while True:
        line = input()
        if not line:
            break
        N, Q = map(int, line.split())
        # except ValueError:
        trie = Trie()
        for _ in range(N):
            code = input().strip()
            trie.insert(code)

        print(f"Case {case_number}:")
        for _ in range(Q):
            query = input().strip()
            print(trie.count_prefix(query))

        case_number += 1

if __name__ == "__main__":
    main()
