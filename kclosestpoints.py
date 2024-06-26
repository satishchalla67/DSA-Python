


import heapq


def kclosest(points, k):
    new_points=[]
    for x,y in points:
        dis=(x**2)+(y**2)
        new_points.append([dis,x,y])
    heapq.heapify(new_points)

    res=[]
    while(k>0):
        dis, x, y=heapq.heappop(new_points)
        res.append([x,y])
        k=k-1
    return res




points=[[1,3],[-2,2]]
k=1
res=kclosest(points,k)
print(res)

#find distance and add it as a first element to inner list
#use heapify to make it a minheap
#pop k elements and store in the new list


#Time complexity
#iterating all the elements and finding thier distance takes O(n)
#heapify uses O(n)
#heappop uses log(n) and for k elements klog(n)
#total = O(n+n+klogn)