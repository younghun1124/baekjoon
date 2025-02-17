#A->B 16953
A,B=map(int,input().split())
ans=float("inf")
def operate(depth,num):
    global ans
    if num==B:
        ans=min(depth,ans)
    elif num>B:
        return
    operate(depth+1,num*10+1)
    operate(depth+1,num*2)
operate(0,A)
if ans==float("inf"):
    print(-1)
else: print(ans+1)