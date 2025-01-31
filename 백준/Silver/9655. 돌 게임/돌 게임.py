n=int(input())
if n==1:
    print('SK')
    exit()
if n==2:
    print('CY')
    exit()
if n==3:
    print('SK')
    exit()
d=[0]*(n+1)



d[1]=0
d[2]=1
d[3]=0


for i in range(4,n+1):
    d[i]=not (min(d[i-1],d[i-3]))
    


if d[i]:
    print('CY')
else:
    print('SK')