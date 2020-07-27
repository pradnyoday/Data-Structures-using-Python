'''

<----------------------------------------------------------------------------- Linked Lists in Python ----------------------------------------------------------------------------->
0) Terminologies : 

    a. Link − Each link of a linked list can store a data called an element.

    b. Next − Each link of a linked list contains a link to the next link called Next.

    c. LinkedList − A Linked List contains the connection link to the first link called First.
    
1) Basics : 

    a. Linked List contains a link element called first.

    b. Each link carries a data field(s) and a link field called next.

    c. Each link is linked with its next link using its next link.

    d. Last link carries a link as null to mark the end of the list.

2) Functions : 

    a. insertElementAtBeginning − Inserts an element at the beginning of the list.
    
    b. insertElementAtEnd - Inserts an element at the end of the list.

    c. insertElementAfter - Inserts an element after the given element.
    
    d. deleteAtBeginning − Deletes an element at the beginning of the list.
    
    e. deleteAtEnd - Deletes an element at the End of the list.

    f. delete - Deletes an element by key.

    g. printLinkedList − Prints out the complete list.

    h. Search − Searches an element using the given key and prints its position.

'''

#Creation of Node
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
#Creation of the Linked List
class LinkedList:
    def __init__(self):
        self.head = None
    
    #a. Inserting an element at the Beginning
    def insertElementAtBeginning(self,data):
        if(self.head == None):
            self.head = Node(data)
            self.head.next = None
        else:
            currentNode = Node(data)
            currentNode.next = self.head
            self.head = currentNode
    
    #b. Inserting an element at the End
    def insertElementAtEnd(self,data):
        currentNode = self.head
        while(currentNode.next != None):
            currentNode = currentNode.next
        newNode = Node(data)
        currentNode.next = newNode
        
    
    #c. Inserting an element at the After a certain Node
    def insertElementAfter(self,prev,data):
        currentNode = self.head
        while(currentNode.data != prev):
            if(currentNode.next == None):
                print('Please enter a valid key!')
                return
            currentNode = currentNode.next
            
        newNode = Node(data)
        newNode.next = currentNode.next
        currentNode.next = newNode
        
    
    
    #d. Delete Node at Beginning in the Linked List
    def deleteAtBeginning(self):
        currentNode = self.head.next
        self.head = currentNode
        
    
    #e. Delete Node at End in the Linked List
    def deleteAtEnd(self):
        currentNode = self.head
        while(currentNode.next.next != None):
            currentNode = currentNode.next
        currentNode.next = None
        
    #f. Delete Node by key in the Linked List
    def delete(self,data):
        currentNode = self.head
        
        #if element is the first key
        if(currentNode.data == data):
            self.head = currentNode.next
            return
        
        #if element is the key in middle
        while(currentNode.next.data != data):
            currentNode = currentNode.next
            if(currentNode.next == None):
                print('Element not Found!')
                return
        currentNode.next = currentNode.next.next
        
        
        
        
        
    #g. prints Linked List from start to end and also keeps track of number of nodes in the Linked List
    def printLinkedList(self):
        value = self.head
        count = 0
        print('\nLinked List : ')
        while value is not None:
            count += 1
            print (value.data,end=" ")
            value = value.next
        print('\n\nCount : ',count)
        
        
    #h. Search an element and print its position
    def search(self,data):
        currentNode = self.head
        position = 0
        while(currentNode.data != data):
            if(currentNode.next == None):
                print('Element not Found!')
                return
            position += 1
            currentNode = currentNode.next
        print('Key : ',currentNode.data)
        print('Position : ',position)
            
    
if __name__ == '__main__':
    ll = LinkedList()
    ll.insertElementAtBeginning(10)
    ll.insertElementAtBeginning(20)
    ll.insertElementAtEnd(110)
    ll.insertElementAtEnd(120)
    ll.insertElementAtEnd(130)
    ll.insertElementAtEnd(140)
    ll.insertElementAtEnd(150)
    ll.insertElementAfter(110,180)
    ll.deleteAtBeginning()
    ll.deleteAtEnd()
    ll.search(110)
    ll.printLinkedList()