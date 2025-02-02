import sys
input=sys.stdin.readline
n=int(input().strip())
s=set()
def operate():
    text=list(input().strip().split())
    op=text[0]
    num=0
    if len(text)>1:
        num=int(text[1])
    if op=="add":
        s.add(num)
    elif op=="remove":
        if num in s:
            s.remove(num)
    elif op=="check":
        if num in s:
            print(1)
        else:
            print(0)
    elif op=="toggle":
        if num in s:
            s.remove(num)
        else:
            s.add(num)
    elif op=="all":
        s.update([x for x in range(1,21)])
    elif op=="empty":
        s.clear()   
for _ in range(n):
    operate()