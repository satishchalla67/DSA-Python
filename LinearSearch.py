def search(arr, x):
    for i in range(0, len(arr)):
        if arr[i]==x:
            return i
    return -1

arr=[20, 45, 27, 47, 55, 67, 75, 88, 90]
x=100
result=search(arr, x)
print(result)