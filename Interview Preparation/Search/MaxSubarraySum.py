



# Naive brute force method


# def maximumSum(a,m):
#     max=0 
#     sum=0
#     for i in range(len(a)):
#         for j in range(i,len(a)):
#             sum=sum+a[j]
#             if sum%m>max:
#                 max=sum%m
#         sum=0
            
#     return max


# a=[3,3,9,9,5]
# m=7
# print(maximumSum(a,m))



# Sliding Window technique

def maximumSum(a,m):
    max=m-1
    curr_max=-float('inf')
    sum=0
    i=0
    track_value=0
    n=len(a)
    while track_value<n:
        if i<=n-1:
            sum+=a[i]
        if sum%m==max:
            return max
        elif sum%m>curr_max:
            curr_max=sum%m
            if i==n-1:
                track_value+=1
        else:
            sum=sum-a[track_value]
            track_value+=1
        if i!=n:
            i+=1
    return curr_max        

a=[1,2,3,4,5,6,7,-8,2,12,11]
m=15
print(maximumSum(a,m))














