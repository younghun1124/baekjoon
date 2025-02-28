T=int(input())
D=[0]*101
D[1]=1
D[2]=1
D[3]=1
D[4]=2
D[5]=2
for i in range(6,101):
    D[i]=D[i-1]+D[i-5]
for _ in range(T):
    N=int(input())
    print(D[N])