from heapq import nlargest
from collections import Counter

def kmostFrequentWords(words,k):
    if k==len(words):
        return words
    else:
        arr= Counter(words)
        return nlargest(k,arr.keys(),key=arr.get)

words = ["priya", "bhatia", "akshay", "arpit", "priya", "arpit"]
K = 3
res=kmostFrequentWords(words, K)
print(res)