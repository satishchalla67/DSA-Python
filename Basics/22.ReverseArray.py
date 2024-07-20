











def reverse(arr):
    n=len(arr)
    for i in range(n//2):
        arr[i],arr[n-i-1]=arr[n-1-i],arr[i]
    return arr
arr=[1,2,3,4,5,6,7,8,9,10]
res=reverse(arr)
print(res)