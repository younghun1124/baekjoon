from collections import deque
N,K=map(int,input().split())
belt=deque(list(map(int,input().split())))
robot=deque([False]*(N))
broken=belt.count(0)
ans=0
while broken<K:
    ans+=1 #1. 벨트 회전
    belt.rotate(1)
    robot.pop()
    robot.appendleft(False)
    robot[N-1]=False
    for i in range(N-1,-1,-1):#2.로봇 이동
        if robot[i]==True:
            if belt[i+1]!=0 and robot[i+1]==False:
                robot[i+1]=True
                robot[i]=False
                belt[i+1]-=1
                if belt[i+1]==0:
                    broken+=1
                
    if belt[0]!=0: #3.벨트에 로봇 올리기
        robot[0]=True
        belt[0]-=1
        if belt[0]==0:
            broken+=1
print(ans)