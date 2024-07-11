
class Node:
    def __init__(self,data):
        self.data=data
        self.nextPtr=None
class LinkedList:
    def __init__(self):
        self.head=None

    def insertAtEnd(self,data):
        newNode=Node(data)

        if self.head is None:
            self.head=newNode
            return
        temp=self.head

        while temp.nextPtr:
            temp=temp.nextPtr
        
        temp.nextPtr=newNode

    def checkLoop(self):
        hier=self.head
        tortoise=self.head

        while hier and tortoise and hier.nextPtr:
            hier=hier.nextPtr.nextPtr
            tortoise=tortoise.nextPtr

            if hier==tortoise:
                return True
        return False
    
    def printLinkedList(self):
        temp=self.head
        while temp:
            print(str(temp.data)+" ", end=" ")
            temp=temp.nextPtr
#Driver Code

llist=LinkedList()
llist.insertAtEnd(10)
llist.insertAtEnd(20)
llist.insertAtEnd(30)
llist.insertAtEnd(40)
llist.insertAtEnd(50)
llist.head.nextPtr.nextPtr=llist.head

if llist.checkLoop():
    print("Loop is inside the Linked List")
else:
    print("No Loop")