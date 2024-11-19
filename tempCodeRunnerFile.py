def floyd_warshall(n, graph):
    # 최단 거리 테이블을 그래프로 초기화
    dist = [[float('inf') if x == -1 else x for x in row] for row in graph]
    
    # 자기 자신으로 가는 비용은 0으로 초기화
    for i in range(n):
        dist[i][i] = 0
    
    # k를 거쳐가는 경우를 고려하여 최단 거리 갱신
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] != float('inf') and dist[k][j] != float('inf'):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    return dist

def main():
    # 마을의 개수 입력
    n = int(input())
    
    # 그래프 정보 입력
    graph = []
    for _ in range(n):
        row = list(map(int, input().split()))
        graph.append(row)
    
    # 플로이드-워셜 알고리즘 수행
    result = floyd_warshall(n, graph)
    
    # 결과 출력
    for row in result:
        print(*row)

if __name__ == "__main__":
    main()
