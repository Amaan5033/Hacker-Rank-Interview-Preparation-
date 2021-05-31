

def alternatingCharacters(s):
    deletion=0
    for i in range(len(s)-1):
        if s[i]==s[i+1]:
            deletion+=1

    return deletion

if __name__=="__main__":
    testcases=['AAAA','BBBBB','ABABABAB','BABABA','AAABBB']
    for i in testcases:
        print(alternatingCharacters(i))


