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
    case_number = 1
    try:
        while True:
            line = input()
            if not line:
                continue
            N, Q = map(int, line.strip().split())
            trie = Trie()

            for _ in range(N):
                number = input().strip()
                trie.insert(number)

            print(f"Case {case_number}:")
            for _ in range(Q):
                query = input().strip()
                print(trie.count_prefix(query))

            case_number += 1
    except EOFError:
        pass

if __name__ == "__main__":
    main()
