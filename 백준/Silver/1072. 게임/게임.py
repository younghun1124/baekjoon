import math
X,Y=map(int,input().split())
Z=(Y*100)//X
# print(Z)
K=Z+1
if K>=100:
    print(-1)
    exit()

i=((K*X)-(100*Y))//(100-K)
i=i if ((K*X)-(100*Y))%(100-K)==0 else i+1
print(i)