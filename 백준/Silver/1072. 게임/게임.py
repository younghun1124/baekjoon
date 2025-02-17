import math
X,Y=map(int,input().split())
Z=(Y*100)//X
K=Z+1
if K>=100:
    print(-1)
    exit()

i=math.ceil((K*X-100*Y)/(100-K))

print(i)