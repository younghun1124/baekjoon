n=int(input())
if n==1:
    print(1)
    exit()
d=[0]*(n+1) #1-index
d[1]=1
d[2]=2

for i in range(3,n+1):
    d[i]=(d[i-1]+d[i-2])%10007
print(d[n])