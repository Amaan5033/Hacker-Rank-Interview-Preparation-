

def countingValleys(steps,path):
    # Write your code here
    countD=0
    countU=0
    consecutiveDU=[]
    count_valley=0
    if path[0]!="U":
        consecutiveDU.append(0)
    for i in path:
        if i=="D" and countU==0:
            countD+=1
        elif i=="D" and countU!=0:
            consecutiveDU.append(countU)
            countU=0
            countD+=1
        else:
            if countD!=0:
                consecutiveDU.append(countD)
                countD=0
            countU+=1
    if path[-1]=="U":
        consecutiveDU.append(countU)
    if path[-1]=="D":
        consecutiveDU.append(countD)
        consecutiveDU.insert(len(consecutiveDU),0)
    i=0
    sea_level=consecutiveDU[i+1]-consecutiveDU[i]
    i=2
    while i<len(consecutiveDU):
        if i%2==0:
            if sea_level>0:
                if sea_level-consecutiveDU[i]<=0:
                    count_valley+=1
            sea_level=sea_level-consecutiveDU[i]
             
        else:
            sea_level+=consecutiveDU[i]
        i+=1
        
    
    return count_valley



if __name__ == '__main__':


    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)
    print(result)


