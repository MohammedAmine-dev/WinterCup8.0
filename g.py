def div(x, k):
    s = 0
    while (x % k == 0):
       x /= k
       s += 1
    return s 

n,q = map(int, input().split())
a = list(map(int, input().split()))

prefix_sum_2 = [0] * (n+1)
prefix_sum_5 = [0] * (n+1)

for i in range(1,n+1):
    prefix_sum_2[i] = prefix_sum_2[i-1] + div(a[i-1], 2)
    prefix_sum_5[i] = prefix_sum_5[i-1] + div(a[i-1], 5)

for _ in range(q):
    l,r,k = map(int, input().split())

    d = min(prefix_sum_2[r] - prefix_sum_2[l-1], prefix_sum_5[r] - prefix_sum_5[l-1])
    
    if d >= k:
        print("YES")
    else:
        print("NO")