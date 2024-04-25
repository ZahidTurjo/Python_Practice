class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class DoublyLL:
    def __init__(self):
        self.head=None
    def traversal_forward(self):
        if self.head == None:
            print('Doubly linked list is empty')
        a=self.head
        while a is not None:
            print(a.data, end=" ")
            a=a.next     
    def traversal_backward(self):
        print()
        a=self.head
        while a.next is not None:
            a=a.next
        while a is not None:
            print(a.data, end=" ")    
            a=a.prev          
    def insert_at_brginnig(self,data):
        print()
        ns=Node(data)
        a=self.head
        a.prev=ns
        ns.next=a
        self.head=ns
    def insert_at_end(self,data):
        print()
        ne=Node(data)
        a=self.head
        while a.next is not None:
            a=a.next
        a.next=ne        
        ne.prev=a
    def insert_at_specified_node(self,data,position):
        print()
        nib=Node(data)
        a=self.head
        for i in range(1,position-1):
            a=a.next    
        nib.next=a.next   
        a.next.prev=nib
        a.next=nib
        nib.prev=a 

    def deletion_at_beginning(self):
        print()
        a=self.head
        self.head=a.next
        self.head.prev=None
        a.next=None
    def deletion_at_end(self):
        print()
        a=self.head.next
        be=self.head
        while a.next is not None:
            be=be.next
            a=a.next
        a.prev=None
        be.next=None 
    def deletion_at_specified_node(self,position):
        print()
        be=self.head
        a=self.head.next
        for i in range(1,position-1):
            be=be.next
            a=a.next
        a.next.prev=be
        be.next=a.next
        a.next=None
        a.prev=None
        

n1= Node(5)
dll=DoublyLL()
dll.head=n1
n2=Node(10)
n2.prev=n1
n1.next=n2
n3=Node(15)
n3.prev=n2
n2.next=n3
n4=Node(20)
n4.prev=n3
n3.next=n4

dll.traversal_forward()
# dll.insert_at_brginnig(0)
dll.insert_at_end(25)

dll.traversal_forward()
dll.deletion_at_specified_node(3)

dll.traversal_forward()
dll.traversal_backward()
