


def rotLeft(a,d):
    a=a[d:]+a[:d]
    return a
    
nd=input().split()
n=int(nd[0])
d=int(nd[1])
a=list(map(int,input().rstrip().split()))

result=rotLeft(a,d)
print(result)