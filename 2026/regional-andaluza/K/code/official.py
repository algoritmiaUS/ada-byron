from collections import deque

def _bfs(capacity, source, sink, parent):
    queue = deque([source])
    visited = set([source])
    while queue:
        u = queue.popleft()
        for v in range(len(capacity)):
            if v not in visited and capacity[u][v] > 0:
                queue.append(v)
                visited.add(v)
                parent[v] = u
                if v == sink:
                    return True
    return False

def edmonds_karp(capacity, source, sink):
    max_flow = 0
    n = len(capacity)
    parent = [-1] * n

    while _bfs(capacity, source, sink, parent):
        path_flow = float('inf')
        v = sink
        while v != source:
            u = parent[v]
            path_flow = min(path_flow, capacity[u][v])
            v = u

        v = sink
        while v != source:
            u = parent[v]
            capacity[u][v] -= path_flow
            capacity[v][u] += path_flow
            v = u

        max_flow += path_flow

    return max_flow


def solve():
    T = int(input())
    for _ in range(T):
        N,M,K = map(int, input().split())
        V = 2 + M + K
        source = 0
        sink = V-1
        capacity = [[0 for _ in range(V)] for _ in range(V)]
        
        dicc = {}
        id = 0
        characters = input().split()
        for c in characters:
            id+=1
            dicc[c]=id 

        for i in range(1,M+1):
            capacity[source][i] = 1

        for i in range(1,M+1):
            c1,c2 = input().split()
            id1 = dicc[c1]
            id2 = dicc[c2]
            capacity[i][M+id1] = 1
            capacity[i][M+id2] =1

        class_limit = N//K
        for i in range(1,K+1):
            vol_node = M+i
            capacity[vol_node][sink] = class_limit

        flow = edmonds_karp(capacity, source, sink)
        print("YES" if flow==M else "NO")

if __name__ == "__main__":
    solve()