import bisect
from collections import Counter

n , q = map(int, input().split())
a = list(map(int, input().split()))
cnt = Counter(a)

a.sort()

        
for _ in range(q):
    y,x = map(int, input().split())
    
    if y == 1:
        print(cnt[x])
    elif y == 2:
        index = bisect.bisect_left(a, x)
        for i in range(index, n):
            if a[i] > x:
                d = cnt[a[i]]
                cnt[a[i]] = 0
                a[i] -= x
                cnt[a[i]] += d