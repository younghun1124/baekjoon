import math

n = int(input())

for i in range(n) :
    x, y = map(int, input().split())
    print(math.ceil(math.sqrt(y-x)*2-1))