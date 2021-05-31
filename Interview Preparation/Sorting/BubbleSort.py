


def countSwaps(a):
    count=0
    k=0
    for i in range(len(a)-k):
        for j in range((len(a)-i)-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
                count+=1
        k+=1
    print(f"Array is sorted in {count} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[-1]}")



a=[6,4,1]
countSwaps(a)