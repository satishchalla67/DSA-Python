def partition(arr,p,q):
    i=p
    j=i+1
    while j<=q:
        if arr[j]<arr[p]:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
        j=j+1
    arr[i],arr[p]=arr[p],arr[i]
    return i

def quickSort(arr,p,q):
    if p<=q:
        mid=partition(arr,p,q)
        quickSort(arr,p,mid-1)
        quickSort(arr,mid+1,q)
    return arr


arr = [50, 70, 29, 67, 12, 15, 46, 100, 26, 29]
p=0
q=len(arr)-1
res=quickSort(arr,p,q)
print(res)