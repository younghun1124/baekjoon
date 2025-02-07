import math
t=int(input())
for _ in range(t):
    x1,y1,r1,x2,y2,r2=map(int,input().split())
    centerdist=math.sqrt((x2-x1)**2+(y2-y1)**2)
    maxr=max(r1,r2)
    minr=min(r1,r2)
    if (x1,y1,r1)==(x2,y2,r2):
        print(-1)
    elif centerdist<maxr: #원 내부에 중심
        if centerdist+minr==maxr:
            print(1)
        elif centerdist+minr>maxr:
            print(2)
        elif centerdist+minr<maxr:
            print(0)
    elif centerdist>maxr: #원 외부에 중심
        if centerdist==r1+r2:
            print(1)
        elif centerdist>r1+r2:
            print(0)
        elif centerdist<r1+r2:
            print(2)        
    elif centerdist==maxr:
        print(2)
    

    