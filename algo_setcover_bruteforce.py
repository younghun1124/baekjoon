from itertools import combinations

def is_cover(sets, U):
    """부분 집합들의 집합이 U를 덮는지 확인"""
    covered = set()
    for s in sets:
        covered.update(s)
    return covered == U

def set_cover(U, subsets):
    """집합 커버 문제에서 최적해를 찾기 위한 완전 탐색"""
    n = len(subsets)
    
    # 부분 집합들의 모든 조합을 검사
    for r in range(1, n+1):
        for comb in combinations(subsets, r):
            if is_cover(comb, U):
                return list(comb)  # 최소 크기 조합을 찾으면 바로 반환

    return []  # 모든 부분 집합 조합을 검사했으나 덮을 수 없을 경우

# 예시 사용
U = {1, 2, 3, 4, 5, 6, 7,8}  # 전체 집합
subsets = [{1, 2, 3}, {2, 3, 4, 8}, {3, 5, 7}, {1, 2, 5, 8}, {2, 4, 6, 8}, {1, 3, 5}]  # 부분 집합들

result = set_cover(U, subsets)

print("최소 부분 집합들:")
for subset in result:
    print(subset)
