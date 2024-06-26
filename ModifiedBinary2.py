
import math
def searchInfinity(arr):
    #search exponentially untill we find infinity
    i=1
    while True:
        try:
            if(math.isinf(arr[i])):
                break
            i*=2
        except IndexError:
            break
    l = max(0, i // 2)
    r = i

    while(l<=r):
        mid=l+(r-l)//2
        if(math.isinf(arr[mid])):
            if(mid==0 or not math.isinf(arr[mid-1])):
                return mid
            else:
                r=mid+1
        else:
            l=mid+1
    return -1



#we are not aware of size of the array
#After a series of int we have infinities and so on, find the index of first index of infinity
arr = [-23,40,55,1,2,27,-89,float('inf'),float('inf'),float('inf'),float('inf'),float('inf'),float('inf'),float('inf'),float('inf')]
index=searchInfinity(arr)
print(index)