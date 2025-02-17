import sys

# 입력 빠르게 받기
n = int(sys.stdin.readline().strip())
n_list = map(int, sys.stdin.readline().split())

# 딕셔너리로 숫자 개수 세기
count_dict = {}
for num in n_list:
    count_dict[num] = count_dict.get(num, 0) + 1

m = int(sys.stdin.readline().strip())
m_list = map(int, sys.stdin.readline().split())

# 결과 출력 (join 사용으로 속도 최적화)
print(' '.join(str(count_dict.get(i, 0)) for i in m_list))