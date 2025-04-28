def dfs(node, adj_list, visited):
    stack = [node]
    size = 0
    while stack:
        current = stack.pop()
        if visited[current]:
            continue
        visited[current] = True
        size += 1
        for neighbor in adj_list[current]:
            if not visited[neighbor]:
                stack.append(neighbor)
    return size

def solve():
    MOD = 10**9 + 7
    
    N, M = [int(x) for x in input().split()]
    
    adj_list = [[] for _ in range(N + 1)]
    visited = [False] * (N + 1)
    
    for _ in range(M):
        u, v = [int(x) for x in input().split()]
        adj_list[u].append(v)
        adj_list[v].append(u)
    
    tent_count = 0
    delegate_ways = 1
    
    for i in range(1, N + 1):
        if not visited[i]:
            component_size = dfs(i, adj_list, visited)
            tent_count += 1
            delegate_ways = (delegate_ways * component_size) % MOD
    
    print(f"{tent_count} {delegate_ways}")

T = int(input())
for _ in range(T):
    solve()