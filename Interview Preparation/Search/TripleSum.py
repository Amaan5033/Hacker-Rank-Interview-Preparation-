from collections import Counter




def search3(value,arr):
    low=0
    high=len(arr)-1
    length=0
    while low<=high:
        mid=(low+high)//2
        if arr[mid]<=value:
            length=mid+1
            low=mid+1
        else:
            high=mid-1
    return length


def search2(value,arr):
    low=0
    high=len(arr)
    while low<high:
        mid=(low+high)//2
        if arr[mid]==value:
            while mid+1<len(arr) and arr[mid+1]==value:
                mid+=1
            break
        elif arr[mid]>value:
            high=mid
        else:
            low=mid+1

    while mid > -1 and arr[mid]>value:
        mid-=1

    return mid+1

def search1 (value,arr):
    length=0
    low=0
    high=len(arr)-1
    while low<high:
        mid=(low+high)//2
        if arr[mid]==value:
            length+=len(arr[low:mid+1])
            if arr[mid+1]==value:
                low=mid+1
            else:
                return length
        elif arr[mid]<value:
            length+=len(arr[low:mid+1])
            low=mid+1
            if low==high and arr[low]<=value:
                length+=1
        else:
            high=mid
    return length



# with Binary Search//


def triplets(a,b,c):
    a=sorted(set(a))
    b=sorted(set(b))
    c=sorted(set(c))
    check=Counter()
    sum=0
    for i in b:
        if i not in check:
            check[i]=True
            avalue=search3(i,a)
            cvalue=search3(i,c)
            sum+=avalue*cvalue
    return sum




a=[1,3,5]
b=[2,3]
c=[1,2,3]
print(triplets(a,b,c))




# Lets's try with 2 pointer technique


def triplets(a,b,c):
    a=sorted(set(a))
    b=sorted(set(b))
    c=sorted(set(c))
    lenA=len(a)
    lenC=len(c)
    lenB=len(b)
    sum=0
    j=0
    avalue,m=0,0
    cvalue,n=0,0
    while j<lenB:
        if m<lenA:
            for i in range(m,lenA):
                if a[i]<=b[j]:
                    avalue+=1
                else:
                    break
        if n<lenC:
            for k in range(n,lenC):
                if c[k]<=b[j]:
                    cvalue+=1
                else:
                    break
        j+=1
        sum+=avalue*cvalue
        m=avalue
        n=cvalue
    return sum


# a=[1,3,5]
# b=[2,3]
# c=[1,2,3]
# 8

# a=[3,5,7]
# b=[3,6]
# c=[4,6,9]
# 4

# a=[1,4,5]
# b=[2,3,3]
# c=[1,2,3]
# 5

a=[1,3,5,7]
b=[5,7,9]
c=[7,9,11,13]
# 12
print(triplets(a,b,c))






