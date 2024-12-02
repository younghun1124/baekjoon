import heapq as hq

def prim(start):
    heap = list()
    # 연결되어 있는지 확인하는 리스트
    connected = [False] * (NODE_CNT + 1)
    
    sum_w = 0
    
    hq.heappush(heap, (0, start, -1))  # 출발 노드와 이전 노드(-1) 정보 추가
    
    # 우선순위 큐에 데이터가 있는 동안
    while heap:
        weight, v, u = hq.heappop(heap)  # (가중치, 현재 노드, 이전 노드)로 받음
        # 뺀 노드가 그래프에 포함되어 있지 않은 경우
        if not connected[v]:
            # 그래프에 포함 처리
            connected[v] = True
            if u != -1:  # 시작 노드는 제외하고, 간선 출력
                if u != -1:  # 시작 노드는 제외하고, 간선 출력
                 print(min(u, v), max(u, v), weight)  # 항상 작은 번호가 먼저 오도록 정렬

            
            
            for i in range(1, NODE_CNT + 1):
                if graph[v][i] != 0 and not connected[i]:
                    hq.heappush(heap, (graph[v][i], i, v))  # i로 가는 간선과 현재 노드(v) 정보 추가
                    
if __name__ == "__main__":
    #내 코드
    NODE_CNT, M = map(int, input().split())
    graph = [[0] * (NODE_CNT + 1) for _ in range(NODE_CNT + 1)]
    
    for _ in range(M):
        i, j, k = map(int, input().split())
        graph[i][j] = k
        graph[j][i] = k  # 무방향 그래프이므로 대칭적으로 간선 추가
                
    prim(0)  # 노드는 1부터 시작한다고 가정
