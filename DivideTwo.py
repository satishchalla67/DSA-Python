def divide(dividend, divisor):
    count=0
    while(dividend>=divisor):
        dividend-=divisor
        count+=1
    return count


res=divide(27,3)
print(res)