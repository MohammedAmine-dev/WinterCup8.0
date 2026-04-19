from collections import Counter

n = int(input())
a = list(map(int, input().split()))
cnt = Counter(a)

if n == 1 or cnt[a[0]] == n:
    print(0)
else:
    print(-1)