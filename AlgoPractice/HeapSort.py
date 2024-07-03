
from heapq import heapify
from heapq import heappop

def heapsort(arr):
    heapify(arr)
    res=[]
    for i in range(len(arr)):
        res.append(heappop(arr))
    return res



arr=[12,45,87,14,25,36,54,28,5,45,1,25,61,32]
res=heapsort(arr)
print(res)