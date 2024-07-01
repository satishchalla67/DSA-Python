

def powerofn(a,n):
    if n<0:
        a=1/a
        n=-n
    if n==0:
        return 1
    if n==1:
        return a
    if n%2==0:
        res=powerofn(a,n//2)*powerofn(a,n//2)
    else:
        res=a*powerofn(a,n//2)*powerofn(a,n//2)
    return res


a=2
n=-17
res=powerofn(a,n)
print(res)
print(2**-17)