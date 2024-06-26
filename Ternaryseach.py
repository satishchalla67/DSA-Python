

def ternarysearch(arr,target,l,r):
    while(l<=r):
        mid1=l+(r-l)//3
        mid2=r-(r-l)//3
        if(arr[mid1]==target):
            return mid1
        elif(arr[mid2]==target):
            return mid2
        elif(arr[mid1]>target):
            return ternarysearch(arr,target,l,mid1-1)
        elif(arr[mid2]<target):
            return ternarysearch(arr,target,mid2+1,r)
        else:
            return ternarysearch(arr,target,mid1+1,mid2-1)
    return -1




arr=[20,25,47,56,59,63,65,79,82]
target=65
index=ternarysearch(arr,target,0,len(arr)-1)
print(index)