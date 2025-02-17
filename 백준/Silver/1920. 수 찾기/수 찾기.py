n=int(input())
nList=set(input().split())
m=int(input())
mList=list(input().split())
for i in mList:
    if i in nList:
       print(1)
    else:  print(0)