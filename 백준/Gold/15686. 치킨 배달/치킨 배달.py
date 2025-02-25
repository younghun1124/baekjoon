from itertools import combinations
from collections import defaultdict
N,M=map(int,input().split())
pos_h=[]
pos_c=[]
dist=defaultdict(list)
for r in range(N):
    for c, val in enumerate(map(int,input().split())):
        if val==1:
            pos_h.append((r,c))
        elif val==2:
            pos_c.append((r,c))
            
def calcdist(hx,hy,cx,cy):
    return abs(hx-cx)+abs(hy-cy)

for hx, hy in pos_h:
    for cx,cy in pos_c:
        dist[(hx,hy)].append(calcdist(hx,hy,cx,cy)) #모든 집에 모든 치킨집과의 거리 계산
        
mindist=int(1e9)
chickendist=[0]*len(pos_h)
visit=[False]*len(pos_c)

for comb in combinations(range(len(pos_c)),M):  
    tempmindist=0
    for h in pos_h:
        tempdhousedist=1e9
        for c in comb:#고른 조합의 치킨집에 따라
            tempdhousedist=min(tempdhousedist,dist[h][c])
        tempmindist+=tempdhousedist
    mindist=min(mindist,tempmindist)
print(mindist)