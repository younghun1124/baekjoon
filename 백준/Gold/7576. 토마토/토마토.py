from collections import deque
from sys import stdin
input=stdin.readline
m,n = list(map(int,input().split()))
board=[list(map(int,input().split())) for _ in range(n)]
dist=[[-1]*m for _ in range(n)]
def dfs():
       dq=deque()       
       for i in range(n):
            for j in range(m):
                if board[i][j]==1:
                    dq.append((i,j))
                    dist[i][j]=0
       
       dx=[-1,1,0,0]
       dy=[0,0,-1,1]
       while dq:
           x,y=dq.popleft()
           for i in range(4):
               nx=dx[i]+x
               ny=dy[i]+y
               if 0<=nx<n and 0<=ny<m and board[nx][ny]!=-1:
                    if dist[nx][ny]==-1:
                        dist[nx][ny]=dist[x][y]+1
                        dq.append((nx,ny))
       ans=0
       for i in range(n):
            for j in range(m):
                if board[i][j]==-1:
                    continue
                elif dist[i][j]==-1:
                    return -1
                else:
                    ans=max(ans,dist[i][j])
       return ans
print(dfs())
                    
                        
                        
                        
        
    