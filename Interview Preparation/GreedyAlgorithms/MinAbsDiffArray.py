


def minimumAbsoluteDifference(arr):
    arr.sort()
    min=abs(arr[0])
    for i in range(len(arr)-1):
        if abs(arr[i]-arr[i+1])<min:
            min=abs(arr[i]-arr[i+1])
    return min


if __name__=="__main__":
    testcases=[[-59,-36,-13,1,-53,-92,-2,-96,-54,75],
               [-2,2,4],
               [3,-7,0],
               [1,-3,71,68,17]]
    for i in testcases:
        print(minimumAbsoluteDifference(i))



# arr=[-59,-36,-13,1,-53,-92,-2,-96,-54,75]
# print(minimumAbsoluteDifference(arr))

