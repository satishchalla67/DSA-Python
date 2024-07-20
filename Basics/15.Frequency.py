






def freq(s):
    hash={}
    for i in range(len(s)):
        hash[s[i]]=hash.get(s[i],0)+1
    return hash





s="today is a sunday, and we are going to park!!"
res=freq(s)
print(res)