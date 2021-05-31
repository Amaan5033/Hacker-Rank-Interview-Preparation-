


# This code cant preserve the sequence of array
# and find accordingly
# But the result are right for all sorted array
# in ascending order

# In hacker Rank it passess 11/13 test cases.

# def countTriplets(arr,r):
#     no_of_triplets=0
#     k=2
#     hashmap={}
#     for i in arr:
#         if i in hashmap:
#             hashmap[i]+=1
#         else:
#             hashmap[i]=1
#     for i in hashmap:
#         if r==1:
#             for j in range(hashmap[i]):
#                 a=hashmap[i]-k
#                 no_of_triplets+=int(a*(a+1)/2)
#                 k+=1
#             k=2
#         else:
#             if i*r in hashmap and i*r*r in hashmap:
#                     no_of_triplets+=hashmap[i]*hashmap[i*r]*hashmap[i*r*r]
            
    # return no_of_triplets

# arr=[25,125,5,1,5]
# r=5
# print(countTriplets(arr,r))



# Better solution after researching from internet
# This sloution is preserving the sequence
# no need to add code for a corner case of r=1


def countTriplets(arr,r):
    no_of_triplets=0
    after,before={},{}
    for value in arr:
        if value in after:
            after[value]+=1
        else:
            after[value]=1
    for value in arr:
        after[value]-=1
        if value%r==0 and value//r in before and value*r in after:
            no_of_triplets+=before[value//r]*after[value*r]
        if value in before:
            before[value]+=1
        else:
            before[value]=1
        
    return no_of_triplets

arr=[1,1,1,1,1,1]
r=1
print(countTriplets(arr,r))

