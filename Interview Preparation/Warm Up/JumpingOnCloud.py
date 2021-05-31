


def jumpingOnClouds(c):
    num_of_jumps=0
    i=0
    while i<len(c)-1:
        num_of_jumps+=1
        if i==len(c)-2:
            break
        if c[i+2]==1:
            i+=1 
        else:
            i+=2
    return num_of_jumps
        
        


c=[0,0,0,1,0,0]
print(jumpingOnClouds(c))






