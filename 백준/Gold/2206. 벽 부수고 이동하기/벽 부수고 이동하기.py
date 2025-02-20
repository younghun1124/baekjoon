import sys
from collections import deque
input=sys.stdin.readline
n,m=map(int,input().split())
board=[list(map(int,input().strip())) for _ in range(n)]
visit=[   [[float("inf")]*2 for _ in range(m)] for _ in range(n)]


def bfs():    
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    dq=deque()
    dq.append((0,0,0))
    visit[0][0][0]=1
    while dq:
        x,y,smash=dq.popleft()
        
        for i in range(4):
            nx,ny=dx[i]+x,dy[i]+y
            if 0<=nx<n and 0<=ny<m:
                
                if board[nx][ny]==0 and visit[nx][ny][smash]>visit[x][y][smash]+1:
                    dq.append((nx,ny,smash))
                    visit[nx][ny][smash]=visit[x][y][smash]+1
                    
                elif board[nx][ny]==1 and smash==0 and visit[nx][ny][1]>visit[x][y][0]+1:
                    dq.append((nx,ny,smash+1))
                    visit[nx][ny][1]=visit[x][y][0]+1
                    
bfs()

print(min(visit[n-1][m-1]) if min(visit[n-1][m-1])!=float("inf") else -1)