n=int(input())

ans=[]
def hanoi(a,b,n):#원판 n개를 기둥 a에서 b로 옮기는 방법을 출력하는 함수
    if n==1:#옮길 원판이 하나일때
        ans.append(str(a)+" "+str(b))
        return
    hanoi(a,6-a-b,n-1) #n-1개 원판을 a에서 6-a-b (a,b 말고 다른 원판)
    ans.append(str(a)+" "+str(b)) #n번째 원판을 b로 옮긴다
    hanoi(6-a-b,b,n-1) #다시 6-a-b 기둥에서 b로 n-1개 원판을 옮긴다
hanoi(1,3,n)
print(len(ans))
for s in ans:
    print(s)
