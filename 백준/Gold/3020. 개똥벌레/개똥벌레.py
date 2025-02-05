import sys
input=sys.stdin.readline
output=sys.stdout.write
N,H=map(int, input().split())
cave=[0]*(H+1)

for i in range(N):
    a=int(input().strip())
    if i%2==0:
        cave[0]+=1
        cave[a]+=-1
    else:
        cave[H-a]+=1
        cave[-1]+=-1
for i in range(1,H+1):
    cave[i]+=cave[i-1]
minans=min(cave[:H])
count=0
for i in cave[:H]:
    if i==minans:
        count+=1
output(' '.join([str(minans),str(count)]))