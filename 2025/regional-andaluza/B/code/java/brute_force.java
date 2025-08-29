import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int caso = 1;

        while (sc.hasNextInt()) {
            int N = sc.nextInt();
            int Q = sc.nextInt();
            sc.nextLine(); // Limpiar salto de línea

            String[] codigos = new String[N];
            for (int i = 0; i < N; i++) {
                codigos[i] = sc.nextLine();
            }

            System.out.println("Case " + caso + ":");
            for (int i = 0; i < Q; i++) {
                String prefijo = sc.nextLine();
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

        sc.close();
    }
}
