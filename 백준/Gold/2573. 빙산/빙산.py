from collections import deque
N,M=map(int,input().split())
board=[list(map(int, input().split())) for _ in range(N)]

def bfs(startx,starty,visit):
    dq=deque()
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    dq.append((startx,starty))
    visit.add((startx,starty))
    decrease={}
    while dq:
        x,y=dq.popleft()
        for i in range(4):
            nx=dx[i]+x
            ny=dy[i]+y
            if 0<=nx<N and 0<=ny<M:
                if (nx,ny) not in visit and board[nx][ny]!=0:#아직 방문하지 않은 빙하일때
                    dq.append((nx,ny))
                    visit.add((nx,ny))
                elif board[nx][ny]==0:
                    decrease[(x,y)]=decrease.get((x,y),0)+1
    for x,y in decrease:
        board[x][y]=max(0,board[x][y]-decrease[(x,y)])
year=0
while True:
    count=0
    visit=set()
    # for row in board:
    #     print(row)
    # print(year)
    
    for x in range(N):
        for y in range(M):
            if board[x][y]!=0 and (x,y) not in visit: #아직 방문하지 않은 빙하일때
                
                count+=1

                if count>=2:
                    print(year)
                    exit()
                bfs(x,y,visit)
    if count==0:
        break
    year+=1                
print(0)
                                         
                