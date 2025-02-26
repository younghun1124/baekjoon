import sys
from heapq import heappop,heappush
input=sys.stdin.readline
n=int(input().strip())
m=int(input().strip())
graph=[list() for _ in range(n+1)]
for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((c,b))
hist=[0]*(n+1)
INF=int(1e18)
D=[INF]*(n+1)
def dijkstra(start):    
    q=[]    
    D[start]=0
    heappush(q,(0,start))
    
    while q:
        w,node=heappop(q)
        if w>D[node]:
            continue
        for n_w, n_node in graph[node]:
            cost=n_w+D[node]
            if cost<D[n_node]:
                heappush(q,(cost,n_node))
                D[n_node]=cost
                hist[n_node]=node #어떤 노드에서 도착했는지 쓰기
start,end=map(int,input().split())

dijkstra(start)
print(D[end])

cur=end
ans=[end]
while True:
    cur=hist[cur]
    ans.insert(0,cur)
    if cur==start:
        break
print(len(ans))
print(' '.join(map(str,ans)))