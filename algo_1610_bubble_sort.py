def bubble_sort(s):
    for p in range(len(s)-1):
        for i in range(len(s)-p-1):
            if(s[i]>s[i+1]):
                s[i],s[i+1]=s[i+1],s[i]
        print(p+1, s)
    return s

t=[40,10,50,90,20,80,30,60]

print(bubble_sort(t))
        
        