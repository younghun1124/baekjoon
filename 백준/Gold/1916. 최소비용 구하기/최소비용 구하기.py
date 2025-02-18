import sys
import heapq

def main():
    input = sys.stdin.readline
    N = int(input().strip())            # 도시의 개수
    M = int(input().strip())            # 버스의 개수
    
    # 그래프 초기화: 각 도시에서 갈 수 있는 (도착 도시, 비용) 정보를 리스트에 저장
    graph = [[] for _ in range(N + 1)]
    for _ in range(M):
        u, v, cost = map(int, input().split())
        graph[u].append((v, cost))
    
    start, end = map(int, input().split())
    
    INF = float("inf")
    # 출발 도시부터 각 도시까지의 최소 비용을 저장할 리스트 초기화
    distance = [INF] * (N + 1)
    distance[start] = 0
    
    # 우선순위 큐에 (비용, 도시) 튜플을 넣음 (처음에는 출발 도시만)
    pq = [(0, start)]
    
    while pq:
        cur_cost, cur_node = heapq.heappop(pq)
        
        # 이미 더 짧은 경로로 방문한 경우 무시
        if cur_cost > distance[cur_node]:
            continue
        
        # 현재 도시와 연결된 모든 도시 확인
        for next_node, next_cost in graph[cur_node]:
            new_cost = cur_cost + next_cost
            # 기존 경로보다 더 짧은 경로를 찾으면 업데이트
            if new_cost < distance[next_node]:
                distance[next_node] = new_cost
                heapq.heappush(pq, (new_cost, next_node))
    
    # 도착 도시까지의 최소 비용 출력
    print(distance[end])

if __name__ == '__main__':
    main()