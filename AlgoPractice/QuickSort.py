
def partition(arr,i,j):
    pivot=arr[i]
    p=i
    q=p+1
    while(q<=j):
        if arr[q]<=pivot:
            p=p+1
            arr[p],arr[q]=arr[q],arr[p]
        q=q+1
    arr[i],arr[p]=arr[p],arr[i]
    return p

def quick(arr,i,j):
    if i<j:
        mid=partition(arr,i,j)
        quick(arr,i,mid-1)
        quick(arr,mid+1,j)
    return arr


arr=[12,45,87,14,25,36,54,28,5,45,1,25,61,32]
i=0
j=len(arr)-1
res=quick(arr,i,j)
print(res)