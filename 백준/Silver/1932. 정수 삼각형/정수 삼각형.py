import sys
input=sys.stdin.readline
n=int(input().strip())
before=[int(input().strip())]
for i in range(2,n+1):
    line=list(map(int,input().split()))
    templine=[0 for _ in range(i)]
    for idx, k in enumerate(before):
        templine[idx]=max(templine[idx],k+line[idx])
        templine[idx+1]=max(templine[idx+1],k+line[idx+1])
    before=templine

print(max(before))