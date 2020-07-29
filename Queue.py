'''

<----------------------------------------------------------------------------- Stacks in Python ----------------------------------------------------------------------------->
0) Terminologies : 

    a. Node − Each Node of a Stack can store a data called an element.

    b. Next − Each link of a stack contains a link to the next link called Next.

    c. Queue − A Queue operates on First In First Out Principal (FIFO).
    
1) Basics : 

    a. Queue has two pointers i. Head ii. Tail.
    
    b. Each link carries a data field(s) and a link field called next.

    c. Each link is linked with its next link using its next link.

    d. Last link carries a link as null to mark the end of the list.

2) Functions : 

    a. enqueue - insert a element at the tail of the queue.
    
    b. dequeue - Remove an element in front of the queue(head).

    c. first - returns the element at the first of the queue.
    
    d. isEmpty - return whether the Queue is empty or not
    
    e. printQueue - Prints the queue.

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
    
    
    def enqueue(self,data):
        newNode = Node(data)
        if(self.tail == None):
            self.head = newNode
            self.tail = self.head
        else:
            self.tail.next = newNode 
            self.tail.next.prev = self.tail 
            self.tail = self.tail.next
    
    def dequeue(self):
        if(self.head == None):
            print('No item in queue to dequeue!')
            return
        dequeued = self.head.data
        print('Dequeued item in the list : ',dequeued)
        self.head = self.head.next
    
    
    def first(self):
        return self.head.data
        
    def isEmpty(self):
        return self.head == None
        
    def printQueue(self):
        currentNode = self.head
        while(currentNode != None):
            print(currentNode.data,end = ' ')
            currentNode = currentNode.next
        
        
if __name__ == '__main__':
    queue = Queue()
    queue.enqueue(110)
    queue.enqueue(120)
    queue.enqueue(130)
    queue.enqueue(140)
    queue.dequeue()
    queue.printQueue()
    print('\nFirst Item : ',queue.first())
    print('If the Queue is empty? : ',queue.isEmpty())
