
def prim_mst(n, distances):
    # MST를 저장하기 위한 리스트
    mst_edges = []
    visited = [False] * n
    visited[0] = True  # 0번 마을을 시작점으로 설정
    edges = []

    # 시작점의 모든 간선을 우선 리스트에 추가
    for i in range(1, n):
        edges.append((distances[0][i], 0, i))

    # 간선을 비용순으로 정렬
    edges.sort()

    while len(mst_edges) < n - 1:
        # 비용이 가장 낮은 간선을 가져옴
        cost, u, v = edges.pop(0)
        if not visited[v]:  # v가 방문되지 않았다면
            visited[v] = True
            mst_edges.append((cost, u, v))
            # v에 연결된 모든 간선을 추가
            for i in range(n):
                if not visited[i]:
                    edges.append((distances[v][i], v, i))
            # 간선을 비용순으로 정렬
            edges.sort()

    return mst_edges


def dfs_path(mst_edges, n, start):
    # MST를 그래프로 변환
    graph = [[] for _ in range(n)]
    for cost, u, v in mst_edges:
        graph[u].append((cost, v))
        graph[v].append((cost, u))

    # DFS로 방문 경로 생성
    visited = [False] * n
    path = []

    def dfs(node):
        visited[node] = True
        path.append(node)
        for cost, neighbor in sorted(graph[node]):
            if not visited[neighbor]:
                dfs(neighbor)

    dfs(start)
    path.append(start)  # 시작점으로 돌아옴
    return path


def tsp_approximation():
    
    import sys    
    input = sys.stdin.read  # 모든 입력 읽기
    data = input().strip().splitlines()

    # 간선 행렬 입력 처리
    distances = [list(map(int, line.split())) for line in data[1:]]
    n = int(len(distances))  # 간선 행렬의 행 수를 n으로 설정

    # MST 계산
    mst_edges = prim_mst(n, distances)

    # MST 출력
    print("MST:", " ".join("({}, {})".format(u, v) for cost, u, v in mst_edges))

    # 최종 방문 경로 계산
    path = dfs_path(mst_edges, n, 0)

    # 방문 경로 출력
    print("방문 경로:", " ".join(map(str, path)))


# 함수 실행
try:
    tsp_approximation()
except Exception as e:  # 모든 예외 처리
    print("에러가 발생했습니다:", e)


