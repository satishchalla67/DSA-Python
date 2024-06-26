
# #Brute force approch
# def maxprofit(prices):
#     max=0
#     for i in range(0, len(prices)-1):
#         for j in range(i+1, len(prices)):
#             profit=prices[j]-prices[i]
#             if(profit>max):
#                 max=profit
#     return max


# optimised approch
def maxprofit(prices):
    min_val = float('inf')
    max = 0
    for i in range(len(prices)):
        if prices[i]<min_val:
            min_val=prices[i]
        if prices[i]-min_val>max:
            max= prices[i]-min_val
    return max

#this is everyday prices of stock calculate maximum profit
prices=[7,17,5,1,3,6,12]
print(maxprofit(prices))