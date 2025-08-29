from collections import deque
import sys
import time

def hopcroft_karp(graph, U, V):
    pairU = {u: None for u in U}
    pairV = {v: None for v in V}
    distance = {}
    
    def bfs():
        queue = deque()
        for u in U:
            if pairU[u] is None:
                distance[u] = 0
                queue.append(u)
            else:
                distance[u] = float('inf')
        distance[None] = float('inf')
        
        while queue:
            u = queue.popleft()
            if distance[u] < distance[None]:
                for v in graph.get(u, []):
                    if distance.get(pairV[v], float('inf')) == float('inf'):
                        distance[pairV[v]] = distance[u] + 1
                        queue.append(pairV[v])
        return distance[None] != float('inf')
    
    def dfs(u):
        if u is not None:
            for v in graph.get(u, []):
                if distance.get(pairV[v], float('inf')) == distance[u] + 1:
                    if dfs(pairV[v]):
                        pairV[v] = u
                        pairU[u] = v
                        return True
            distance[u] = float('inf')
            return False
        return True
    
    matching = 0
    while bfs():
        for u in U:
            if pairU[u] is None:
                if dfs(u):
                    matching += 1
    return matching

def main():
    # Lectura de la entrada
    # La primera línea contiene R y C
    N = int(sys.stdin.readline().strip())
    if not N:
        return
    for _ in range(N):
        line = sys.stdin.readline().strip()
        R, C = map(int, line.split())
        grid = []
        for _ in range(R):
            grid.append(sys.stdin.readline().strip())
        
        # ---------------------------
        # Paso 1: Extraer segmentos horizontales
        # ---------------------------
        horizontal_id = 0
        hseg_map = {}         # Mapea cada celda (i, j) al id de su segmento horizontal.
        horizontal_segments = {}  # Información opcional del segmento (fila, inicio, fin).
        
        for i in range(R):
            j = 0
            while j < C:
                if grid[i][j] == 'X':  # Pared.
                    j += 1
                else:
                    start = j
                    while j < C and grid[i][j] != 'X':
                        hseg_map[(i, j)] = horizontal_id
                        j += 1
                    horizontal_segments[horizontal_id] = (i, start, j - 1)
                    horizontal_id += 1
        
        # ---------------------------
        # Paso 2: Extraer segmentos verticales
        # ---------------------------
        vertical_id = 0
        vseg_map = {}         # Mapea cada celda (i, j) al id de su segmento vertical.
        vertical_segments = {}  # Información opcional del segmento (columna, inicio, fin).
        
        for j in range(C):
            i = 0
            while i < R:
                if grid[i][j] == 'X':
                    i += 1
                else:
                    start = i
                    while i < R and grid[i][j] != 'X':
                        vseg_map[(i, j)] = vertical_id
                        i += 1
                    vertical_segments[vertical_id] = (j, start, i - 1)
                    vertical_id += 1
        
        # ---------------------------
        # Paso 3: Construir el grafo bipartito a partir de los puestos de estudio ("T")
        # Cada "T" se encuentra en la intersección de un segmento horizontal y uno vertical.
        # Creamos una arista entre el segmento horizontal y el vertical correspondientes.
        # ---------------------------
        graph = {}
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 'T':
                    h_id = hseg_map[(i, j)]
                    v_id = vseg_map[(i, j)]
                    if h_id not in graph:
                        graph[h_id] = []
                    graph[h_id].append(v_id)
        for h_id in graph:
            graph[h_id] = list(set(graph[h_id]))
        
        U = list(range(horizontal_id))
        V = list(range(vertical_id))
        
        # ---------------------------
        # Paso 4: Calcular el emparejamiento máximo (y por König, el mínimo número de faroles)
        # ---------------------------
        max_matching = hopcroft_karp(graph, U, V)
        
        print(max_matching)
        

if __name__ == "__main__":
    main()