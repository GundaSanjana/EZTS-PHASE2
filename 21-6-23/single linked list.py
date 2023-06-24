#Single Linked List
#creation node-declaration & definition
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class singlelinkedlist:
    def _init_(self):
        self.head=None

    def insert_beginning(self,data):
        nb=Node(data)
        nb.next=self.head
        self.head=nb
        
    def insert_end(self,data):
        ne=Node(data)
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=ne
        ne.next=None
        
    def insert_position(self,pos,data):
        np=Node(data)
        temp=self.head
        for i in range (pos-1):#1 iteration 1 happen
            temp=temp.next

        np.next=temp.next
        temp.next=np

    def delete_beg(self):
        temp=self.head
        self.head=temp.next
        temp.next=None
        
    def delete_end(self):
        temp=self.head.next
        prev=self.head
        while temp.next is not None:
            temp=temp.next
            prev=prev.next
        prev.next=None #last but before node
        
    def delete_position(self,pos):
        temp=self.head.next
        prev=self.head
        #2 iterations
        for i in range(1,pos-1):
            temp=temp.next
            prev=prev.next
        prev.next=temp.next #20  1 point 40
        temp.next=None #30s next will be None:
        
    def display(self):
        if self.head is None:
            print("linked list is empty")
        else:
            temp=self.head #temp = first node
            while temp:
                if temp.next!=None:
                    print(temp.data,end=" -> ")
                else:
                    print(temp.data,end=" ")
            #temp.data means first node's data
                temp=temp.next#establish link
obj=singlelinkedlist()
#node creation - initialising
n=Node(10)#so n,data in node class will be 10
obj.head=n      #displaying first node as head
n1=Node(20)
obj.head.next=n1#next node value
n2=Node(30)
n1.next=n2
n3=Node(40)
n2.next=n3
n4=Node(50)
n3.next=n4
n5=Node(60)
n4.next=n5

#Insertion
print("Before insertion")
obj.display()
print()
print("After insertion at beginning")
obj.insert_beginning(5)
obj.display()
print()
print("After insertion at end")
obj.insert_end(70)
obj.display()
print()
print("After insertion in between")
obj.insert_position(3,1000)
obj.display()
print()

#Deletion
print("After deleting at first")
obj.delete_beg()
obj.display()
print()
print("After deleting at last")
obj.delete_end()
obj.display()
print()
print("After deleting in between")
obj.delete_position(3)
obj.display()
print()
