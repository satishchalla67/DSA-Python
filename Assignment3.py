# 3. Given a positive integer num, write a program that returns True if num is a perfect
# square else return False. Do not use built-in functions like sqrt. Also, talk about the time
# complexity of your code.
# Test Cases:
# Input: 16
# Output: True
# Input: 14
# Output: False

def isPerfectSquare(num):
    arr=[]
    for i in range(1, num//2):
        arr.append(i*i)
    l=0
    r=len(arr)-1
    while(l<=r):
        mid=l+(r-l)//2
        if arr[mid]==num:
            return True
        elif(arr[mid]>num):
            r=mid-1
        else:
            l=mid+1
    return False



num=25
val=isPerfectSquare(num)
print(val)