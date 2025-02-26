import sys
from heapq import heappush, heappop
INF=int(1e9)
def dijkstra(start,end):
    D=[INF]*(N+1)
    D[start]=0
    q=[]
    heappush(q,(0,start))
    while q:
        w,node=heappop(q)
        if w>D[node]:
            continue
        for n_w, n_node in graph[node]:
            cost=D[node]+n_w
            if cost<D[n_node]:
                D[n_node]=cost
                heappush(q,(n_w,n_node))
    return D[end]


input=sys.stdin.readline
N,E=map(int,input().split())
graph=[list() for _ in range(N+1)]
for _ in range(E):
    a,b,c=map(int,input().split())
    graph[a].append((c,b))
    graph[b].append((c,a))
v1,v2=map(int,input().split())

one_v1=dijkstra(1,v1)
one_v2=dijkstra(1,v2)
v1_v2=dijkstra(v1,v2)
v1_N=dijkstra(v1,N)
v2_N=dijkstra(v2,N)
ans=INF
ans=min(one_v1+v2_N,one_v2+v1_N)+v1_v2
if ans>=INF:
    print(-1)
else:
    print(ans)