import sys
sys.stdin.readline
T=int(input())

def DFS(start):
    global team
    temp=[]
    node=start
    while True:
        visit[node]=True
        temp.append(node)
        node=board[node]
        if visit[node]:
            if node in temp:
                team+=len(temp)-temp.index(node)
            return
        
for _ in range(T):
    n=int(input())
    board=[0]+list(map(int,input().split()))
    visit=[False]*(n+1)
    team=0

    for start in range(1,n+1):
        if not visit[start]:
            DFS(start)

    print(n-team)