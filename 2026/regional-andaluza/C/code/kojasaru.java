import java.util.*;
import java.io.*;

public class kojasaru {
    static class FastReader {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        String next() {
            while (st == null || !st.hasMoreElements()) {
                try { st = new StringTokenizer(br.readLine()); }
                catch (IOException e) { return null; }
            }
            return st.nextToken();
        }
        int nextInt() { return Integer.parseInt(next()); }
    }

    static class Show {
        int u, n;
        int[] powders;
    }

    static int[] head, next, to, headRev, nextRev, toRev;
    static int edgeCount, nodeCount;

    static void addEdge(int u, int v) {
        to[edgeCount] = v; next[edgeCount] = head[u]; head[u] = edgeCount;
        toRev[edgeCount] = u; nextRev[edgeCount] = headRev[v]; headRev[v] = edgeCount;
        edgeCount++;
    }

    // Clausula (A o B) -> (!A -> B) y (!B -> A)
    // node(x) = 2x, node(!x) = 2x + 1
    static void addClause(int uNode, int vNode, int totalVars) {
        int notU = uNode ^ 1;
        int notV = vNode ^ 1;
        addEdge(notU, vNode);
        addEdge(notV, uNode);
    }

    static int[] order, scc, callStack;
    static boolean[] visited;
    static int orderPtr, sccPtr;

    static void iterativeDFS1(int startNode, int totalNodes) {
        int top = 0;
        callStack[top++] = startNode;
        callStack[top++] = head[startNode];
        visited[startNode] = true;

        while (top > 0) {
            int edgeIdx = callStack[--top];
            int u = callStack[--top];

            if (edgeIdx != -1) {
                int v = to[edgeIdx];
                callStack[top++] = u;
                callStack[top++] = next[edgeIdx];
                if (!visited[v]) {
                    visited[v] = true;
                    callStack[top++] = v;
                    callStack[top++] = head[v];
                }
            } else {
                order[orderPtr++] = u;
            }
        }
    }

    static void iterativeDFS2(int startNode, int c) {
        int top = 0;
        callStack[top++] = startNode;
        scc[startNode] = c;

        while (top > 0) {
            int u = callStack[--top];
            for (int i = headRev[u]; i != -1; i = nextRev[i]) {
                int v = toRev[i];
                if (scc[v] == -1) {
                    scc[v] = c;
                    callStack[top++] = v;
                }
            }
        }
    }

    static boolean check(int K, int P, Show[][] shows, List<Integer>[] pMap) {
        int occCount = 0;
        for (int p = 1; p <= P; p++) {
            for (int occ : pMap[p]) if (occ / 2 < K) occCount++;
        }

        int totalVars = K + occCount;
        int totalNodes = 2 * totalVars;

        // Reiniciar grafos
        head = new int[totalNodes]; Arrays.fill(head, -1);
        headRev = new int[totalNodes]; Arrays.fill(headRev, -1);
        int maxEdges = K * 8 + occCount * 6; // Estimación segura
        to = new int[maxEdges]; next = new int[maxEdges];
        toRev = new int[maxEdges]; nextRev = new int[maxEdges];
        edgeCount = 0;

        // 1. CPP Constraints
        for (int i = 0; i < K - 1; i++) {
            for (int a = 0; a < 2; a++) {
                for (int b = 0; b < 2; b++) {
                    if (shows[i][a].u > shows[i+1][b].n) {
                        // !(Choice_i == a AND Choice_i+1 == b)
                        int uNode = (2 * i) + (a == 0 ? 0 : 1);
                        int vNode = (2 * (i + 1)) + (b == 0 ? 0 : 1);
                        addClause(uNode ^ 1, vNode ^ 1, totalVars);
                    }
                }
            }
        }

        // 2. Powder Constraints (Prefixes)
        int aux = K;
        for (int p = 1; p <= P; p++) {
            int lastAux = -1;
            for (int occ : pMap[p]) {
                int w = occ / 2; if (w >= K) continue;
                int literal = (2 * w) + (occ % 2); // 2w si A, 2w+1 si B
                int currentAuxNode = 2 * aux; // El literal positivo de la var aux

                // literal -> aux  <=> (!literal or aux)
                addClause(literal ^ 1, currentAuxNode, totalVars);
                if (lastAux != -1) {
                    int lastAuxNode = 2 * lastAux;
                    // lastAux -> currentAux <=> (!lastAux or currentAux)
                    addClause(lastAuxNode ^ 1, currentAuxNode, totalVars);
                    // lastAux -> !literal <=> (!lastAux or !literal)
                    addClause(lastAuxNode ^ 1, literal ^ 1, totalVars);
                }
                lastAux = aux++;
            }
        }

        // Kosaraju
        order = new int[totalNodes]; orderPtr = 0;
        visited = new boolean[totalNodes];
        callStack = new int[totalNodes * 2];
        for (int i = 0; i < totalNodes; i++) if (!visited[i]) iterativeDFS1(i, totalNodes);

        scc = new int[totalNodes]; Arrays.fill(scc, -1);
        sccPtr = 0;
        for (int i = totalNodes - 1; i >= 0; i--) {
            if (scc[order[i]] == -1) iterativeDFS2(order[i], sccPtr++);
        }

        for (int i = 0; i < totalVars; i++) {
            if (scc[2 * i] == scc[2 * i + 1]) return false;
        }
        return true;
    }

    public static void main(String[] args) {
        FastReader fr = new FastReader();
        PrintWriter out = new PrintWriter(System.out);
        int T = fr.nextInt();
        while (T-- > 0) {
            int M = fr.nextInt();
            int P = fr.nextInt(), I = fr.nextInt(), Np = fr.nextInt();
            boolean[] isU = new boolean[P + 1], isN = new boolean[P + 1];
            for (int i = 0; i < I; i++) isU[fr.nextInt()] = true;
            for (int i = 0; i < Np; i++) isN[fr.nextInt()] = true;

            Show[][] shows = new Show[M][2];
            List<Integer>[] pMap = new ArrayList[P + 1];
            for (int i = 1; i <= P; i++) pMap[i] = new ArrayList<>();

            for (int i = 0; i < M; i++) {
                for (int j = 0; j < 2; j++) {
                    int k = fr.nextInt();
                    shows[i][j] = new Show();
                    shows[i][j].powders = new int[k];
                    for (int l = 0; l < k; l++) {
                        int p = fr.nextInt();
                        shows[i][j].powders[l] = p;
                        if (isU[p]) shows[i][j].u++;
                        if (isN[p]) shows[i][j].n++;
                        pMap[p].add(i * 2 + j);
                    }
                }
            }

            int low = 1, high = M, ans = 0;
            while (low <= high) {
                int mid = (low + high) / 2;
                if (check(mid, P, shows, pMap)) { ans = mid; low = mid + 1; }
                else high = mid - 1;
            }
            out.println(ans);
        }
        out.flush();
    }
}
