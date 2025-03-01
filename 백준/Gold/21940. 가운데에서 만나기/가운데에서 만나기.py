import sys
sys.stdin.readline
N,M=map(int,input().split())
INF=int(1e9)
G=[[INF]*(N+1) for _ in range(N+1)]
for _ in range(M):
    a,b,t=map(int,input().split())
    G[a][b]=min(t,G[a][b])
K=int(input())
C=list(map(int,input().split()))
for i in range(N+1):
    G[i][i]=0
def floyd():
    for k in range(1,N+1):
        for i in range(1,N+1):
            for j in range(1,N+1):
                G[i][j]=min(G[i][k]+G[k][j],G[i][j])
                
floyd()
ans=[]
mindist=INF
for x in range(1,N+1):
    dist=0
    for f in C:
        if dist>=INF:
            break
        dist=max(G[f][x]+G[x][f],dist)
    if dist<mindist:
        ans=[x]
        mindist=dist
    elif dist==mindist:
        ans.append(x)
        
print(' '.join(map(str,ans)))