N=int(input())
li=[0]+[list(map(int,input().split())) for _ in range(N)]
D=[0]*(N+1)
for i in range(1,N+1):
    t,p=li[i]
    D[i]=max(D[i-1],D[i])
    end=t+i-1
    if end<=N:
        D[end]=max(D[i-1]+p,D[end])
print(D[-1])