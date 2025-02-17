def solution(numbers):
    # 숫자들을 문자열로 변환
    numbers = list(map(str, numbers))
    
    # 숫자들을 정렬하는 함수
    numbers.sort(key=lambda x: x*4, reverse=True)
    
    # 정렬된 숫자들을 이어 붙임
    result = ''.join(numbers)
    
    # 결과가 '0'으로만 이루어져 있다면 "0" 반환
    if result[0] == '0':
        return '0'
    
    return result
