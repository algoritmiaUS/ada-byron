def main():
    adn = input().strip()
    motivos = input().strip().split()
    k = int(input().strip())

    m = len(motivos)
    if k > m:
        print(0)
        return

    # Eliminar duplicados por si acaso
    motivos = list(dict.fromkeys(motivos))
    m = len(motivos)
    if k > m:
        print(0)
        return

    # Todas las ocurrencias: (fin, inicio, id_motivo)
    ocurrencias = []

    for idx, motivo in enumerate(motivos):
        start = 0
        while True:
            pos = adn.find(motivo, start)
            if pos == -1:
                break
            ocurrencias.append((pos + len(motivo) - 1, pos, idx))
            start = pos + 1  # permitir solapamientos

    if not ocurrencias:
        print(0)
        return

    ocurrencias.sort()  # por fin, luego por inicio

    # latest_start[i] = mayor inicio de una ocurrencia del motivo i
    # cuyo fin <= R actual
    latest_start = [-1] * m

    INF = 10**18
    ans = INF

    for r, l, idx in ocurrencias:
        if l > latest_start[idx]:
            latest_start[idx] = l

        activos = [x for x in latest_start if x != -1]
        if len(activos) >= k:
            activos.sort(reverse=True)
            L = activos[k - 1]   # el k-ésimo mayor inicio
            ans = min(ans, r - L + 1)

    print(0 if ans == INF else ans)


if __name__ == "__main__":
    main()
