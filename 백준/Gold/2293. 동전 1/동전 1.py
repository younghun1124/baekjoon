import sys
input=sys.stdin.readline
N,K= map(int,input().split())
coin=[0]*(N)
coin.sort()
D=[0]*(K+1)
D[0]=1
for i in range(N):
    a=int(input())
    coin[i]=a
    # D[a]=1

for c in coin:
    for i in range(c,K+1):
        D[i]+=D[i-c]
print(D[-1])