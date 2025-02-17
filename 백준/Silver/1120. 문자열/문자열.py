def calcdiff(A,B,offset):
    cnt=0
    for i in range(len(A)):
        if A[i]!=B[i+offset]:
            cnt+=1
    return cnt

A,B=input().split()
diff=len(A)+10
for offset in range(len(B)-len(A)+1):
    diff=min(calcdiff(A,B,offset),diff)
print(diff)