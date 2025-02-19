import heapq
import sys
input=sys.stdin.readline
output=sys.stdout.write
V,E=map(int,input().split())
start=int(input().strip())
D=[float("inf")]*(V+1)
graph=[[]for _ in range(V+1)]
for _ in range(E):
    u,v,w=map(int,input().split())    
    graph[u].append((v,w))

def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    D[start]=0
    while q:
        dist, node=heapq.heappop(q)
        for next in graph[node]:
            if dist>D[node]:#이미 도달한 경우
                continue
            cost=next[1]+D[node]
            if cost<D[next[0]]:
                D[next[0]]=cost
                heapq.heappush(q,(cost,next[0]))
dijkstra(start)
for i in D[1:]:
    if i==float("inf"):
        output('INF\n')
    else:
        output(f"{i}\n")