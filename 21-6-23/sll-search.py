#creaing node
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class sll:
    def __init__(self):
        self.head=None
    def dispaly(self):
        if self.head is None:
            print("linked list is empty")
        else:
            temp=self.head#temp assigned to first node
            while temp:
                print(temp.data,end=" ")
                if temp.next!=None:
                    print("->",end=" ")
                temp=temp.next
    def search(self,num):
        temp=self.head
        flag=0
        while temp:
            if temp.data==num:
                flag=1
                break
            temp=temp.next
        if flag==1:
            print("element found")
        else:
            print("element not found")
obj=sll()
#node creation-initializing
n=node(10)
obj.head=n
n1=node(20)
obj.head.next=n1
n2=node(30)
n1.next=n2
n3=node(40)
n2.next=n3
n4=node(50)
n3.next=n4
n5=node(60)
n4.next=n5
obj.dispaly()
s=int(input("\nenter data to search:"))
obj.search(s)
