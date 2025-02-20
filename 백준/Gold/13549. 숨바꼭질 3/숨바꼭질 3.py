from collections import deque
N,K=map(int,input().split())
dq=deque()
vis=[float("inf")]*100002
dq.append((N,0))
while dq:
    d,t=dq.popleft()
    def in_range(x):
        if (0<=x<=100000): return True
        else: return False
    if d==K:
        print(t)
        break
    if in_range(d*2) and vis[d*2]>t  :
        vis[d*2]=t
        dq.appendleft((d*2,t))
    if  in_range(d-1) and vis[d-1]>t+1 :
        vis[d-1]=t+1
        dq.append((d-1,t+1))
    if in_range(d+1) and vis[d+1]>t+1  :
        vis[d+1]=t+1
        dq.append((d+1,t+1))    