import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

# CCTV의 위치와 타입 저장
cctvs = []
for i in range(n):
    for j in range(m):
        if board[i][j] in [1, 2, 3, 4, 5]:
            cctvs.append((i, j, board[i][j]))

# 방향별 변화량 (상, 우, 하, 좌)
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# CCTV 타입별 가능한 방향
cctv_directions = {
    1: [[0], [1], [2], [3]],
    2: [[0, 2], [1, 3]],
    3: [[0, 1], [1, 2], [2, 3], [3, 0]],
    4: [[0, 1, 3], [0, 1, 2], [1, 2, 3], [0, 2, 3]],
    5: [[0, 1, 2, 3]],
}

# CCTV가 감시하는 영역 표시
def mark(board, r, c, dirs, value):
    for d in dirs:
        nr, nc = r, c
        while 0 <= nr < n and 0 <= nc < m and board[nr][nc] != 6:
            if board[nr][nc] == 0:
                board[nr][nc] = value
            nr += directions[d][0]
            nc += directions[d][1]

# 백트래킹 함수
def backtrack(depth, board):
    global result

    if depth == len(cctvs):
        # 남은 빈칸 수 계산
        result = min(result, sum(row.count(0) for row in board))
        return

    r, c, cctv_type = cctvs[depth]
    for dirs in cctv_directions[cctv_type]:
        # 현재 방향으로 CCTV 표시
        mark(board, r, c, dirs, '#')
        backtrack(depth + 1, board)
        # 표시 복원
        mark(board, r, c, dirs, 0)

# 결과 저장 변수
result = float('inf')

# 백트래킹 시작
backtrack(0, board)
print(result)
