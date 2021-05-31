


# def maxSubsetSum(arr):
#     n=len(arr)
#     dp=[[0]*(n+1) for i in range(n+1)]
#     for i in range(n):
#         for j in range(n):
#             if i>=j or i+1==j:
#                 dp[i+1][j+1]=max(dp[i][j+1],dp[i+1][j])
#             else:
#                 if max(dp[i][j+1],dp[i+1][j])>=arr[i]+arr[j]:
#                     dp[i+1][j+1]=max(dp[i][j+1],dp[i+1][j])+arr[i]
#                 else:
#                     dp[i+1][j+1]=arr[i]+arr[j]

#     return dp

# arr=[2,1,5,8,4]
# print(maxSubsetSum(arr))

# def sum(arr):
#     value=0
#     for i in range(0,len(arr),2):
#         value+=arr[i]
#     return value


# def maxSubsetSum(arr):
#     max=0
#     for i in range(len(arr)):
#         value=arr[i]+sum(arr[i+2:])
#         if value>max:
#             max=value
#     return max


# arr=[[2,1,5,8,4],
#      [-2,1,3,-4,5],
#      [3,7,4,6,5],
    #  [3,5,-7,8,10]]
# for i in arr:
#     print(maxSubsetSum(i))

# arr=[3,5,-7,8,10]
# print(maxSubsetSum(arr))


def maxSubsetSum(arr):



arr=[2,1,5,8,4]
print(maxSubsetSum(arr))







