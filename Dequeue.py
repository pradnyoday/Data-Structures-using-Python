'''

Dequeue

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
        
