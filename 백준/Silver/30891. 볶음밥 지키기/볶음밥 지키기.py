import sys
input=sys.stdin.readline
N,R=map(int,input().split())
bap=[tuple(map(int,input().split())) for _ in range(N)]
def is_in_wok(W,B):
    X,Y=W
    bx,by=B
    if (X-bx)**2+(Y-by)**2<=R**2:
        return True
    else:
        return False

ans=0
count=0
for X in range(-100,101):
    for Y in range(-100,101):
        temp=0
        for B in bap:
            if is_in_wok((X,Y),B):
                temp+=1
        if count<temp:
            count=temp
            ans=(X,Y)
print(*ans)
            
    