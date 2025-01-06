
n,m,k=list(map(int,input().split()))
stickers=[]
board=[[0]*m for _ in range(n)]
for _ in range(k):
    r,c=list(map(int,input().split()))
    sticker=[list(map(int,input().split())) for _ in range(r)]
    stickers.append(sticker)


def ismatch(br,bc,sticker):
    for sr, row in enumerate(sticker):
        for sc, pixel in enumerate(row):
            if pixel==1:
                if board[br+sr][bc+sc]==0:
                    continue
                else:
                    return False
    return True
def insert_sticker(br,bc,sticker):
    for sr, row in enumerate(sticker):
        for sc, pixel in enumerate(row):
            if pixel==1:
                board[br+sr][bc+sc]=1
                
def match_sticker(sticker):                
    for br in range(n-len(sticker)+1): #가로 반복
        for bc in range(m-len(sticker[0])+1):#세로반복
            if ismatch(br,bc,sticker):
                insert_sticker(br,bc,sticker)
                return True
    return False

def rotate(sticker):#  1회전한 스티커를 반환하는 함수
    r=len(sticker)
    c=len(sticker[0])
    new_sticker=[]
    for nc in range(0,c): #첫 col부터
        new_row=[sticker[nr][nc] for nr in range(r-1,-1,-1)]
        new_sticker.append(new_row)
    return new_sticker

def solve():
    for sticker in stickers:
        for _ in range(4):
            if match_sticker(sticker):
                break
            sticker=rotate(sticker)
            
    ans=0
    for row in board:
        for pixel in row:
            if pixel==1:
                ans+=1
    print(ans)
    
solve()
            

        
            
        
        
        

          
        
        
