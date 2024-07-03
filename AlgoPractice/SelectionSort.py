


def selection(arr):
    for i in range(len(arr)):
        min_val=i
        for j in range(i+1,len(arr)):
            if arr[min_val]>arr[j]:
                min_val=j
        arr[min_val],arr[i]=arr[i],arr[min_val]

arr=[12,45,87,14,25,36,54,28,5,45,1,25,61,32]
selection(arr)
print(arr)