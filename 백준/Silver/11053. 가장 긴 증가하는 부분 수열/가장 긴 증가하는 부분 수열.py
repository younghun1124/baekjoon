n=int(input())
A=list(map(int,input().split()))
d=[1]*n #그냥 선택해도 길이는 1
for i in range(n):
    for j in range(i):
        if A[i]>A[j]:#i 번째 A가 j 번 A 보다 커서 바로 뒤에 붙일 수 있을 때
            d[i]=max(d[i],d[j]+1) #A[j] 뒤에 A[i] 붙이기 vs 그대로 두기
print(max(d))