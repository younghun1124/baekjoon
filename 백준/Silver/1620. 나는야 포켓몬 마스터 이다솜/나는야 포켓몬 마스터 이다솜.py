import sys
input=sys.stdin.readline
n, m= map(int,input().strip().split())
dogam={}
for i in range(1,n+1):
    a=input().strip()
    dogam[str(i)]=a
    dogam[a]=str(i)
for _ in range(m):
    print(dogam[input().strip()])