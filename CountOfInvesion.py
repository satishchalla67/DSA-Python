


def mergeProcedure(arr, p, mid, q):
    count=0
    n = mid - p + 1
    m = q - mid
    leftSubArray = [0] * n
    rightSubArray = [0] * m

    for i in range(n):
        leftSubArray[i] = arr[p + i]
    for j in range(m):
        rightSubArray[j] = arr[mid + 1 + j]

    i = 0
    j = 0
    k = p

    while i < n and j < m:
        if leftSubArray[i] <= rightSubArray[j]:
            arr[k] = leftSubArray[i]
            i += 1
        else:
            arr[k] = rightSubArray[j]
            j += 1
            count+=m-i
        k += 1

    while i < n:
        arr[k] = leftSubArray[i]
        i += 1
        k += 1

    while j < m:
        arr[k] = rightSubArray[j]
        j += 1
        k += 1
    return count


def countInversion(arr,p,q):
    if p>=q:
        return 0
    mid=p+(q-p)//2
    leftSum=countInversion(arr,p,mid)
    righSum=countInversion(arr,mid+1,q)
    combinemerge=mergeProcedure(arr,p,mid,q)
    return righSum+leftSum+combinemerge

arr=[70,50,60,10,20,30,80,15]
inversions=countInversion(arr,0,len(arr)-1)
print(inversions)