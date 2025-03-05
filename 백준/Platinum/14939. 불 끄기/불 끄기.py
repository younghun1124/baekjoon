import copy
board=[list(map(str,input())) for _ in range(10)]

dx=[0,-1,1,0,0]
dy=[0,0,0,-1,1]
ans=101

for x in range(1<<10):
    cnt=0
    tboard=copy.deepcopy(board)
    for i in range(10):
        
        if x&(1<<i): #경우의 수 비트와 i 번째 전구를 & 연산 해서 0이 아니면(i 번째 전구를 키는거면)
            cnt+=1
            print
            for r,c in zip(dx,dy):
                    nx=0+r
                    ny=i+c
                    if 0<=nx<10 and 0<=ny<10:
                        if tboard[nx][ny]=='#':
                            tboard[nx][ny]='O'
                        else: tboard[nx][ny]='#'       
    for i in range(1,10):
        for j in range(10):
            if tboard[i-1][j]=='O':
                cnt+=1
                for r,c in zip(dx,dy):
                    nx=i+r
                    ny=j+c
                    if 0<=nx<10 and 0<=ny<10:
                        if tboard[nx][ny]=='#':
                            tboard[nx][ny]='O'
                        else: tboard[nx][ny]='#'
    if tboard[9].count('O')==0:#전구가 모두 꺼졌다면
        ans=min(ans,cnt)
if ans==101:
    print(-1)
else: print(ans)