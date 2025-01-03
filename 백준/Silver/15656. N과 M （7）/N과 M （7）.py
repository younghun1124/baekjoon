n,m = list(map(int,input().split()))
li=list(map(int,input().split()))
li.sort()
ans=[0]*m

def backT(depth):
    if depth==m:
        print(" ".join(map(str,ans)))
        return
    for i in li:
        ans[depth]=i
        backT(depth+1)
backT(0)