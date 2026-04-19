def solve():
    s = input().strip()
    motifs = input().split()
    k = int(input())

    # Motivos distintos, porque piden k motivos diferentes
    unique = []
    seen = set()
    for w in motifs:
        if w not in seen:
            seen.add(w)
            unique.append(w)

    motifs = unique
    m = len(motifs)

    if k == 0:
        print(0)
        return

    if k > m:
        print(0)
        return

    # ---------- Aho-Corasick ----------
    nexts = [{}]
    fail = [0]
    out = [[]]

    lengths = []

    for idx, w in enumerate(motifs):
        lengths.append(len(w))
        node = 0
        for ch in w:
            if ch not in nexts[node]:
                nexts[node][ch] = len(nexts)
                nexts.append({})
                fail.append(0)
                out.append([])
            node = nexts[node][ch]
        out[node].append(idx)

    from collections import deque

    q = deque()
    for ch, v in nexts[0].items():
        q.append(v)

    while q:
        u = q.popleft()
        for ch, v in nexts[u].items():
            f = fail[u]
            while f and ch not in nexts[f]:
                f = fail[f]
            fail[v] = nexts[f][ch] if ch in nexts[f] else 0
            out[v].extend(out[fail[v]])
            q.append(v)

    # occurrences_by_color[c] = lista de inicios de ese motivo
    occurrences_by_color = [[] for _ in range(m)]
    all_occ = []   # (start, color)

    node = 0
    for i, ch in enumerate(s):
        while node and ch not in nexts[node]:
            node = fail[node]
        if ch in nexts[node]:
            node = nexts[node][ch]
        else:
            node = 0

        for idx in out[node]:
            start = i - lengths[idx] + 1
            occurrences_by_color[idx].append(start)
            all_occ.append((start, idx))

    # Cuántos motivos aparecen al menos una vez
    present = sum(1 for lst in occurrences_by_color if lst)
    if present < k:
        print(0)
        return

    all_occ.sort()

    # ptr[c] = primera ocurrencia de c aún disponible en el sufijo actual
    ptr = [0] * m

    INF = 10**18
    ans = INF

    for start, color in all_occ:
        # Evaluamos usar este start como extremo izquierdo L
        ends = []
        for c in range(m):
            if ptr[c] < len(occurrences_by_color[c]):
                st = occurrences_by_color[c][ptr[c]]
                ends.append(st + lengths[c] - 1)

        if len(ends) >= k:
            ends.sort()
            R = ends[k - 1]
            ans = min(ans, R - start + 1)

        # Quitamos esta ocurrencia del sufijo
        if ptr[color] < len(occurrences_by_color[color]) and occurrences_by_color[color][ptr[color]] == start:
            ptr[color] += 1

    print(0 if ans == INF else ans)


solve()