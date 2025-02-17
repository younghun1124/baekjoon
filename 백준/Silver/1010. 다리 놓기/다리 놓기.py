# def backt(depth,prev):
#     if depth==n:
#         count[0]+=1
#         return
#     for i in range(prev+1,depth+m-n+1):
#         # print(depth,i)
#         backt(depth+1,i)
def fact(a):
    ans=1
    for i in range(2,a+1):
        ans*=i
    return ans
def comb(n,r):
    return fact(n)//(fact(r)*fact(n-r))
    

t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    
    print(comb(m,n))
    