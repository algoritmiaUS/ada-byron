import java.util.*;

public class official {

    // El BFS y Edmonds-Karp se mantienen óptimos usando Lista de Adyacencia
    static boolean bfs(int[][] capacity, ArrayList<Integer>[] adj, int source, int sink, int[] parent) {
        int n = capacity.length;
        boolean[] visited = new boolean[n];
        Queue<Integer> queue = new ArrayDeque<>();

        queue.add(source);
        visited[source] = true;
        parent[source] = -1;

        while (!queue.isEmpty()) {
            int u = queue.poll();
            for (int v : adj[u]) {
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

    static int edmondsKarp(int[][] capacity, ArrayList<Integer>[] adj, int source, int sink) {
        int n = capacity.length;
        int[] parent = new int[n];
        int maxFlow = 0;

        while (bfs(capacity, adj, source, sink, parent)) {
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

    public static void main(String[] args) {
        // Usamos Scanner básico
        Scanner sc = new Scanner(System.in);
        
        if (!sc.hasNextInt()) return;
        int T = sc.nextInt();

        while (T-- > 0) {
            int N = sc.nextInt();
            int M = sc.nextInt();
            int K = sc.nextInt();

            int V = 2 + M + K;
            int source = 0;
            int sink = V - 1;

            int[][] capacity = new int[V][V];
            
            @SuppressWarnings("unchecked")
            ArrayList<Integer>[] adj = new ArrayList[V];
            for (int i = 0; i < V; i++) {
                adj[i] = new ArrayList<>();
            }

            HashMap<String, Integer> map = new HashMap<>();
            for (int i = 1; i <= K; i++) {
                map.put(sc.next(), i);
            }

            for (int i = 1; i <= M; i++) {
                capacity[source][i] = 1;
                adj[source].add(i);
                adj[i].add(source);
            }

            for (int i = 1; i <= M; i++) {
                String c1 = sc.next();
                String c2 = sc.next();

                int id1 = map.get(c1);
                int id2 = map.get(c2);

                capacity[i][M + id1] = 1;
                adj[i].add(M + id1);
                adj[M + id1].add(i);

                capacity[i][M + id2] = 1;
                adj[i].add(M + id2);
                adj[M + id2].add(i);
            }

            int classLimit = N / K;
            for (int i = 1; i <= K; i++) {
                int volNode = M + i;
                capacity[volNode][sink] = classLimit;
                adj[volNode].add(sink);
                adj[sink].add(volNode);
            }

            int flow = edmondsKarp(capacity, adj, source, sink);

            // Salida lenta caso por caso
            if (flow == M) {
                System.out.println("YES");
            } else {
                System.out.println("NO");
            }
        }
        sc.close();
    }
}