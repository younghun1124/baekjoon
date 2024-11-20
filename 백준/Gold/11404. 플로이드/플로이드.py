import sys
input = sys.stdin.read
INF = float('inf')

def floyd_warshall(n, bus_info):
    # 초기 비용 테이블 생성
    dist = [[INF] * n for _ in range(n)]
    
    # 자기 자신으로 가는 비용은 0으로 설정
    for i in range(n):
        dist[i][i] = 0
    
    # 버스 정보를 이용해 초기 거리 설정
    for a, b, c in bus_info:
        a -= 1  # 도시 번호를 0부터 시작하도록 변경
        b -= 1
        dist[a][b] = min(dist[a][b], c)  # 같은 경로 여러 개일 수 있으므로 최소값 사용
    
    # 플로이드-워셜 알고리즘 실행
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    # 결과 테이블 처리
    for i in range(n):
        for j in range(n):
            if dist[i][j] == INF:  # 경로가 없는 경우
                dist[i][j] = 0
    
    return dist

# 입력 받기
data = input().splitlines()
n = int(data[0])
m = int(data[1])
bus_info = [tuple(map(int, line.split())) for line in data[2:]]

# 플로이드-워셜 수행
result = floyd_warshall(n, bus_info)

# 결과 출력
for row in result:
    print(' '.join(map(str, row)))
