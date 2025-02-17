from collections import deque
N,K=map(int,input().split())
dq=deque()
vis=[float("inf")]*100002
dq.append((N,0))
while dq:
    d,t=dq.popleft()
    
    if d==K:
        print(t)
        break
    if not (0<=d<=100000):
        
    if vis[d*2]>t:
        vis[d*2]=t
        dq.appendleft((d*2,t))
    if vis[d-1]>t+1:
        vis[d-1]=t+1
        dq.append((d-1,t+1))
    if vis[d+1]>t+1:
        vis[d+1]=t+1
        dq.append((d+1,t+1))    
    
    
    
    