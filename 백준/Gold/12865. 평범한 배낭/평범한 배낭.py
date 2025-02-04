import sys
input=sys.stdin.readline
n,k=map(int,input().split())
d=[[0]*(k+1) for _ in range(n+1)]
item=[(0,0)]
item.extend([tuple(map(int,input().split())) for _ in range(n)]) #무게, 가치

for i in range(1,n+1): #i는 아이템 인덱스
    for bagW in range(1,k+1):
        W,V=item[i]
        if W<=bagW: #가방에 넣을 수 있다.
            d[i][bagW]=max(d[i-1][bagW],V+d[i-1][bagW-W])
        if W>bagW: #가방에 넣지못한다
            d[i][bagW]=d[i-1][bagW]
print(d[n][k])