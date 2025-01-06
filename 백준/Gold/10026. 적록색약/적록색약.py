#적록색약 https://www.acmicpc.net/problem/10026
from collections import deque
n= int(input())
board=[list(input().strip()) for _ in range(n)]
visit=set()
visit2=set()

def bfs(start_x,start_y,visit):
    dq=deque()
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    dq.append((start_x,start_y))
    while(dq):
        x,y=dq.popleft()
        for i in range(4):
            nx= dx[i]+x
            ny= dy[i]+y
            if 0<=nx<n and 0<=ny<len(board[0]):
                if (nx,ny) not in visit and board[nx][ny]==board[x][y]:                
                    dq.append((nx,ny))
                    visit.add((nx,ny))
def solve():
    ans1=0
    for r in range(n):
        for c in range(len(board[0])):
            if (r,c) not in visit:
                bfs(r,c,visit)
                ans1+=1
                
    for r in range(n):
        for c in range(len(board[0])):
            if board[r][c]=='G':
                board[r][c]='R'
                
    ans2=0
    for r in range(n):
        for c in range(len(board[0])):
            if (r,c) not in visit2:
                bfs(r,c,visit2)
                ans2+=1
    print(f"{ans1} {ans2}")
solve()
                
            
        