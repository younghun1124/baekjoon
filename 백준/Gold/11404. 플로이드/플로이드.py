import sys
input=sys.stdin.readline
print=sys.stdout.write
n=int(input())
m=int(input())
D=[[float("inf")]*n for _ in range(n)]
for i in range(n):
    D[i][i]=0
for _ in range(m):
    a,b,c= list(map(int,input().split()))
    D[a-1][b-1]=min(D[a-1][b-1],c) #시작도시와 도착 도시를 연결하는 노선은 하나가 아닐 수 있으므로 최소값 사용

for k in range(n):
    for i in range(n):
       
        for j in range(n):
           
            D[i][j]=min(D[i][j],D[i][k]+D[k][j])
result = []
for row in D:
    result.append(" ".join(str(0 if i == float("inf") else i) for i in row))
sys.stdout.write("\n".join(result) + "\n")
    