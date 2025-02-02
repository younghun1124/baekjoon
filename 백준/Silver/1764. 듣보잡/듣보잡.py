n,m =map(int, input().split())
d=set()
b=set()
for _ in range(n):
    d.add(input())
for _ in range(m):
    b.add(input())
c= d&b
print(len(c))
for i in sorted(list(c)):
    print(i)
    