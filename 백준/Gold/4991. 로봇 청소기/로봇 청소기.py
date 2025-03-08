import sys
input = sys.stdin.readline
from collections import deque
dy = [1,-1,0,0]
dx = [0,0,1,-1]
INF = 10**6

def BFS(y,x,n):
  visited = [[0]*M for i in range(N)]
  dq = deque()
  dq.append((y,x,0))

  while dq:
    y,x,d = dq.popleft()
    if visited[y][x]:
      continue
    visited[y][x] = 1
    if room[y][x] == "*":
      n1 = numdict[(y,x)]
      graph[n][n1] = graph[n1][n] = d
    for i in range(4):
      y1,x1 = y+dy[i],x+dx[i]
      if N>y1>=0 and M>x1>=0:
        if room[y1][x1] == "x" or visited[y1][x1]:
          continue
        dq.append((y1,x1,d+1))    

def DFS(now,distance,cnt):
  global result
  if distance >= result:
    return
  if cnt == num:
    result = min(result,distance)
    return
  for next in range(1,num+1):
    if visited[next]:
      continue
    visited[next] = 1
    DFS(next,distance+graph[now][next],cnt+1)
    visited[next] = 0

while True:
  M,N = map(int,input().split())
  if not N:
    break
  room = []
  for i in range(N):
    room.append([*input().strip()])

  numdict = {}
  dirty = {}
  num = 0
  for y in range(N):
    for x in range(M):
      if room[y][x] == "o":
        robot = (y,x)
      elif room[y][x] == "*":
        num += 1
        numdict[(y,x)] = num
        dirty[num] = (y,x)

  result = INF
  graph = [[INF]*(num+1) for i in range(num+1)]
  BFS(*robot,0)
  
  for i in range(1,num+1):
    if graph[0][i] == INF:
      result = -1
      break
  if result == -1:
    print(-1)
    continue

  for i in range(1,num):
    BFS(*dirty[i],i)

  visited = [0]*(num+1)
  DFS(0,0,0)
  print(result)