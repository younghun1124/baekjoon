N=int(input())
div=int(1e9)

if N==0:
    print(0)
    print(0)
    exit()

prev,next=0,1
n=abs(N)
for i in range(n-1):
    prev,next=next%div,(prev+next)%div
if N>0:
    print(1)
elif N<0:
    if n%2==0:
        print(-1)
    else:
        print(1)
print(next)