"""
Get-Content K/a.in | ./la_receta_definitiva.py > K/out/a.out
"""

from math import dist


class UnionFind:

    def __init__(self, size: int):
        self.parent = list(range(size))

    def find(self, node: int):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, node1: int, node2: int):
        """
        Join the connected components of `node1` and `node2`.

        Returns `True` if they were not already connected, `False`
        otherwise.
        """

        root1 = self.find(node1)
        root2 = self.find(node2)

        if root1 != root2:
            self.parent[root2] = root1
            return True
        else:
            return False


def read_int():
    return int(input())


def read_ints():
    return map(int, input().split())


def binary_search(
    sorted_distances: list[float],
    lower_bound: int,
    upper_bound: int,
    is_feasible,
):
    # print(lower_bound)  # TEMP Debug
    # print(upper_bound)  # TEMP Debug

    left = lower_bound
    right = upper_bound

    # patata = 7  # TEMP Debug

    used_edges = None  # TEMP Debug
    last_feasible = None  # TEMP Debug
    while right - left > 0:
        mid = (left + right) // 2
        # print(left, right, mid)  # TEMP Debug
        (
            feasible,
            used_edges_,  # TEMP Debug
        ) = is_feasible(sorted_distances[mid])

        # print(f"{left=} {right=} {feasible=}", flush=True)  # TEMP Debug
        # patata -= 1  # TEMP Debug
        # if patata == 0:  # TEMP Debug
        #     exit()  # TEMP Debug

        if feasible:
            right = mid
            used_edges = used_edges_  # TEMP Debug
            last_feasible = mid
        else:
            left = mid + 1

    if last_feasible is None:
        raise Exception("Cagada en la búsqueda binaria")  # TEMP Debug

    return (
        sorted_distances[last_feasible],
        used_edges,  # TEMP Debug
    )


def maximal_spanning_tree(
    n_nodes: int,
    edges: list[tuple[int, int, int]],
):
    """
    The function returns the weight of the maximal spanning tree by
    following Kruskal's algorithm.

    `edges` is a list of tuples of the form (weight, node1, node2).

    If the graph is not connected, return -1, otherwise return the
    weight of the maximal spanning tree.
    """
    used_edges = []  # TEMP Debug

    uf = UnionFind(n_nodes)

    edges.sort(reverse=True)
    max_tree_weight = 0
    for v, a, b in edges:
        if uf.union(a, b):
            max_tree_weight += v
            used_edges.append((a, b))  # TEMP Debug

    roots = {uf.find(i) for i in range(n_nodes)}
    if len(roots) > 1:
        return (
            -1,
            [],  # TEMP Debug
        )

    return (
        max_tree_weight,
        used_edges,  # TEMP Debug
    )


def is_feasible(
    views: dict[tuple[int, int], int],
    distances: list[list[float]],
    max_distance: float,
    s: int,
):
    """
    Check if the constraints can be satisfied for the given distance.

    Returns a tuple with the first element being a boolean indicating
    whether the constraints can be satisfied, and the second element
    indicating the number of edges in the original graph.
    """

    n = len(distances)
    edges = [
        (views.get((i, j), 0), i, j)
        for i in range(n)
        for j in range(i + 1, n)
        if distances[i][j] <= max_distance
    ]

    # res = s <= maximal_spanning_tree(n, edges)  # TEMP Debug
    # print(f"{max_distance=} {s=} {res=} n_edges={len(edges)}")  # TEMP Debug

    res = maximal_spanning_tree(n, edges)  # TEMP Debug

    return s <= res[0], res[1]  # TEMP Debug


t = read_int()
for iter in range(t):
    n, x, y = read_ints()
    s = read_int()

    nodes = [(x, y)]
    for _ in range(n):
        a, b = read_ints()
        nodes.append((a, b))

    min_distance = float("inf")
    max_distance = 0
    distances: list[list[float]] = [
        [0] * (n + 1) for _ in range(n + 1)
    ]
    for i in range(n + 1):
        for j in range(i + 1, n + 1):
            distance = dist(nodes[i], nodes[j])
            distances[i][j] = distance

            if distance < min_distance:
                min_distance = distance

            if distance > max_distance:
                max_distance = distance

    m = read_int()
    views = {}
    for _ in range(m):
        a, b, v = read_ints()

        if a < b:
            views[(a, b)] = v
        else:
            views[(b, a)] = v

    feasible, _ = is_feasible(views, distances, max_distance, s)
    if not feasible:
        print("-1.00")
    else:
        sorted_distances = sorted(
            set(
                distances[i][j]
                for i in range(n + 1)
                for j in range(i + 1, n + 1)
            )
        )
        (
            result,
            used_edges,  # TEMP Debug
        ) = binary_search(
            sorted_distances=sorted_distances,
            lower_bound=0,
            upper_bound=len(sorted_distances),
            is_feasible=lambda d: is_feasible(views, distances, d, s),
        )

        # if iter == 1:  # TEMP Debug
        #     print(f"{result:.2f} {used_edges=}")  # TEMP Debug
        print(f"{result:.2f}")
