from itertools import permutations

N=int(input())
playernums=[x for x in range(1,9)]
result=[list(map(int,input().split())) for _ in range(N)]

ans=0
for sequence in permutations(playernums,8):
    seq=list(sequence)
    seq.insert(3,0)
    
    score=0
    playernum=0
    

    for i in range(N): #매 이닝마다 초기화
        b1,b2,b3=0,0,0
        predict=result[i]
        # print(player)
        out=0
        while out<3:
            player=seq[playernum]
            if predict[player]==0:
                out+=1
            elif predict[player]==1:
                score+=b3
                b3,b2,b1=b2,b1,1
            elif predict[player]==2:
                score+=(b3+b2)
                b3,b2,b1=b1,1,0
            elif predict[player]==3:
                score+=(b3+b2+b1)
                b3,b2,b1=1,0,0
            elif predict[player]==4:
                score+=(b3+b2+b1+1)
                b3,b2,b1=0,0,0   
            if playernum==8:
                playernum=0
            else: playernum+=1
    if ans<score:
        ans=score
print(ans)