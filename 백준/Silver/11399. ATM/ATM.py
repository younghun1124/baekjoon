n=int(input())
li=list(map(int, input().split()))
li.sort()
ans=0
for i in li:
    ans+=i*n
    n-=1
print(ans)