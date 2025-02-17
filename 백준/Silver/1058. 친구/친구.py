n = int(input())
board = {i: set() for i in range(n)}  # 모든 사람을 key로 갖는 딕셔너리 생성

for i in range(n):
    row = input().strip()
    for idx, val in enumerate(row):
        if val == 'Y':
            board[i].add(idx)

ans = [0] * n

for i in range(n):  # 모든 사람을 검사
    for k in range(n):
        if i == k:  # 자기 자신은 스킵
            continue
        if k in board[i]:  # 직접 친구면
            ans[i] += 1
        else:
            for j in board[i]:  # i의 친구들만 검사
                if k in board[j]:  # i의 친구 j가 k와도 친구라면
                    ans[i] += 1
                    break  # 중복 카운트 방지

print(max(ans))
