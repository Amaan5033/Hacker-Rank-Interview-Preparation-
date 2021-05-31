

def sockMerchant(n, ar):
    ar.sort()
    i=0
    num_of_pairs=0
    count=0
    while i<len(ar)-1:
        if ar[i]==ar[i+1]:
            num_of_pairs+=1
            i+=2
        else: 
            i+=1
    return num_of_pairs



if __name__ == '__main__':
    

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    print(result)