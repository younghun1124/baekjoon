import sys
from collections import deque
from itertools import combinations
input=sys.stdin.readline
N,M=map(int,input().split())
board=[list(map(int,input().split())) for _ in range(N)]
virus=[]
empty=[]
for i in range(N):
    for j in range(M):
        if board[i][j]==0:
            empty.append((i,j))
        elif board[i][j]==2:
            virus.append((i,j))
def bfs():
    dq=deque(virus)
    visit=[[0]*M for _ in range(N)]
    while dq:

for wall in combinations(empty,3):
    for x,y in wall:
        board[x][y]=1
    bfs()
    for x,y in wall:
        board[x][y]=0 #원래대로 돌려두기
