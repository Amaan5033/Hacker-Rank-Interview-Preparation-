

def swapCount(arr,first,mid,last,temp_arr):
    count=0
    i,j,k=first,mid+1,first

    while i<=mid and j<=last:
        if arr[i]>arr[j]:
            count+=(mid-i+1)
            temp_arr[k]=arr[j]
            j+=1
        else:
            temp_arr[k]=arr[i]
            i+=1
        k+=1
    while i<=mid:
        temp_arr[k]=arr[i]
        i+=1
        k+=1
    while j<=last:
        temp_arr[k]=arr[j]
        j+=1
        k+=1
    for i in range(first,last+1):
        arr[i]=temp_arr[i]
    return count


def countInversion(arr):
    temp_arr=[0]*len(arr)
    return mergeSort(arr,0,len(arr)-1,temp_arr)


def mergeSort(arr,first,last,temp_arr):
    count=0
    if first<last:
        mid=(first+last)//2
        count+=mergeSort(arr,first,mid,temp_arr)
        count+=mergeSort(arr,mid+1,last,temp_arr)
        count+=swapCount(arr,first,mid,last,temp_arr)
    return count

arr=[7,5,3,1]
print(countInversion(arr))

