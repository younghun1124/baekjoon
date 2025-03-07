import sys
from collections import deque
input=sys.stdin.readline

K=int(input())
W,H=map(int,input().split())
dxh=[-2,-1,1,2,2,1,-1,-2]
dyh=[1,2,2,1,-1,-2,-2,-1]
dx=[-1,1,0,0]
dy=[0,0,-1,1]

board=[ list(map(int,input().split())) for _ in range(H)]
INF=int(1e9)
visit=[ [[INF]*(K+1) for _ in range(W)] for _ in range(H)]
def bfs():
    
    dq=deque([(0,0,K)]) #x,y,점프 남은횟수
    visit[0][0][K]=0
    while dq:
        x,y,h=dq.popleft()
        if h!=0:
            for i in range(8):
                nx,ny=dxh[i]+x,dyh[i]+y
                if 0<=nx<H and 0<=ny<W:
                    if board[nx][ny]==0 and visit[nx][ny][h-1]>visit[x][y][h]+1:
                        visit[nx][ny][h-1]=visit[x][y][h]+1
                        dq.append((nx,ny,h-1))
        for i in range(4):
            nx,ny=dx[i]+x,dy[i]+y
            if 0<=nx<H and 0<=ny<W:
                if board[nx][ny]==0 and visit[nx][ny][h]>visit[x][y][h]+1:
                    visit[nx][ny][h]=visit[x][y][h]+1
                    dq.append((nx,ny,h))
bfs()
ans=min(visit[-1][-1])
if ans==INF:
    print(-1)
else:
    print(ans)