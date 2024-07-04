def partition(arr, l, r):
    pivot = arr[r]
    i = l
    for j in range(l, r):
        if arr[j] >= pivot:  # For k-th largest, use >= instead of <=
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[r] = arr[r], arr[i]
    return i

def quickselect(arr, l, r, k):
    if l <= r:
        pivot_index = partition(arr, l, r)
        if pivot_index == k:
            return arr[pivot_index]
        elif pivot_index > k:
            return quickselect(arr, l, pivot_index - 1, k)
        else:
            return quickselect(arr, pivot_index + 1, r, k)
    return -1

def find_kth_largest(arr, k):
    n = len(arr)
    # k-th largest is the (n - k)-th smallest
    return quickselect(arr, 0, n - 1, k - 1)

# Example usage
arr = [40, 25, 68, 79, 52, 66, 89, 97]
k = 2
result = find_kth_largest(arr, k)
print(result)  # Output should be 89
