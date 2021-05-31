from collections import Counter


def reverse(split):
    return split[::-1]

def shufflestr(rev):
    

def splitstr(s):
    count=Counter(s)
    str=""
    for i in count:
        str=str+i
    return str



def reverseShuffleMerge(s):
    split=splitstr(s)
    rev=reverse(split)
    shuffle=shufflestr(rev)



s="abcdefgabcdefg"
print(reverseShuffleMerge(s))










