

def heapify(arr,n):
    num=n//2-1
    for i in range(num, -1, -1):
        heap(arr,n,i)
    

def heap(arr,n,i):
    l=2*i+1
    r=2*i+2
    smallest=i
    if(l<n and arr[smallest]>arr[l]):
        smallest=l
    if(l<n and arr[smallest]>arr[r]):
        smallest=r
    if(smallest!=i):
        arr[smallest], arr[i]=arr[i], arr[smallest]
        heap(arr,n,smallest)



arr=[145,40,25,65,12,48,18]
heapify(arr, len(arr))
print(arr)