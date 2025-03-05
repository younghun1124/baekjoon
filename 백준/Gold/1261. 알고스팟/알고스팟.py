from collections import deque
M,N=map(int,input().split())
INF=int(1e9)
board=[list(map(int,input())) for _ in range(N)]
visit=[[INF]*M for _ in range(N)]
def bfs():
    visit[0][0]=0
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]  
    dq=deque()
    dq.append((0,0)) #0인덱스
    while dq:
        
        x,y=dq.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<N and 0<=ny<M: #방문지가 보드 안쪽
                if visit[nx][ny]>visit[x][y]+board[nx][ny]:#이번 방문이 이전 방문보다 부순 횟수가 적으면
                    visit[nx][ny]=visit[x][y]+board[nx][ny] 
                    dq.append((nx,ny))
bfs()
print(visit[N-1][M-1])