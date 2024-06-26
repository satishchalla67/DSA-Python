# #Bruteforce Approch
# def search(arr, target):
#     for i in range(len(arr)):
#         for j in range(len(arr[i])):
#             if arr[i][j]==target:
#                 return i,j
#     return -1
def binarysearch(arr, target):
    l=0
    r=len(arr)*len(arr[0])-1
    n=len(arr[0])
    while(l<=r):
        mid=l+(r-l)//2
        if(arr[mid//n][mid%n]==target):
            return mid//n, mid%n
        elif(arr[mid//n][mid%n]>target):
            r=r-1
        else:
            l=l+1
    return -1



#search for the element using BINARY SEARH
arr=[[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target=34
print(binarysearch(arr, target))