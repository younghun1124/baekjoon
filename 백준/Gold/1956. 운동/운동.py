import sys
input=sys.stdin.readline
V,E=map(int,input().split())
INF=int(1e7)
G=[[INF]*(V+1) for _ in range(V+1)]
for _ in range(E):
    a,b,c=map(int,input().split())
    G[a][b]=c
    
for i in range(V+1):
    G[i][i]=0

for k in range(1,V+1):
    for i in range(1,V+1):
        for j in range(1,V+1):
            G[i][j]=min(G[i][j],G[i][k]+G[k][j])
ans=INF

for i in range(1,V+1):
    for j in range(1,V+1):
        if i==j:
            continue
        ans=min(G[i][j]+G[j][i],ans)
if ans==INF:
    print(-1)
else : print(ans)