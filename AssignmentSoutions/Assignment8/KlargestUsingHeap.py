# 3. Kth Largest Element in an array [Facebook]
# Given an integer array nums and an integer k, return the kth largest element present in
# an array.
# For example:
# arr = [40, 25, 68, 79, 52, 66, 89, 97]
# k = 2
# result = 89
from heapq import heappop

def heapify(arr):
    n=len(arr)-1
    startIndex=n//2-1
    for i in range(startIndex, -1,-1):
        heap(arr,n,i)
def heap(arr,n,i):
    l=2*i+1
    r=2*i+2
    smallest=i
    if l<n and arr[smallest]<arr[l]:
        smallest=l
    if r<n and arr[smallest]<arr[r]:
        smallest=r
    if smallest!=i:
        arr[i], arr[smallest]=arr[smallest],arr[i]
        heap(arr,n,smallest)

def Klargest(arr,k):
    heapify(arr)
    res=None
    for _ in range(len(arr) - k + 1):
        res=heappop(arr)
        k=k-1
    return res

arr = [40, 25, 68, 79, 52, 66, 89, 97]
k = 2
result = Klargest(arr,k)
print(result)