N=int(input())
board=[[0]*N for _ in range(N)]
ans=0
pos=[0]*((N**2)+1)
li=[list(map(int,input().split())) for _ in range(N**2)]
dx=[-1,1,0,0]
dy=[0,0,-1,1]
for L in li:
    st=L[0]
    L=L[1:]
    
    maxmeet=-1
    empty=-1
    # print(st)
    for i in range(N):
        for j in range(N):
            if board[i][j]==0: #일단 빈칸이고
                
                tempmeet=0
                tempempty=0
                for k in range(4): #주변의 빈칸과 좋아하는 학생수 세기
                    nx=i+dx[k]
                    ny=j+dy[k]
                    if 0<=nx<N and 0<=ny<N:
                        if board[nx][ny] in L:
                            tempmeet+=1
                        elif board[nx][ny]==0:
                            tempempty+=1
                if tempmeet>maxmeet:
                    maxmeet=tempmeet
                    empty=tempempty
                    r,c=i,j
                elif tempmeet==maxmeet:
                    if tempempty>empty:
                        empty=tempempty
                        r,c=i,j
                
    board[r][c]=st
    pos[st]=(r,c)

# for row in board:
#     print(row)

for L in li:
    st=L[0]
    L=L[1:]
    
    meet=0
    r,c=pos[st]
    for k in range(4): #주변의 빈칸과 좋아하는 학생수 세기
        nx=r+dx[k]
        ny=c+dy[k]
        if 0<=nx<N and 0<=ny<N:
            if board[nx][ny] in L:
                meet+=1
    if meet==0:
        ans+=0
    elif meet==1:
        ans+=1
    elif meet==2:
        ans+=10
    elif meet==3:
        ans+=100
    else : ans+=1000

print(ans)