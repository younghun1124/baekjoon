a=input()
for x in a:
    if 'A'<=x and x<='Z':
        print(lower(x),end="")
    else:
        print(upper(x),end="")