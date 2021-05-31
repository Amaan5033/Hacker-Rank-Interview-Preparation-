
from collections import Counter

def pairs(k,arr):
    count=0
    arr.sort(reverse=True)
    array=Counter(arr)
    for i in arr:
        if i-k in array:
            count+=1
    return count


k=1
# arr=[363374326,364147530,
#      61825163,1073065718,
#      1281246024,1399469912,
#      428047635,491595254,
#      879792181,1069262793]

arr=[1,2,3,4]

print(pairs(k,arr))

