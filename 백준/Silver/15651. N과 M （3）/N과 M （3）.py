n,m =list(map(int,input().split()))
ans=[0]*m
def backtrack(depth):#배열에 1부터 n까지 수를 배열이 꽉 찰때까지 순서대로 넣는 함수
    if depth==m:
        print(" ".join(map(str,ans)))
        return
    for i in range(1,n+1):
        ans[depth]=i
        backtrack(depth+1)        
backtrack(0)