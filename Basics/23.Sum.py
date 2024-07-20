




def add(arr):
    sm=0
    for i in range(len(arr)):
        sm+=arr[i]
    return sm



arr=[1,2,3,4,5,6,7,8,9]
res=add(arr)
print(res)