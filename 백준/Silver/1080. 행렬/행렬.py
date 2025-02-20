n,m=map(int,input().split())
A=[list(map(int,input())) for _ in range(n)]
B=[list(map(int,input())) for _ in range(n)]

def flip(r,c):
    for i in range(r,r+3):
        for j in range(c,c+3):
            A[i][j]=not A[i][j]              
ans=0
for i in range(n-2):
    for j in range(m-2):
        if A[i][j]!=B[i][j]:
            flip(i,j)
            ans+=1
if A != B:
    ans=-1
print(ans)