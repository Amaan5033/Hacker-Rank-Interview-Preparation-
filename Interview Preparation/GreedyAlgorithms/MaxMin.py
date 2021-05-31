


def merge(arr,l,m,r):
    left_array=arr[l:m+1]
    right_array=arr[m+1:r+1]

    i,j,k=0,0,l
    while i<len(left_array) and j<len(right_array):
        if left_array[i]<=right_array[j]:
            arr[k]=left_array[i]
            i+=1
        else:
            arr[k]=right_array[j]
            j+=1
        k+=1
    while i<len(left_array):
        arr[k]=left_array[i]
        i+=1
        k+=1
    while j<len(right_array):
        arr[k]=right_array[j]
        j+=1
        k+=1
    return arr



def mergeSort(arr,l,r):
    if l<r:
        m=(l+(r-1))//2
        mergeSort(arr,l,m)
        mergeSort(arr,m+1,r)
        merge(arr,l,m,r)
    return arr




def maxMin(k,arr):
    minUnfairness=float("inf")
    arr.sort()
    # array=mergeSort(arr,0,len(arr)-1)
    a=0
    for i in range(len(arr)-k+1):
        if (arr[a+k-1]-arr[a])<minUnfairness:
            minUnfairness=(arr[a+k-1]-arr[a])
        a+=1
    return minUnfairness


k=4
arr=[1,2,3,4,10,20,20,40,100,200]
print(maxMin(k,arr))





