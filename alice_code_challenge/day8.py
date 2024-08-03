n, m, k, t = map(int, input().split())
time_table = [0] * (n + 2)  # 1-indexed, n + 1을 위해 한 칸 더 추가
for _ in range(m):
    start, end = map(int, input().split())
    for i in range(start, end):
        time_table[i] += 1

sections = []
if time_table[1] < t:
    sections.append([1])

for i in range(1, n + 1):
    if time_table[i] < t:
        continue
    if time_table[i - 1] < t:
        sections[-1].append(i - 1)
    if i + 1 <= n and time_table[i + 1] < t:
        sections.append([i + 1])

if len(sections[-1]) == 1:
    sections[-1].append(n)

select_list = []
for start, end in sections:
    curr_stack = 0
    remain_section = time_table[start:end + 1]
    start_len = len(remain_section)
    temp_list = []
    while remain_section:
        remain_max = max(remain_section)
        curr_stack = t - remain_max
        remain_section = [x for x in remain_section if x != remain_max]
        temp_list.append([curr_stack, start_len - len(remain_section)])
    select_list.append([start, temp_list])

item_length = len(select_list)
dp = [0] * (k + 1)

for item in select_list:
    item_type, item_options = item
    new_dp = dp[:]
    for weight, value in item_options:
        for w in range(k, weight - 1, -1):
            new_dp[w] = max(new_dp[w], dp[w - weight] + value)
    dp = new_dp

max_time = max(dp) + sum([1 for x in time_table if x >= t])
print(max_time)
