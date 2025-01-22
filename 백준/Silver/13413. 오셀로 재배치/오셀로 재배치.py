import sys
input=sys.stdin.readline
T=int(input())

for _ in range(T): #말 색깔이 다른부분을 찾아서 
    n=int(input())
    start=list(input().strip())
    goal=list(input().strip())
    count_w=0
    count_b=0
    ans=0
    for i in range(n):
        if start[i]!=goal[i]:
            if goal[i]=='W': count_w+=1
            else : count_b+=1
    ans=min(count_b,count_w)
    ans+=abs(count_w-count_b)
    
    print(ans)
       

   
    