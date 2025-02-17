N,L=map(int,input().split())
def getsum(start,end):
    return (start+end)*(end-start+1)//2
for i in range(L,101):
    #start j
    t=N//i-i//2-1
    for j in range(t,t+3): 
        # print(j) # 디버그용
        if j<0:
            continue
        sumd=getsum(j,j+i-1)
        if sumd==N:
            for k in range(j,j+i):
                print(k,end=' ')
            exit()
print(-1)
    #시간복잡도 초과..
        
    