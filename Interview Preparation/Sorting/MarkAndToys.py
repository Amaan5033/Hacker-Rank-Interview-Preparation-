

def maximumToys(prices,k):
    noOfToys=0
    prices.sort()
    for i in prices:
        if i<k:
            noOfToys+=1
            k=k-i
 
    return noOfToys

k=7
prices=[1,2,3,4]
print(maximumToys(prices,k))





