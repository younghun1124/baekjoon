n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()  # 사전 순 출력을 위해 정렬

ans = []
used = [False] * n  # 사용 여부를 체크하는 리스트

def backtrack(depth):
    if depth == m:
        print(' '.join(map(str, ans)))  # 중복 없이 출력
        return
    
    prev = -1  # 같은 depth에서 이전 숫자를 저장
    for i in range(n):
        if not used[i] and nums[i] != prev:  # 같은 depth에서 같은 숫자는 건너뛰기
            ans.append(nums[i])
            used[i] = True
            prev = nums[i]  # 현재 숫자를 prev로 설정
            backtrack(depth + 1)
            used[i] = False
            ans.pop()

backtrack(0)
