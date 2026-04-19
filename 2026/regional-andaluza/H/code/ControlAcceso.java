import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class ControlAcceso {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int T = Integer.parseInt(br.readLine().trim());
        StringBuilder out = new StringBuilder();

        while (T-- > 0) {
            int C = Integer.parseInt(br.readLine().trim());
            String s = br.readLine().trim();

            int ocupacion = 0;
            boolean valido = true;

            for (int i = 0; i < s.length(); i++) {
                char ch = s.charAt(i);

                if (ch == 'E') {
                    ocupacion++;
                    if (ocupacion > C) {
                        valido = false;
                        break;
                    }
                } else { // 'S'
                    ocupacion--;
                    if (ocupacion < 0) {
                        valido = false;
                        break;
                    }
                }
            }

            if (ocupacion != 0) {
                valido = false;
            }

            if (valido) {
                out.append("VALIDO\n");
            } else {
                out.append("INVALIDO\n");
            }
        }

        System.out.print(out.toString());
    }
}