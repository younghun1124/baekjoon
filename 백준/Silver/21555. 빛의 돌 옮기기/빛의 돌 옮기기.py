n, k=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
d=[[0]*2 for _ in range(n)]
d[0][0]=A[0]
d[0][1]=B[0]
for i in range(1,n):
    d[i][0]=min(d[i-1][0]+A[i],d[i-1][1]+A[i]+k)
    d[i][1]=min(d[i-1][1]+B[i],d[i-1][0]+B[i]+k)
print(min(d[n-1]))