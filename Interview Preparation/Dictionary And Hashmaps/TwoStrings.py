

from collections import Counter
def twoStrings(s1,s2):
    s3="abcdefghijklmnopqrstuvwxyz"
    countS1=Counter(s1)
    countS2=Counter(s2)
    for i in s3:
        if i in countS1 and i in countS2:
            return 'YES'
    
    return 'NO'






s1=input()
s2=input()
print(twoStrings(s1,s2))