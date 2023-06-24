class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def inorder(root):
    #Set current to root of binary tree
    current=root
    stack=[] #initializing stack
    done=0
    while True:
        #Reach the left most node of the current node
        if current is not None:
    #Place pointer to a tree node on the stack
    #before traversing the nodes left subtree
            stack.append(current)
            current=current.left
#Backtrack tree empty subtree & visit node
#at the top of the stack
#however if the stack is empty you are done
        elif(stack):
            current=stack.pop()
            print(current.data,end=" ")

            #we have visited the node and the left
            #subtree. Now its right subtrees turn
            current=current.right
        else:
            break
    print()
#INPUT
"""
       1
      / \
     2   3
    / \    
   4   5
             """
root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
inorder(root)
