from sys import stdin
input=stdin.readline
n=int(input())
board=[list(map(int,input().split())) for _ in range(n)]
ans=[0,0,0]
def paper_check(r,c,n):
    z=board[r][c]
    for row in board[r:r+n]:
        for e in row[c:c+n]:
            if z!=e:
                return False
    return True
def paper(r,c,n): #받은 종이에서 같은 숫자로 채워진 종이를 찾아내는 함수        
    if paper_check(r,c,n):#종이가 하나로 이루어져 있으면
        ans[board[r][c]+1]=ans[board[r][c]+1]+1  #종이 개수 늘리기(z가 -1 일수 있으니까 인덱스 1씩 더하기)
        return    
    for rstep in range(3):
        for cstep in range(3):
            paper(r+rstep*(n//3),c+cstep*(n//3),n//3)
           
paper(0,0,n)
for i in ans:
    print(i)                