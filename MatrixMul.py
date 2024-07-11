
def matrixMul(A,B,C,n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j]+=A[i][k]*B[k][j]
    return C



A= [[1,2,3],
    [2,3,4],
    [4,5,6]]
B=[[9,8,7],
   [4,6,7],
   [9,6,1]]
n=len(A)
C=[[0 for _ in range(n)] for _ in range(n)]
res=matrixMul(A,B,C,n)
print(res)