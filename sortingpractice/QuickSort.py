
def partition(arr,p,q):
    pivot=arr[p]
    i=p
    for j in range(i+1,q+1):
        if arr[j]<=pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i],arr[p]=arr[p],arr[i]
    return i



def quickSort(arr,p,q):
    if p<q:
        mid=partition(arr,p,q)
        quickSort(arr,p,mid-1)
        quickSort(arr,mid+1,q)
    return arr



arr=[70,50,60,10,20,30,80,15]
res=quickSort(arr,0,len(arr)-1)
print(res)