

def intersect(a,b):
    return [b[i] for i in range(len(b)) if b[i] in a]

def intersect2(a,b):
    res=set(a) & set(b)
    return list(res)

a=[1,3,4,5,7,8,9]
b=[2,4,6,8,10]
res=intersect2(a,b)
print(res)