#BST-INSERT
class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key

def insert(root,key):
    if root is None:
        return Node(key)
    else:
        if root.val==key:
            return root
        elif root.val<key:
            root.right=insert(root.right,key)
        else:
            root.left=insert(root.left,key)
    return root

#inorder traversal
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

'''      50
       /    \
      30    70
     /  \  /  \
    20  40 60 80  '''
x=Node(50)
x=insert(x,30)
x=insert(x,20)
x=insert(x,40)
x=insert(x,70)
x=insert(x,60)
x=insert(x,80)
inorder(x)


