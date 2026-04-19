#include <stdio.h>


static const char *piece_utf8(char c) {
  switch (c) {
    // White pieces (Spanish initials)
    case 'R': return "\u2654";  // ♔ Rey
    case 'D': return "\u2655";  // ♕ Dama
    case 'T': return "\u2656";  // ♖ Torre
    case 'A': return "\u2657";  // ♗ Alfil
    case 'C': return "\u2658";  // ♘ Caballo
    case 'P': return "\u2659";  // ♙ Peon
    // Black pieces
    case 'r': return "\u265A";
    case 'd': return "\u265B";
    case 't': return "\u265C";
    case 'a': return "\u265D";
    case 'c': return "\u265E";
    case 'p': return "\u265F";
    default: return 0;
  }
}

static const char *empty_square(int file_idx, int rank_idx) {
  // a1 is dark.
  int dark = ((file_idx + rank_idx) % 2 == 0);
  return dark ? "\u25FC" : "\u25FB";  // ◼ y ◻
}

int main(void) {
  int T;
  if (scanf("%d", &T) != 1) return 0;

  for (int tc = 0; tc < T; ++tc) {
    int P;
    scanf("%d", &P);

    // Memory: store (square id -> piece) as two arrays.
    // Square id is 0..63 with id = rank*8 + file, where rank=0 is '1' and file=0 is 'a'.
    int keys[32];
    const char *vals[32];
    int nmem = 0;

    for (int i = 0; i < P; ++i) {
      char piece[8];
      char pos[8];
      scanf("%7s %7s", piece, pos);

      int file_idx = pos[0] - 'a';
      int rank_idx = pos[1] - '1';
      int sq_id = rank_idx * 8 + file_idx;

      keys[nmem] = sq_id;
      vals[nmem] = piece_utf8(piece[0]);
      nmem++;
    }

    // Build the 64 squares.
    const char *squares[64];
    for (int rank_idx = 0; rank_idx < 8; ++rank_idx) {
      for (int file_idx = 0; file_idx < 8; ++file_idx) {
        int sq_id = rank_idx * 8 + file_idx;
        const char *v = 0;
        for (int k = 0; k < nmem; ++k) {
          if (keys[k] == sq_id) {
            v = vals[k];
            break;
          }
        }
        squares[sq_id] = (v != 0) ? v : empty_square(file_idx, rank_idx);
      }
    }

    // Print from rank 8 down to 1.
    for (int rank_idx = 7; rank_idx >= 0; --rank_idx) {
      for (int file_idx = 0; file_idx < 8; ++file_idx) {
        fputs(squares[rank_idx * 8 + file_idx], stdout);
        if (file_idx != 7) fputc(' ', stdout);
      }
      fputc('\n', stdout);
    }

    if (tc != T - 1) fputc('\n', stdout);
  }
  return 0;
}
