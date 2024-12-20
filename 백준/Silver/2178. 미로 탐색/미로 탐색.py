from sys import stdin
from collections import deque
input=stdin.readline
def sol():
    n,m = list(map(int,input().split()))
    board=[[int(i) for i in input().strip()] for _ in range(n)] #string 배열
    
    print(bfs(n,m,board)) #거리 리턴
def bfs(n,m,board):
    dist={(0,0):1}
    dq=deque([(0,0)])
    visit=set([(0,0)])
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    
    while dq:
        x,y=dq.popleft()        
        if (x,y) == (n-1,m-1):
            return dist[(x,y)]
        for i in range(4):
            nx= x+dx[i]
            ny= y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if (nx,ny) not in visit and board[nx][ny]==1:
                    dq.append((nx,ny))
                    visit.add((nx,ny))
                    dist[(nx,ny)]=dist[(x,y)]+1
sol()