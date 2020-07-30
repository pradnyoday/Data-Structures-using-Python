'''
Reverse a Linked List

'''


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self,data):
        newNode = Node(data)
        if(self.head == None):
            self.head = newNode
        else:
            currentNode = self.head
            while(currentNode.next != None):
                currentNode = currentNode.next
            currentNode.next = newNode
            
    def printLinkedList(self):
        currentNode = self.head
        while(currentNode != None):
            print(currentNode.data,end = ' ')
            currentNode = currentNode.next
            
    def reverse(self):
        currentNode = self.head
        prev = None
        while(currentNode != None): 
            temp = currentNode.next
            currentNode.next = prev 
            prev = currentNode
            currentNode = temp
        self.head = prev

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert(110)
    ll.insert(120)
    ll.insert(130)
    ll.insert(140)
    ll.insert(150)
    print('Linked List : ',end = '')
    ll.printLinkedList()
    ll.reverse()
    print('\nReversed Linked List : ',end = ' ')
    ll.printLinkedList()
    
