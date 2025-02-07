n=int(input())
board=[int(input()) for _ in range(n)]
piano=['A',0,'B','C',0,'D',0,'E','F',0,'G',0]#CDEFGABC

for first in [0,2,3,5,7,8,10]:
    nowidx=first
    check=True
    # print( piano[first])
    for note in board:
        nowidx=(nowidx+note)%12
        # print(nowidx, piano[nowidx])
        if piano[nowidx]==0:
            check=False
            break
    if check==True:
        print(piano[first], piano[nowidx])
        
