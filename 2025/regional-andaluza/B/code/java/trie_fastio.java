import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

class TrieNode {
    TrieNode[] children;
    int count;

    public TrieNode() {
        children = new TrieNode[10];
        count = 0;
    }
}

class Trie {
    private TrieNode root;

    public Trie() {
        root = new TrieNode();
    }

    public void insert(String number) {
        TrieNode node = root;
        for (char ch : number.toCharArray()) {
            int index = ch - '0';
            if (node.children[index] == null) {
                node.children[index] = new TrieNode();
            }
            node = node.children[index];
            node.count++;
        }
    }

    public int countPrefix(String prefix) {
        TrieNode node = root;
        for (char ch : prefix.toCharArray()) {
            int index = ch - '0';
            if (node.children[index] == null) {
                return 0;
            }
            node = node.children[index];
        }
        return node.count;
    }
}

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line;
        int caseNumber = 1;

        while ((line = br.readLine()) != null && !line.isEmpty()) {
            StringTokenizer st = new StringTokenizer(line);
            int N = Integer.parseInt(st.nextToken());
            int Q = Integer.parseInt(st.nextToken());

            Trie trie = new Trie();

            for (int i = 0; i < N; i++) {
                String number = br.readLine().trim();
                trie.insert(number);
            }

            System.out.println("Case " + caseNumber + ":");
            for (int i = 0; i < Q; i++) {
                String prefix = br.readLine().trim();
                System.out.println(trie.countPrefix(prefix));
            }

            caseNumber++;
        }
    }
}
