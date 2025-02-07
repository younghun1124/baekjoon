n,m=map(int,input().split())
li=list(map(int,input().split()))
li.sort()
ans=[0]*(m+1)

def backt(depth):
    if depth==(m+1):
        print(' '.join(map(str,ans[1:])))
        return
    prev=-1 #이번 깊이에 넣은친구
    for i in range(n):
        if ans[depth-1]<=li[i] and li[i]!=prev:
            prev=li[i]
            ans[depth]=li[i]
            backt(depth+1)
                     
backt(1)