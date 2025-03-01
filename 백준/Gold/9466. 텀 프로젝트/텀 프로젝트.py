import sys
sys.setrecursionlimit(10**6)  
input = sys.stdin.readline  

T = int(input())  

for _ in range(T):  
    N = int(input())  
    board = [0] + list(map(int, input().split()))  
    visit = [False] * (N + 1)  
    team = 0  

    for start in range(1, N + 1):  
        if not visit[start]:  
            cycle = []  
            node = start  

            while not visit[node]:  
                visit[node] = True  
                cycle.append(node)  
                node = board[node]  

            if node in cycle:  # 사이클이 존재하면
                team += len(cycle[cycle.index(node):])  

    print(N - team)
