import java.io.*;
import java.util.*;

public class solucion {
    public static int maxCristales(int n, int m, int[][] grid) {
        int[][] dp = new int[n][m];
        dp[0][0] = grid[0][0];

        // Primera fila
        for (int j = 1; j < m; j++) {
            dp[0][j] = dp[0][j - 1] + grid[0][j];
        }

        // Primera columna
        for (int i = 1; i < n; i++) {
            dp[i][0] = dp[i - 1][0] + grid[i][0];
        }

        // Resto de la matriz
        for (int i = 1; i < n; i++) {
            for (int j = 1; j < m; j++) {
                dp[i][j] = grid[i][j] + Math.max(dp[i - 1][j], Math.max(dp[i][j - 1], dp[i - 1][j - 1]));
            }
        }

        return dp[n - 1][m - 1];
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line;
        StringBuilder output = new StringBuilder();

        while ((line = br.readLine()) != null) {
            String[] dimensions = line.split(" ");
            int n = Integer.parseInt(dimensions[0]);
            int m = Integer.parseInt(dimensions[1]);

            int[][] grid = new int[n][m];
            for (int i = 0; i < n; i++) {
                String[] row = br.readLine().split(" ");
                for (int j = 0; j < m; j++) {
                    grid[i][j] = Integer.parseInt(row[j]);
                }
            }

            int result = maxCristales(n, m, grid);
            output.append(result).append("\n");
        }

        System.out.print(output);
    }
}
