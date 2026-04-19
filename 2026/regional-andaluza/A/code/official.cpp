#include <array>
#include <iostream>
#include <string>
#include <unordered_map>

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
    case 'r': return "\u265A";  // ♚
    case 'd': return "\u265B";  // ♛
    case 't': return "\u265C";  // ♜
    case 'a': return "\u265D";  // ♝
    case 'c': return "\u265E";  // ♞
    case 'p': return "\u265F";  // ♟
    default: return nullptr;
  }
}

static const char *empty_square(int file_idx, int rank_idx) {
  // a1 is dark.
  bool dark = ((file_idx + rank_idx) % 2 == 0);
  return dark ? "\u25FC" : "\u25FB";  // ◼ y ◻
}

int main() {
  std::ios::sync_with_stdio(false);
  std::cin.tie(nullptr);

  int T;
  if (!(std::cin >> T)) return 0;

  for (int tc = 0; tc < T; ++tc) {
    int P;
    std::cin >> P;

    // Memory: map square id -> piece.
    // Square id is 0..63 with id = rank*8 + file, where rank=0 is '1' and file=0 is 'a'.
    std::unordered_map<int, const char *> memory;
    memory.reserve(static_cast<size_t>(P) * 2);

    for (int i = 0; i < P; ++i) {
      std::string piece, pos;
      std::cin >> piece >> pos;
      int file_idx = pos[0] - 'a';
      int rank_idx = pos[1] - '1';
      int sq_id = rank_idx * 8 + file_idx;

      memory[sq_id] = piece_utf8(piece[0]);
    }

    // Build the 64 squares.
    std::array<const char *, 64> squares{};
    for (int rank_idx = 0; rank_idx < 8; ++rank_idx) {
      for (int file_idx = 0; file_idx < 8; ++file_idx) {
        int sq_id = rank_idx * 8 + file_idx;
        auto it = memory.find(sq_id);
        squares[sq_id] = (it != memory.end()) ? it->second : empty_square(file_idx, rank_idx);
      }
    }

    // Print from rank 8 down to 1.
    for (int rank_idx = 7; rank_idx >= 0; --rank_idx) {
      for (int file_idx = 0; file_idx < 8; ++file_idx) {
        std::cout << squares[rank_idx * 8 + file_idx];
        if (file_idx != 7) std::cout << ' ';
      }
      std::cout << '\n';
    }

    if (tc != T - 1) std::cout << '\n';
  }
  return 0;
}
