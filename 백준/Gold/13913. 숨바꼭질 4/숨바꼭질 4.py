N,K=map(int,input().split())
from collections import deque
INF=int(1e6)
visit=[INF]*200000
visit[N]=0
hist=[-1]*200000
hist[N]=N
dq=deque([N])
while dq:
    p=dq.popleft()
    for nxt in [p-1,p*2,p+1]:
        if 0<=nxt<=199999:
            if visit[nxt]>visit[p]+1:
                visit[nxt]=visit[p]+1
                hist[nxt]=p
                
                dq.append(nxt)
print(visit[K])
idx=K
ans=deque([K])
while True: 
    if idx==N:
        break
    idx=hist[idx]
    ans.appendleft(idx)

print(' '.join(map(str,ans)))