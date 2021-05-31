





# from statistics import median


# def medianCalculate(arr):
#     if len(arr)%2!=0:
#         return arr[int(len(arr)/2)]
#     else:
#         a=int(len(arr)/2)
#         return (arr[a]+arr[a-1])/2

# def activityNotifications(expenditure,d):
#     i=d
#     notification=0
#     a=0
#     while i<len(expenditure):
#         med=median(expenditure[a:i])
#         if expenditure[i]>=2*med:
#             notification+=1
#         i+=1
#         a+=1
#     return notification












# def medianCalculate(arr,first,last):
#     if last>=arr[-1]:
#         arr.append(last)
#     else:
#         for i in range(len(arr)):
#             if arr[i]>=last:
#                 arr.insert(i,last)
#                 break
#     if len(arr)%2!=0:
#         c=arr[int(len(arr)/2)]
#     else:
#         b=int(len(arr)/2)
#         c=(arr[b]+arr[b-1])/2
#     arr.remove(first)
#     return c,arr


# def activityNotifications(expenditure, d):
#     # Write your code here
#     i=d
#     notification=0
#     arr=expenditure[:i-1]
#     arr.sort()
#     a=0
#     while i<len(expenditure):
#         median=medianCalculate(arr,expenditure[a],expenditure[i-1])
#         if expenditure[i]>=2*median[0]:
#             notification+=1
#         i+=1
#         a+=1
    # return notification



# We are gonna apply the concept of counting Sort
# bcuz expenditure<=200

def medianCalculate(countSort,d,position):
    count=0
    left=0
    while count<position:
        count+=countSort[left]
        left+=1
    
    right=left
    left-=1

    if count>position or d%2!=0:
        return left
    else:
        while countSort[right]==0:
            right+=1
        return (left+right)/2


def activityNotifications(expenditure,d):
    notification=0
    countSort=[0]*201
    for i in range(d):
        countSort[expenditure[i]]+=1

    first=0
    # finding the median position
    if d%2==0:
        position=int(d/2)
    else:
        position=int(d/2)+1

    i=d
    while i<len(expenditure):
        median=medianCalculate(countSort,d,position)
        if expenditure[i]>=median*2:
            notification+=1
        countSort[expenditure[first]]-=1
        countSort[expenditure[i]]+=1
        first+=1
        i+=1

    return notification






# expenditure=[10,20,30,40,50]
expenditure=[2,3,4,2,3,6,8,4,5]
d=5
print(activityNotifications(expenditure,d))


