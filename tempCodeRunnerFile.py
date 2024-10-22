n, m = map(int, input().split())
k = 0
INF = 999999999999

graph = [[] for _ in range(n)]

visited = [False] * (n)
distance = [INF] * (n)

for _ in range(m):
    u, v, w = map(int, input().split())  # u: 출발노드, v: 도착노드, w: 연결된 간선의 가중치
    graph[u].append((v, w))              # 거리 정보와 도착노드를 같이 입력합니다.

def get_smallest_node():
    min_val = INF
    index = 0
    for i in range(0, n):
        if distance[i] < min_val and not visited[i]: #기존 최소보다 짧고, 방문하지 않은 노드라면
            min_val = distance[i]
            index = i
    return index

def dijkstra(start):
    distance[start] = 0  # 시작 노드는 0으로 초기화
    visited[start] = True

    for i in graph[start]: #시작 노드와 연결된 간선정보들 i
        distance[i[0]] = i[1]  # 시작 노드와 연결된 노드들의 거리 입력

    for _ in range(n - 1):
        now = get_smallest_node()  # 거리가 구해진 노드 중 가장 짧은 거리인 것을 선택
        visited[now] = True        # 방문 처리

        for j in graph[now]:
            if distance[now] + j[1] < distance[j[0]]:  #now점에 연결된 점들 중에 now를 거쳐 가는게 더 짧은 거리가 나오면
                distance[j[0]] = distance[now] + j[1]  #값을 갱신한다.
dijkstra(k)

# 결과 출력 (정점 0을 제외한 가중치 출력)
for i in range(1, n):
    print(i, distance[i])  # 정점, 가중치 순으로 출력