import sys
from collections import deque
from itertools import combinations
import copy
input=sys.stdin.readline
N,M=map(int,input().split())
board=[list(map(int,input().split())) for _ in range(N)]
virus=[]
empty=[]
dx=[-1,1,0,0]
dy=[0,0,1,-1]
for i in range(N):
    for j in range(M):
        if board[i][j]==0:
            empty.append((i,j))
        elif board[i][j]==2:
            virus.append((i,j))
def bfs(wall):
    global ans
    dq=deque(virus)
    tempboard=copy.deepcopy(board)
    for x,y in wall:
        tempboard[x][y]=1 #벽 세우기
    visit=[[False]*M for _ in range(N)]
    while dq:
        x,y=dq.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<N and 0<=ny<M:
                if visit[nx][ny]==False and tempboard[nx][ny]==0:
                    visit[nx][ny]=True
                    tempboard[nx][ny]=2
                    dq.append((nx,ny))
    safearea=0
    for row in tempboard:
        safearea+=row.count(0)
    if ans<safearea:
        ans=safearea
ans=0
for wall in combinations(empty,3):
    bfs(wall)
print(ans)