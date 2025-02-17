import sys
input=sys.stdin.readline
t=int(input())
for _ in range(t):        
    I,N=map(int,input().split())
    minnum=0
    maxnum=0
    for _ in range(N):
        pos=int(input().strip())
        maxnum=max(max(I-pos,pos),maxnum)
        minnum=max(minnum,min(I-pos,pos))
    print(minnum,maxnum)