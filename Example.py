
def printNumbers(n):
    if n == 0:
        return
    printNumbers(n-1)
    print(n,end=" ")
printNumbers(5)  # Output: 1 2 3 4 5
