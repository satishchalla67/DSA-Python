




def binary(arr,k):
    l=0
    r=len(arr)-1
    while(l<=r):
        mid=l+(r-l)//2
        if arr[mid]==k:
            return mid
        elif arr[mid]>k:
            r=mid-1
        else:
            l=mid+1
    return -1
        




arr=[12,45,87,14,25,36,54,28,5,45,1,25,61,32]
target=32
arr.sort()
resIndex=binary(arr,target)
print(resIndex)