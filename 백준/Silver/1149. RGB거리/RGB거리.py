n=int(input())
c=[list(map(int,input().split())) for _ in range(n)]
d=[[0]*3 for _ in range(n)]
d[0]=c[0]
for i in range(1,n):
    d[i][0]=min(d[i-1][1],d[i-1][2])+c[i][0]
    d[i][1]=min(d[i-1][0],d[i-1][2])+c[i][1]
    d[i][2]=min(d[i-1][0],d[i-1][1])+c[i][2]
print(min(d[n-1]))