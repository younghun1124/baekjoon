T,W=map(int,input().split())
D=[[0]*(W+1) for _ in range(T+1)]  #D[T][W]
tree=[0]+[int(input())-1 for _ in range(T)] #나무 인덱스 1빼기(0인덱스)

for t in range(1,T+1):
    
    if tree[t]==0: #안움직이고 있을때의 초기값.
        D[t][0]=D[t-1][0]+1
    else : D[t][0]=D[t-1][0]
    
    for w in range(1,min(t+1,W+1)):  
        if w%2==tree[t]: #w번 움직였을때 t초의 자두를 먹을 수 있으면
            D[t][w]=max(D[t-1][w],D[t-1][w-1])+1 #이전에 w 번 움직였을때 가만히 있다가 한번 더 먹기vs 이번에 움직여서 먹기
        else: #굳이 움직이긴 하기
            D[t][w]=max(D[t-1][w],D[t-1][w-1]) #근데 그 이전에 w번 움직여 놨을때vs이번에 움직이기
print(max(D[t])) #t초때 결국 최대로 먹은 수 찾기.