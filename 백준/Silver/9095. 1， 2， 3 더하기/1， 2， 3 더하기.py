t=int(input())
D=[0]*12
D[1]=1
D[2]=2
D[3]=4
for i in range(4,12):
    D[i]=D[i-1]+D[i-2]+D[i-3]

for _ in range(t):
    n=int(input())
    print(D[n])
    
    