

def rotateString(s1,s2):
    p=0
    q=0
    start=0
    while q<len(s2):
        if s1[p]!=s2[q]:
            q+=1
            start=q
            p=0
        elif s1[p]==s2[q]:
            p+=1
            q+=1
    p-=1
    q-=1
    if s1[0:p+1]==s2[start:q+1] and s1[p+1:len(s1)]==s2[0:start]:
        return True
    return False

def rotateString2(s1,s2):
    if len(s1)!=len(s2):
        return False
    if s2 in (s1+s1):
        return True
    return False

s1="satish"
s2="ishsa"
res=rotateString2(s1,s2)
print(res)