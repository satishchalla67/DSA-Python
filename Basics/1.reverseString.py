


def reverseString(str):
    s=list(str)
    n=len(s)
    for i in range(n//2):
        s[i],s[n-1-i]=s[n-1-i],s[i]
    return "".join(s)


#Driver Code
s="pink"
res=reverseString(s)
print(res)