a,b=map(int,input().split())
ans=0
i=1
idx=1
while True:
    for _ in range(i):
        if a<=idx<=b:
           ans+=i
        idx+=1
    i+=1
    if idx>b:
        break
print(ans) 