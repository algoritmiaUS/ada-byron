import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.NoSuchElementException;

public class official {

    private class Bosque {
        private int [] parent;
        private int [] rank;
        private int numberOfSets;

        public Bosque(int n) {
            this.parent = new int [n];
            this.rank = new int [n];
            clear();
        }

        public void hazArbol(int x) {
            if (rank[x] < 0) {
                parent[x] = x;
                rank[x] = 0;
                numberOfSets++;
            }
        }

        public int encuentraArbol(int x) {
            if (rank[x] < 0) {
                throw new NoSuchElementException();
            }
            int v = x;
            while (parent[v]!=v) {
                v = parent[v];
            }
            while (parent[x]!=v) {
                int t = parent[x];
                parent[x] = v;
                x = t;
            }
            return v;
        }

        public void union(int x, int y) {
            x = encuentraArbol(x);
            y = encuentraArbol(y);
            if (x != y) {
                if (rank[x] < rank[y]) {
                    parent[x] = y;
                } else {
                    parent[y] = x;
                    if (rank[x] == rank[y]) {
                        rank[y]++;
                    }
                }
                numberOfSets--;
            }
        }

        public int getNumeroArboles() {
            return numberOfSets;
        }

        public void clear() {
            numberOfSets=0;
            for (int i=0; i < rank.length; i++) {
                rank[i]=-1;
            }
        }

    }

    record Arista(int i, int j, long tiempo) implements Comparable<Arista> {
        @Override
        public int compareTo(Arista o) {
            return Long.compare(this.tiempo, o.tiempo);
        }
    }


    private static long COSTE_POR_DIA = 1L;
    private static long KILOMETROS_METROS = 1_000L;

    private static long GRANITO = 1L; // Metros por día
    private static long ARENISCA = 4L;
    private static long PIZARRA = 10L;
    private static long LIMO = 20L;

    private int n;
    private long [][] distancia;
    private char [][] material;

    private Arista [] aristas;
    private Bosque bosque;

    private long coste;

    public static void main (String [] args) {
        official official = new official();
        official.run();
    }

    public void run() {
        leerInstancia();
        calcularCoste();
        System.out.println(coste);
    }

    private void leerInstancia() {
        try (InputStreamReader isr = new InputStreamReader(System.in);
             BufferedReader brd = new BufferedReader(isr)) {
            n = Integer.parseInt(brd.readLine());
            distancia = new long[n][n];
            material = new char[n][n];
            for (int i = 0; i < n; i++) {
                String [] aux = brd.readLine().split(" ");
                for (int j = 0; j < n; j++) {
                    distancia[i][j] = Long.parseLong(aux[j]);
                }
            }
            for (int i = 0; i < n; i++) {
                String [] aux = brd.readLine().split(" ");
                for (int j = 0; j < n; j++) {
                    material[i][j] = aux[j].charAt(0);
                }
            }
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    private void calcularCoste() {
        calcularTiempos();
        bosque = new Bosque(n);
        for (int i=0; i < n; ++i) {
            bosque.hazArbol(i);
        }
        Arrays.sort(aristas);
        coste = 0L;
        int index = 0;
        while (bosque.getNumeroArboles() > 1) {
            if (bosque.encuentraArbol(aristas[index].i) != bosque.encuentraArbol(aristas[index].j)) {
                // No están en el mismo árbol y no forman ciclo, así que añadimos la arista y unimos los árboles
                bosque.union(aristas[index].i, aristas[index].j);
                coste += aristas[index].tiempo * COSTE_POR_DIA;
            }
            index++;
        }
    }

    private void calcularTiempos() {
        // En realidad la entrada debe tener matrices simétricas, pero aquí no se da por hecho.
        aristas = new Arista[n*n];
        for (int i=0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                long tiempo = 0L;
                switch (material[i][j]) {
                    case 'G':
                        tiempo = distancia[i][j] * KILOMETROS_METROS / GRANITO;
                        break;
                    case 'A':
                        tiempo = distancia[i][j] * KILOMETROS_METROS / ARENISCA;
                        break;
                    case 'P':
                        tiempo = distancia[i][j] * KILOMETROS_METROS / PIZARRA;
                        break;
                    case 'L':
                        tiempo = distancia[i][j] * KILOMETROS_METROS / LIMO;
                        break;
                    default:
                        throw new IllegalArgumentException("Material desconocido: " + material[i][j]);
                }
                aristas[i*n+j] = new Arista(i, j, tiempo);
            }
        }
    }
}
