from collections import deque
N = int(input())
visited = [1e9]*(N+1)
def bfs():
    q = deque()
    q.append(N)
    visited[N]=0
    while q:
        cur = q.popleft()
        if cur==1:
            break
        if cur%3==0 and visited[cur//3]>visited[cur] + 1:
            visited[cur//3] = visited[cur] + 1
            q.append(cur//3)
        if cur%2 == 0 and visited[cur//2]>visited[cur] + 1:
            visited[cur//2] = visited[cur] + 1
            q.append(cur//2)
        if visited[cur-1]>visited[cur] + 1:
            visited[cur-1] = visited[cur] + 1
            q.append(cur-1)

bfs()
print(visited[1])