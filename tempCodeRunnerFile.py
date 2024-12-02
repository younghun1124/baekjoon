def mat_chain_X_DP(c,n):
    s=[[0]*n for _ in range(n)]
    t=[[0]*n for _ in range(n)]
    for d in range(1,n):
        for i in range(n-d):
            j=i+d
            s[i][j]=float('inf')
            for k in range(i,j):
                if(s[i][k]+s[k+1][j]+c[i-1]*c[k]*c[j]<s[i][j]):
                    s[i][j]=s[i][k]+s[k+1][j]+c[i-1]*c[k]*c[j]
                    t[i][j]=k
    return s, t