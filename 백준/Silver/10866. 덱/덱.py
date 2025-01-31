import sys
from collections import deque
input=sys.stdin.readline
n=int(input().strip())

dq=deque()

def operate():
    row=list(input().strip().split())
    i=0
    op=row[0]
    if len(row)>1:
        i=row[1]
    if op=='push_back':
        dq.append(i)
    elif op=='push_front':
        dq.appendleft(i)
    elif op=='pop_front':
        if not dq:
            print(-1)
            return
        print(dq.popleft())
    elif op=='pop_back':
        if not dq:
            print(-1)
            return
        print(dq.pop())
    elif op=='size':
        print(len(dq))
    elif op=='empty':
        if dq:
            print(0)
        else:
            print(1)
    elif op=='front':
        if not dq:
            print(-1)
            return
        print(dq[0])
    elif op=='back':
        if not dq:
            print(-1)
            return
        print(dq[-1])
for _ in range(n):
    operate()            
        