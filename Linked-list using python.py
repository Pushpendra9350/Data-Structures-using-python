#node class to make new nodes
class node:
    def __init__(self,key):
        self.data=key
        self.next=None
        
# function to print your list
def prnt(head):
    temp=head
    while temp:
        print(temp.data,end=" ")
        temp=temp.next

# function to insert an element at starting position
def insert_at_start(head,key):
    temp=head
    new_node=node(key)
    new_node.next=temp
    head=new_node
    return head

# function to insert an element at ending position
def insert_at_last(head,key):
    temp=head
    new_node=node(key)
    while temp.next:
        temp=temp.next
    temp.next=new_node
    return head

# function to insert an element at a given position
def insert_at_position(head,pos,key):
    if pos==1:
        head=insert_at_start(head,key)
        return head
    temp=head
    prev=head
    new_node=node(key)
    count=0
    while count<pos-1:
        count+=1
        prev=temp
        temp=temp.next
    prev.next=new_node
    new_node.next=temp
    return head

# function to search an element is present or not in the list
def search(head,key):
    temp=head
    count=1
    while temp:
        if temp.data==key:
            print(f"{key} is present at {count} position")
            return
        temp=temp.next
        count+=1
    print(f"{key} is not present in this list")

# function to delete a key from starting of the list
def delete_at_start(head):
    temp=head
    head=temp.next
    return head

# function to delete a key from the last of the list
def delete_at_last(head):
    temp=head
    prev=head
    while temp.next:
        prev=temp
        temp=temp.next
    prev.next=None
    return head

# function to delete a key at a given place
def delete_at_position(head,place):
    temp = head
    prev = head
    if place==1:
        head=delete_at_start(head)
        return head
    count=0
    while count<place-1:
        prev=temp
        temp=temp.next
        count+=1
    prev.next=temp.next
    return head

# function to make reverse a list
def reverse(head):
    curr=head
    prev=head
    prev=None
    Next=head
    while Next:
        Next=curr.next
        curr.next=prev
        prev=curr
        curr=Next
    head=prev
    return head

# this is a first node on the linked list
head=node(10)
l=[20,30,40,50,60,70,80,90,100]
for i in l:
    head=insert_at_last(head,i)
print("Our final list is:=>")
prnt(head)
print("\n")
print("Insert an element at start :=>")
head=insert_at_start(head,25)
prnt(head)
print("\n")
print("Delete an element at start :=>")
head=delete_at_start(head)
prnt(head)
print("\n")
print("Insert an element at a given position :=>")
head=insert_at_position(head,5,25)
prnt(head)
print("\n")
print("Deletion an element at given position :=>")
head=delete_at_position(head,5)
prnt(head)
print("\n")
print("Reverse your linked list :=>")
head=reverse(head)
prnt(head)
print("\n")
print("Search an element in your list :=>")
search(head,40)
prnt(head)

OUTPUT:
# Our final list is:=>
# 10 20 30 40 50 60 70 80 90 100 

# Insert an element at start :=>
# 25 10 20 30 40 50 60 70 80 90 100 

# Delete an element at start :=>
# 10 20 30 40 50 60 70 80 90 100 

# Insert an element at a given position :=>
# 10 20 30 40 25 50 60 70 80 90 100 

# Deletion an element at given position :=>
# 10 20 30 40 50 60 70 80 90 100 

# Reverse your linked list :=>
# 100 90 80 70 60 50 40 30 20 10 

# Search an element in your list :=>
# 40 is present at 7 position
# 100 90 80 70 60 50 40 30 20 10 
