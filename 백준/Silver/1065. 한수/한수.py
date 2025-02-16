n=int(input())
ans=0
if n<100:
    ans=n
else:
    ans+=99
    for i in range(100,n+1):
        if i==1000:
            continue
        i=str(i)
       
        if int(i[1])==((int(i[0])+int(i[2]))/2):
            ans+=1
        


print(ans)
    


    