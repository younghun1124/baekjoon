N=int(input())
li=list(map(int,input().split()))
li=li[::-1]
ans=[]
for i in range(N):
    ans.insert(li[i],N-i)
print(' '.join(map(str,ans)))