

def findmaxmin(arr,i,j):
    #small problem
    if i==j:
        max=arr[i]
        min=arr[i]
    elif i==j-1:
        if arr[i]>arr[j]:
            max=arr[i]
            min=arr[j]
        else:
            max=arr[j]
            min=arr[i]
    else:
        #divide
        mid=i+(j-i)//2
        #conquer
        max1, min1=findmaxmin(arr,i,mid)
        max2, min2=findmaxmin(arr,mid+1,j)
        #combine
        if(max1>max2):
            max=max1
        else:
            max=max2
        if(min1<min2):
            min=min1
        else:
            min=min2
    return max,min



arr=[50,24,2,35,64,85,7,15,42,35,16,24,51,20,35]
i=0
j=len(arr)-1
max,min=findmaxmin(arr,i,j)
print(max,min)