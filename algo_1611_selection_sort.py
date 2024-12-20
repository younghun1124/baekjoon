def selection_sort(s):
    n=len(s)
    for i in range(n-1):
        print(s)
        minidx=i
       
        for j in range(i+1,n):
            if(s[j]<s[minidx]):
                minidx=j
        s[i],s[minidx]=s[minidx],s[i]
       
    return s

t=[40,10,50,90,20,80,30,60]
print(selection_sort(t))