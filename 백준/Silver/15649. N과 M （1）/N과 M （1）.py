from collections import deque
n,m=list(map(int,input().split()))
used=[False]*(n+1)
ans=deque()
def recursion(depth): # 1부터 n까지 중복없이 ans 에 수열을 집어넣는 함수
    if depth==m:
        print(" ".join(map(str,ans)))   
        return
    for i in range(1,n+1):
        if used[i]!=True:
            ans.append(i)
            used[i]=True
            recursion(depth+1)
            ans.pop()
            used[i]=False
recursion(0)    
    
        