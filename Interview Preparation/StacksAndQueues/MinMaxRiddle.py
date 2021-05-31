

# def formingMagicSquare(s):
#     a=0
#     b=0
#     cost=0
#     # Write your code here
#     miss=[]
#     value=[]
#     for i in s:
#         if type(i)==list:
#             miss=miss+i
#     for i in range(1,10):
#         if i not in miss:
#             value.append(i)
#     if sum(s[1])!=15:
#         number=15-sum(s[1])
#         if number>0:
#             if s[1][0]+number in value:
#                 cost+=number
#                 s[1][0]+=number
                
#             elif s[1][2]+number in value:
#                 cost+=number
#                 s[1][2]+=number
        
#         else:
#             number=abs(number)
#             if s[1][0]-number in value:
#                 cost+=number
#                 s[1][0]-=number
                
#             elif s[1][2]-number in value:
#                 cost+=number
#                 s[1][2]-=number
#     # return value
#     # if value:
#     #     if sum(s[0][1]+5+s[2][1])!=15:
#     #         number=15-sum(s[0][1]+5+s[2][1])
#     #         if number>0:
#     #             if s[0][1]+number in value:
#     #                 cost+=number
#     #                 s[0][1]+=number
#     #                 value.remove(s[0][1]+number)
#     #             elif s[2][1]+number in value:
#     #                 cost+=number
#     #                 s[2][1]+=number
#     #                 value.remove(s[2][1]+number)
#     #         else:
#     #             number=abs(number)
#     #             if s[0][1]-number in value:
#     #                 cost+=number
#     #                 s[0][1]-=number
#     #                 value.remove(s[0][1]-number)
#     #             elif s[2][1]-number in value:
#     #                 cost+=number
#     #                 s[2][1]-=number
#     #                 value.remove(s[2][1]-number)
#     # return s

        

            
    

# s = [[5, 3, 4], [1, 5, 8], [6, 4, 2]]
# print(formingMagicSquare(s))




# def extraLongFactorials(n):
#     # Write your code here
#     if n==1 or n==0:
#         return 1
#     else:
#         fact=n*extraLongFactorials(n-1)
#     global a
#     if a==n:
#         print(fact)
#     return fact

# n=1
# a=n
# extraLongFactorials(n)



# def countApplesAndOranges(s, t, a, b, apples, oranges):
#     countapple=0
#     countorange=0
#     for i in apples:
#         if i>0 and (i+a>=s and i+a<=t):
#             countapple+=1
#     for i in oranges:
#         if i<0 and (b-abs(i)<=t) and (b-abs(i)>=s):
#             countorange+=1
#     print(countapple)
#     print(countorange)
    

# s=7
# t=11
# a=5
# b=15
# apples=[-2,2,1]
# oranges=[5,-6]
# countApplesAndOranges(s,t,a,b,apples,oranges)



# def gradingStudents(grades):
#     for i in range(len(grades)):
#         if grades[i]>=38:
#             remainder=grades[i]%5
#             diff=5-remainder
#             if diff<3:
#                 grades[i]+=diff
#     return grades





# testcases=[73,67,38,33]
# print(gradingStudents(testcases))






# def kangaroo(x1, v1, x2, v2):
#     if x2>x1 and v2>=v1:
#         return 'NO'
#     else:
#         for i in range(10001):
#             x1+=v1
#             x2+=v2
#             if x1==x2:
#                 return 'YES'
#     return 'NO'




# x1,v1,x2,v2=0,2,5,3
# print(kangaroo(x1,v1,x2,v2))



def getTotalX(a, b):
    values=[]
    count=0
    flag=True
    for i in range(1,min(b)+1):
        for j in a:
            if i%j!=0:
                flag=False
                break
        if flag==True:
            values.append(i)
        flag=True
    a=len(values)
    for i in range(a):
        for j in b:
            if j%values[i]!=0:
                values[i]=False
                break
    for i in values:
        if i:
            count+=1

    return count

a=[1]
b=[72,48]
print(getTotalX(a,b))





