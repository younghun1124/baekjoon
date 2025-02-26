from collections import deque

T=[deque(map(int,input()))for _ in range(4)]
K=int(input())
def spin(tidx,x,flow):
    right=T[tidx][2]
    left=T[tidx][6]
    T[tidx].rotate(x)
    # print(tidx,'회전',x, flow)
    next=tidx+flow
    if 0<=next<4:
        if flow==-1:
            if T[next][2]!=left:
                spin(next,flip(x),flow)
        if flow==1:
            if T[next][6]!=right:
                spin(next,flip(x),flow)
def flip(x):
    if x==1:
        return -1
    elif x==-1:
        return 1

        
for _ in range(K):
    tidx,direct=map(int,input().split())
    tidx-=1
    right=T[tidx][2]
    left=T[tidx][6]
    T[tidx].rotate(direct)
    # print(tidx,'회전', direct)
    for flow in [-1,1]:
        next=tidx+flow
        if 0<=next<4:
            if flow==-1:
                if T[next][2]!=left:
                    spin(next,flip(direct),flow)
            if flow==1:
                if T[next][6]!=right:
                    spin(next,flip(direct),flow)
score=0
if T[0][0]==1:
    score+=1
if T[1][0]==1:
    score+=2
if T[2][0]==1:
    score+=4
if T[3][0]==1:
    score+=8
print(score)