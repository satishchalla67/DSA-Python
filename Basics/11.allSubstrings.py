






def allSubstrings(s):
    res=[]
    for i in range(len(s)):
        for j in range(i, len(s)):
            res.append(s[i:j+1])
    return res



s="satish"
res=allSubstrings(s)
print(res)