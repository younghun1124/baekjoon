from sys import stdin
input=stdin.readline
n=int(input())
board=[list(map(int,input().split())) for _ in range(n)]
ans=[0,0,0]
def check(board):
    z=board[0][0]
    for row in board:
        for e in row:
            if z!=e:
                return 2
    return z
def cut(r,c,board):
    size=len(board)//3
    newboard=[row[c*size:(c+1)*size] for row in board[r*size:(r+1)*size]]
    return newboard
def paper(board): #받은 종이에서 같은 숫자로 채워진 종이를 찾아내는 함수    
    z=check(board)
    if z!=2:#종이가 하나로 이루어져 있으면
        ans[z+1]=ans[z+1]+1 #종이 개수 늘리기(z가 -1 일수 있으니까 인덱스 1씩 더하기)
        return    
    for r in range(3):
        for c in range(3):
            paper(cut(r,c,board))
paper(board)
for i in ans:
    print(i)
                