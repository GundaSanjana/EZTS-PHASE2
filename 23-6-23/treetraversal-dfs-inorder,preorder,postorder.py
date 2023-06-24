#TREE TRAVERSAL-DEPTH FIRST TRAVERSAL
#INORDER,PREORDER,POSTORDER
#USING RECURSION
class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key

def printinorder(root):
    if root:
        #first recur on left child
        printinorder(root.left)
        #then print the data of the node
        print(root.val,end=" "),
        #now recur on right child
        printinorder(root.right)

def printpostorder(root):
    if root:
        #first recur on left child
        printpostorder(root.left)
        #now recur on right child
        printpostorder(root.right)
        #then print the data of the node
        print(root.val,end=" "),

def printpreorder(root):
    if root:
        #print the data of the node
        print(root.val,end=" "),
        #now recur on left child
        printpreorder(root.left)
        #now recur on right child
        printpreorder(root.right)
        
root=Node(100)
root.left=Node(400)
root.right=Node(500)
root.left.left=Node(700)
root.left.right=Node(600)
root.left.right.left=Node(900)
root.right.left=Node(800)
root.right.right=Node(200)
root.right.right.left=Node(300)
print("PRE-ORDER:")
printpreorder(root)
print()
print("IN-ORDER:")
printinorder(root)
print()
print("POST-ORDER:")
printpostorder(root)


