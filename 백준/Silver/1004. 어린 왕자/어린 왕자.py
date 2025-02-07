import math
def is_in_circle(x,y,circle):
    circle_x,circle_y,r=circle
    dist=math.sqrt((circle_x-x)**2+(circle_y-y)**2)
    if dist<r:
        return True
    else:
        return False

t=int(input())
for _ in range(t):
    x1,y1,x2,y2=map(int,input().split())
    n=int(input())
    circles=[list(map(int,input().split())) for _ in range(n)]
    count=0
    for circle in circles:
        if is_in_circle(x1,y1,circle):
            if not is_in_circle(x2,y2,circle):
                count+=1
        if not is_in_circle(x1,y1,circle):
            if is_in_circle(x2,y2,circle):
                count+=1

    print(count)