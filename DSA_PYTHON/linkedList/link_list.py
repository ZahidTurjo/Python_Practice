# creating a node
class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.next=None

# creating a linked list
class LinkedList:
    def __init__(self):
        self.head=None
    def traversal(self):
        if self.head is None:
            print('Linked list is empty')
        else:
            a =self.head
            while a is not None:
                print(a.data ,end=" ")
                a=a.next    
    
    def insert_at_beginning(self,data):
        print()
        nb=Node(data)
        nb.next=self.head
        self.head=nb
    def insert_at_end(self,data):
        print()
        ne=Node(data)
        a=self.head
        while a.next is not None:
            a=a.next
        a.next=ne        
    def insert_at_specified_node(self,position,data):
        print()
        nib=Node(data)
        a=self.head
        for i in range(1,position-1):
            a=a.next
        nib.next=a.next
        a.next=nib   

    def delete_at_beginning(self):
        print()
        a=self.head
        self.head=a.next
        a.next=None
    def deletion_at_end(self):
        print()
        prev=self.head
        a=self.head.next
        while a.next is not None:
            a=a.next
            prev=prev.next
        prev.next=None   
    def deletion_at_specified_node(self,position):
        print()
        prev=self.head
        a=self.head.next
        for i in range(1,position-1):
            a=a.next
            prev=prev.next
        prev.next=a.next
        a.next=None


n1=Node(5)
sll=LinkedList() 
sll.head=n1 
n2=Node(10)
n1.next=n2
n3=Node(15)
n2.next=n3
n4=Node(20)
n3.next=n4

sll.traversal()
# sll.insert_at_beginning(89)
# sll.traversal()
sll.insert_at_end(90)
sll.traversal()
sll.insert_at_specified_node(2,100)
sll.traversal()

sll.deletion_at_specified_node(3)
sll.traversal()
                