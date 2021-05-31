
from collections import Counter
def checkMagazine(magazine,note):
    count=Counter(magazine)
    for i in note:
        if count[i]>=1:
            count[i]-=1
        else:
            print("No")
            return
    print("Yes")
        

        


# magazine=['two','times','three','is','not','four']
# note=['two','times','two','is','four']

# magazine=['give','me','one','grand','today','night']
# note=['give','one','grand','today']

magazine = input().rstrip().split()

note = input().rstrip().split()

print(checkMagazine(magazine,note))