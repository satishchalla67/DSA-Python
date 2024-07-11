

def multiply(A, B, C):
    N = len(A)  # Assuming A is an NxN matrix
    # Initialize C as an NxN matrix filled with zeros
    for i in range(N):
        C.append([0] * N)
    
    for i in range(N):
        for j in range(N):
            for k in range(N):
                C[i][j] += A[i][k] * B[k][j]

# Matrix multiplication
A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
B = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
C = []
multiply(A, B, C)
print(C)
