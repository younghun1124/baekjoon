import math
xa,ya,xb,yb,xc,yc=map(int,input().split())

def calc_dist(x1,y1,x2,y2):
    return math.sqrt((x1-x2)**2+(y2-y1)**2)
xa,ya,xb,yb,xc,yc

def calc_slope(x1,y1,x2,y2):
    if x1==x2:
        return float("inf")
    return (y1-y2)/(x1-x2)

if calc_slope(xa,ya,xb,yb)==calc_slope(xa,ya,xc,yc):
    print(-1)
else:
    s1=(calc_dist(xa,ya,xb,yb)+calc_dist(xb,yb,xc,yc))*2
    s2=(calc_dist(xa,ya,xc,yc)+calc_dist(xb,yb,xc,yc))*2
    s3=(calc_dist(xa,ya,xb,yb)+calc_dist(xa,ya,xc,yc))*2
    ans=max(s1,s2,s3)-min(s1,s2,s3)
    print(ans)