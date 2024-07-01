# 1. Compute and return the square root of x, where x is guaranteed to be a non-negative
# integer. And since the return type is an integer, the decimal digits are truncated and only
# the integer part of the result is returned. Also, talk about the time complexity of your
# code.
# Test Cases:
# Input: 4
# Output: 2
# Input: 8
# Output: 2
# Explanation: The square root of 8 is 2.8284…., the decimal part is truncated and 2 is
# returned.
# Hint: Try to use a modified binary search approach for an optimized solution
    
#Time omplexity=o(logn)

def squareof(n):
    l=1
    r=l+1
    while(r<=n):
        if(l*l==n):
            return l
        elif(r*r==n):
            return r
        if(l*l<n and r*r>n):
            return l
        else:
            l=r
            r=r+1

n=17
res=squareof(n)
print(res)

