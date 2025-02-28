import sys
input=sys.stdin.readline
n=int(input())

li=[0]+[int(input()) for _ in range(n)]
if n==1:
    print(li[1])
    exit()

D=[[0]*3 for _ in range(n+1)]
D[1][1]=li[1]
ans=0
for i in range(2,n+1):
    D[i][0]=max(D[i-1]) #한번 건너뛰기(이전꺼를 절대 안마신 것이므로 i-2로 한다)
    D[i][1]=li[i]+D[i-1][0]
    D[i][2]=li[i]+D[i-1][1]
    ans=max(*D[i],ans)
# for row in D:
#     print(row)
print(ans)