import sys
input= sys.stdin.readline
t=int(input().strip())

for _ in range(t):
    n=int(input().strip())
    li=set()
    li.add(1)
    for i in range(n):
        newli=set()
        op=input().split()
        for x in li:
            if op[0]=='+':
                newli.add(((x+int(op[1]))%7))
            else:
                newli.add(((x*int(op[1]))%7))
            if op[2]=='+':
                newli.add(((x+int(op[3]))%7))
            else:
                newli.add(((x*int(op[3]))%7))
        li=newli
    isLuck=False    
    for i in li:
        if i==0:
            isLuck=True
            break
    if isLuck:
        print('LUCKY')
    else:
        print('UNLUCKY')