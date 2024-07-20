












def missingNum(arr,n):
    nsum=n*(n+1)//2
    return nsum-sum(arr)


arr=[1,2,3,4,5,6,8,9,10,11,12,13]
n=13
res=missingNum(arr,n)
print(res)
