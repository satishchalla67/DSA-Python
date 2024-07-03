
def linear(arr,k):
    for i in range(len(arr)):
        if k==arr[i]:
            return i
    return -1


arr=[12,45,87,14,25,36,54,28,5,45,1,25,61,32]
target=32
resIndex=linear(arr,target)
print(resIndex)