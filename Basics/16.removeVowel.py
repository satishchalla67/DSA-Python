




def removeVowel(s):
    res=""
    for i in s:
        if i not in "aeiou":
            res+=i
    return res



s="satish"
res=removeVowel(s)
print(res)