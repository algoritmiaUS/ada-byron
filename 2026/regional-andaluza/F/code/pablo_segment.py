class Node:
    __slots__ = ('left', 'right', 'sum')
    def __init__(self, left=None, right=None, sum=0):
        self.left = left
        self.right = right
        self.sum = sum


def build(arr, l, r):
    if l == r:
        return Node(sum=arr[l])
    m = (l + r) // 2
    left = build(arr, l, m)
    right = build(arr, m + 1, r)
    return Node(left, right, left.sum + right.sum)


def update(node, l, r, pos, val):
    if l == r:
        return Node(sum=val)

    m = (l + r) // 2
    if pos <= m:
        new_left = update(node.left, l, m, pos, val)
        return Node(new_left, node.right, new_left.sum + node.right.sum)
    else:
        new_right = update(node.right, m + 1, r, pos, val)
        return Node(node.left, new_right, node.left.sum + new_right.sum)


def query(node, l, r, ql, qr):
    if ql <= l and r <= qr:
        return node.sum
    if r < ql or qr < l:
        return 0

    m = (l + r) // 2
    return query(node.left, l, m, ql, qr) + query(node.right, m + 1, r, ql, qr)


N, Q = map(int, input().split())
arr = [0] + list(map(int, input().split()))

roots = [build(arr, 1, N)]

for _ in range(Q):
    parts = input().split()

    if parts[0] == 'U':
        i = int(parts[1])
        x = int(parts[2])
        new_root = update(roots[-1], 1, N, i, x)
        roots.append(new_root)
    else:  # S v l r
        v = int(parts[1])
        l = int(parts[2])
        r = int(parts[3])
        print(query(roots[v], 1, N, l, r))