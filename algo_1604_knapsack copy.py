class Item:
    def __init__(self, weight, value, index):
        self.weight = weight
        self.value = value
        self.index = index
        self.ratio = value / weight

def fractional_knapsack(n, items, capacity):
    # 아이템을 가치 대비 무게 비율로 내림차순 정렬
    items.sort(key=lambda x: x.ratio, reverse=True)

    total_value = 0
    selected_items = []

    for item in items:
        if capacity <= 0:
            break

        if item.weight <= capacity:
            # 아이템을 전부 담을 수 있는 경우
            selected_items.append((item.index, 1.0))
            total_value += item.value
            capacity -= item.weight
        else:
            # 아이템의 일부만 담아야 하는 경우
            fraction = capacity / item.weight
            selected_items.append((item.index, fraction))
            total_value += item.value * fraction
            capacity = 0  # 배낭이 가득 찼으므로 capacity를 0으로 설정

    return selected_items, total_value

# 입력 처리
n = int(input())
items = []

for i in range(n):
    w, v = map(int, input().split())
    items.append(Item(w, v, i))

capacity = int(input())

# 알고리즘 실행
selected_items, total_value = fractional_knapsack(n, items, capacity)

# 결과 출력
for index, fraction in selected_items:
    print(index, fraction)

print(int(total_value))
