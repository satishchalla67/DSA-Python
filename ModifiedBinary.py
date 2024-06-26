import math
def findFirstInfinity(arr):
    l=0
    r=len(arr)-1
    while(l<=r):
        mid=l+(r-l)//2
        if math.isinf(arr[mid]):
            if(mid==0 or not math.isinf(arr[mid-1])):
                return mid
            else:
                r=mid-1
        else:
            l=mid+1
    return -1

# find the index of first occurence of infinity
arr=[-23,40,55,1,2,27,-89,float('inf'),float('inf'),float('inf'),float('inf')]
index=findFirstInfinity(arr)
print(index)