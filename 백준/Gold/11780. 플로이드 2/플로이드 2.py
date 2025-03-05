import sys
input=sys.stdin.readline
output=sys.stdout.write
n=int(input())
m=int(input())
G=[list() for _ in range(n+1)]
INF=int(1e9)
D=[[INF]*(n+1) for _ in range(n+1)]
nxt=[[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a,b,c=map(int,input().split())
    if D[a][b]>c:
        D[a][b]=c
        nxt[a][b]=b
    
for i in range(1,n+1): D[i][i]=0 #자기 자신으로 가는 거리 0 세팅


def floyd():
    for k in range(1,n+1):
        for i in range(1,n+1):
            if k==i:
                continue
            for j in range(1,n+1):
                if k==i:
                    continue
                if D[i][k]+D[k][j]<D[i][j]:
                    D[i][j]=D[i][k]+D[k][j]
                    nxt[i][j]=nxt[i][k]
floyd()
for row in D[1:]:
    for i in row[1:]:
        if i==INF:
            output('0 ')
        else: output(f"{i} ")
    output("\n")
for i in range(1,n+1):
    for j in range(1,n+1):
        if D[i][j]==0 or D[i][j]==INF:
            output('0')
        else:
            ans=[i]
            start=i
            while True:
                start=nxt[start][j]
                ans.append(start)
                if start==j:
                    break
            output(f"{len(ans)} ")
            output(' '.join(map(str,ans)))
        output("\n")