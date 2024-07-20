




def capital(s):
    res=s.split(" ")
    for i in range(len(res)):
        res[i]=res[i][0].upper()+res[i][1:]
    return " ".join(res)



s="today is a sunday, and we are going to park!!"
res=capital(s)
print(res)