#STACK IMPLEMENTATION USING ARRAYS LIFO (LAST IN FIRST OUT)
stack=[]
def push():
    element=int(input("Enter the element:"))
    stack.append(element)
    print(stack)

def pop_element():
    if not stack:
        print("stack is empty")
    else:
        e=stack.pop()
        print("Removed element:",e)
        print(stack)

def peek():
     if not stack:
        print("stack is empty")
     else:
        e=stack.pop()
        print("Peek is:",e)

def display():
    print(stack)

while True:
    print("Select operation 1.push 2.pop 3.peek 4.display 5.quit")
    choice=int(input())
    if choice==1:
        push()
    elif choice==2:
        pop_element()
    elif choice==3:
        peek()
    elif choice==4:
        display()
    elif choice==5:
        break
    else:
        print("Enter the valid operation")

    
