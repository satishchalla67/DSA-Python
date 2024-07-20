

def anagram(s1,s2):
    if len(s1)!=len(s2):
        return False
    hash1={}
    hash2={}
    for i in range(len(s1)):
        hash1[s1[i]]=hash1.get(s1[i],0)+1
    for i in range(len(s2)):
        hash2[s2[i]]=hash2.get(s2[i],0)+1
    for i in s1:
        if hash1.get(i)!=hash2.get(i):
            return False
    return True



s1="peach"
s2="cheap"
res=anagram(s1,s2)
print(res)