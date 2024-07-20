
def movezero(arr):
    res=[]
    for i in range(len(arr)):
        if arr[i]!=0:
            res.append(arr[i])
    dif=len(arr)-len(res)
    return res+[0]*dif


arr=[1,0,2,0,0,3,4,0]
res=movezero(arr)
print(res)