tile_num=1
def tromino(K,start, board, hole):
    
    if K==2:
        fill_board(hole,board,start)
        return
    
    tromino(K,board,hole)
    tromino(K,board,hole)
    
def hole_check(K,hole):
    if hole[0]<2**(K-1):
        if hole[1]<2**(K-1): return 2
        else : return 3
    else :
        if hole[1]<2**(K-1): return 1
        else: return 4

def fill_board(hole_pass, board, start):
    for i in range(start,start+2):
        for j in range(start, start+2):
            if not (i==hole_pass[0] and j==hole_pass[1]):
                board[i][j]=tile_num
                
            
      

if __name__ =='__main__':
    K=int(input())
    board=[[-1 for _ in range(2**K)] for _ in range(2**K)]
    hole=tuple(map(int,input()))
    start=(0,0)
    tromino(K,start,board,hole)

