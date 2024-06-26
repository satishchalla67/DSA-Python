

def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        min_index=i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index=j
        arr[i], arr[min_index]=arr[min_index], arr[i]
    return arr

arr = [59,48,100,70, 20, 50, 60, 35, 47]
sortedArr=selectionSort(arr)
print(f'Sorted array: {sortedArr}')
