import sys
from collections import deque
sys.setrecursionlimit(100000)
class Node:
    def __init__(self,value):
        self.value=value
        self.leftChild=None
        self.rightChild=None

def Tree(root,indexes):
    queue=deque([root])
    for i,j in indexes:
        temp=queue.popleft()
        if i!=-1:
            temp.leftChild=Node(i)
            queue.append(temp.leftChild)

        if j!=-1:
            temp.rightChild=Node(j)
            queue.append(temp.rightChild)
    return root

def swap(root,k,level,l):
    if root:
        if level%k==0:
            root.leftChild,root.rightChild=root.rightChild,root.leftChild

        swap(root.leftChild,k,level+1,l)
        l.append(root.value)
        swap(root.rightChild,k,level+1,l)


def swapNodes(indexes,queries):
    root=Node(1)
    root=Tree(root,indexes)
    result=[]
    for k in queries:
        l=[]
        swap(root,k,1,l)
        result.append(l)

    return result




# indexes=[[2, 3],
#          [4, -1],
#          [5, -1],
#          [6, -1],
#          [7, 8],
#          [-1, 9],
#          [-1, -1],
#          [10, 11],
#          [-1, -1],
#          [-1, -1],
        #  [-1, -1]]

indexes=[[2,3],
         [-1,4],
         [-1,5],
         [-1,-1],
         [-1,-1]]


queries=[2]

print(swapNodes(indexes,queries))



# output1=[2 9 6 4 1 3 7 5 11 8 10]
# output2=[2 6 9 4 1 3 7 5 10 8 11]




# if __name__=="__main__":
#     n=int(input())
#     indexes=[]
#     for _ in range(n):
#         indexes.append(list(map(int,input().rstrip().split())))


#     queries_count=int(input())
#     queries=[]

#     for _ in range(queries_count):
#         queries_item=int(input())
#         queries.append(queries_item)

#     swapNodes(indexes,queries)



