import sys
input=sys.stdin.readline
N,M=map(int,input().split())
r,c,d=map(int,input().split())
dx=[-1,0,1,0]
dy=[0,1,0,-1]
board=[list(map(int,input().split())) for _ in range(N)]
ans=0
while True:
    if board[r][c]==0:
        ans+=1
        board[r][c]=2
        continue
    found=False
    nd=d
    for _ in range(4):
        nd= nd-1 if nd!=0 else 3 #반시계 90도 회전
        nr,nc=r+dx[nd],c+dy[nd]
        if board[nr][nc]==0:
            r=nr
            c=nc
            d=nd
            found=True
            break
    if found==True:
        continue
    nr,nc=r+dx[(d+2)%4] ,c+dy[(d+2)%4]
    if board[nr][nc]!=1:
        r=nr
        c=nc
        continue
    else:
        break

print(ans)