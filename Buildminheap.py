
import heapq

def buidheap(arr,n):
    startIndex=n//2-1
    for i in range(startIndex, -1,-1):
         heap(arr,n,i)
def heap(arr,n,i):
        smallest=i
        l=2*i+1
        r=2*i+2
        if(l<n and arr[l]<arr[smallest]):
              smallest=l
        if(r<n and arr[r]<arr[smallest]):
              smallest=r
        if smallest != i:
              arr[i], arr[smallest] = arr[smallest], arr[i]
              heap(arr, n, smallest)

arr=[145,40,25,65,12,48,18]
n=len(arr)
buidheap(arr,n)



print(arr)

res=[]
for i in range(n):
      res.append(heapq.heappop(arr))

print(res)