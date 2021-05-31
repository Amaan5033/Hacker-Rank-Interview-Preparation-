

from collections import Counter
def isValid(s):
    s=Counter(s)
    count=Counter()
    for i in s:
        count[s[i]]+=1
    if len(count)>2:
        return "NO"
    elif len(count)==1:
        return "YES"
    else:
        for i in count:
            if (abs(i-count[i])!=i and abs(i-count[i]) in count)\
             or i==1 and count[i]==1:
                return "YES"
            
    return "NO"

s="aaaabbcc"
print(isValid(s))

# if __name__=="__main__":
#     testcases=["aabbccddeefghi",'abccc','aabbcd','abcdefghhgfedecba']
#     for i in testcases:
#         print(isValid(i))


