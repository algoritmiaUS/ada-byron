import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String linea;
        int caso = 1;

        while ((linea = br.readLine()) != null && !linea.isEmpty()) {
            StringTokenizer st = new StringTokenizer(linea);
            int N = Integer.parseInt(st.nextToken());
            int Q = Integer.parseInt(st.nextToken());

            String[] codigos = new String[N];
            for (int i = 0; i < N; i++) {
                codigos[i] = br.readLine();
            }

            System.out.println("Case " + caso + ":");

            for (int i = 0; i < Q; i++) {
                String prefijo = br.readLine();
                int contador = 0;
                for (int j = 0; j < N; j++) {
                    if (codigos[j].startsWith(prefijo)) {
                        contador++;
                    }
                }
                System.out.println(contador);
            }

            caso++;
        }
    }
}
