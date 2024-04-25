class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.next=None
class Queue:
    def __init__(self) -> None:
        self.front=None
        self.rear=None
    def enqueue(self,data):
        new_node=Node(data)
        if self.rear == None:
            self.front=new_node
            self.rear=self.front
        else:
            self.rear.next=new_node
            self.rear=new_node
    def dequeue(self):
        print()
        if self.front == None:
            print("empty")
            return
        else:
            self.front=self.front.next 
    def is_empty(self):
        return self.front == None
    def size(self):
        print()
        temp=self.front
        count=0
        while temp is not None:
            count+=1
            temp=temp.next
        print(count)    

    def front_item(self):
        print()
        if self.front == None:
            print("empty")
            return
        else:
            print(self.front.data)       
    def rear_item(self):
        print()
        if self.rear == None:
            print("empty")
            return
        else:
            print(self.rear.data)              
    def traverse(self):
        temp=self.front
        while temp is not None:
            print(temp.data, end= " ")
            temp=temp.next 
   
                 

q=Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.traverse()
q.dequeue()
q.traverse()
q.size()
q.front_item()
q.rear_item()