)


def SherlockAndAnagrams(s):
    hashmap={}
    no_of_anagrams=0
    str=""
    for i in range(len(s)):
        for j in range(i,len(s)):
            str=str+s[j]
            str=''.join(sorted(str))
            if str in hashmap:
                hashmap[str]+=1
            else:
                hashmap[str]=1
        str=""
    for values in hashmap.values():
        no_of_anagrams+=int(values*(values-1)/2)

    return no_of_anagrams


if __name__=="__main__":
    testcases=['abba',
               'abcd',
               'mom',
               'ifailuhkqq',
               'kkkk',
               'cdcd']
    for i in testcases:
        print(SherlockAndAnagrams(i))