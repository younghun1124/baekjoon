from collections import deque
n=int(input())
board=[list(map(int,input().split())) for _ in range(n)]
dx=[-1,1,0,0]
dy=[0,0,-1,1]
def bfs(startx,starty,h):

    dq=deque([(startx,starty)])
    visit[startx][starty]=True
    while dq:
        x,y=dq.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n:
                if visit[nx][ny]==False and board[nx][ny]>h: #아직 방문안했고 안전구역이면
                    dq.append((nx,ny))
                    visit[nx][ny]=True
ans=0
for h in range(101):
    visit=[[False]*n for _ in range(n)]
    tempcount=0
    for i in range(n):
        for j in range(n):
            if visit[i][j]==False and board[i][j]>h:
                bfs(i,j,h)
                tempcount+=1
    ans=max(tempcount,ans)
print(ans)