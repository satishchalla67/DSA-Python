
def binarysearch(arr,x,l,r):
    mid=l+(r-l)//2
    if(arr[mid]==x):
        return mid
    elif(arr[mid]>x):
        return binarysearch(arr,x,l,mid-1)
    else:
        return binarysearch(arr,x,mid+1,r)
    return -1


array = [20, 30, 40, 50, 60, 70, 80, 90]
n=len(array)-1
x=90
print(binarysearch(array,x,0,n))