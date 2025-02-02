import sys
input = sys.stdin.readline
output = sys.stdout.write

n, f, T = map(int, input().split())
t = [tuple(map(int, input().split())) for _ in range(n)]
friend = {}

for _ in range(f):
    c, d = map(int, input().split())
    friend.setdefault(c, []).append(d)

ans = [0] * (T + 1)  # 차이 배열을 위한 크기 (T+1)

# 차이 배열을 이용한 갱신
for i in range(1, n + 1):
    if i in friend:
        for j in friend[i]:
            start = max(t[i - 1][0], t[j - 1][0])
            end = min(t[i - 1][1], t[j - 1][1])
            if start < end:  # 유효한 시간 구간만 갱신
                ans[start] += 1
                ans[end] -= 1  # end에서 감소

# 누적 합 계산 (Prefix Sum)
for k in range(1, T):
    ans[k] += ans[k - 1]

# 출력
output("\n".join(map(str, ans[:T])) + "\n")
