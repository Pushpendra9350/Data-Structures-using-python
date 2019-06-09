#In order to construct a node of the tree make a class called "node"
# class node have to pointers called left and right for left subtree and right subtree
#and a data variable which contains data of that node

class node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.data=key

# tree traversal preorder
#        a
#       / \     ==>   abc
#      b   c
def preorder(temp):
    if not temp:
        return

    # temp.left points to left subtree
    # temp.right points to right subtree
    # temp.data points to data of the node
    
    print(temp.data,end=" ")
    inorder(temp.left)
    inorder(temp.right)

# tree traversal inorder
#        a
#       / \     ==>   bac
#      b   c
def inorder(temp):
    if not temp:
        return
    inorder(temp.left)
    print(temp.data,end=" ")
    inorder(temp.right)

# tree traversal postorder
#        a
#       / \     ==>   bca
#      b   c
def postorder(temp):
    if not temp:
        return
    inorder(temp.left)
    inorder(temp.right)
    print(temp.data,end=" ")


# Insert a key/element in tree from left to right manner let insert(root,"d") 
#        a                   a
#       / \       ==>       / \
#      b   c               b   c
#                         /
#                        d
def insert(temp,key):
    q=[]
    q.append(temp)
    while len(q):
        temp=q[0]
        q.pop(0)
        if not temp.left:
            temp.left=node(key)
            break
        else:
            q.append(temp.left)
        if not temp.right:
            temp.right=node(key)
            break
        else:
            q.append(temp.right)

# this function is delete the deepest node from the tree
#        a                   a
#       / \        ==>      / 
#      b   c               b
def delete_deepest(root,d_node):
    q=[]
    q.append(root)
    while len(q):
        temp=q.pop(0)
        if temp is d_node:
            temp=None
            retrun
        if temp.right:
            if temp.right is d_node:
                temp.right=None
                return
            else:
                q.append(temp.right)
        if temp.left:
            if temp.left is d_node:
                temp.left=None
                return
            else:
                q.append(temp.left)

# this function is delete a node from the tree "delete_by_key(root,"C")"
#        a                   a
#       / \        ==>      / 
#      b   c               b
def delete_by_key(temp,dkey):
    q=[]
    q.append(temp)
    while len(q):
        temp=q[0]
        q.pop(0)
        if temp.data==dkey:
            dkey_node=temp
        if temp.left:
            q.append(temp.left)
        if temp.right:
            q.append(temp.right)
    x=temp.data
    delete_deepest(root,temp)
    dkey_node.data=x

#search is tells about function is present or not 
def search(temp,key):
    q=[]
    q.append(temp)
    while len(q):
        temp=q.pop(0)
        if temp.data==key:
            return 1
        if temp.left:
            if temp.left.data==key:
                return 1
            else:
                q.append(temp.left)
        if temp.right:
            if temp.right==key:
                return 1
            else:
                q.append(temp.right)
    return 0
                
# Now we create a root node with value=5
root=node(5)

# taking inputs from user to insert into tree
x=int(input("Enter the number of nodes : "))
l=list(map(int,input(f"Please enter {x} Values space seprated e.g='2 3 6 5' : ").split(" ")))
for i in l:
    insert(root,i)
print()
# all three types of traversals
def travers(root):
    print("Preorder : ",end="")
    preorder(root)
    print()
    print("inorder  : ",end="")
    inorder(root)
    print()
    print("Postorder : ",end="")
    postorder(root)
    print()
travers(root)
print()
# take input to delete a key from tree
dkey=int(input("Enter key to delete : "))
delete_by_key(root,dkey)
print()
travers(root)
print()

# to rearceh a key
skey=int(input("Enter key to search : "))
print("Element is present" if search(root,skey) else "Element is not present" )



# OUTPUT
#Enter the number of nodes : 5
#Please enter 5 Values space seprated e.g='2 3 6 5' : 6 8 10 9 7

#Preorder : 5 10 6 9 7 8 
#inorder  : 10 6 9 5 7 8 
#Postorder : 10 6 9 7 8 5 

#Enter key to delete : 9

#Preorder : 5 10 6 7 8 
#inorder  : 10 6 7 5 8 
#Postorder : 10 6 7 8 5 

#Enter key to search : 8
#Element is present
