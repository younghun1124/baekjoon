n=list(input())
ans=0
starcoff=0
for i in range(13):
    coff=0
    if i%2==0:
        coff=1
    else:
        coff=3
    if n[i]!='*':
        ans+=int(n[i])*coff
    else:
        starcoff=coff
for i in range(10):
    if (i*starcoff+ans)%10==0:
        print(i)