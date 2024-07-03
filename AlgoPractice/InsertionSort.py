

def insertion(arr):
    for i in range(1, len(arr)):
        key=arr[i]
        j=i-1
        while(j>=0 and key<arr[j]):
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=key


arr=[12,45,87,14,25,36,54,28,5,45,1,25,61,32]
insertion(arr)
print(arr)