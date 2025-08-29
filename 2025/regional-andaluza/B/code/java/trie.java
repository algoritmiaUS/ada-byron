import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

class TrieNode {
    Map<Character, TrieNode> children;
    int count;

    public TrieNode() {
        this.children = new HashMap<>();
        this.count = 0;
    }
}

class Trie {
    private TrieNode root;

    public Trie() {
        this.root = new TrieNode();
    }

    public void insert(String number) {
        TrieNode node = root;
        for (int i = 0; i < number.length(); i++) {
            char digit = number.charAt(i);
            if (!node.children.containsKey(digit)) {
                node.children.put(digit, new TrieNode());
            }
            node = node.children.get(digit);
            node.count++;
        }
    }

    public int countPrefix(String prefix) {
        TrieNode node = root;
        for (int i = 0; i < prefix.length(); i++) {
            char digit = prefix.charAt(i);
            if (!node.children.containsKey(digit)) {
                return 0;
            }
            node = node.children.get(digit);
        }
        return node.count;
    }
}


class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int caseNum = 1;

        while (scanner.hasNext()) {
            try {
                int N = scanner.nextInt();
                int Q = scanner.nextInt();
                scanner.nextLine(); // Consumir el resto de la línea

                Trie trie = new Trie();

                for (int i = 0; i < N; i++) {
                    String number = scanner.nextLine().trim();
                    trie.insert(number);
                }

                System.out.printf("Case %d:\n", caseNum);
                for (int i = 0; i < Q; i++) {
                    String prefix = scanner.nextLine().trim();
                    System.out.println(trie.countPrefix(prefix));
                }

                caseNum++;
            } catch (Exception e) {
                break;
            }
        }
        scanner.close();
    }
}
