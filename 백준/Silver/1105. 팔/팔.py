L,R=map(str,input().split())
L=[x for x in L]
R=[x for x in R]

if len(L)>len(R):
    R=['0']*(len(L)-len(R))+R
elif len(L)<len(R):
    L=['0']*(len(R)-len(L))+L
    
ans=0
for i in range(len(L)):
    if L[i]==R[i]:
        if L[i]=='8':
            ans+=1    
    if L[i]!=R[i]:
        break
print(ans)