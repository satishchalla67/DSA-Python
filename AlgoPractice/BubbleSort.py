

def bubblesort(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i]>arr[j]:
                arr[i],arr[j]=arr[j],arr[i]


arr=[12,45,87,14,25,36,54,28,5,45,1,25,61,32]
bubblesort(arr)
print(arr)