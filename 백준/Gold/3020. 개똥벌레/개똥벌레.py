import sys
input= sys.stdin.readline
N,H=map(int,input().split())
cave=[0]*(H+1) #동굴의 높이만큼 누적합

for i in range(N):
    n=int(input().strip())
    if i%2==0:
        cave[0]+=1
        cave[n]-=1
    else:
        cave[H-n]+=1
        cave[H]-=1
for i in range(1,H+1):
    cave[i]+=cave[i-1]
minnum=min(cave[:H])
count=0
for i in cave[:H]:
    if minnum==i:
        count+=1   
print(minnum, count)
    