import heapq
from collections import defaultdict
N,E= map(int,input().split())
board=defaultdict(list)
for _ in range(E):
    a,b,c= map(int,input().split())
    board[a].append((c,b)) #거리, 정점 순
    board[b].append((c,a))

v1,v2= map(int,input().split())
q=[]
INF=int(1e9)

def dstra(start,end):
    D=[INF]*(N+1)
    D[start]=0
    heapq.heappush(q,(0,start))
    while q:
        w,node=heapq.heappop(q)
        if w>D[node]: #이미 너무 느려진 간선 버리기
            continue
        for n_w,n_node in board[node]: 
            cost=n_w+D[node]
            if D[n_node]>cost:
                heapq.heappush(q,(n_w,n_node))
                D[n_node]=cost
    
    return D[end]

start_to_v1=dstra(1,v1)
start_to_v2=dstra(1,v2)
v1_to_v2=dstra(v1,v2)
v1_to_end=dstra(v1,N)
v2_to_end=dstra(v2,N)
ans=min(start_to_v1+v2_to_end,start_to_v2+v1_to_end)+v1_to_v2  
if ans>=INF:
    print(-1)
else :print(ans)
        