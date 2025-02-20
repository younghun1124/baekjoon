#https://www.acmicpc.net/problem/18290
from itertools import combinations
N,M,K=map(int,input().split())
board=[list(map(int,input().split())) for _ in range(N)]
idxs=[(r,c) for r in range(N) for c in range(M)]

def isclose(comb): 
    for i,j in combinations(comb,2):
        r,c=i
        if j==(r-1,c) or j==(r+1, c) or j==(r, c-1)or j==(r, c+1):
            return True
    return False
ans=-60000
for comb in combinations(idxs,K):
    
    if not isclose(comb):
        tempans=0
        for r,c in comb:
            tempans+=board[r][c]
        ans=max(tempans,ans)
print(ans)

# def backt(r,c,depth):
#     global ans
#     if depth==K:
#         ans=max(sum(select),ans)
#         return
    
#     for i in range(N):
#         for j in range(c,M+1):
    