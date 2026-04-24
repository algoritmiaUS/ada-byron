import sys


def can_partition(h, k, limit):
    used = 1
    current = 0

    for x in h:
        if x > limit:
            return False

        if current + x <= limit:
            current += x
        else:
            used += 1
            current = x
            if used > k:
                return False

    return True


def solve():
    data = sys.stdin.buffer.read().split()
    pos = 0
    out = []

    while pos < len(data):
        n = int(data[pos])
        k = int(data[pos + 1])
        pos += 2

        h = list(map(int, data[pos:pos + n]))
        pos += n

        left = max(h)
        right = sum(h)

        while left < right:
            mid = (left + right) // 2
            if can_partition(h, k, mid):
                right = mid
            else:
                left = mid + 1

        out.append(str(left))

    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    solve()