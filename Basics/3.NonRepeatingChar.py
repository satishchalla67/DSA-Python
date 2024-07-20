


def nonrepeat(s):
    hash={}
    for i in range(len(s)):
        hash[s[i].lower()]=hash.get(s[i],0)+1
    for k,v in hash.items():
        if v==1:
            return k
    return -1



s="Satish"
res=nonrepeat(s)
print(res)