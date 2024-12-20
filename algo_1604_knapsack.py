def fractional_knapsack(n, items, capacity):
    items.sort(key=lambda x: (x[1] / x[0]), reverse=True)    
    total_value = 0  # 배낭에 담긴 총 가치
    selected_items = []  # 선택된 물건과 그 비율

    for i in range(n):
        weight, value, idx = items[i]
        if capacity >= weight:
            # 배낭에 물건을 전부 담을 수 있는 경우
            selected_items.append((idx, 1.0))
            total_value += value
            capacity -= weight
        else:
            # 배낭에 부분적으로 담아야 하는 경우
            fraction = capacity / weight
            selected_items.append((idx, fraction))  # 소수점 처리 없음
            total_value += value * fraction
            break  # 배낭 용량을 채웠으므로 반복 종료

    # 선택된 물건과 비율 출력
    for idx, frac in selected_items:
        print(idx, frac)  
    
    # 배낭에 담긴 총 가치 출력
    print(int(total_value))

# Sample Input
n = int(input())
items = [(*map(int, input().split()), x) for x in range(n)]

capacity = int(input())
fractional_knapsack(n, items, capacity)
