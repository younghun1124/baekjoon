def mat_chain_X_DP(c,n):
    s=[[0]*n for _ in range(n)]
    t=[[0]*n for _ in range(n)]
    for d in range(1,n):
        for i in range(n-d):
            j=i+d
            s[i][j]=float('inf')
            for k in range(i,j):
                if(s[i][k]+s[k+1][j]+c[i]*c[k+1]*c[j+1]<s[i][j]):
                    s[i][j]=s[i][k]+s[k+1][j]+c[i]*c[k+1]*c[j+1]
                    t[i][j]=k
    return s, t

def mat_chain_X_recap(c,n):
    s=[[0]*(n+1) for _ in range(n+1)]
    t=[[0]*(n+1) for _ in range(n+1)]
    for d in range(1,n):
        for i in range(1,n-d+1):
            j=d+i
            s[i][j]=float('inf')
            for k in range(i,j):
                if(s[i][k]+s[k+1][j]+c[i-1]*c[k]*c[j]<s[i][j]):
                    s[i][j]=s[i][k]+s[k+1][j]+c[i-1]*c[k]*c[j]
                    t[i][j]=k
    return s[1][n], s, t

c=[ 10, 5, 20, 4, 30]
print(mat_chain_X_recap(c,4))

