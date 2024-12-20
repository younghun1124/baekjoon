n=int(input())
dist=[list(map(int,input().split()))for _ in range(n)]

for i in range(n):
    for j in range(n):
        if dist[i][j]==-1:
            dist[i][j]=float("inf")

for k in range(n):
    for i in range(n):
        if i==k:
            continue
        for j in range(n):
            if j!=k or j!=i:
                dist[i][j]=min(dist[i][k]+dist[k][j],dist[i][j])
            
for row in dist:
    print(" ".join(map(str,row)))