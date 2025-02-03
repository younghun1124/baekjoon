from collections import deque
n= int(input())
board=[input() for _ in range(n)]
dx=[-1,1,0,0]
dy=[0,0,-1,1]
ans=[]

visit=set()
def bfs(r,c):
    dq=deque([(r,c)])
    num=0
    while dq:
        x,y=dq.popleft()
        num+=1
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n:
                if board[nx][ny]=='1':
                    if (nx,ny) not in visit:
                        dq.append((nx,ny))
                        visit.add((nx,ny))
    return num
        
for r in range(n):
    for c in range(n):
        if board[r][c]=='1' and (r,c) not in visit :
            visit.add((r,c))
            ans.append(bfs(r,c))
print(len(ans))
for i in sorted(ans):
    print(i)

    