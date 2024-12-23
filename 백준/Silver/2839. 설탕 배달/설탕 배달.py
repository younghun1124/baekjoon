n=int(input())

kg5=n//5

def sol():    
    for i in range(kg5,-1,-1):
        if (n-(i*5))%3==0:
            print(i+((n-(i*5))//3))
            return
    print(-1)
sol()
    