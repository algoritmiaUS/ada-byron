def can_form_teams(n, rivalries):
    # Crear un diccionario de adyacencia para el grafo
    graph = [[] for _ in range(n + 1)]
    for u, v in rivalries:
        graph[u].append(v)
        graph[v].append(u)
    
    # Colores asignados, -1 significa no coloreado
    color = [-1] * (n + 1)

    def dfs(node, c):
        # Asignar el color al nodo
        color[node] = c
        # Intentar colorear los vecinos con el color opuesto
        for neighbor in graph[node]:
            if color[neighbor] == -1:  # Si no está coloreado
                if not dfs(neighbor, 1 - c):
                    return False
            elif color[neighbor] == c:  # Conflicto de colores
                return False
        return True
    
    for i in range(1, n + 1):
        if color[i] == -1:
            if not dfs(i, 0):
                return False
    
    return True

num_cases = int(input())

for _ in range(num_cases):
    n, m = map(int, input().split())
    rivalries = []
    for _ in range(m):
        u, v = map(int, input().split())
        rivalries.append((u, v))
    
    if can_form_teams(n, rivalries):
        print("Que comience la batalla")
    else:
        print("Mejor nos vamos de cena o algo")