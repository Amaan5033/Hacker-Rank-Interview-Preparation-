

from collections import Counter
def substrCount(n,s):
    nstr=""
    substr=[]
    for i in range(len(s)):
        for j in range(i,len(s)):
            nstr=nstr+s[j]
            cstr=Counter(nstr)
            if len(cstr)==1:
                substr.append(nstr)
            elif len(nstr)>2 and len(cstr)==2:
                mid=nstr[len(nstr)//2]
                if cstr[mid]==1:
                    substr.append(nstr)
            else:
                pass
        nstr=""
    return substr


def substrCount2(n,s):
    count=0
    i=0
    while i<n:
        char_count=1
        while (i+1<n and s[i]==s[i+1]):
            i+=1
            char_count+=1
        
        count+=int(char_count*(char_count+1)/2)
        i+=1
    for i in range(1,n):
        char_count=1
        while (
            i+char_count<n and
            i-char_count>=0 and
            s[i]!=s[i-1] and
            s[i-char_count]==s[i+char_count] and
            s[i-1]==s[i-char_count]
        ):
            char_count+=1
        count+=char_count-1

    return count


n=4
s="aaaa"
print(substrCount2(n,s))