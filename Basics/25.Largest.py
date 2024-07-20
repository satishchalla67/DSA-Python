
def heap(arr):
    n=len(arr)
    startindex=n//2-1
    for i in range(startindex,-1,-1):
        heapify(arr,n,i)

def heapify(arr,n,i):
    largest=i
    l=2*i+1
    r=2*i+2
    if l<n and arr[l]>arr[largest]:
        largest=l
    if r<n and arr[r]>arr[largest]:
        largest=r
    if largest!=i:
        arr[i],arr[largest]=arr[largest],arr[i]
        heapify(arr,n,largest)
def extractlargest(arr,size):
    temp=arr[0]
    arr[0],arr[size-1]=arr[size-1],arr[0]
    size-=1
    heapify(arr,size,0)
    return temp,size
def kthlargestElement(arr,k):
    heap(arr)
    size=len(arr)
    res=None
    for _ in range(k):
        res,size=extractlargest(arr,size)
    return res
    
    

arr=[1,3,77,7,84,4,5,7,9,10,23,45,67,9]
k=14
res=kthlargestElement(arr,k)
print(res)