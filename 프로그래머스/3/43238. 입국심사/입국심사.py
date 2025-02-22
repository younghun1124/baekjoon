def solution(n, times):
    times.sort()
    answer = 0
    s=0
    e=max(times)*n
    while s<=e:
        m=(s+e)//2 #m 시간 동안 심사한다고 했을때
        people=0
        for time in times:
            people+=m//time
            if people>=n:
                break
        if people>=n:#시간 안에 모두 심사
            answer=m
            e=m-1
        else :
            s=m+1
    return answer