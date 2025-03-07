import sys
from itertools import permutations
sys.stdin.readline
N,K=map(int,input().split())
INF=int(1e9)
planet=[x for x in range(N)]
del planet[K]
G=[list(map(int,input().split())) for _ in range(N)]

for k in range(N):
    for i in range(N):
        for j in range(N):
            if G[i][j]>G[i][k]+G[k][j]:
                G[i][j]=G[i][k]+G[k][j]
# for row in G:           
#     print(row)
# visit=[False]*N
ans=INF

for sequence in permutations(planet,N-1):
    prev=K
    # print(sequence)
    temp=0
    for i in sequence:
        # print(G[prev][i])
        temp+=G[prev][i]
        prev=i
    if ans>temp:
        ans=temp
print(ans)    