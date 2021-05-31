

from collections import Counter

def makeAnagrams(a,b):
    deletion=0
    s1=Counter(a)
    s2=Counter(b)
    for i in s1:
        if i in s2 and s1[i]==s2[i]:
            pass
        elif i in s2 and s1[i]!=s2[i]:
            if s1[i]>s2[i]:
                deletion+=s1[i]-s2[i]
            else:
                deletion+=s2[i]-s1[i]
        else:
            deletion+=s1[i]
        s2[i]="T"
    for i in s2:
        if s2[i]!="T":
            deletion+=s2[i]
            s2[i]="T"
    return deletion

a='cde'
b='abc'
print(makeAnagrams(a,b))



