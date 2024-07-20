
def validShuffle(s1,s2,s3):
    hash1={}
    hash2={}
    for i in range(len(s1)):
        hash1[s1[i]]=hash1.get(s1[i],0)+1
    for i in range(len(s2)):
        hash1[s2[i]]=hash1.get(s2[i],0)+1
    for i in range(len(s3)):
        hash2[s3[i]]=hash2.get(s3[i],0)+1
    for i in range(len(s3)):
        if hash2.get(s3[i])!=hash1.get(s3[i]):
            return False
    return True

    
#Check if a string is a valid shuffle of two other strings.
s1="satish"
s2="challa"
s3="satichalshla"
res=validShuffle(s1,s2,s3)
print(res)