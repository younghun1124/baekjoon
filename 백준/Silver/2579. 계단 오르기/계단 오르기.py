n=int(input())
s=[int(input()) for _ in range(n)]
d=[[0]*2 for _ in range(n+1)]



if n==1:
    print(s[0])
else:
    d[0][0]=s[0]
    d[1][0]=s[1]
    d[1][1]=s[0]+s[1]
    for i in range(2,n):
        d[i][0]=max(d[i-2][0],d[i-2][1])+s[i]
        d[i][1]=d[i-1][0]+s[i]
    print(max(d[n-1][0],d[n-1][1]))

