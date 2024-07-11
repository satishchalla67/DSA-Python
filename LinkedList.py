class Node:
    def __init__(self,data):
        self.data=data
        self.nextPtr=None

class LinkedList:
    def __init__(self):
        self.head=None


    def insertAtBegining(self,data):

        newNode=Node(data)

        if self.head is None:
            self.head=newNode
            return
        newNode.nextPtr=self.head
        self.head=newNode

    def insertAtEnd(self,data):
        newNode=Node(data)
        if self.head is None:
            self.head=newNode
            return
        
        temp=self.head
        while temp.nextPtr:
            temp=temp.nextPtr
        
        temp.nextPtr=newNode
    
    def insertAfterNode(self, prevNode, data):
        if prevNode.nextPtr is None:
            return
        
        newnode=Node(data)
        newnode.nextPtr=prevNode.nextPtr
        prevNode.nextPtr=newnode
    
    def printLinkedList(self):
        temp=self.head
        while temp:
            print(str(temp.data)+" ", end=" ")
            temp=temp.nextPtr
    def getNode(self, count):
        current=self.head

        while count>1:
            current=current.nextPtr
            count-=1
        return current

#Driver Code
llist=LinkedList()

llist.insertAtEnd(10)
llist.insertAtEnd(20)

llist.insertAtBegining(5)
llist.insertAtBegining(3)

llist.insertAfterNode(llist.head.nextPtr, 100)
node=llist.getNode(3)
llist.insertAfterNode(node, 120)

llist.printLinkedList()
    


