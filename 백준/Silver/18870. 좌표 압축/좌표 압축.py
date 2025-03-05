import sys
output=sys.stdout.write
N=int(input())
X=list(map(int,input().split()))
sorted_X=sorted(list(set(X)))
D={}
ans=[0]*N
for i in range(N):#X`i 찾기
    x=X[i]
    s=0
    e=len(sorted_X)-1
    if D.get(x,-1)!=-1:
        ans[i]=D[x]
        continue
    
    while s<=e: # m번째 수(sorted_X)가 xi 보다 큰지 작은지 확인 
        m=(s+e)//2
        if x<sorted_X[m]: #넘친다
            e=m-1
            
        else:
            s=m+1
            ans[i]=m
    D[x]=ans[i]
output(' '.join(map(str,ans)))