class Fenwick:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, i, delta):
        while i <= self.n:
            self.bit[i] += delta
            i += i & -i

    def sum(self, i):
        res = 0
        while i > 0:
            res += self.bit[i]
            i -= i & -i
        return res

    def range_sum(self, l, r):
        return self.sum(r) - self.sum(l - 1)


N, Q = map(int, input().split())
initial = [0] + list(map(int, input().split()))  # 1-indexado

# current = valor actual mientras vamos leyendo updates
current = initial[:]

# updates[v] = (idx, delta), para pasar de versión v-1 a versión v
updates = [None]

# como mucho habrá Q versiones
queries = [[] for _ in range(Q + 1)]

answers = []
version = 0

for _ in range(Q):
    parts = input().split()

    if parts[0] == 'U':
        i = int(parts[1])
        x = int(parts[2])

        version += 1
        delta = x - current[i]
        current[i] = x
        updates.append((i, delta))

    else:  # S v l r
        v = int(parts[1])
        l = int(parts[2])
        r = int(parts[3])

        qid = len(answers)
        answers.append(0)
        queries[v].append((l, r, qid))

total_versions = version

fw = Fenwick(N)
for i in range(1, N + 1):
    fw.add(i, initial[i])

for l, r, qid in queries[0]:
    answers[qid] = fw.range_sum(l, r)

for v in range(1, total_versions + 1):
    idx, delta = updates[v]
    fw.add(idx, delta)

    for l, r, qid in queries[v]:
        answers[qid] = fw.range_sum(l, r)

for ans in answers:
    print(ans)