

def largestRectangle(h):
    stack=[]
    left=[]
    right=[]
    max=0
    a=len(h)
    for i in range(a):
        if not stack:
            left.append(0)
            stack.append(i)
        elif h[stack[-1]]<h[i]:
            left.append(stack[-1]+1)
            stack.append(i)
        else:
            while h[stack[-1]]>=h[i]:
                stack.pop()
                if not stack:
                    left.append(0)
                    break
            if stack:
                left.append(stack[-1]+1)
            stack.append(i)
    stack=[]
    for i in range(a-1,-1,-1):
        if not stack:
            right.append(a-1)
            stack.append(i)
        elif h[stack[-1]]<h[i]:
            right.append(stack[-1]-1)
            stack.append(i)
        else:
            while h[stack[-1]]>=h[i]:
                stack.pop()
                if not stack:
                    right.append(a-1)
                    break
            if stack:
                right.append(stack[-1]-1)
            stack.append(i)
    right=right[::-1]
    for i,j,k in zip(h,left,right):
        area=i*((k-j)+1)
        if area>max:
            max=area
            
    return max
    
h=[1,2,3,4,5]
print(largestRectangle(h))




