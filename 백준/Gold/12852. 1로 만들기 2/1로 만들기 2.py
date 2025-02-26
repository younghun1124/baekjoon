from collections import deque
N = int(input())
INF=int(1e9)
visited = [INF]*(N+1)
hist=[list() for _ in range(N+1)]
def bfs():
    q = deque()
    q.append(N)
    visited[N]=0
    hist[N].append(N)
    while q:
        cur = q.popleft()
        if cur==1:
            break
        if cur%3==0 and visited[cur//3]>visited[cur] + 1:
            visited[cur//3] = visited[cur] + 1
            hist[cur//3].extend(hist[cur])
            hist[cur//3].append(cur//3)
            q.append(cur//3)
        if cur%2 == 0 and visited[cur//2]>visited[cur] + 1:
            visited[cur//2] = visited[cur] + 1
            hist[cur//2].extend(hist[cur])
            hist[cur//2].append(cur//2)
            q.append(cur//2)
        if visited[cur-1]>visited[cur] + 1:
            visited[cur-1] = visited[cur] + 1
            hist[cur-1].extend(hist[cur])
            hist[cur-1].append(cur-1)
            q.append(cur-1)

bfs()

print(visited[1])
print(" ".join(map(str,hist[1])))