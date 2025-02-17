n=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
ans=0
for _ in range(n):
    sm=101
    smidx=0
    lg=0
    lgidx=0
    for idx, i in enumerate(A):
        if i<sm:
            sm=i
            smidx=idx
    for idx, j in enumerate(B):
        if j>lg:
            lg=j
            lgidx=idx
    ans+=lg*sm
    del A[smidx]
    del B[lgidx]
print(ans)