N=int(input())
li=list(map(int,input().split()))
D=[0]*(N)#D[i]는 i 번째 데이터를 반드시 포함할때 1부터 i 수열까지 합의 최대
ans=-2000
for i in range(N):
    D[i]=max(D[i-1]+li[i],li[i]) 
    ans=max(D[i],ans)
print(ans)