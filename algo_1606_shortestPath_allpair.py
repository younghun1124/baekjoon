# 플로이드-워셜 알고리즘을 사용하여 모든 쌍 최단 경로를 계산하는 함수
def floyd_warshall(n, D):
    # 초기화
    dist = [[float('inf')] * n for _ in range(n)]
    
    # 초기 거리 행렬 설정
    for i in range(n):
        for j in range(n):
            if i == j:
                dist[i][j] = 0
            elif D[i][j] != -1:
                dist[i][j] = D[i][j]
    
    # 플로이드-워셜 알고리즘 적용
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] < float('inf') and dist[k][j] < float('inf'):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    # 무한대 값을 -1로 변경하여 출력 형식에 맞춤
    for i in range(n):
        for j in range(n):
            if dist[i][j] == float('inf'):
                dist[i][j] = -1
    
    return dist

# 입력 처리
n = int(input().strip())
D = [list(map(int, input().strip().split())) for _ in range(n)]

# 결과 계산
result = floyd_warshall(n, D)

# 결과 출력
for row in result:
    print(" ".join(map(str, row)))
