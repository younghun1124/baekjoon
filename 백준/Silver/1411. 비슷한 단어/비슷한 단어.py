n=int(input())
li=[input()for _ in range(n)]
shome={}
ans=0
for word in li:
    temp={}
    idx=0
    wordli=[]
    for c in word:
        if c not in temp:
            temp[c]=idx
            idx+=1
        wordli.append(temp[c])
    # print(word, wordli)
    wordli=tuple(wordli)
    shome[wordli]=shome.get(wordli,0)+1
for i in shome:
    # print(i,shome[i])
    N=shome[i]
    ans+=N*(N-1)//2
print(ans)