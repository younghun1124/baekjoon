#0 빈칸 6: 벽 1~5:cctv 번호 
#TODO: 시간초과 해결하기
import sys
import copy
input=sys.stdin.readline
n,m=list(map(int,input().split()))
board=[list(map(int,input().split())) for _ in range(n)]
cctvs=[]
counts=[]


for ridx, row in enumerate(board):
    for cidx, i in enumerate(row):        
        if i in [1,2,3,4,5]:            
            cctvs.append((ridx,cidx,i))
used=[False]*len(cctvs)  


          
def shootfromcctv(ridx,cidx,option,direction,board):#쏘는방향 <-에서부터 반시계방향 0123
    def shoot(ridx,cidx,arrows,board):
        
        for arrow in arrows: #0 1 2 3     
            if arrow==0:
                for i in range(cidx-1,-1,-1):
                    if board[ridx][i]!=6:
                        if board[ridx][i]==0:   
                            board[ridx][i]='#'
                            
                    else:
                        break
            if arrow==1:
                for i in range(ridx+1,n):
                    if board[i][cidx]!=6:
                        if board[i][cidx]==0:                       
                            board[i][cidx]='#'
                    else:
                        break
            if arrow==2:
                for i in range(cidx+1,m):
                    if board[ridx][i]!=6:
                        if board[ridx][i]==0:                       
                            board[ridx][i]='#'
                    else:
                        break
            if arrow==3:
                for i in range(ridx-1,-1,-1):
                    if board[i][cidx]!=6:
                        if board[i][cidx]==0:                       
                            board[i][cidx]='#'
                    else:
                        break
        return board
    
    def getarrows(option, direction):
        if option==1:
            return [direction]
        elif option==2:
            return [direction%4, (direction+2)%4]
        elif option==3:
            return [direction%4, (direction+1)%4]
        elif option==4:
            return [direction%4,(direction+1)%4,(direction+2)%4 ]
        elif option==5:
            return [0,1,2,3]    
    arrows=getarrows(option,direction)
    tempboard=copy.deepcopy(board)
    return shoot(ridx,cidx,arrows,tempboard)

def backtrack(depth, board):    
    if depth==len(cctvs):
        ans=0
        for row in board:
            for i in row:
                if i==0:
                    ans=ans+1
        counts.append(ans)
        return 
      
    for idx, cctv in enumerate(cctvs):
        if used[idx]==False:
            ridx,cidx,i=cctv
            used[idx]=True
            for dir in range(4):
                backtrack(depth+1,shootfromcctv(ridx,cidx,i,dir,board))
            used[idx]=False
                
backtrack(0,board)
print(min(counts))