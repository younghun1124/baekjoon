import sys
input=sys.stdin.readline

n,m=map(int,input().split())
board=[[0]*(n+1)]+[[0]+list(map(int,input().split())) for _ in range(n)]

for a in range(1,n+1):
    for i in range(1,n+1):
        board[a][i]+=board[a][i-1]
for a in range(1,n+1):
    for i in range(1,n+1):
        board[i][a]+=board[i-1][a]
    
    
for _ in range(m):
    x1,y1,x2,y2=map(int,input().split())
    print(board[x2][y2]-board[x1-1][y2]-board[x2][y1-1]+board[x1-1][y1-1])
    