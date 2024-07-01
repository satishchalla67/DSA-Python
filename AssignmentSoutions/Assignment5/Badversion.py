# 2. You are a product manager and currently leading a team to develop a new product.
# Unfortunately, the latest version of your product fails the quality check. Since each
# version is developed based on the previous version, all the versions after a bad version
# are also bad. Suppose you have n version and you want to find out the first bad one,
# which causes all the following ones to be bad. Also, talk about the time complexity of
# your code.
# Test Cases:
# Input: [0,0,0,1,1,1,1,1,1]
# Output: 3
# Explanation: 0 indicates a good version and 1 indicates a bad version. So, the index of
# the first 1 is at 3. Thus, the output is 3
#T(n)=o(log n)

def badVersion(arr):
    n=len(arr)
    l=0
    r=n-1
    while(l<=r):
        mid=l+(r-l)//2
        if(arr[mid]==0):
            l=mid+1
        else:
            if(mid==0 or arr[mid-1]==0):
                return mid
            else:
                r=mid-1


versions=[0,0,0,0,1,1,1,1,1,1]
badVersionIndex=badVersion(versions)
print(badVersionIndex)