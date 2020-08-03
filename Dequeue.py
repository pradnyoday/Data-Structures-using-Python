'''

<----------------------------------------------------------------------------- DeQueues in Python ----------------------------------------------------------------------------->
0) Terminologies : 

    a. Node − Each Node of a Queue can store a data called an element.

    b. Next − Each link of a Queue contains a link to the next link called Next.

    c. Queue − A Queue operates on First In First Out Principal (FIFO).
    
1) Basics : 

    a. Queue has two pointers i. Head ii. Tail.
    
    b. Each link carries a data field(s) and a link field called next.

    c. Each link is linked with its next link using its next link.

    d. Last link carries a link as null to mark the end of the list.

2) Functions : 

    a. enqueueAtFront - insert a element at the head of the queue.
    
    b. enqueueAtEnd - insert a element at the tail of the queue.
    
    c. dequeueAtFront - Remove an element in front of the queue(head).

    d. dequeueAtEnd - Remove an element in end of the queue(tail).
    
    e. isEmpty - return whether the Queue is empty or not
    
    f. printQueue - Prints the queue.

'''
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
        
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def enqueueAtFront(self,data):
        newNode = Node(data)
        if(self.head == None):
            self.tail = self.head = newNode
            return
        
        newNode.next = self.head
        self.head.prev = newNode
        self.head = newNode
    
    def enqueueAtEnd(self,data):
        newNode = Node(data)
        if(self.tail == None):
            self.tail = self.head = newNode
            return
        self.tail.next = newNode
        newNode.prev = self.tail
        self.tail = newNode
        
    def dequeueAtFront(self):
        self.head = self.head.next
        
    def dequeueAtEnd(self):
        self.tail = self.tail.prev
        self.tail.next = None
    
    
    def first(self):
        return self.head.data
        
    def isEmpty(self):
        return self.head == None
        
    
    def printQueue(self):
        currentNode = self.head
        while(currentNode):
            print(currentNode.data,end = ' ')
            currentNode = currentNode.next
        print()

if __name__ == '__main__':
    queue = Queue()
    queue.enqueueAtFront(110)
    queue.enqueueAtFront(120)
    queue.enqueueAtFront(130)
    queue.enqueueAtFront(140)
    queue.enqueueAtFront(150)
    queue.enqueueAtEnd(160)
    queue.enqueueAtEnd(180)
    queue.enqueueAtEnd(170)
    queue.enqueueAtEnd(175)
    queue.enqueueAtEnd(101)
    queue.enqueueAtEnd(102)
    queue.dequeueAtFront()
    queue.dequeueAtEnd()
    
    queue.printQueue()
    print('\nFirst Item : ',queue.first())
    print('If the Queue is empty? : ',queue.isEmpty())
        
