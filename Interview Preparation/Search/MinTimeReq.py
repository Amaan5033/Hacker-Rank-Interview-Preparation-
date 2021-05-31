# from fractions import Fraction
# from math import ceil




# def minTime1(machines,goal):
#     sum=float(0)
#     for i in machines:
#         sum+=Fraction(1,i)
#     sum=round(1/sum,1) 
#     # sum=ceil(float(goal)*sum)
#     return sum





# machines=[63,2,26,59,16,55,99,21,98,65]
# goal=56
# print(minTime(machines,goal))

# machines=[[(4,5,6),12],
#           [(2,3,2),10],
#           [(2,3),5],
#           [(1,3,4),10]]
# # 20 8 6 7

# for i,j in machines:
#     print(minTime(i,j))



# def search(arr,goal):   
#     low=1
#     high=arr[-1]*goal
#     while low<high:
#         work=0
#         min=float("inf")
#         mid=(low+high)//2
#         for i in arr:
#             work+=int(mid/i)
#             if mid%i<min:
#                 min=mid%i
#         if work==goal:
#             return mid-min
#         elif work>goal:
#             high=mid-min
#         else:
#             low=mid


# def minTime(machines,goal):
#     machines.sort()
#     days=search(machines,goal)
#     return days


# machines=[[[4,5,6],12],
#           [[2,3,2],10],
#           [[2,3],5],
#           [[1,3,4],10]]
# # 20 8 6 7

# for i,j in machines:
#     print(minTime(i,j))





# machines=[4,5,6]
# goal=12
# print(minTime(machines,goal))


# Efficient Python3 program to find
# minimum time required to produce m items.
import sys
 
def findItems(arr, n, temp):
    ans = 0
    for i in range(n):
        ans += temp // arr[i]
    return ans
 

def bs(arr, n, m, high):
    low = 1
    while low < high:
        mid = (low + high) >> 1
        itm = findItems(arr, n, mid)
        if itm < m:
            low = mid + 1
        else:
            high = mid
    return high
 
def minTime(arr,m):
    maxval = -sys.maxsize
    n=len(arr)
    for i in range(n):
        maxval = max(maxval, arr[i])
 
    return bs(arr, n, m, maxval * m)
 


# machines=[4,5,6]
# goal=12
# print(minTime(machines,goal))

machines=[[[4,5,6],12],
          [[2,3,2],10],
          [[2,3],5],
          [[1,3,4],10]]
# 20 8 6 7

for i,j in machines:
    print(minTime(i,j))



