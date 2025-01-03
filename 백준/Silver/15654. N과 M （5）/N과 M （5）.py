n, m = list(map(int,input().split()))
li=list(map(int,input().split()))
used=[False]*(n)
li.sort()
ans=[0]*m
def backtrack(depth):#아직 사용되는 않은 요소를 현재 정답리스트[depth]에 넣는 함수
    if depth==m:
        print(" ".join(map(str,ans)))
        return
    for idx, i in enumerate(li):
        if used[idx]==False:
            ans[depth]=i
            used[idx]=True
            backtrack(depth+1)
            used[idx]=False
backtrack(0)