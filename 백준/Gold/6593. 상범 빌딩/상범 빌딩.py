import sys
from collections import deque
input=sys.stdin.readline
dx=[-1,1,0,0,0,0]
dy=[0,0,-1,1,0,0]
dz=[0,0,0,0,-1,1]
def bfs(sz,sx,sy):
    visit=[[[-1]*C for _ in range(R)] for _ in range(L)]
    visit[sz][sx][sy]=0
    dq=deque([(sz,sx,sy)])
    while dq:
        z,x,y=dq.popleft()
        for i in range(6):
            nz=z+dz[i]  
            nx=x+dx[i]  
            ny=y+dy[i]
            if 0<=nx<R and  0<=ny<C and 0<=nz<L:
                if (visit[nz][nx][ny]==-1 or visit[nz][nx][ny]>visit[z][x][y]+1) and B[nz][nx][ny]!='#':
                    
                    dq.append((nz,nx,ny))
                    visit[nz][nx][ny]=visit[z][x][y]+1
    for z in range(L):
        for x in range(R):
            for y in range(C):
                if B[z][x][y]=='E':
                    return visit[z][x][y]
while True:
    L,R,C=map(int,input().split())
    if L==0 and R==0 and C==0:
        break
    B=[0]*L
    for i in range(L):
        B[i]=[input().strip() for _ in range(R)] #[층][행][열]
        input()
    for z in range(L):
        for x in range(R):
            for y in range(C):
                if B[z][x][y]=='S':
                    ans=bfs(z,x,y)
                    if ans==-1:
                        print("Trapped!")
                    else: print(f"Escaped in {ans} minute(s)." )