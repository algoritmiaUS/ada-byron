import java.util.*;

public class genomaV2 {

    public static List<String> eliminarDuplicados(String[] motivosArray) {
        LinkedHashSet<String> set = new LinkedHashSet<>(Arrays.asList(motivosArray));
        return new ArrayList<>(set);
    }

    public static List<int[]> buscarOcurrencias(String adn, List<String> motivos) {
        List<int[]> ocurrencias = new ArrayList<>();

        for (int id = 0; id < motivos.size(); id++) {
            String motivo = motivos.get(id);
            int start = 0;

            while (true) {
                int pos = adn.indexOf(motivo, start);
                if (pos == -1) {
                    break;
                }

                // Guardamos: [fin, inicio, idMotivo]
                ocurrencias.add(new int[] { pos + motivo.length() - 1, pos, id });
                start = pos + 1; // permitir solapamientos
            }
        }

        return ocurrencias;
    }

    public static int calcularMinimaLongitud(List<int[]> ocurrencias, int numMotivos, int k) {
        int[] latestStart = new int[numMotivos];
        Arrays.fill(latestStart, -1);

        int ans = Integer.MAX_VALUE;

        for (int[] ocurrencia : ocurrencias) {
            int fin = ocurrencia[0];
            int inicio = ocurrencia[1];
            int id = ocurrencia[2];

            if (inicio > latestStart[id]) {
                latestStart[id] = inicio;
            }

            List<Integer> activos = new ArrayList<>();
            for (int x : latestStart) {
                if (x != -1) {
                    activos.add(x);
                }
            }

            if (activos.size() >= k) {
                activos.sort(Collections.reverseOrder());
                int L = activos.get(k - 1);
                ans = Math.min(ans, fin - L + 1);
            }
        }

        return ans == Integer.MAX_VALUE ? 0 : ans;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        String adn = scanner.nextLine();
        String lineaMotivos = scanner.nextLine();
        int k = scanner.nextInt();

        List<String> motivos = eliminarDuplicados(lineaMotivos.split(" "));

        if (k > motivos.size()) {
            System.out.println(0);
            scanner.close();
            return;
        }

        List<int[]> ocurrencias = buscarOcurrencias(adn, motivos);

        if (ocurrencias.isEmpty()) {
            System.out.println(0);
            scanner.close();
            return;
        }

        ocurrencias.sort((a, b) -> {
            if (a[0] != b[0]) return Integer.compare(a[0], b[0]); // por fin
            if (a[1] != b[1]) return Integer.compare(a[1], b[1]); // luego por inicio
            return Integer.compare(a[2], b[2]); // luego por id
        });

        int resultado = calcularMinimaLongitud(ocurrencias, motivos.size(), k);
        System.out.println(resultado);

        scanner.close();
    }
}