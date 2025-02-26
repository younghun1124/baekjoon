import sys
input=sys.stdin.readline
N=int(input().strip())
item=[0]+[list(map(int,input().split())) for _ in range(N)]

D=[0]*(N+1) #D[i] i일의 수익 최대값
for i in range(1,N+1): #i일째 상담스케쥴 고려하기
    t,p=item[i]
    finsh=i+t-1
    if finsh<=N:#상담 완료 날짜가 N 안쪽이면 계산
        D[finsh]=max(D[finsh],D[i-1]+p)
    D[i]=max(D[i],D[i-1]) #그리고 i일째 최대값은 전날꺼 그대로 하기vs 

print(D[N])