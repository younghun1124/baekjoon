def insertion_sort(s):
    n=len(s)
    for i in range(1,n):
        print(s)
        current=s[i]
        j= i-1
        while(j>=0 and s[j]>current):            
            s[j+1]=s[j]
            j=j-1
        s[j+1]=current
    return s
    

t=[40,10,50,90,20,80,30,60]
print(insertion_sort(t))