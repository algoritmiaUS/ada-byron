import java.math.BigInteger;
import java.util.Scanner;

public class EstrategiaEstelar {

    public static void main (String [] args) {
        new EstrategiaEstelar().run();
    }

    private void run () {
        try (Scanner scanner = new Scanner(System.in)) {
            int [][] coordenadas = new int[3][3];
            for (int flota = 0; flota < 3; flota++) {
                for (int coordenada = 0; coordenada < 3; coordenada++) {
                    coordenadas[flota][coordenada] = scanner.nextInt();
                }
            }

            BigInteger periodo = BigInteger.ONE;
            for (int coordenada=0; coordenada < 3; coordenada++) {
                BigInteger longituCiclo = BigInteger.valueOf(calculaCiclo(coordenadas, coordenada));
                BigInteger gcd = longituCiclo.gcd(periodo);
                periodo = longituCiclo.divide(gcd).multiply(periodo);
                //System.out.println(longituCiclo);
            }
            System.out.println(periodo);
        }
    }

    private long calculaCiclo (int [][] coordenadas, int coordenada) {
        int [] posicion = new int [3];
        int [] velocidad = new int [3];

        for (int flota=0; flota < 3;  flota++) {
            posicion[flota] = coordenadas[flota][coordenada];
        }

        int [] original = posicion.clone();

        int dia = 0;
        do {
            // Actualizar velocidades
            for (int flota = 0; flota < 3; flota++) {
                for (int f = 0; f < 3; f++) {
                    if (f != flota) {
                        if (posicion[f] > posicion[flota]) {
                            velocidad[flota]++;
                        } else if (posicion[f] < posicion[flota]) {
                            velocidad[flota]--;
                        }
                    }
                }
            }
            for (int flota=0; flota < 3;  flota++) {
                posicion[flota] += velocidad[flota];
            }
            dia++;
        } while (!velocidadCero(velocidad) || !posicionesIguales(posicion, original));


        return dia;
    }

    private boolean velocidadCero(int [] velocidad) {
        for (int i = 0; i < velocidad.length; i++) {
            if (velocidad[i] != 0) {
                return false;
            }
        }
        return true;
    }

    private boolean posicionesIguales(int [] posicion, int [] original) {
        for (int i = 0; i < posicion.length; i++) {
            if (posicion[i] != original[i]) {
                return false;
            }
        }
        return true;
    }


}
