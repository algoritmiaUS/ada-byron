import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;
import java.util.PriorityQueue;
import java.util.Scanner;

class Cociente {
    int cliente;
    int gasto;
    int divisor;

    public Cociente(int cliente, int gasto, int divisor) {
        this.cliente = cliente;
        this.gasto = gasto;
        this.divisor = divisor;
    }
}

// Orden decreciente para el montículo
class CocienteComparator implements Comparator<Cociente> {
    @Override
    public int compare(Cociente a, Cociente b) {
        int comp = Integer.compare(b.gasto / b.divisor, a.gasto / a.divisor);
        if (comp == 0)
            return Integer.compare(b.gasto, a.gasto);
        return comp;
    }
}

public class ValesDescuento {

    public static void repartir_vales(int m, int n, Scanner scanner) {
        List<Integer> vales = new ArrayList<>(Collections.nCopies(m, 0)); // Número de vales de cada cliente
        PriorityQueue<Cociente> mayores_cocientes = new PriorityQueue<>(new CocienteComparator()); // Montículo de máximos
        int gasto;

        // Inicialización con los gastos de los m clientes.
        for (int k = 0; k < m; ++k) {
            gasto = scanner.nextInt();
            mayores_cocientes.add(new Cociente(k, gasto, 1));
        }

        // Seleccionar los n mayores cocientes
        for (int i = 1; i <= n; ++i) {
            // Extraer mayor cociente y asignar vale al cliente
            Cociente mayor = mayores_cocientes.poll();
            vales.set(mayor.cliente, vales.get(mayor.cliente) + 1);
            // Añadir nuevo cociente
            mayor.divisor += 1;
            mayores_cocientes.add(mayor);
        }

        for (int i = 0; i < vales.size(); ++i) {
            System.out.print(vales.get(i));
            if (i < vales.size() - 1)
                System.out.print(" ");
        }
        System.out.println();
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int nCli, nVales;
        nCli = scanner.nextInt();
        nVales = scanner.nextInt();
        while (nCli > 0 && nVales > 0) {
            repartir_vales(nCli, nVales, scanner);
            nCli = scanner.nextInt();
            nVales = scanner.nextInt();
        }
        scanner.close();
    }
}
