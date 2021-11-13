'''

<----------------------------------------------------------------------------- Stacks in Python ----------------------------------------------------------------------------->
0) Terminologies : 

    a. Node − Each Node of a Stack can store a data called an element.

    b. Next − Each link of a stack contains a link to the next link called Next.

    c. Stack − A Stack operates on Last In First Out Principal (LIFO).
    
1) Basics : 

    a. Stack has element on the top which is called Stack Top.

    b. Each link carries a data field(s) and a link field called next.

    c. Each link is linked with its next link using its next link.

    d. Last link carries a link as null to mark the end of the list.

2) Functions : 

    a. push - insert a element at the top of stack
    
    b. pop - Remove an element on the top in the stack

    c. Stack Top / Peek - returns the element at the top of the stack
    
    d. isEmpty - return whether the Stack is empty or not
    
    e. printStack - Prints the stack in order of insertion

'''

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
     
    #a. push - insert a element at the top of stack 
    def push(self,data):
        newNode = Node(data)
        if(self.top == None):
            self.top = newNode
        else:
            currentNode = self.top
            while(currentNode.next != None):
                currentNode = currentNode.next
            currentNode.next = newNode
    
    #b. pop - Remove an element on the top in the stack
    def pop(self):
        if(self.top == None):
            print('No elements in Stack to pop!')
            return
        currentNode = self.top
        if(currentNode.next == None):
            print('Popped Element : ',currentNode.data)
            self.top = None
            return
            
        while(currentNode.next.next != None):
            currentNode = currentNode.next
        print('Popped Element : ',currentNode.next.data)
        currentNode.next = None
        
    #c. Stack Top / Peek - returns the element at the top of the stack  
    def stackTop(self):
        if(self.top == None):
            print('No elements in Stack!')
            return
        currentNode = self.top
        while(currentNode.next != None):
            currentNode = currentNode.next
        return currentNode.data
    
    #d. isEmpty - return whether the Stack is empty or not 
    def isEmpty(self):
        return self.top == None
    
    #e. printStack - Prints the stack in order of insertion    
    def printStack(self):
        if(self.top == None):
            print('No elements in Stack!')
            return
        print('Stack Elements : ',end=' ')
        currentNode = self.top
        while(currentNode != None):
            print(currentNode.data,end = ' ')
            currentNode = currentNode.next
        print()
        
        
        
stack = Stack()
stack.push(110)
stack.push(120)
stack.push(130)
stack.push(139)
stack.printStack()
print('Stack Top : ',stack.stackTop())
print('Is stack Empty ? : ',stack.isEmpty())
