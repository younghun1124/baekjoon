N=int(input())
D=[0]*(N+1)
if N==1:
    print(1)
    exit()
M=int(input())
vip=set()
for _ in range(M):
    vip.add(int(input()))
D[0]=1
D[1]=1
if 1 not in vip and 2 not in vip:
    D[2]=2
else: D[2]=1

for i in range(3,N+1):
    if i in vip:
        D[i]=D[i-1]
    elif i-1 in vip:
        D[i]=D[i-1]
    else:
        D[i]=D[i-2]+D[i-1]
print(D[N])