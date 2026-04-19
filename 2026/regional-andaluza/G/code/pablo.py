def can(h, k, limit):
    used = 1
    current = 0

    for x in h:
        if current + x <= limit:
            current += x
        else:
            used += 1
            current = x
            if used > k:
                return False

    return True


def solve():
    while True:
        try:
            line = input().strip()
            if not line:
                continue
            n, k = map(int, line.split())
            h = list(map(int, input().split()))
        except EOFError:
            break

        left = max(h)
        right = sum(h)

        while left < right:
            mid = (left + right) // 2
            if can(h, k, mid):
                right = mid
            else:
                left = mid + 1

        print(left)


solve()