import sys

sys.setrecursionlimit(1_000_000)
input = sys.stdin.readline


class Node:
    # Para eficiencia de memoria, no usamos un diccionario para los nodos, sino atributos directos.
    # __slots__ = ("left", "right", "sum")
    def __init__(self, left=None, right=None, s=0):
        self.left = left
        self.right = right
        self.sum = s


def build(arr, l, r):
    if l == r:
        return Node(s=arr[l])
    m = (l + r) // 2
    left = build(arr, l, m)
    right = build(arr, m + 1, r)
    return Node(left, right, left.sum + right.sum)


def update(prev, l, r, pos, val):
    if l == r:
        return Node(s=val)

    m = (l + r) // 2
    if pos <= m:
        new_left = update(prev.left, l, m, pos, val)
        return Node(new_left, prev.right, new_left.sum + prev.right.sum)
    else:
        new_right = update(prev.right, m + 1, r, pos, val)
        return Node(prev.left, new_right, prev.left.sum + new_right.sum)


def query(node, l, r, ql, qr):
    if qr < l or r < ql:
        return 0
    if ql <= l and r <= qr:
        return node.sum
    m = (l + r) // 2
    return query(node.left, l, m, ql, qr) + query(node.right, m + 1, r, ql, qr)


def solve():
    n, q = map(int, input().split())
    arr = list(map(int, input().split()))
    roots = [build(arr, 0, n - 1)]

    out = []
    for _ in range(q):
        parts = input().split()
        if parts[0] == "U":
            i = int(parts[1]) - 1
            x = int(parts[2])
            roots.append(update(roots[-1], 0, n - 1, i, x))
        else:
            v = int(parts[1])
            l = int(parts[2]) - 1
            r = int(parts[3]) - 1
            out.append(str(query(roots[v], 0, n - 1, l, r)))

    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    solve()