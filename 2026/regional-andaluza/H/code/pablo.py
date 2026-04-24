import sys

def solve(c: int, s: str) -> str:
    inside = 0
    valid = True

    for ch in s:
        if ch == 'E':
            inside += 1
            if inside > c:
                valid = False
                break
        else:  # ch == 'S'
            if inside == 0:
                valid = False
                break
            inside -= 1

    if valid and inside == 0:
        return "VALIDO"
    else:
        return "INVALIDO"

if __name__ == "__main__":
    data = sys.stdin.read().strip().split()
    if not data:
        exit(0)
    
    t = int(data[0])
    idx = 1
    sols = []

    for _ in range(t):
        c = int(data[idx])
        idx += 1
        s = data[idx]
        idx += 1
        sols.append(solve(c,s))
    
    print("\n".join(sols))
