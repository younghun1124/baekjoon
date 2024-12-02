def matrix_chain_order(p, n):
    # dp 테이블 초기화
    m = [[0] * n for _ in range(n)]
    s = [[0] * n for _ in range(n)]
    
    # 연쇄 행렬 곱셈 계산
    for l in range(1, n):
        for i in range(n - l):
            j = i + l
            m[i][j] = float("inf")
            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k
    return m, s

def get_optimal_parens(s, i, j):
    if i == j:
        return "M" + str(i + 1)
    else:
        return "(" + get_optimal_parens(s, i, s[i][j]) + get_optimal_parens(s, s[i][j] + 1, j) + ")"

# 입력 처리
n = int(input())
dimensions = []
first_row = True

# 행렬 크기 입력 처리
for i in range(n):
    r, c = map(int, input().split())
    if first_row:
        dimensions.append(r)
        first_row = False
    dimensions.append(c)

# 최적의 곱셈 순서 계산
m, s = matrix_chain_order(dimensions, n)

# 결과 출력
print(str(m[0][n-1]))
print(get_optimal_parens(s, 0, n-1))
