mus=[int(input()) for _ in range(10)]
ans=0

for j in range(1,11):
    score=sum(mus[:j])
    if abs(100-score)<=abs(100-ans):
        if abs(100-score)==abs(100-ans):
            ans=max(score,ans)
        else:
            ans=score
print(ans)