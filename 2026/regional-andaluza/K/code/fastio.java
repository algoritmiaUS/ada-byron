import java.io.*;
import java.util.*;

public class fastio {

    static boolean bfs(int[][] capacity, int source, int sink, int[] parent) {
        int n = capacity.length;
        boolean[] visited = new boolean[n];
        Queue<Integer> queue = new ArrayDeque<>();

        queue.add(source);
        visited[source] = true;
        parent[source] = -1;

        while (!queue.isEmpty()) {
            int u = queue.poll();

            for (int v = 0; v < n; v++) {
                if (!visited[v] && capacity[u][v] > 0) {
                    queue.add(v);
                    visited[v] = true;
                    parent[v] = u;

                    if (v == sink) return true;
                }
            }
        }
        return false;
    }

    static int edmondsKarp(int[][] capacity, int source, int sink) {
        int n = capacity.length;
        int[] parent = new int[n];
        int maxFlow = 0;

        while (bfs(capacity, source, sink, parent)) {
            int pathFlow = Integer.MAX_VALUE;

            int v = sink;
            while (v != source) {
                int u = parent[v];
                pathFlow = Math.min(pathFlow, capacity[u][v]);
                v = u;
            }

            v = sink;
            while (v != source) {
                int u = parent[v];
                capacity[u][v] -= pathFlow;
                capacity[v][u] += pathFlow;
                v = u;
            }

            maxFlow += pathFlow;
        }

        return maxFlow;
    }

    public static void solve() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int T = Integer.parseInt(br.readLine());

        while (T-- > 0) {
            st = new StringTokenizer(br.readLine());
            int N = Integer.parseInt(st.nextToken());
            int M = Integer.parseInt(st.nextToken());
            int K = Integer.parseInt(st.nextToken());

            int V = 2 + M + K;
            int source = 0;
            int sink = V - 1;

            int[][] capacity = new int[V][V];

            HashMap<String, Integer> map = new HashMap<>();
            st = new StringTokenizer(br.readLine());

            for (int i = 1; i <= K; i++) {
                String c = st.nextToken();
                map.put(c, i);
            }

            for (int i = 1; i <= M; i++) {
                capacity[source][i] = 1;
            }

            for (int i = 1; i <= M; i++) {
                st = new StringTokenizer(br.readLine());
                String c1 = st.nextToken();
                String c2 = st.nextToken();

                int id1 = map.get(c1);
                int id2 = map.get(c2);

                capacity[i][M + id1] = 1;
                capacity[i][M + id2] = 1;
            }

            int classLimit = N / K;

            for (int i = 1; i <= K; i++) {
                int volNode = M + i;
                capacity[volNode][sink] = classLimit;
            }

            int flow = edmondsKarp(capacity, source, sink);

            if (flow == M) System.out.println("YES");
            else System.out.println("NO");
        }
    }

    public static void main(String[] args) throws Exception {
        solve();
    }
}