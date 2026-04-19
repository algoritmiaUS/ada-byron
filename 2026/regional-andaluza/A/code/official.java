import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.nio.charset.StandardCharsets;
import java.util.HashMap;
import java.util.StringTokenizer;

public class official {
  private static final String LIGHT = "\u25FB"; // ◻
  private static final String DARK = "\u25FC";  // ◼

  private static String piece(String c) {
    switch (c.charAt(0)) {
      // White pieces (Spanish initials)
      case 'R': return "\u2654"; // ♔ Rey
      case 'D': return "\u2655"; // ♕ Dama
      case 'T': return "\u2656"; // ♖ Torre
      case 'A': return "\u2657"; // ♗ Alfil
      case 'C': return "\u2658"; // ♘ Caballo
      case 'P': return "\u2659"; // ♙ Peon
      // Black pieces
      case 'r': return "\u265A";
      case 'd': return "\u265B";
      case 't': return "\u265C";
      case 'a': return "\u265D";
      case 'c': return "\u265E";
      case 'p': return "\u265F";
      default: return null;
    }
  }

  private static String emptySquare(int fileIdx, int rankIdx) {
    // a1 is dark
    return ((fileIdx + rankIdx) & 1) == 0 ? DARK : LIGHT;
  }

  public static void main(String[] args) throws Exception {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in, StandardCharsets.UTF_8));
    StringBuilder out = new StringBuilder();

    int T = Integer.parseInt(br.readLine().trim());
    for (int tc = 0; tc < T; tc++) {
      int P = Integer.parseInt(br.readLine().trim());

      // Memory: map square id -> piece.
      // Square id is 0..63 with id = rank*8 + file, where rank=0 is '1' and file=0 is 'a'.
      HashMap<Integer, String> memory = new HashMap<>(P * 2);

      for (int i = 0; i < P; i++) {
        StringTokenizer st = new StringTokenizer(br.readLine());
        String pieceTok = st.nextToken();
        String pos = st.nextToken();

        int fileIdx = pos.charAt(0) - 'a';
        int rankIdx = pos.charAt(1) - '1';
        int sqId = rankIdx * 8 + fileIdx;
        memory.put(sqId, piece(pieceTok));
      }

      // Build the 64 squares.
      String[] squares = new String[64];
      for (int rankIdx = 0; rankIdx < 8; rankIdx++) {
        for (int fileIdx = 0; fileIdx < 8; fileIdx++) {
          int sqId = rankIdx * 8 + fileIdx;
          String v = memory.get(sqId);
          squares[sqId] = (v != null) ? v : emptySquare(fileIdx, rankIdx);
        }
      }

      // Print from rank 8 down to 1.
      for (int rankIdx = 7; rankIdx >= 0; rankIdx--) {
        for (int fileIdx = 0; fileIdx < 8; fileIdx++) {
          out.append(squares[rankIdx * 8 + fileIdx]);
          if (fileIdx != 7) out.append(' ');
        }
        out.append('\n');
      }

      if (tc != T - 1) out.append('\n');
    }

    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out, StandardCharsets.UTF_8));
    bw.write(out.toString());
    bw.flush();
  }
}
