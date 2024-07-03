

def ternary(arr,k,l,r):
    while(l<=r):
        mid1=l+(r-l)//3
        mid2=r-(r-l)//3
        if arr[mid1]==k:
            return mid1
        elif arr[mid2]==k:
            return mid2
        elif k<arr[mid1]:
            return ternary(arr,k,l,mid1-1)
        elif k>arr[mid2]:
            return ternary(arr,k,mid2+1,r)
        else:
            return ternary(arr,k,mid1+1,mid2-1)

arr=[1, 5, 12, 14, 25, 25, 28, 32, 36, 45, 45, 54, 61, 87]
target=1
i=0
j=len(arr)-1
resIndex=ternary(arr,target,i,j)
print(resIndex)