
def majorityElement(arr):
    candidate=None
    count=0
    n=len(arr)
    for i in range(n):
        if count==0:
            candidate=arr[i]
            count=1
        elif candidate==arr[i]:
            count+=1
        else:
            count-=1
    freqCount=0
    for i in range(n):
        if arr[i]==candidate:
            freqCount+=1
    if freqCount>n//2:
        return candidate
    else:
        return -1


#Boyer Moore Voting Algorithm
arr=[3,2,3,3,1,3,2]
res=majorityElement(arr)
print(res)
