a,b,c=list(map(int,input().split()))
sum=a+b+c
avg="{:.0f}".format(sum/3)
print(sum)
print()
print(sum-avg)