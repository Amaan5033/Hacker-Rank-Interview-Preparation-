
class MyQueue(object):
    def __init__(self):
        self.stack1=[]
        self.stack2=[]
    
    def peek(self):
        if self.stack1:
            return self.stack1[0]
        else:
            return self.stack2[-1]
        
    def pop(self):
        if self.stack1:
            self.stack2=self.stack1[::-1]
            self.stack1=[]
        self.stack2.pop()
        

        
    def put(self, value):
        if self.stack2:
            self.stack1=self.stack2[::-1]
            self.stack2=[]
        self.stack1.append(value)
        
        

queue = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])        
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())

# 10
# 1 42
# 2
# 1 14
# 3
# 1 28
# 3
# 1 60
# 1 78
# 2
# 2