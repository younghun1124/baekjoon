n,m = list(map(int,input().split()))
li=list(map(int,input().split()))
li.sort()
ans=[0]*(m+1)
used=[False]*n
def backtrack(depth):
    if depth==m:
        print(" ".join(map(str,ans[:m])))
        return
    for idx, i in enumerate(li):
        if used[idx]==False and ans[depth-1]<=i:
            used[idx]=True
            ans[depth]=i
            backtrack(depth+1)
            ans[depth]=0
            used[idx]=False
backtrack(0)
            