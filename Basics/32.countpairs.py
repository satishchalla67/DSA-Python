#Time complexity o(n2)
def countpairs(arr,sum):
    count=0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i]+arr[j]==sum:
                count+=1
    return count


def countpairs2(arr,sum):
    freq={}
    count=0
    for i in arr:
        compliment=sum-i
        if compliment in freq:
            count+=freq[compliment]
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    return count



#Find the count of pairs with a given sum in an array.
arr=[1,2,4,5,6,7,1,2,3,4,5,5,6,6]
sum=10
res=countpairs(arr,sum)
print(res)