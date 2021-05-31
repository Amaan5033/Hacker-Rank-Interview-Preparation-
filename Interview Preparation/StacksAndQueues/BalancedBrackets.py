
from collections import Counter
def isBalanced(s):
    count=Counter()
    stack=[]
    for i in s:
        stack.append(i)
    prev=stack.pop()
    count[prev]+=1
    for i in range(len(stack)):
        popstack=stack.pop()
        if popstack in [']',')','}']:
            count[popstack]+=1
            prev=popstack
        elif (prev==']' and popstack=='[') or (prev==')' and popstack=='(') or (prev=='}' and popstack=='{'):
            count[prev]-=1
            prev=popstack
        elif (prev==']' and popstack in ['(','{']) or (prev==')' and popstack in ['[','{']) or (prev=='}' and popstack in ['(','[']):
            return 'NO'
        else:
            if popstack=='[':
                if count[']']>=1:
                    count[']']-=1
                else:
                    return 'NO'
            elif popstack=='{':
                if count['}']>=1:
                    count['}']-=1
                else:
                    return 'NO'
            else:
                if count[')']>=1:
                    count[')']-=1
                else:
                    return 'NO' 
    sum=0
    for i in count:
        sum+=count[i]
    if sum==0:
        return 'YES'
    else:
        return 'NO'
        
testcases=['{[()]}','{[(])}','{{[[(())]]}}',
           '{{)[](}}','{(([])[])[]}','{(([])[])[]]}',
           '{(([])[])[]}[]']
for i in testcases:
    print(isBalanced(i))





