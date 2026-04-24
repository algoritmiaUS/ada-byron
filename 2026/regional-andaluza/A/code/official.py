from __future__ import annotations

import sys

PIECE_TO_UNICODE = {
    "R": "\u2654",  # Rey
    "D": "\u2655",  # Dama
    "T": "\u2656",  # Torre
    "A": "\u2657",  # Alfil
    "C": "\u2658",  # Caballo
    "P": "\u2659",  # Peon
    "r": "\u265a",
    "d": "\u265b",
    "t": "\u265c",
    "a": "\u265d",
    "c": "\u265e",
    "p": "\u265f",
}

LIGHT = "\u25fb"  # ◻ (casilla blanca)
DARK  = "\u25fc"  # ◼ (casilla negra)

def empty_square(file_idx: int, rank_idx: int) -> str:
    # a1 is dark
    return DARK if (file_idx + rank_idx) % 2 == 0 else LIGHT

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    t = int(next(it))
    out_lines = []
    for case in range(t):
        p = int(next(it))
        board: list[list[str | None]] = [[None] * 8 for _ in range(8)]  # rank 0 is "1"
        for _ in range(p):
            piece = next(it).decode("ascii")
            pos = next(it).decode("ascii")
            f = ord(pos[0]) - ord("a")
            r = ord(pos[1]) - ord("1")
            board[r][f] = PIECE_TO_UNICODE[piece]
        for r in range(7, -1, -1):  # 8 down to 1
            row = []
            for f in range(8):
                ch = board[r][f]
                if ch is None:
                    ch = empty_square(f, r)
                row.append(ch)
            out_lines.append(" ".join(row))
        if case != t - 1:
            out_lines.append("")
    out = "\n".join(out_lines) + "\n"
    sys.stdout.buffer.write(out.encode("utf-8"))

if __name__ == "__main__":
    solve()
