from heapq import heappop, heappush
import sys
input=sys.stdin.readline
N,M,X=map(int,input().split())
INF=int(1e11)
graph=[list() for _ in range(N+1)]
for _ in range(M):
    a,b,c=map(int,input().split())
    graph[a].append((c,b))
def djikstra(start,end):
    q=[]
    D=[INF]*(N+1)
    D[start]=0
    heappush(q,(0,start))    
    while q:
        w,node=heappop(q)
        if w>D[node]:
            continue
        for n_w, n_node in graph[node]:
            cost= n_w+D[node]
            if cost<D[n_node]:
                D[n_node]=cost
                heappush(q,(cost,n_node))
    return D[end]
ans=0
for start in range(1,N+1):
    ans=max(djikstra(start,X)+djikstra(X,start), ans)
print(ans)