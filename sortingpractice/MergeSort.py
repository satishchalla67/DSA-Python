

def mergePartition(arr,p,mid,q):
    n=mid-p+1
    m=q-mid
    leftSubArray=[0]*n
    rightSubArray=[0]*m

    for i in range(n):
        leftSubArray[i]=arr[p+i]
    for j in range(m):
        rightSubArray[j]=arr[mid+1+j]

    print(leftSubArray)
    print(rightSubArray)
    
    i=0
    j=0
    k=p
    while i<n and j<m:
        if leftSubArray[i]<=rightSubArray[j]:
            arr[k]=leftSubArray[i]
            i+=1
        else:
            arr[k]=rightSubArray[j]
            j+=1
        k+=1

    while i<n:
        arr[k]=leftSubArray[i]
        i+=1
        k+=1
    while j<m:
        arr[k]=rightSubArray[j]
        j+=1
        k+=1

def mergeSort(arr,p,q):
    if p<q:
        mid=p+(q-p)//2
        mergeSort(arr,p,mid)
        mergeSort(arr,mid+1,q)
        mergePartition(arr,p,mid,q)
    return arr

#Driver code
arr=[70,50,60,10,20,30,80,15]
res=mergeSort(arr,0,len(arr)-1)
print(res)