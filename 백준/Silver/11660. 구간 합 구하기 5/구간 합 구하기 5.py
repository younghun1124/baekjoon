import sys
input=sys.stdin.readline
output=sys.stdout.write
n,m=map(int,input().split())
board=[[0]*(n+1)]+[[0]+list(map(int,input().split())) for _ in range(n)]

for a in range(1,n+1):
    for i in range(1,n+1):
        board[a][i]+=board[a][i-1]
for a in range(1,n+1):
    for i in range(1,n+1):
        board[i][a]+=board[i-1][a]
    
ans=[0]*m    
for i in range(m):
    x1,y1,x2,y2=map(int,input().split())
    ans[i]=str(board[x2][y2]-board[x1-1][y2]-board[x2][y1-1]+board[x1-1][y1-1])
output('\n'.join(ans))