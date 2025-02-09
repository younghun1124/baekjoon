n,m=map(int,input().split())
s=min(n,m)
board=[input().strip() for _ in range(n)]
for i in range(s):
    for j in range(n):
        for k in range(m):
            if j+i>=n or k+i>=m: continue
            if board[j][k]==board[j+i][k] and board[j][k]==board[j][k+i] and board[j][k]==board[j+i][k+i]:
                ans=i+1
print(ans**2)