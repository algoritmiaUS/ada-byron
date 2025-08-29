t = int(input().strip())
for _ in range(t):
    L, K_min, K_max, T_req, U_limit = map(int, input().split())
    s = input().strip()
    
    # Precalcular los prefix sums para cada nucleótido.
    pA = [0] * (L + 1)
    pC = [0] * (L + 1)
    pG = [0] * (L + 1)
    pT = [0] * (L + 1)
    for i in range(L):
        pA[i + 1] = pA[i] + (1 if s[i] == 'A' else 0)
        pC[i + 1] = pC[i] + (1 if s[i] == 'C' else 0)
        pG[i + 1] = pG[i] + (1 if s[i] == 'G' else 0)
        pT[i + 1] = pT[i] + (1 if s[i] == 'T' else 0)
    
    ans = 0
    r = 0
    # Para cada índice de inicio i
    for i in range(L):
        # Aseguramos que r esté al menos en i.
        if r < i:
            r = i
        # Avanzamos r mientras la ventana [i, r] sea válida en cuanto a 'A' y 'T'
        while r < L and (pA[r + 1] - pA[i] < U_limit) and (pT[r + 1] - pT[i] < U_limit):
            r += 1
        # r es el primer índice que viola la condición; la ventana válida es hasta r - 1.
        r_at = r - 1
        # La ventana debe tener al menos longitud K_min.
        if i + K_min - 1 > r_at:
            continue
        # No se consideran ventanas de longitud mayor a K_max.
        R_bound = min(i + K_max - 1, r_at)
        
        # Buscamos de forma lineal el primer índice j en [i+K_min-1, R_bound] que cumpla:
        # al menos T_req nucleótidos 'G' y al menos T_req nucleótidos 'C'.
        j_gc = None
        for j in range(i + K_min - 1, R_bound + 1):
            if (pG[j + 1] - pG[i] >= T_req) and (pC[j + 1] - pC[i] >= T_req):
                j_gc = j
                break
        if j_gc is None:
            continue
        # Todas las ventanas que terminen en índices desde j_gc hasta R_bound son válidas.
        ans += (R_bound - j_gc + 1)
    
    print(ans)