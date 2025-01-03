n ,r, c= list(map(int,input().split()))
def zet(n,r,c):#2^n*2^n 배열에서 r행 c열을 몇번째로 방문했는지 출력하는 함수
    if n==0:#전체가 1행 1열(인덱스는 0,0)일때 자기 자신을 제일 먼저 방문한다(하나밖에없으니까) 근데 순서를 0부터 세므로 0반환
        return 0    
    # 0 1 
    # 2 3
    half=2**(n-1)
    #r,c 가 0번사각형일때
    if r<half and c<half:    
        return zet(n-1,r,c)
    #1번사각형일때
    elif r<half and c>=half:
        return half*half+zet(n-1,r,c-half)
    #2번사각형일때
    elif r>=half and c<half:
        return 2*half*half+zet(n-1,r-half,c)
    #3번사각형일때
    elif r>=half and c>=half:
        return 3*half*half+zet(n-1,r-half,c-half)
print(zet(n,r,c))