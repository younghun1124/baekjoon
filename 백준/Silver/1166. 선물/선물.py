import math

N,L,W,H=map(int,input().split())
start=0
end=min(L,W,H)
for _ in range(200):
    mid=(start+end)/2
    
    if (L//mid)*(W//mid)*(H//mid)>=N:
        start=mid
    else : #A가 커서 너무 적게 들어감
        end=mid
print(start)