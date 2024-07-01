

def fibanacci(n):
    if n<=3:
        return n
    else:
        res=(n-1)+(n-2)
    return res



n=4
res=fibanacci(n)
print(res)