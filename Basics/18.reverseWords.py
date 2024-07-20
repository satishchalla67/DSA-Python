




def reverseWords(s):
    res=s.split(" ")
    n=len(res)
    for i in range(n//2):
        res[i],res[n-1-i]=res[n-1-i],res[i]
    return " ".join(res)





s="Today is monday and iam going to school"
res=reverseWords(s)
print(res)