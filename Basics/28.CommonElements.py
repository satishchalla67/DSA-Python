





def common(m,n):
    res=[]
    if len(m)>len(n):
        m,n=n,m
    for i in range(len(m)):
        if m[i] in n:
            res.append(m[i])
    return res

#Find the common elements in two arrays.
m=[1,2,3,4,5,6,7]
n=[7,3,1,8,9]
res=common(m,n)
print(res)