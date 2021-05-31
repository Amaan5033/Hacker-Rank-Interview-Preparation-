
# Hashmap with cycle approach

def minimumSwaps(arr):
    swap=0
    hashmap={}
    for i in range(len(arr)):
        hashmap[i+1]=False
    i=1
    a=1
    while i<len(arr)+1:
        if hashmap[i]!=True:
            hashmap[i]=True
            if i!=arr[i-1]:
                if hashmap[arr[i-1]]==False:
                    swap+=1
                    i=arr[i-1]
        else:
            a+=1
            i=a

    return swap

arr=[2,1,3,1,2]
print(minimumSwaps(arr))
 
# if __name__=="__main__":
#     testcases=[[7,1,3,2,4,5,6],
#                [4,3,1,2],
#                [2,3,4,1,5],
#                [1,3,5,2,4,6,7]
#     ]
#     for i in testcases:
#         print(minimumSwaps(i))

# Brute Force Method


# def minimumSwaps(arr):
#     swap=0
#     for i in range(len(arr)-1):
#         if i+1!=arr[i]:
#             for j in range(i+1,len(arr)):
#                 if arr[j]==i+1:
#                     arr[i],arr[j]=arr[j],arr[i]
#                     swap+=1
#                     break
#     return arr
            
# if __name__=="__main__":
#     testcases=[[7,1,3,2,4,5,6],
#                [4,3,1,2],
#                [2,3,4,1,5],
#                [1,3,5,2,4,6,7]
#     ]
#     for i in testcases:
#         print(minimumSwaps(i))


