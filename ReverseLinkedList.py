
class Node:
    def __init__(self, data):
        self.data=data
        self.nextPtr=None

class LinkedList:
    def __init__(self):
        self.head=None
    
    def InsertAtBegining(self,data):
        newnode=Node(data)
        
        if self.head is None:
            self.head=newnode
            return
        newnode.nextPtr=self.head
        self.head=newnode
    
    def reverseLinkedList(self):
        curr=self.head
        prev=None
        next=None
        while curr:
            next=curr.nextPtr
            curr.nextPtr=prev
            prev=curr
            curr=next
        self.head=prev

    def printLinkedList(self):
        temp=self.head
        while temp:
            print(str(temp.data)+" ", end=" ")
            temp=temp.nextPtr
#Driver Code
llist=LinkedList()
llist.InsertAtBegining(50)
llist.InsertAtBegining(40)
llist.InsertAtBegining(30)
llist.InsertAtBegining(20)
llist.InsertAtBegining(10)
print("Before reverse: ", end=" ")
llist.printLinkedList()
print()
llist.reverseLinkedList()
print("After reverse: ", end=" ")
llist.printLinkedList()
