import java.io.*;
import java.util.*;

public class dinic_solve {
    static class Edge {
        int to, cap, rev;
        Edge(int to, int cap, int rev) {
            this.to = to;
            this.cap = cap;
            this.rev = rev;
        }
    }

    static class Dinic {
        int n;
        ArrayList<Edge>[] g;
        int[] level, it;

        @SuppressWarnings("unchecked")
        Dinic(int n) {
            this.n = n;
            g = new ArrayList[n];
            for (int i = 0; i < n; i++) g[i] = new ArrayList<>();
            level = new int[n];
            it = new int[n];
        }

        void addEdge(int u, int v, int cap) {
            g[u].add(new Edge(v, cap, g[v].size()));
            g[v].add(new Edge(u, 0, g[u].size() - 1));
        }

        boolean bfs(int s, int t) {
            Arrays.fill(level, -1);
            Queue<Integer> q = new ArrayDeque<>();
            level[s] = 0;
            q.add(s);

            while (!q.isEmpty()) {
                int u = q.poll();
                for (Edge e : g[u]) {
                    if (e.cap > 0 && level[e.to] == -1) {
                        level[e.to] = level[u] + 1;
                        q.add(e.to);
                    }
                }
            }

            return level[t] != -1;
        }

        int dfs(int u, int t, int f) {
            if (u == t) return f;

            for (; it[u] < g[u].size(); it[u]++) {
                Edge e = g[u].get(it[u]);
                if (e.cap > 0 && level[e.to] == level[u] + 1) {
                    int pushed = dfs(e.to, t, Math.min(f, e.cap));
                    if (pushed > 0) {
                        e.cap -= pushed;
                        g[e.to].get(e.rev).cap += pushed;
                        return pushed;
                    }
                }
            }

            return 0;
        }

        int maxFlow(int s, int t) {
            int flow = 0;
            final int INF = 1_000_000_000;

            while (bfs(s, t)) {
                Arrays.fill(it, 0);
                while (true) {
                    int pushed = dfs(s, t, INF);
                    if (pushed == 0) break;
                    flow += pushed;
                }
            }

            return flow;
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int TC = Integer.parseInt(br.readLine().trim());
        StringBuilder out = new StringBuilder();

        while (TC-- > 0) {
            st = new StringTokenizer(br.readLine());
            int N = Integer.parseInt(st.nextToken());
            int M = Integer.parseInt(st.nextToken());
            int K = Integer.parseInt(st.nextToken());

            st = new StringTokenizer(br.readLine());
            HashMap<String, Integer> roleId = new HashMap<>();
            for (int i = 0; i < K; i++) {
                roleId.put(st.nextToken(), i);
            }

            int limit = N / K;

            int S = 0;
            int firstPlayer = 1;
            int firstRole = 1 + M;
            int T = 1 + M + K;

            Dinic dinic = new Dinic(T + 1);

            for (int i = 0; i < M; i++) {
                dinic.addEdge(S, firstPlayer + i, 1);
            }

            for (int i = 0; i < M; i++) {
                st = new StringTokenizer(br.readLine());
                String a = st.nextToken();
                String b = st.nextToken();
                dinic.addEdge(firstPlayer + i, firstRole + roleId.get(a), 1);
                dinic.addEdge(firstPlayer + i, firstRole + roleId.get(b), 1);
            }

            for (int j = 0; j < K; j++) {
                dinic.addEdge(firstRole + j, T, limit);
            }

            int flow = dinic.maxFlow(S, T);
            out.append(flow == M ? "YES" : "NO").append('\n');
        }

        System.out.print(out);
    }
}