n,m =list(map(int,input().split()))
li=list(map(int,input().split()))
li.sort()
ans=[0]*(m+1)
def backtrack(depth):
    if depth==m:
        print(" ".join(map(str,ans[0:m])))
        return
    for i in li:
        if ans[depth-1]<=i:
            ans[depth]=i
            backtrack(depth+1)
            ans[depth]=0
backtrack(0)