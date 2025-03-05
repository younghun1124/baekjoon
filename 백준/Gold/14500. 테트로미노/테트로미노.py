import sys
sys.stdin.readline
N,M=map(int,input().split())
board=[list(map(int,input().split())) for _ in range(N)]
ans=0
stick=[[(0,0),(1,0),(2,0),(3,0)],[(0,0),(0,1),(0,2),(0,3)]]
box=[[(0,0),(1,0),(0,1),(1,1)]]
L=[[(0,0),(1,0),(2,0),(2,1)],[(0,0),(1,0),(0,1),(0,2)],[(0,0),(0,1),(1,1),(2,1)],[(1,0),(1,1),(1,2),(0,2)]]
invertL=[[(2,0),(2,1),(1,1),(0,1)],[(0,0),(1,0),(1,1),(1,2)],[(0,0),(1,0),(2,0),(0,1)],[(0,0),(0,1),(0,2),(1,2)]]
O=[[(0,0),(0,1),(0,2),(1,1)],[(1,0),(0,1),(1,1),(2,1)],[(1,0),(1,1),(0,1),(1,2)],[(0,0),(1,0),(2,0),(1,1)]]
S=[[(0,0),(1,0),(1,1),(2,1)],[(1,0),(1,1),(0,1),(0,2)],[(0,0),(0,1),(1,1),(1,2)],[(1,0),(2,0),(1,1),(0,1)]]
shapes=[*stick,*box,*L,*invertL,*S,*O]
def solve():
    global ans
    for i in range(N):
        for j in range(M):
            for shape in shapes:
               
                temp=0
                for k in range(4):
                    r,c=i+shape[k][0],j+shape[k][1]
                    if 0<=r<N and 0<=c<M:
                        temp+=board[r][c]
                    else:
                        temp=0 
                        break
                ans=max(temp,ans)
solve()
print(ans)