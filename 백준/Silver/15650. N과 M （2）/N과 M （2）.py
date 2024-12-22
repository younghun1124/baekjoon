n,m= map(int,input().split())
ans=[0]
used=[False]*(n+1)
def recursion(depth):#depth가 m에 도달할때까지 ans에 오름차순을 만족하는 수를 중복없이 넣는 함수
    if depth==m:
        print(" ".join(map(str,ans[1:])))
        return
    
    for i in range(1, n+1):
        if used[i]==False and ans[-1]<i:
            ans.append(i)
            used[i]=True
            recursion(depth+1)
            ans.pop()
            used[i]=False
recursion(0)           
        