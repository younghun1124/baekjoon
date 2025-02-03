import sys
input=sys.stdin.read
output=sys.stdout.write
data=input().splitlines()
n,m,t=map(int,data[0].split())
time=[tuple(map(int,x.split())) for x in data[1:1+n]]
friend={}
for row in data[1+n:]:
    c,d=map(int,row.split())
    friend.setdefault(c,[]).append(d)

ans=[0]*(t+1) #딱 t 까지 회의가 있으니까 t+1 이어야 함.
for i in friend:
    for j in friend[i]:
        start= max(time[i-1][0],time[j-1][0])
        end= min(time[i-1][1],time[j-1][1])
        if start<end:
            ans[start]+=1
            ans[end]-=1
for i in range(1,t+1):
    ans[i]+=ans[i-1]

output('\n'.join(map(str,ans[:t])))