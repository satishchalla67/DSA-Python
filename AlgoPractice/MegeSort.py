

def mergepartition(arr,p,mid,q):
    n=mid-p+1
    m=q-mid
    leftSubArray=[0]*n
    rightSubArray=[0]*m
    for i in range(n):
        leftSubArray[i]=arr[p+i]
    for j in range(m):
        rightSubArray[j]=arr[mid+1+j]

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
def mergesort(arr,p,q):
    if p<q:
        mid=p+(q-p)//2
        mergesort(arr,p,mid)
        mergesort(arr,mid+1,q)
        mergepartition(arr,p,mid,q)
    return arr

arr=[12,45,87,14,25,36,54,28,5,45,1,25,61,32]
p=0
q=len(arr)-1
res=mergesort(arr,p,q)
print(res)