def set_cover_problem(U, subsets):
    covered = set()  # 현재 커버된 원소들
    selected_subsets = []  # 선택된 부분 집합의 인덱스

    while len(covered) < len(U):
        best_subset = -1
        best_cover = 0
        
        for i, subset in enumerate(subsets):
            cover_size = len(set(subset) - covered)
            if cover_size > best_cover:
                best_cover = cover_size
                best_subset = i

        selected_subsets.append(best_subset + 1)  # 인덱스는 1부터 시작
        covered.update(subsets[best_subset])  # 선택한 부분 집합으로 커버 업데이트

    return selected_subsets

# 입력 처리
U = list(map(int, input().split()))  # 전체 집합 U
m = int(input())  # 부분 집합의 개수
subsets = []

for _ in range(m):
    subset = list(map(int, input().split()))
    subsets.append(subset[1:])  # 첫 번째 원소는 집합의 크기이므로 제외

# 집합 커버 문제 해결
selected_subsets = set_cover_problem(U, subsets)

# 결과 출력
print(" ".join(map(str, selected_subsets)) + " ")  # 선택된 부분 집합 인덱스 출력 (끝에 공백 추가)
print(len(selected_subsets))  # 선택된 부분 집합의 개수 출력
