s1=input()
s2=input()

D=[[0]*(len(s2)+1) for _ in range(len(s1)+1)]
for i in range(1,len(s1)+1):
    for j in range(1,len(s2)+1):
        if s1[i-1]==s2[j-1]:
            D[i][j]=D[i-1][j-1]+1
        else:
            D[i][j]=max(D[i-1][j],D[i][j-1])
print(D[-1][-1])