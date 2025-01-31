n=int(input())


d=[0]*(n+1) #d[i]는 i 개 돌이 있을때 이기는 사람 (0이 상근)

def dp():
    if n==1 or n==3 or n==4:
        print('SK')
        return
    if n==2:
        print('CY')
        return
    d[1],d[2],d[3],d[4]=0,1,0,0
    for i in range(5,n+1):
        d[i]= min(not d[i-1],not d[i-3],not d[i-4]) #전에 꺼에서 이기는사람이 바뀌고, 그중 최소(상근이 우선 선택)   
    if d[n]==0:
         print('SK')
    else : print('CY')
dp()