n=int(input())
li=[0]+list(map(int,input().split()))
D=[0]*(n+1)
for i in range(1,n+1):
    for j in range(i-1,-1,-1):
        if li[j]<li[i]: #증가하는 부분수열 조건 만족
            D[i]=max(D[j]+li[i],D[i])
print(max(D))