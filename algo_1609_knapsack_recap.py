n=4
c=10
val=[10,40,30,50]
weight=[5,4,6,3]
def knapsack():
    K=[[0]*(c+1) for _ in range(n+1)]
    # for i in range(n+1):
    #     K[i][0]=0
    # for i in range(c+1):
    #     K[0][i]=0

    for i in range(1,n+1):
        for w in range(1,c+1):
            if(weight[i-1]<w): # 이번에 넣을 물건의 무게가 임시 가방 무게보다 가벼우면 (i-1인 이유는 weight가 0 인덱스라서) 
                K[i][w]=max(K[i-1][w-weight[i-1]]+val[i-1],K[i-1][w]) # 담았을 경우와 담지 않았을 경우 중 최고 value
            else:
                K[i][w]=K[i-1][w]
    return K[n][c]

def knapsack_recap():
    K=[[0]*(c+1) for _ in range(n+1)]
    for x in range(n+1):
        K[x][0]=0
    for x in range(c+1):
        K[0][x]=0
    for i in range(1,n+1): #넣을 물건을 하나씩 늘려본다
        for w in range(1,c+1): #임시 가방의 무게를 늘려본다
            if(weight[i-1]>w): #임시가방보다 넣을 물건 무게가 크면(어차피 못넣으면)
                K[i][w]=K[i-1][w]
            else:
                K[i][w]=max(K[i-1][w-weight[i-1]]+val[i-1],K[i-1][w])
    return K[n][c]
                
        







print(knapsack_recap())