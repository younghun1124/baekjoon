n= int(input())
A=list(map(int,input().split()))
P=[0]*n
for num in range(n):
    for i in range(n):
        if A[i]==min(A):
            A[i]=1001
            P[i]=num
            break
print(*P)