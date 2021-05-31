

def BinarySearch(solution,value):
    low,high=0,len(solution)-1
    while low<high:
        mid=(low+high)//2
        if solution[mid]==value:
            return True
        elif solution[mid]<value:
            low=mid+1
        else:
            high=mid 
    return False   

def whatFlavors(cost,money):
    ocost=cost
    cost=sorted(cost)
    flag=False
    for i in range(len(ocost)):
        if flag!=True:
            if ocost[i]<money:
                find=BinarySearch(cost,money-ocost[i])
                if find==True:
                    for j in range(len(ocost)):
                        if j!=i and ocost[j]==(money-ocost[i]):
                            print(min(i,j)+1,end=" ")
                            print(max(i,j)+1)
                            flag=True
                            break
        else:
            break


cost=[1,4,5,3,2]
money=4

whatFlavors(cost,money)





