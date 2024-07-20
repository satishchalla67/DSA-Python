
def maxmin(arr):
    min=float("inf")
    max=0
    for i in range(len(arr)):
        if arr[i]>max:
            max=arr[i]
        elif arr[i]<min:
            min=arr[i]
    return max,min

arr=[1,5,16,3,8,1,9,2,19,3,7,2]
max,min=maxmin(arr)
print(f'Maximum element is: {max}')
print(f'Minimum element is: {min}')