# 2. Given three points, check whether they lie on a straight (collinear) or not. [Google]
# For example:
# Input- [(1,1), (1,6), (0,9)]
# Output- No
# Input- [(1,1), (1,4), (1,5)]
# Output- Yes


def isCollinear(arr):
    x1=arr[0][0]
    y1=arr[0][1]
    x2=arr[1][0]
    y2=arr[1][1]
    x3=arr[2][0]
    y3=arr[2][1]
    if (x2-x1)*(y3-y2)==(x3-x2)*(y2-y1):
        return True
    return False


arr=[[1,1],[1,4],[1,5]]
res=isCollinear(arr)
print(res)