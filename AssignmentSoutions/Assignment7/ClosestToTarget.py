# 1. Given an integer array nums of length n and an integer target, find three integers in nums
# such that the sum is closest to the target.[Amazon]
# You need to return the sum of three integers.
# For example:arr = [-1, 2, 1, -4], target = 1
# Output: 2
# Explanation: [-1+2+1] = 2 (The sum that is closest to the target is 2)




from itertools import combinations


def closest(arr, k, start,current_combiations, all_combinations):
    if(len(current_combiations)==k):
        all_combinations.append(current_combiations[:])
        return
    for i in range(start, len(arr)):
        current_combiations.append(arr[i])
        closest(arr, k,i+1,current_combiations,all_combinations)
        current_combiations.pop()

def closestTarget(arr,target):
    num=3
    all_combinations=[]
    closest(arr, num,0,[],all_combinations)
    elements_sum={}
    for item in all_combinations:
        cSum=sum(item)
        elements_sum[cSum]=item
    clos=0
    smallest=float("inf")
    for k,v in elements_sum.items():
        if abs(k-target)<smallest:
            clos=k
            smallest=abs(k-target)
    return elements_sum.get(clos)

arr = [-1, 2, 1, -4]
target = 1
res=closestTarget(arr,target)
print(res)