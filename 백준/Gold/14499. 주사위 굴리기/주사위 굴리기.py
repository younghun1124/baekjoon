import sys
input=sys.stdin.readline
N,M,x,y,K=map(int,input().split())
D=[0]*6
board=[list(map(int,input().split())) for _ in range(N)]
dx=[0]+[0,0,-1,1]
dy=[0]+[1,-1,0,0]
Klist=list(map(int,input().split()))

def rolldice(k):
    if k==1:
        D[0],D[1],D[2],D[3],D[4],D[5]=D[3],D[1],D[0],D[5],D[4],D[2]
    elif k==4:
        D[0],D[1],D[2],D[3],D[4],D[5]=D[1],D[5],D[2],D[3],D[0],D[4]
    elif k==2:
        D[0],D[1],D[2],D[3],D[4],D[5]=D[2],D[1],D[5],D[0],D[4],D[3]
    else:
        D[0],D[1],D[2],D[3],D[4],D[5]=D[4],D[0],D[2],D[3],D[5],D[1]

for k in Klist:
    nx=dx[k]+x
    ny=dy[k]+y
    
    if 0<=nx<N and 0<=ny<M:
        
        rolldice(k)
        if board[nx][ny]==0:
            board[nx][ny]=D[5]
        else:
            D[5]=board[nx][ny]
            board[nx][ny]=0
        x,y=nx,ny
        print(D[0])