

# def repeatedString(s,n):
#     position_of_a=[]
#     A=0
#     total_a=0
#     for i in range(len(s)):
#         if s[i]=="a":
#             A+=1
#             position_of_a.append(i)
#     total_a=A
#     difference=n-len(s)
#     i=0
#     while i<n+1:
#         if difference>=len(s):
#             total_a+=A
#             difference-=len(s)
#         else:
#             for j in range(len(position_of_a)):
#                 if position_of_a[j]+1<=difference:
#                     total_a+=1
#                 else:
#                     i=n
#                     break
#         i+=1
#     return total_a
# s="a"
# n=10000000000000
# print(repeatedString(s,n))



def RepeatedString(s,n):
    no_of_A=0
    for i in range(len(s)):
        if s[i]=="a":
            no_of_A+=1
    difference=n-len(s)*(int(n/len(s)))
    no_of_A=no_of_A*(int(n/len(s)))
    for i in range(difference):
        if s[i]=='a':
            no_of_A+=1

    return no_of_A

s="a"
n=10000000000000
print(RepeatedString(s,n))

