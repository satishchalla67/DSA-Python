

def findSum(arr, target):
    l=0
    r=len(arr)-1
    while(l<=r):
        currentSum=arr[l]+arr[r]
        if(currentSum==target):
            return (l,r)
        elif(currentSum>target):
            r=r-1
        else:
            l=l+1
    return -1



#Find 2 index which are equal to the given sum
arr=[20, 40, 60, 80, 90, 120, 240]
target=210
index1, index2=findSum(arr, target)
print(index1)
print(index2) 