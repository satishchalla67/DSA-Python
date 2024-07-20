







def removeDup(arr):
    res=""
    for i in range(len(arr)):
        if arr[i] not in res:
            res+=arr[i]
    return list(res)


arr=['s','w','e','r','y','d','s','e','v','n']
res=removeDup(arr)
print(res)