import java.util.Scanner;

public class TorneoGuerreros {

    public static void main (String [] args) {
        new TorneoGuerreros().run();
    }

    public void run () {
        try (Scanner scanner = new Scanner(System.in)) {
            int torneos = scanner.nextInt();
            for (int i=0; i < torneos; i++) {
                int guerreros = scanner.nextInt();
                int combates = calculaCombates(guerreros);
                System.out.println(combates);
            }
        }
    }

    private int calculaCombates(int guerreros) {
        int combates = 0;
        while (guerreros > 1) {
            guerreros >>>= 1;
            combates += guerreros;
            if ((guerreros != 1) && (guerreros & 0x01) != 0) {
                guerreros++;
            }
        }
        return combates;
    }

}
