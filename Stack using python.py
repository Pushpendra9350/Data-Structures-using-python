# This function is used to push your element into your satck
#    |   |            |   |
#    |   |            |   |
#    |   |    ==>     | 5 |
#    |___|            |___|
def push(key):
    if len(stack)>=size:
        print("Stack is overflow! we can't push your element right now")
        print()
    else:
        stack.append(key)

# This function is used to pop your element from your satck
#    | 3 |            |   |
#    | 4 |            | 4 |
#    | 6 |    ==>     | 6 |
#    |___|            |___|
def pop():
    if len(stack)==0:
        print("Stack is underflow! we can't pop any element right now")
        print()
    else:
        stack.pop(-1)

# this is print function to print your stack
def prnt():
    if len(stack)==0:
        print("Stack is empty! ")
    else:
        print(*stack)
        print()

# to get top element from your element
def top():
    print(stack[-1])
size=int(input("Enter the size of the stack :\t"))
#this is your stack
stack=[]

while 1:
    print("1. Push an element")
    print("2. Pop an element")
    print("3. Print stack")
    print("4. Top element")
    print("5. Exit")
    print()
    choice=int(input("Enter your choice :\t"))
    print()
    if choice==1:
        key=int(input("Enter the element to push :\t"))
        push(key)
    elif choice==2:
        pop()
    elif choice==3:
        prnt()
    elif choice==4:
        top()
    elif choice==5:
        break
    else:
        print("Wrong choice! Please enter a correct option")

OUTPUT:
#Enter the size of the stack :	2

#1. Push an element
#2. Pop an element
#3. Print stack
#4. Top element
#5. Exit

#Enter your choice :	1

#Enter the element to push :	20
#1. Push an element
#2. Pop an element
#3. Print stack
#4. Top element
#5. Exit

#Enter your choice :	1

#Enter the element to push :	10
#1. Push an element
#2. Pop an element
#3. Print stack
#4. Top element
#5. Exit

#Enter your choice :	1

#Enter the element to push :	30

#Stack is overflow! we can't push your element right now

#1. Push an element
#2. Pop an element
#3. Print stack
#4. Top element
#5. Exit

#Enter your choice :	2

#1. Push an element
#2. Pop an element
#3. Print stack
#4. Top element
#5. Exit

#Enter your choice :	3

#20

#1. Push an element
#2. Pop an element
#3. Print stack
#4. Top element
#5. Exit

#Enter your choice :	5
