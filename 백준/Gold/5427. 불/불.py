from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(n, m):
    dq_fire = deque()
    dq_man = deque()
    visit_fire = [[-1] * m for _ in range(n)]  # -1은 아직 불이 닿지 않은 상태
    
    for ridx, row in enumerate(board):
        for cidx, cell in enumerate(row):
            if cell == '*':
                dq_fire.append((ridx, cidx))
                visit_fire[ridx][cidx] = 0
            elif cell == '@':
                dq_man.append((ridx, cidx, 0))  # 초기 시간 포함
    
    # 불 먼저 확산
    while dq_fire:
        fire_x, fire_y = dq_fire.popleft()
        for i in range(4):
            fire_nx, fire_ny = fire_x + dx[i], fire_y + dy[i]
            if 0 <= fire_nx < n and 0 <= fire_ny < m:
                if board[fire_nx][fire_ny] != '#' and visit_fire[fire_nx][fire_ny] == -1:
                    visit_fire[fire_nx][fire_ny] = visit_fire[fire_x][fire_y] + 1
                    dq_fire.append((fire_nx, fire_ny))
    
    visited = [[False] * m for _ in range(n)]  # 상근이의 방문 여부
    is_escape = False

    while dq_man and not is_escape:
        man_x, man_y, t = dq_man.popleft()
        
        for i in range(4):
            man_nx, man_ny = man_x + dx[i], man_y + dy[i]
            
            # 탈출 조건
            if man_nx < 0 or man_nx >= n or man_ny < 0 or man_ny >= m:
                is_escape = True
                print(t + 1)
                break
            
            # 다음 이동 가능한 조건
            if not visited[man_nx][man_ny] and board[man_nx][man_ny] == '.':
                if visit_fire[man_nx][man_ny] == -1 or visit_fire[man_nx][man_ny] > t + 1:
                    visited[man_nx][man_ny] = True
                    dq_man.append((man_nx, man_ny, t + 1))
    
    if not is_escape:
        print('IMPOSSIBLE')

t = int(input())
for _ in range(t):
    m, n = map(int, input().split())
    board = [list(input().strip()) for _ in range(n)]
    bfs(n, m)
