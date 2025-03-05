import sys
from collections import deque
sys.stdin.readline
N=int(input())
K=int(input())
dx=[-1,0,1,0]
dy=[0,1,0,-1]
board=[[False]*(N+1) for _ in range(N+1)]
for _ in range(K):
    r,c=map(int,input().split())
    board[r][c]=True
L=int(input())

op=[0]*(10001)
for _ in range(L):
    X,C=input().split()
    X=int(X)
    op[X]=C
t=0
direction=1
startr,startc=1,1
snake=deque([(startr,startc)])
while True:
        
        t+=1
        r,c=snake[0]
        r+=dx[direction]
        c+=dy[direction]
        if (r,c) in snake or not (1<=r<=N and 1<=c<=N):
            break
        snake.appendleft((r,c))
        if board[r][c]==True:
            board[r][c]=False
        else: snake.pop()
        if op[t]=='L':
            if direction!=0:
                direction-=1  
            else : direction=3
        elif op[t]=='D':
            if direction!=3:
                direction+=1  
            else : direction=0
print(t)
        