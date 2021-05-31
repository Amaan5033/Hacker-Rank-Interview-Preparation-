


def minimumBribes(q):
    bribes=0
    for i in range(len(q)-1,-1,-1):
        if q[i]!=i+1:
            if q[i-1]==i+1:
                bribes+=1
                q[i],q[i-1]=q[i-1],q[i]
            elif q[i-2]==i+1:
                bribes+=2
                q[i-2],q[i-1]=q[i-1],q[i-2]
                q[i-1],q[i]=q[i],q[i-1]
            else:
                print("Too chaotic")
                return

    print(bribes)
if __name__=="__main__":
    testcases=[[1,2,3,4,8,5,6,7],
               [3,1,2,6,4,5,8,7],
               [1,2,3,4,5,8,6,7,11,9,10]]
    for i in testcases:
        minimumBribes(i)


