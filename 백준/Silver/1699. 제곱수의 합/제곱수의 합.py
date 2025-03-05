N=int(input())
D=[x for x in range(N+1)]
for i in range(1,N+1):
    for j in range(1,i):
        if j*j>i:
            break
        if D[i]>1+D[i-j*j]:
            D[i]=1+D[i-j*j]
print(D[-1])