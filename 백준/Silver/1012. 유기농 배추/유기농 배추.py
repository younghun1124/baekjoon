import sys
from collections import deque
input= sys.stdin.readline

T=int(input())
def sol():
    m,n,k=list(map(int,input().split()))
    board=[[0]*m for _ in range(n)]
    visit=[[0]*m for _ in range(n)]
    for _ in range(k):#보드 세팅
        i,j=list(map(int,input().split()))
        board[j][i]=1 
    print(bfs(n,m,board,visit))
        
def bfs(n,m,board,visit):
    dq=deque()
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    ans=0
    for ridx, row in enumerate(board):
        for cidx, c in enumerate(row):
            if c==1 and visit[ridx][cidx]==0: #배추가 있고 미방문이면 dfs 시작
                ans=ans+1
                dq.append((ridx,cidx))
                while dq:
                    x,y=dq.popleft()
                    for i in range(4):
                        nx=dx[i]+x
                        ny=dy[i]+y
                        if 0<=nx<n and 0<=ny<m: #board 내부
                            if visit[nx][ny]==0 and board[nx][ny]==1: #방문안했고 배추 위치함
                                dq.append((nx,ny))
                                visit[nx][ny]=1
    return ans
                    
    
    
for _ in range(T):
    sol()
