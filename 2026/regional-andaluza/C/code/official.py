import sys
from bisect import bisect_right
from collections import defaultdict
def kosaraju_scc(adj, radj):
    """Return comp id array for each node (0..n-1). Iterative Kosaraju."""
    n = len(adj)
    vis = bytearray(n)
    order = []

    # 1st pass: order by finish time
    for s in range(n):
        if vis[s]:
            continue
        stack = [(s, 0)]
        vis[s] = 1
        while stack:
            u, idx = stack[-1]
            if idx < len(adj[u]):
                v = adj[u][idx]
                stack[-1] = (u, idx + 1)
                if not vis[v]:
                    vis[v] = 1
                    stack.append((v, 0))
            else:
                order.append(u)
                stack.pop()

    # 2nd pass on reversed graph
    comp = [-1] * n
    cid = 0
    for s in reversed(order):
        if comp[s] != -1:
            continue
        comp[s] = cid
        st = [s]
        while st:
            u = st.pop()
            for v in radj[u]:
                if comp[v] == -1:
                    comp[v] = cid
                    st.append(v)
        cid += 1
    return comp


def check_prefix(k, occ_by_powder, stability_req):
    """
    occ_by_powder[powder] = list of (week, opt) sorted by week, opt in {0(A),1(B)}
    stability_req: list indexed by week 1..N:
        stability_req[i] = (uA_i, uB_i, nA_i, nB_i)  counts for week i
    Return True iff weeks 1..k are feasible.
    """
    if k <= 0:
        return True
    n_nodes = 2 * k
    adj = [[] for _ in range(n_nodes)]
    radj = [[] for _ in range(n_nodes)]

    def add_imp(u, v):
        adj[u].append(v)
        radj[v].append(u)

    def add_excl(l1, l2):
        # not(l1 and l2): l1 -> not l2, l2 -> not l1
        add_imp(l1, l2 ^ 1)
        add_imp(l2, l1 ^ 1)

    # --- (1) Uniqueness constraints (powder used at most once) ---
    # For each powder, take occurrences with week <= k and add pairwise exclusions.
    for lst in occ_by_powder.values():
        # lst is sorted by week
        # find prefix length with week <= k
        # (list length <= 10 by problem guarantee)
        m = 0
        for (w, _) in lst:
            if w <= k:
                m += 1
            else:
                break
        if m <= 1:
            continue
        # map each occurrence to a literal node
        # week w (1-based) -> var idx = w-1, A node = 2*(w-1), B node = 2*(w-1)+1
        lits = []
        for i in range(m):
            w, opt = lst[i]
            base = 2 * (w - 1)
            lits.append(base + opt)

        # pairwise exclusions
        # m <= 10 => at most 45 pairs
        for i in range(m):
            li = lits[i]
            for j in range(i + 1, m):
                add_excl(li, lits[j])

    # --- (2) Stability constraints between consecutive weeks ---
    # If week i has u unstable, then week i+1 must have >=u neutral.
    # This becomes forbidden pairs between choices at i and choices at i+1.
    for i in range(1, k):  # i and i+1 are within prefix
        uA_i, uB_i, nA_i, nB_i = stability_req[i]
        uA_next, uB_next, nA_next, nB_next = stability_req[i + 1]

        # literal nodes for week i
        Ai = 2 * (i - 1)
        Bi = Ai + 1
        # literal nodes for week i+1
        Aj = 2 * i
        Bj = Aj + 1

        # If choose A at i, need >= uA_i neutrals at i+1
        req = uA_i
        if nA_next < req:
            add_excl(Ai, Aj)
        if nB_next < req:
            add_excl(Ai, Bj)

        # If choose B at i, need >= uB_i neutrals at i+1
        req = uB_i
        if nA_next < req:
            add_excl(Bi, Aj)
        if nB_next < req:
            add_excl(Bi, Bj)

    comp = kosaraju_scc(adj, radj)
    for v in range(k):
        if comp[2 * v] == comp[2 * v + 1]:
            return False
    return True


def max_prefix(N, occ_by_powder, stability_req):
    lo, hi = 0, N
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if check_prefix(mid, occ_by_powder, stability_req):
            lo = mid
        else:
            hi = mid - 1
    return lo


# ------------------------------------------------------------
# Reading + building data
# ------------------------------------------------------------

def read_ints():
    return list(map(int, sys.stdin.readline().split()))

def solve():
    T = int(sys.stdin.readline())
    out_lines = []

    for _ in range(T):
        N = int(sys.stdin.readline())
        P, I, Nt = read_ints()

        unstable_ids = set(read_ints()) if I > 0 else set()
        neutral_ids = set(read_ints()) if Nt > 0 else set()

        # For each powder, list occurrences (week, opt) where opt 0=A,1=B
        occ_by_powder = defaultdict(list)

        # We also need counts per week:
        # stability_req[i] = (uA_i, uB_i, nA_i, nB_i)
        stability_req = [(0, 0, 0, 0)] * (N + 1)  # index 0 unused

        # We’ll store shows just to compute counts; occurrences are built directly.
        for week in range(1, N + 1):
            a_line = read_ints()
            b_line = read_ints()

            a_ids = a_line[1:]
            b_ids = b_line[1:]

            # occurrences
            for x in a_ids:
                occ_by_powder[x].append((week, 0))
            for x in b_ids:
                occ_by_powder[x].append((week, 1))

            # counts
            uA = sum(1 for x in a_ids if x in unstable_ids)
            nA = sum(1 for x in a_ids if x in neutral_ids)
            uB = sum(1 for x in b_ids if x in unstable_ids)
            nB = sum(1 for x in b_ids if x in neutral_ids)
            stability_req[week] = (uA, uB, nA, nB)

        # sort occurrences by week (important for quick prefix cutoff)
        for p in occ_by_powder:
            occ_by_powder[p].sort(key=lambda t: t[0])

        ans = max_prefix(N, occ_by_powder, stability_req)
        out_lines.append(str(ans))

    sys.stdout.write("\n".join(out_lines) + "\n")


if __name__ == "__main__":
    solve()
