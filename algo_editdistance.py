s="strong"
t="stone"



def edit_distance(s, t):
    m = len(s)
    n = len(t)
    E = [[0] * (n + 1) for _ in range(m + 1)]
    for x in range(n+1):
        E[0][x]=x
    for x in range(m+1):
        E[x][0]=x
    for i in range(m+1):
        for j in range(n+1):
            if(s[i-2]==t[j-2]):
                E[i][j]=E[i-1][j-1]
            else:
                E[i][j]=min(E[i-1][j]+1,E[i-1][j-1]+1,E[i][j-1]+1)
    return E[m][n]

print(edit_distance(s,t))
    
