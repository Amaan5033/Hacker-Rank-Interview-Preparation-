


def luckBalance(k,contests):
    luckbalance=0
    a=0
    contests.sort(key=lambda x:x[0],reverse=True)
    for i,j in contests:
        if j==0:
            luckbalance+=i
        elif a<k and j==1:
            luckbalance+=i
            a+=1
        else:
            luckbalance-=i
    return luckbalance


k=2
contests=[[5,1],
          [1,1],
          [4,0]]
        #   [8,1],
        #   [10,0],
        #   [5,0]]
print(luckBalance(k,contests))

