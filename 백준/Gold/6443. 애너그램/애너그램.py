import sys
input=sys.stdin.readline
output=sys.stdout.write

n=int(input().strip())
def backtrack(depth):
    if depth==wordlen:
        print(''.join(ans))
        return
    prev='*'
    for i in range(wordlen):
        if used[i]==False and prev!=word[i]:
            used[i]=True
            ans[depth]=(word[i])
            backtrack(depth+1)
            used[i]=False
            prev=word[i] #방금 했던거 또 안들어가게 하기
        
    
for _ in range(n):
    word=list(map(str,input().strip()))
    word.sort()
    used=[False]*len(word)
    ans=['']*len(word)
    wordlen=len(word)
    backtrack(0)