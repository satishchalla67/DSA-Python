



#Brute Force Approch
#Time Complexity=O(n2)
def countInversion(arr):
    totalSum=0
    for i in range(len(arr)):
        currentSum=0
        for j in range(i+1, len(arr)):
            if arr[i]>arr[j]:
                currentSum+=1
        totalSum+=currentSum
    return totalSum

def currentSum(arr,p,q,k):
    if p>q:
        return 0
    if p==q:
        if arr[p]<k:
            return 1
        else:
            return 0
    mid=p+(q-p)//2
    leftSum=currentSum(arr,p,mid,k)
    righSum=currentSum(arr,mid+1,q,k)
    return leftSum+righSum

def countInversion2(arr):
    n=len(arr)
    totalSum=0
    for i in range(n):
        res=currentSum(arr,i+1,n-1,arr[i])
        if res:
            totalSum+=res
    return totalSum

arr=[70,50,60,10,20,30,80,15]
inversions=countInversion2(arr)
print(inversions)