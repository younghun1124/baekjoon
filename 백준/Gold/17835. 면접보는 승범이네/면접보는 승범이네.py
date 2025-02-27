from heapq import heappush, heappop
import sys
input=sys.stdin.readline
N,M,K=map(int,input().split())
graph=[list() for _ in range(N+1)]
for _ in range(M):
    a,b,c=map(int,input().split())
    graph[b].append((c,a)) #시간초과때문에 면접장->도시로 탐색할건데, 그럼 방향이 반대니까 그래프 입력 받을때도 반대로 하기. 이래도 되나보네..
Klist=list(map(int,input().split()))
INF=int(1e18)

D=[INF]*(N+1)
D[0]=0

def djikstra():
    q=[]
    for start in Klist:
        D[start]=0
        heappush(q,(0,start))
    while q:
        w,node=heappop(q)
        if w>D[node]:
            continue
        for n_w, n_node in graph[node]:
            cost=n_w+D[node]
            if D[n_node]>cost:
                
                heappush(q,(cost,n_node))
                D[n_node]=cost

djikstra()
maxdist=max(D)
maxnode=D.index(maxdist)
    
print(maxnode)
print(maxdist)