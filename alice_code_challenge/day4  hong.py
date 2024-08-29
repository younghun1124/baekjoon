n = int(input())

edges = []
neighbor = [set() for i in range(n + 1)]

for _ in range(n - 1):
    u, v = map(int, input().split())
    neighbor[u].add(v)
    neighbor[v].add(u)

def set_child(i):
    for j in neighbor[i]:
        neighbor[j].remove(i)
        set_child(j)

set_child(1)

dp = [-100000 for i in range(n + 1)]

def cal(i):
    if dp[i] != -100000:
        return dp[i]
    arr = []
    if len(neighbor[i]) == 0:
        dp[i] = i
        return dp[i]
    for j in neighbor[i]:
        arr.append(cal(j))
    
    dp[i] = -min(arr) + i

    return dp[i]

cal(1)

for i in range(1, n + 1):
    print(1if dp[i] >= 0 else 0)
    
