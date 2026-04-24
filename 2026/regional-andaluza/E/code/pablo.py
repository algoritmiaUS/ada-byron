n = int(input())

count = 0

while n != 6174:
    s = str(n).zfill(4)
    mx = int("".join(sorted(s, reverse=True)))
    mn = int("".join(sorted(s)))
    n = mx - mn
    count += 1

print(count)