def solve():
    t = int(input())

    for _ in range(t):
        c = int(input())
        s = input().strip()

        inside = 0
        ok = True

        for ch in s:
            if ch == 'E':
                inside += 1
                if inside > c:
                    ok = False
                    break
            else:  # ch == 'S'
                if inside == 0:
                    ok = False
                    break
                inside -= 1

        if inside != 0:
            ok = False

        print("VALIDO" if ok else "INVALIDO")


solve()