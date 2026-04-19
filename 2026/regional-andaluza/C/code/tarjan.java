import java.util.*;
import java.io.*;

public class tarjan {
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
        int[] powders;
        int unstable, neutral;
    }

    static List<Integer>[] adj;
    static int[] disc, low, scc;
    static boolean[] onStack;
    static Stack<Integer> stack;
    static int timer, sccCount;

    static void addClause(int u, boolean uVal, int v, boolean vVal, int n) {
        // 2-SAT: (u or v) <=> (!u -> v) and (!v -> u)
        int uNode = uVal ? u : u + n;
        int vNode = vVal ? v : v + n;
        int notUNode = uVal ? u + n : u;
        int notVNode = vVal ? v + n : v;
        adj[notUNode].add(vNode);
        adj[notVNode].add(uNode);
    }

    static void tarjan(int u) {
        disc[u] = low[u] = ++timer;
        stack.push(u);
        onStack[u] = true;
        for (int v : adj[u]) {
            if (disc[v] == -1) {
                tarjan(v);
                low[u] = Math.min(low[u], low[v]);
            } else if (onStack[v]) {
                low[u] = Math.min(low[u], disc[v]);
            }
        }
        if (low[u] == disc[u]) {
            while (true) {
                int v = stack.pop();
                onStack[v] = false;
                scc[v] = sccCount;
                if (u == v) break;
            }
            sccCount++;
        }
    }

    static boolean check(int K, int M, int P, Show[][] shows, List<Integer>[] powderMap) {
        // Variables: K (semanas) + Variables de prefijo para cada aparición de polvo
        int totalOccurrences = 0;
        for (int p = 1; p <= P; p++) {
            int count = 0;
            for (int idx : powderMap[p]) if (idx / 2 < K) count++;
            if (count > 0) totalOccurrences += count;
        }

        int nVars = K + totalOccurrences;
        adj = new ArrayList[2 * nVars];
        for (int i = 0; i < 2 * nVars; i++) adj[i] = new ArrayList<>();

        // 1. Restricciones CPP entre semanas consecutivas [cite: 14]
        for (int i = 0; i < K - 1; i++) {
            for (int a = 0; a < 2; a++) {
                for (int b = 0; b < 2; b++) {
                    if (shows[i][a].unstable > shows[i+1][b].neutral) {
                        // Clausula: !(Si_a AND Si+1_b) => (!Si_a OR !Si+1_b)
                        addClause(i, a != 0, i + 1, b != 0, nVars);
                    }
                }
            }
        }

        // 2. Restricciones de Polvos (At-Most-One) usando prefijos [cite: 10, 12]
        int auxBase = K;
        for (int p = 1; p <= P; p++) {
            int lastAux = -1;
            for (int occ : powderMap[p]) {
                int week = occ / 2;
                if (week >= K) continue;
                int showIdx = occ % 2; // 0 para A, 1 para B
                
                int currentVar = week;
                boolean isTrueVar = (showIdx == 0); // Variable x_i es Show A
                
                int currentAux = auxBase++;
                
                // Si se elige este espectáculo, se activa el prefijo actual
                // show -> aux
                addClause(currentVar, !isTrueVar, currentAux, true, nVars);
                
                if (lastAux != -1) {
                    // Si el prefijo anterior estaba activo, el actual también
                    // lastAux -> currentAux
                    addClause(lastAux, false, currentAux, true, nVars);
                    // Si el prefijo anterior estaba activo, no se puede elegir este espectáculo
                    // lastAux -> !show
                    addClause(lastAux, false, currentVar, !isTrueVar, nVars);
                }
                lastAux = currentAux;
            }
        }

        // Tarjan SCC
        disc = new int[2 * nVars];
        Arrays.fill(disc, -1);
        low = new int[2 * nVars];
        scc = new int[2 * nVars];
        onStack = new boolean[2 * nVars];
        stack = new Stack<>();
        timer = 0; sccCount = 0;

        for (int i = 0; i < 2 * nVars; i++) if (disc[i] == -1) tarjan(i);
        for (int i = 0; i < nVars; i++) if (scc[i] == scc[i + nVars]) return false;
        
        return true;
    }

    public static void main(String[] args) {
        FastReader sc = new FastReader();
        String tStr = sc.next();
        if (tStr == null) return;
        int T = Integer.parseInt(tStr);

        while (T-- > 0) {
            int M = sc.nextInt();
            int P = sc.nextInt(), I = sc.nextInt(), N = sc.nextInt();
            boolean[] isU = new boolean[P + 1];
            boolean[] isN = new boolean[P + 1];
            for (int i = 0; i < I; i++) isU[sc.nextInt()] = true;
            for (int i = 0; i < N; i++) isN[sc.nextInt()] = true;

            Show[][] shows = new Show[M][2];
            List<Integer>[] powderMap = new ArrayList[P + 1];
            for (int i = 1; i <= P; i++) powderMap[i] = new ArrayList<>();

            for (int i = 0; i < M; i++) {
                for (int j = 0; j < 2; j++) {
                    int k = sc.nextInt();
                    shows[i][j] = new Show();
                    shows[i][j].powders = new int[k];
                    for (int p = 0; p < k; p++) {
                        int id = sc.nextInt();
                        shows[i][j].powders[p] = id;
                        if (isU[id]) shows[i][j].unstable++;
                        if (isN[id]) shows[i][j].neutral++;
                        powderMap[id].add(i * 2 + j);
                    }
                }
            }

            int low = 1, high = M, ans = 0;
            while (low <= high) {
                int mid = (low + high) / 2;
                if (check(mid, M, P, shows, powderMap)) {
                    ans = mid;
                    low = mid + 1;
                } else {
                    high = mid - 1;
                }
            }
            System.out.println(ans);
        }
    }
}
