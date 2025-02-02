from collections import deque
n=int(input())
t=int(input())
graph=[[] for _ in range(n+1)]
for _ in range(t):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
link=set()
dq=deque()
dq.append(1)
link.add(1)
for i in range(n+1):
    while dq:
        x=dq.popleft()
        for i in graph[x]:
            if i in link:
                continue
            dq.append(i)
            link.add(i)
print(len(link)-1)