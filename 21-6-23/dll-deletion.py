#Doubly Linked List-Deletion
#create node
class Node:
    def __init__(self,data):
        self.data=data
        self.previous=None
        self.next=None

class dll:
    def __init__(self):
        self.head=None

    def delete_beg(self):
        temp=self.head
        self.head=temp.next
        temp.next=None
        temp.prev=None

    def delete_end(self):
        temp=self.head.next
        prev=self.head
        while temp.next is not None:
            temp=temp.next
            prev=prev.next
        prev.next=None
        temp.prev=None
        
    def delete_pos(self,pos):
         temp=self.head.next
         prev=self.head
         for i in range(1,pos-1):
                temp=temp.next
                prev=prev.next
         prev.next=temp.next
         
         temp.next=prev.next
        
    def display(self):
        if self.head is None:
            print("Empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"<-->",end=" ")
                temp=temp.next
                     
l=dll()
n1=Node(100)
l.head=n1
n2=Node(200)
n2.prev=n1
n1.next=n2
n3=Node(300)
n3.prev=n2
n2.next=n3
n4=Node(400)
n4.prev=n3
n3.next=n4
n5=Node(500)
n5.prev=n4
n4.next=n5
l.display()
print()
print("After deletion at beginning")
l.delete_beg()
l.display()
print()
print("After deletion at end")
l.delete_end()
l.display()
print()
print("After deletion in between")
l.delete_pos(2)
l.display()
print()

