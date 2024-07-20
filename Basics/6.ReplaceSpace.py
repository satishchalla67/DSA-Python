



def replacesub(s,sub):
    lst=s.split(" ")
    res=sub.join(lst)
    return res



s="Today is monday"
sub="-"
res=replacesub(s,sub)
print(res)