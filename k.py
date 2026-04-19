from collections import defaultdict

def shift(s):
    x = list(s)
    for i in range(len(s)):
        if x[i] == "z":
            x[i] = "a"
        else:
            x[i] = chr(ord(x[i])+1)
        
    return "".join(x)
    
n = int(input())
s = list(input().split())

graph = defaultdict(list)

for i in range(n): 
    graph[len(s[i])].append(s[i])
    
    
m = int(input())
output = set()

for _ in range(m):
    text = input()
    for i in range(0, 26):
        if text in graph[len(text)]:
            output.add(i)
        text = shift(text)   
    
    if len(output) == 0 or len(output) > 1:
        break
    
if len(output)!=1:
    print(-1)
else:
    print(output.pop())
    
    
"""from collections import defaultdict, Counter

def shift(s):
    x = list(s)
    for i in range(len(s)):
        if x[i] == "z":
            x[i] = "a"
        else:
            x[i] = chr(ord(x[i])+1)
        
    return "".join(x)
    
n = int(input())
s = list(input().split())

graph = defaultdict(list)

for i in range(n): 
    graph[len(s[i])].append(s[i])

concerned = set()
but = set()
but2 = []
m = int(input())
for _ in range(m):
    text = input()
    concerned.update(graph[len(text)])
    but.add(text)
    but2.append(text)

s=0
for text in but:
    s+=len(graph[len(text)])
results = []
results = []
ok = False
for i in range(0, 26):
    concerned = set(concerned)
    k = concerned.intersection(but)
    if len(k) == len(but) and len(but2) == s:
        results.append((26-i)%26)
    
    concerned = list(concerned)
    for i in range(len(concerned)):
        concerned[i] = shift(concerned[i])

if len(results) != 1:
    print(-1)  
else:
    print(results[0])
    
        
    
    
    
"""