import sys
from heapq import heappush, heappop

input = sys.stdin.readline

INF = 10e14
N, M, A, B, C = map(int, input().rstrip().split())

adj = [[] for _ in range(N + 1)]
costs = []

for _ in range(M):
    u, v, w = map(int, input().rstrip().split())
    adj[u].append((w, v))
    adj[v].append((w, u))
    costs.append(w)
def djk(st: int, en: int, maximum: int) -> bool:
    """
    st에서 en까지 가장 비싼 골목을 maximum이라고 두었을 때 최종 C원 이하로 갈 수 있는지의 여부를 반환한다.
    """
    # 초기화
    dist = [INF for _ in range(N + 1)]
    dist[st] = 0
    heap = [(0, st)]

    while heap:
        w, v = heappop(heap)

        # 이미 더 적은 경로로 업데이트 된 경우
        if dist[v] != w:
            continue

        for nxt_w, nxt_v in adj[v]:
            # 거리 업데이트
            cost = w + nxt_w
            # 골목의 가중치는 maximum을 넘으면 안됨
            if nxt_w <= maximum and cost < dist[nxt_v]:
                dist[nxt_v] = cost
                heappush(heap, (cost, nxt_v))
    # C원 이하로 갈 수 있는지 여부 반환
    return dist[en] <= C
# 결정문제를 통해 최소 maximum을 찾아낸다.
costs.sort() # 이진 탐색을 적용하기 위해 값 정렬
low, high = 0, len(costs) - 1
answer = INF

while low <= high:
    mid = (low + high) // 2
    if djk(A, B, costs[mid]): # maximum을 mid로 설정했을 때 결정 문제를 만족하면
        high = mid - 1  # maximum을 작게하여 탐색
        if costs[mid] < answer: # 최소값 업데이트
            answer = costs[mid]
    else: # 결정 문제를 만족하지 못하면
        low = mid + 1 # maximum을 크게하여 탐색

print(answer if answer != INF else -1)