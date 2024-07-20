
def longestsub(s):
    char=set()
    l=0
    maxlen=0
    maxsub=""
    for r in range(len(s)):
        while s[r] in char:
            char.remove(s[l])
            l+=1
        char.add(s[r])
        if r-l+1>maxlen:
            maxlen=r-l+1
            maxsub=s[l:r+1]
    return maxsub



s="abeabaehjklankiolnmsbhfnjyaeiomn"
res=longestsub(s)
print(res)
