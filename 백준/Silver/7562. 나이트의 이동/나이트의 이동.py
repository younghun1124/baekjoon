from collections import deque
T=int(input())
def bfs():
    visit=[[1e9]*N for _ in range(N)]
    dq=deque()
    dxy=[(-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1)]
    dq.append((startx,starty))
    visit[startx][starty]=0
    while dq:
        x,y=dq.popleft()
        if x==endx and y==endy:
                return visit[x][y]
        for i in range(8):
            nx,ny=dxy[i]
            nx+=x
            ny+=y
            
            if 0<=nx<N and 0<=ny<N:
                if visit[nx][ny]>visit[x][y]+1:
                    dq.append((nx,ny))
                    visit[nx][ny]=visit[x][y]+1
      
for _ in range(T):
    N=int(input())
    startx,starty=map(int,input().split())
    endx,endy=map(int,input().split())
    print(bfs())
    
    