import java.util.Scanner;

public class G {

    /**
     * Función de verificación: O(n)
     * @param cargaMax: Máxima carga que se puede asignar a una brigada.
     * @param k: Número de brigadas disponibles.
     * @param horas: Arreglo de horas de trabajo por tramo.
     * @return Si se pueden o no repartir todos los tramos entre 
     * k brigadas a lo sumo sin superar cargaMax.
     */
    public static boolean esSolucion(long cargaMax, int k, int[] horas)
    {
        long carga = 0;

        // Asignar carga de trabajo consecutivamente a las
        // brigadas sin superar cargaMax por brigada.
        for (int hi : horas)
            if ((carga += hi) > cargaMax) {
                --k;
                carga = hi;
            }

        return k > 0; // ¿Hay suficientes brigadas disponibles?
    }

    // Mínima carga máxima de n tramos entre k brigadas como mucho:
    // O(n log(carga_total))
    public static long minCargaMax(int n, int k, Scanner sc)
    {
        int[] horas = new int[n];
        long inf = 0, sup = 0, mCM = 0;

        for (int i = 0; i < n; ++i) {
            horas[i] = sc.nextInt();
            // Intervalo de la solución [inf, sup]
            inf = Math.max(inf, horas[i]); // Máximo de horas de todos los tramos
            sup += horas[i];               // Total de horas de todos los tramos
        }

        // Búsqueda de la solución óptima
        while (inf <= sup) { // O(n log(suma horas[i]))
            long cargaMax = inf + (sup - inf) / 2;
            if (esSolucion(cargaMax, k, horas)) {
                mCM = cargaMax; // cargaMax es solución, intentar algo menor
                sup = cargaMax - 1;
            }
            else
                inf = cargaMax + 1; // No es solución, se necesita mayor carga de trabajo
        }
        return mCM;
    }

    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        
        while (sc.hasNextInt()) {
            int n = sc.nextInt();
            int k = sc.nextInt();
            
            // Imprimir el resultado
            System.out.println(minCargaMax(n, k, sc));
        }
        
        sc.close();
    }
}
