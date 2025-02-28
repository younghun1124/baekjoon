N=int(input())
li=[0]+list(map(int,input().split()))
D=[0]*(N+1)
for i in range(1,N+1):
    D[i]=list([li[i]])
    for j in range(1,i):
        if D[j][-1]<li[i] and len(D[j])+1>len(D[i]):
            D[i]=D[j]+[li[i]]
ans=1

for i in range(1,N+1):
    if len(D[i])>len(D[ans]):
        ans=i
print(len(D[ans]))
print(' '.join(map(str,D[ans])))