from collections import deque
n,m=list(map(int,input().split()))

ans=deque()
def recursion(n): # 1부터 n까지 중복없이 ans 에 수열을 집어넣는 함수
    if len(ans)==m:
        print(" ".join(map(str,ans)))   
        return
    for i in range(1,n+1):
        if i not in ans:
            ans.append(i)
            recursion(n)
            ans.pop()
recursion(n)    
    
        