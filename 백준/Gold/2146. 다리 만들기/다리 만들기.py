import sys
import copy
from collections import deque
input=sys.stdin.readline
N=int(input())
board=[list(map(int,input().split())) for _ in range(N)]
dx=[-1,1,0,0]
dy=[0,0,-1,1]
def bfs_set_island(startx,starty,islandnum):
    visit=[[False]*N for _ in range(N)]
    board[startx][starty]=islandnum
    dq=deque()
    dq.append((startx,starty))
    while dq:
        x,y=dq.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<N and 0<=ny<N:
                if board[nx][ny]==1 and visit[nx][ny]==False: #방문한적 없는 새 섬이면
                    board[nx][ny]=islandnum
                    visit[nx][ny]=True
                    dq.append((nx,ny))

def bfs_set_bridge(islandnum):
    visit=[[0]*N for _ in range(N)]
    dq=deque()
    global ans
    for i in range(N):
        for j in range(N):
            if board[i][j]==islandnum:
                dq.append((i,j))
    while dq:
        x,y=dq.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<N and 0<=ny<N:
                # if board[nx][ny]==islandnum:
                #     print(islandnum, nx,ny)
                #     continue #시작섬이랑 같은곳 이면 패스
                if board[nx][ny]==0 and visit[nx][ny]==0:
                    visit[nx][ny]=visit[x][y]+1
                    dq.append((nx,ny))
                elif board[nx][ny]!=islandnum and board[nx][ny]!=0: #새로운 섬 도착, 거리 판별
                    if ans>visit[x][y]:
                        ans=visit[x][y]
    
                    
                   

islandnum=2
for i in range(N):
    for j in range(N):
        if board[i][j]==1:
            bfs_set_island(i,j,islandnum)
            islandnum+=1

ans=int(1e9)
for island in range(2,islandnum):
    bfs_set_bridge(island)
print(ans)