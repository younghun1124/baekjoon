n,m=list(map(int,input().split()))
ans=[0]*(m+1)
def sol(depth):
    if depth==m:
        print(" ".join(map(str,ans[:m])))
        return
    for i in range(1,n+1):
        if ans[depth-1]<=i:
            ans[depth]=i
            sol(depth+1)
            ans[depth]=0
sol(0)