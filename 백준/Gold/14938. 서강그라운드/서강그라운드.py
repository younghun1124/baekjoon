import heapq
n,m,r=map(int,input().split())
item=[0]
item.extend(list(map(int,input().split())))
graph=[[]for _ in range(n+1)]
INF=int(1e9)

for _ in range(r):
    a,b,L=map(int,input().split())
    graph[a].append((L,b)) #가중치, 정점 순
    graph[b].append((L,a))
def dijkstra(start):
    D=[INF]*(n+1)
    D[start]=0
    q=[]   
    heapq.heappush(q,(0,start))
    while q:
        dist,node=heapq.heappop(q)
        for next in graph[node]:
            next_w,next_node=next
            if dist>D[node]:
                continue
            cost=next_w+D[node]
            if cost<D[next_node] and cost<=m:
                D[next_node]=cost
                heapq.heappush(q,(cost,next_node))
    return D
def calc_item_sum(D):
    ans=0
    for idx, dist in enumerate(D):
        if dist!=INF:
            ans+=item[idx]
    return ans
ans=0
for i in range(1,n+1):
    ans=max(ans,calc_item_sum(dijkstra(i)))
print(ans)