

from collections import Counter
from heapq import nlargest

def kmostfrequent(words,k):
    if k==len(words):
        return words
    else:
        count=Counter(words)
        return nlargest(k, count.keys(), key=count.get)



words=["priya", "bhatia", "akshay", "arpit", "priya", "arpit"]
res=kmostfrequent(words,2)
res.sort()
print(res)