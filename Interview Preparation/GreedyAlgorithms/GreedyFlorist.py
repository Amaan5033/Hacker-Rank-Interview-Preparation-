

def getMinimumCost(k,c):
    minCost=0
    if k>=len(c):
        minCost+=int(k/len(c))*sum(c)
        for i in range(k%len(c)):
            minCost+=c[i]
    else:
        c.sort(reverse=True)
        minCost+=sum(c[:k])
        i,j,a=k,0,2
        while i<len(c):
            while j<k:
                minCost+=a*c[i]
                j+=1
                i+=1
                if i>=len(c):
                    break
            j=0
            a+=1
    return minCost
            



k=3
c=[1,2,3,4]
print(getMinimumCost(k,c))


