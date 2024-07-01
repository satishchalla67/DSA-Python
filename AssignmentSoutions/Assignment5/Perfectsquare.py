# 3. Given a positive integer num, write a program that returns True if num is a perfect
# square else return False. Do not use built-in functions like sqrt. Also, talk about the time
# complexity of your code.
# Test Cases:
# Input: 16
# Output: True
# Input: 14
# Output: False

#Time Complexity o(log n)

def isPerfect(n):
    if n==1:
        return True
    l=1
    r=n//2
    while(l<=r):
        mid=l+(r-l)//2
        if(mid*mid==n):
            return True
        elif(mid*mid>n):
            r=mid-1
        else:
            l=l+1
    return False



n=1
res=isPerfect(n)
print(res)