def solve():
    s = input().strip()
    motifs = list(dict.fromkeys(input().split()))
    k = int(input())

    n = len(s)
    ans = float('inf')
    right = 0

    for left in range(n):
        while right < n:
            sub = s[left:right+1]
            cnt = 0
            for w in motifs:
                if w in sub:
                    cnt += 1
            if cnt >= k:
                ans = min(ans, right - left + 1)
                break
            right += 1

        if right == n:
            break

    print(0 if ans == float('inf') else ans)

solve()