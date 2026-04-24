package sol;

import java.io.*;
import java.util.*;

public class SolucionPiramide3D {

    public static void main(String[] args) throws IOException {
        // Usamos Reader rápido para evitar TLE (Time Limit Exceeded)
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        if (!st.hasMoreTokens()) return;

        double liquidoInicial = Double.parseDouble(st.nextToken());
        int H = Integer.parseInt(st.nextToken());

        // 1. Leer Capacidades
        // Usamos una estructura de array dentado para ahorrar memoria
        double[][] capacidades = new double[H][];
        for (int i = 0; i < H; i++) {
            int numCopasNivel = (i + 1) * (i + 1);
            capacidades[i] = new double[numCopasNivel];
            
            // Los niveles pueden venir en varias líneas o una sola larga
            int leidas = 0;
            while (leidas < numCopasNivel) {
                st = new StringTokenizer(br.readLine());
                while (st.hasMoreTokens()) {
                    capacidades[i][leidas++] = Double.parseDouble(st.nextToken());
                }
            }
        }

        // 2. Procesar el líquido con DP
        // dp[i][r][c] guardará TODO el líquido que pasa por esa copa
        double[][] flujoTotal = resolverDP(H, liquidoInicial, capacidades);

        // 3. Responder Consultas
        st = new StringTokenizer(br.readLine());
        if (st.hasMoreTokens()) {
            int Q = Integer.parseInt(st.nextToken());
            PrintWriter out = new PrintWriter(System.out);
            
            for (int q = 0; q < Q; q++) {
                st = new StringTokenizer(br.readLine());
                int nivel = Integer.parseInt(st.nextToken());
                int fila = Integer.parseInt(st.nextToken());
                int col = Integer.parseInt(st.nextToken());

                // El volumen real es el mínimo entre lo que llegó y la capacidad
                int idx = fila * (nivel + 1) + col;
                double contenido = Math.min(capacidades[nivel][idx], flujoTotal[nivel][idx]);
                
                out.printf(Locale.US, "%.6f\n", contenido);
            }
            out.flush();
        }
    }

    private static double[][] resolverDP(int H, double liquido, double[][] caps) {
        double[][] dp = new double[H][];
        for (int i = 0; i < H; i++) {
            dp[i] = new double[(i + 1) * (i + 1)];
        }

        // Vertido inicial
        dp[0][0] = liquido;

        // Propagar líquido nivel a nivel
        for (int i = 0; i < H - 1; i++) {
            int ladoActual = i + 1;
            int ladoSiguiente = i + 2;

            for (int r = 0; r < ladoActual; r++) {
                for (int c = 0; c < ladoActual; c++) {
                    int idxActual = r * ladoActual + c;
                    double sobrante = dp[i][idxActual] - caps[i][idxActual];

                    if (sobrante > 0) {
                        double cuarto = sobrante / 4.0;
                        
                        // Distribución a las 4 copas inferiores
                        dp[i + 1][r * ladoSiguiente + c] += cuarto;
                        dp[i + 1][(r + 1) * ladoSiguiente + c] += cuarto;
                        dp[i + 1][r * ladoSiguiente + (c + 1)] += cuarto;
                        dp[i + 1][(r + 1) * ladoSiguiente + (c + 1)] += cuarto;
                    }
                }
            }
        }
        return dp;
    }
}