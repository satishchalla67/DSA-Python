



def lonprefix(arr):
    res=""
    for i in range(len(arr[0])):
        for j in range(len(arr)):
            if arr[0][i]!=arr[j][i]:
                return res
        res+=arr[0][i]
    return res




arr=["flick","flicker","fling"]
res=lonprefix(arr)
print(res)