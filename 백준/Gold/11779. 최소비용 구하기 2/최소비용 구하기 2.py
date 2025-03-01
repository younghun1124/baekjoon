import sys
from heapq import heappop, heappush
input=sys.stdin.readline
n=int(input())
m=int(input())
INF=int(1e9)
G=[list() for _ in range(n+1)] 
D=[INF]*(n+1)
pre=[0]*(n+1)
for _ in range(m):
    a,b,c=map(int,input().split())
    G[a].append((c,b))
start,end=map(int,input().split())
def dijkstra(start):
    D[start]=0
    q=[]
    heappush(q,(0,start))
    while q:
        w,node=heappop(q)
        if w>D[node]:
            continue
        for n_w,n_node in G[node]:
            cost=n_w+D[node]
            if cost<D[n_node]:
                D[n_node]=cost
                heappush(q,(cost,n_node))
                pre[n_node]=node
dijkstra(start)
print(D[end])
i=end
way=[]
while True:
    way.append(i)
    if i==start:
        break
    i=pre[i]
print(len(way))
way.reverse()
print(' '.join(map(str,way)))