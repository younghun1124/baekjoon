import sys
input = sys.stdin.readline
N, R = map(int, input().split())
bap = [list(map(int, input().split())) for _ in range(N)]  # 튜플 → 리스트

def is_in_wok(x, y, bx, by):
    return (x - bx) ** 2 + (y - by) ** 2 <= R ** 2  # 튜플 언패킹 제거

ans = 0
count = 0
for X in range(-100, 100):  # 101 → 100
    for Y in range(-100, 100):
        temp = sum(1 for bx, by in bap if is_in_wok(X, Y, bx, by))  # 리스트 컴프리헨션 사용
        if count < temp:
            count = temp
            ans = (X, Y)

print(ans[0], ans[1])
