





from collections import Counter

def freqQuery(queries):
    hashmap1=Counter()
    hashmap2=Counter()
    ans=[]
    for i,j in queries:
        if i==1:
            hashmap2[hashmap1[j]]-=1
            hashmap1[j]+=1
            hashmap2[hashmap1[j]]+=1
        elif i==2:
            if hashmap1[j]>0:
                hashmap2[hashmap1[j]]-=1
                hashmap1[j]-=1
                hashmap2[hashmap1[j]]+=1
        else:
            if hashmap2[j]>0:
                ans.append(1)
            else:
                ans.append(0)

    return ans

queries=[(1,3),(2,3),(3,2),(1,4),
         (1,5),(1,5),(1,4),(3,2),
         (2,4),(3,2)]

# queries=[(1,1),(2,2),(3,2),(1,1),(1,1),(2,1),(3,2)]

# queries=[(1,5),(1,6),(3,2),(1,10),(1,10),(1,6),(2,5),(3,2)]

# queries=[(3,4),(2,1003),(1,16),(3,1)]

print(freqQuery(queries))

