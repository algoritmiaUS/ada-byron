nums = list(map(int, input().split()))

# Fase 1
s = []

for x in nums:
    if x >= 0:
        s.append(x)
    else:
        k = -x
        if k >= len(s):
            s = []
        else:
            s = s[:-k]

# Fase 2
e = []

for i in range(0, len(s), 4):
    block = s[i:i+4]

    for x in block:
        if x % 2 == 0:
            e.append(x)

    for x in block:
        if x % 2 != 0:
            e.append(x)

if e:
    print(*e)
else:
    print("NOPROCESO")
