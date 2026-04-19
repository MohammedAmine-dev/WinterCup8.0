from collections import deque


q = int(input())
qu = deque()


for _ in range(q):
    data = list(map(int, input().split()))
    
    if data[0] == 1:
        qu.append(data[1])
    elif data[0] == 2:
        qu.appendleft(data[1])
    elif data[0] == 3:
        for _ in range(data[1]):
            qu.pop()
    elif data[0] == 4:
        for _ in range(data[1]):
            qu.popleft()
    elif data[0] == 5:
        l,r = data[1], data[2]
        k = list(qu)[l:r+1]
        print(sum(k))
        
    