#Get conbination of paranthesis as input and check whether it is
#balanced or not.
stack=[]
s=input()
n=len(s)
flag=1
if s[0]==']' or s[0]=='}' or s[0]==')':
    print(False)
else:
    for i in range(n):
        if s[i]=='[' or s[i]=='(' or s[i]=='{':
            stack.append(s[i])
        elif s[i]==']' or s[i]=='}' or s[i]==')':
            if (stack[-1]=='{' and s[i]=='}') or (stack[-1]=='[' and s[i]==']') or (stack[-1]=='(' and s[i]==')'):
                stack.pop()
            else:
                flag=0
                break
        else:
            flag=-1
            break
    if flag==1:
        print(True)
    elif flag==0:
        print(False)
    else:
        print("Invalid paranthesis")
