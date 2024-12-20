def sol():
    a,b,c=list(map(int,input().split()))
    print(pow(a,b,c))

def pow(a,b,c):
    if b==1:
        return a%c
    val=pow(a,b//2,c)
    val=val*val%c
    if b%2==0:
        return val
    else:
        return val*a%c
    
sol()