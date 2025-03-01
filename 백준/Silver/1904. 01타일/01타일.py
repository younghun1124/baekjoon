N=int(input())

if N==1:
    print(1)
    exit()
D=[0]*(N)
D[0]=1
D[1]=2
for i in range(2,N):
    D[i]=(D[i-1]+D[i-2])%15746
print(D[-1])