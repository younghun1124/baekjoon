n,k=map(int,input().split())

items=[list(map(int,input().split())) for _ in range(n)] #W, V
d=[[0]*(k+1) for _ in range(n+1)] #0 인덱스 아이템

for i in range(1,n+1): 
    W,V=items[i-1]
    for j in range(1,k+1):
        if W>j: #담을수 없다
            d[i][j]=d[i-1][j] #이전 무게 그대로 유지
        else:
            d[i][j]=max(d[i-1][j-W]+V,d[i-1][j]) #빼고 새로 담는것과 안담는것 사이에 더 큰값
print(d[n][k])