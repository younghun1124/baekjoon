a=input()
for x in a:
    if 'A'<=x and x<='Z':
        print(x.lower(),end="")
    else:
        print(x,end="")