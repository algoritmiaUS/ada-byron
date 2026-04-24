import sys
from array import array

def solve():
    input = sys.stdin.buffer.readline

    n = int(input())

    # Guardamos la matriz de distancias de forma compacta
    dist = []
    for _ in range(n):
        dist.append(array('I', map(int, input().split())))

    # Guardamos la matriz de materiales como bytes
    mats = []
    for _ in range(n):
        mats.append(b''.join(input().split()))

    # Factor de coste por km según material
    # coste = distancia_km * factor
    factor = {
        ord('G'): 1000,
        ord('A'): 250,
        ord('P'): 100,
        ord('L'): 50,
    }

    INF = 10**30
    used = [False] * n
    min_cost = [INF] * n
    min_cost[0] = 0

    total = 0

    for _ in range(n):
        v = -1
        best = INF

        # Elegir el vértice no usado con menor coste de conexión
        for i in range(n):
            if not used[i] and min_cost[i] < best:
                best = min_cost[i]
                v = i

        used[v] = True
        total += best

        # Relajar conexiones desde v
        dist_v = dist[v]
        mats_v = mats[v]

        for u in range(n):
            if not used[u]:
                w = dist_v[u] * factor[mats_v[u]]
                if w < min_cost[u]:
                    min_cost[u] = w

    print(total)

if __name__ == "__main__":
    solve()