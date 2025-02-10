
n,a,b=map(int,input().split())
count=1
a=a-1
b=b-1
while 1:
    if abs(b-a)==1 and (a+b)%4==1:
        print(count)
        break
    a=a//2
    b=b//2
    count+=1