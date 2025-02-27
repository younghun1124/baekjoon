import sys
input=sys.stdin.readline
N=int(input())
item=[0]+[list(map(int,input().split())) for _ in range(N)]
D=[0]*(N+1)
for i in range(1,N+1):
    D[i]=max(D[i-1],D[i])
    t,p=item[i]
    end=t+i-1
    if end<=N:
        D[end]=max(D[end],D[i-1]+p)
print(D[N])