n=int(input())
D=[list(map(int,input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if D[i][j]==-1:
            D[i][j]=float("inf")

for k in range(n):
    for i in range(n):
        for j in range(n):            
            D[i][j]=min(D[i][k]+D[k][j],D[i][j])
for row in D:
    print(" ".join(map(str,row)))
            
            
        

