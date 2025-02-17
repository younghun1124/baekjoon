T=int(input())
for _ in range(T):
    n=int(input())
    board=[list(map(int,input().split())) for _ in range(2)]
    D=[[0]*n for _ in range(2)]
    if n==1:
        print(max(board[0][0],board[1][0]))
        continue
    D[0][0]=board[0][0]
    D[1][0]=board[1][0]
    D[0][1]=D[1][0]+board[0][1]
    D[1][1]=D[0][0]+board[1][1]
    if n==2:
        print(max(D[0][1],D[1][1]))
        continue
    for i in range(2,n):
        D[0][i]=max(D[1][i-2]+board[0][i],D[1][i-1]+board[0][i])
        D[1][i]=max(D[0][i-2]+board[1][i],D[0][i-1]+board[1][i])
    print(max(D[0][n-1],D[1][n-1]))
        
    
    
    