from collections import deque
m, n, k=list(map(int,input().split()))
#위아래 뒤집었다고 생각
#n 이 가로 개수(x) m이 세로 개수(y)
board=[[0]*n for _ in range(m)]
ans=[]
anscount=0
def bfs(start_x,start_y):
    dq=deque()
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    dq.append((start_x,start_y))
    count=0
    while(dq):
        x,y=dq.popleft()
        count+=1
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<m and 0<=ny<n:
                if board[nx][ny]==0:
                    board[nx][ny]=1
                    dq.append((nx,ny))
                    
                    
    return count
    
for _ in range(k):   
    x_start,y_start, x_end, y_end=list(map(int,input().split()))
    for r in range(y_start,y_end):
        for c in range(x_start,x_end):
            board[r][c]=1


           
for ridx, row in enumerate(board):
    for cidx, box in enumerate(row):
        if box==0:
            anscount+=1
            board[ridx][cidx]=1
            ans.append(bfs(ridx,cidx))
            
print(anscount)
for i in sorted(ans):
    print(i, end=' ')