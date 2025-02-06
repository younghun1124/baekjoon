import math

n, m = map(int, input().split())
board = [list(map(int, input())) for _ in range(n)]

ans = -1

# 가능한 모든 step 크기 조합 탐색 (-n ~ n, -m ~ m)
for stepx in range(-n, n):
    for stepy in range(-m, m):
        if stepx == 0 and stepy == 0:
            continue
        # 시작점 탐색
        for x in range(n):
            for y in range(m):
                tempx, tempy = x, y
                num = 0
                # 범위를 벗어나지 않는 동안 숫자 생성
                while 0 <= tempx < n and 0 <= tempy < m:
                    num = num * 10 + board[tempx][tempy]
                    # 완전 제곱수 판별
                    if int(math.sqrt(num))**2 == num:
                        ans = max(ans, num)
                    tempx += stepx
                    tempy += stepy

print(ans)