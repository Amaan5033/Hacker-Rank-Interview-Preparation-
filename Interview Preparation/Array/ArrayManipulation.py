

def arrayManipulation(n,queries):
    dp=[[0 for i in range(n+1)] for j in range(m+1)]

    #-----------------------------------------------# 
    k=0
    for i in range(1,m+1):
        for j in range(1,n+1):
            if j>=queries[i-1][k] and j<=queries[i-1][k+1]:
                dp[i][j]=queries[i-1][k+2]+dp[i-1][j]
            else:
                dp[i][j]=dp[i-1][j]
    return max(dp[-1])

    # Time Complexity O(NxM) Space Complexity O(NxM)
    # ---------------------------------------------#


    # ---------------------------------------------#

    i,k,a,max=1,1,0,0
    while i<len(dp):
        if k<queries[i-1][a]:
            dp[i][k]=dp[i-1][k]
        elif k>=queries[i-1][a] and k<=queries[i-1][a+1]:
            dp[i][k]=queries[i-1][a+2]+dp[i-1][k]
            if dp[i][k]>max:
                max=dp[i][k]
        elif k>queries[i-1][a+1] and k<len(dp[i]):
            dp[i][k]=dp[i-1][k]
        else:
            i+=1
            k=0
        k+=1
        
    return max
     
    # Time Complexity O(N) Space Complexity O(NxM)
    # ----------------------------------------------#

    # ----------------------------------------------#
    arr=[0]*(n+2)
    for a,b,k in queries:
        arr[a]+=k
        arr[b+1]-=k
    
    max=0
    temp=0
    for i in arr:
        temp+=i
        if max<temp:
            max=temp
    print(arr)
    return max 

    # Time Complexity O(m+n) Space Complexity O(1)
    # ----------------------------------------------#






queries=[[1,2,100],
         [2,5,100],
         [3,4,100]]
n=10
m=3
print(arrayManipulation(n,queries))


# nm=input().split()
# n=int(nm[0])
# m=int(nm[1])

# queries=[]

# for _ in range(m):
#     queries.append(list(map(int,input().rstrip().split())))


# result=arrayManipulation(n,queries)

# print(result)