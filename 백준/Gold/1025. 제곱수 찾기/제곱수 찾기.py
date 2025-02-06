import math

n,m=map(int,input().split())
board=[list(map(int,input())) for _ in range(n)]

ans=-1
for stepx in range(-n,n+1):
    for stepy in range(-m,m+1):
        if stepx==0 and stepy==0:
            continue
        for x in range(0,n): #x시작점
            for y in range(0,m): #y시작점
                tempx=x
                tempy=y
                temp=0
                while 0<=tempx<n and 0<=tempy<m:
                    temp=temp*10+board[tempx][tempy]
                    if int(math.sqrt(temp))**2 == temp:
                        ans=max(ans,temp)
                    tempx+=stepx
                    tempy+=stepy
                    
print(ans)