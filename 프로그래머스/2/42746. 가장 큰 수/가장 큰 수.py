from functools import cmp_to_key

def solution(numbers):
    # 숫자를 문자열로 변환
    numbers = list(map(str, numbers))
    
    # 두 숫자를 이어 붙였을 때 더 큰 값이 나오도록 비교하는 함수
    def compare(x, y):
        if x + y > y + x:
            return -1  # x가 먼저 오는 것이 더 큼
        elif x + y < y + x:
            return 1   # y가 먼저 오는 것이 더 큼
        else:
            return 0   # 두 값이 같음
    
    # 비교 함수로 정렬
    numbers.sort(key=cmp_to_key(compare))
    
    # 정렬된 숫자들을 이어 붙임
    result = ''.join(numbers)
    
    # 결과가 '0'으로만 이루어져 있다면 "0" 반환
    if result[0] == '0':
        return '0'
    
    return result
