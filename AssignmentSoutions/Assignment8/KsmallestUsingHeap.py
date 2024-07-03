# 1. Kth smallest element [Amazon]
# Given an array of n-elements and an integer k, find the kth smallest element present in
# an array.
# For example:
# arr = [40, 25, 68, 79, 52, 66, 89, 97]
# k = 2
# result = 40

from heapq import heappop


def heapify(arr):
    n=len(arr)-1
    start=n//2-1
    for i in range(start, -1, -1):
        heap(arr,n,i)

def heap(arr,n,i):
    l=2*i+1
    r=2*i+2
    smallest=i
    if l<n and arr[smallest]>arr[l]:
        smallest=l
    if r<n and arr[smallest]>arr[r]:
        smallest=r
    if smallest!=i:
        arr[i], arr[smallest]=arr[smallest],arr[i]
        heap(arr,n,smallest)


def kSmallest(arr, k):
    heapify(arr)
    res=None
    while(k>0):
        res=heappop(arr)
        k=k-1
    return res



arr = [40, 25, 68, 79, 52, 66, 89, 97]
k = 2
res=kSmallest(arr, k)
print(res)