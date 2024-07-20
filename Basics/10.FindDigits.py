





import re


def checkDigits(s):
    res=re.sub("[0-9]", "", s)
    return True if res=="" else False

s1="111011s"
s2="Satish1"
print(checkDigits(s1))
print(checkDigits(s2))