from sys import stdin
from collections import deque
input=stdin.readline
n,m= list(map(int, input().split()))
board=[list(map(int,input().split())) for _ in range(n)]
visit=set()
dq=deque() 
size=[0,]
def bfs(start_x, start_y):
   dx=[-1,1,0,0]
   dy=[0,0,-1,1]
   dq.append((start_x,start_y))
   visit.add((start_x,start_y))
   size.append(1)
   while(dq):
    x,y=dq.popleft()
    for i in range(4):
        nx= x+dx[i]
        ny= y+dy[i]
        if 0<=nx<n and 0<=ny<m:
            if (nx,ny) not in visit and board[nx][ny]==1:
                dq.append((nx,ny))
                visit.add((nx,ny))
                size[-1]=size[-1]+1
def sol():
    for i in range(n):
        for j in range(m):
            if (i,j) not in visit and board[i][j]==1:
                
                bfs(i,j)
sol()
print(len(size)-1)
print(max(size))