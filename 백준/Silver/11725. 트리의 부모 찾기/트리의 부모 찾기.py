import sys
input=sys.stdin.readline
output=sys.stdout.write
from collections import deque
n=int(input().strip())
dict={}

visit=[False]*(n+1)
ans=[0]*(n+1)
for _ in range(n-1):
    a,b=map(int,input().split())
    dict.setdefault(a,[]).append(b)
    dict.setdefault(b,[]).append(a)
def search():
    dq=deque()
    dq.append(1)
    visit[1]=True
    while dq:
        x=dq.popleft()
        for i in dict[x]:
            if visit[i]==False:
                visit[i]=True
                dq.append(i)
                ans[i]=x
search()
for i in ans[2:]:
    output(f"{i}\n")
        