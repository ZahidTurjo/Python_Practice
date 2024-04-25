
class Node:
    def __init__(self,value):
        self.data=value
        self.next=None
class Stack:

    def __init__(self):
        self.top=None
    def isempty(self):
        return self.top == None
    def push(self,data):
        new_node=Node(data)
        new_node.next=self.top
        self.top=new_node
    def pop(self):
        
        
        if (self.isempty()):
            print("Stack is empty")
        else:
            data=self.top.data
            self.top=self.top.next   
            return data     
    def peek(self):
        if (self.isempty()):
            print("Stack is Empty") 
        else:
            print(self.top.data )    
    def traverse(self):
        temp=self.top
        while temp is not None:
            print(temp.data, end= " ")
            temp=temp.next

    def undo(self):
        self.push(self.pop())




# undo and redo
def text_editor(text,pattern):
    u=Stack()
    r=Stack()
    for i in text:
        u.push(i)
    
    for i in pattern:
        if i == "u":
            data=u.pop()
            r.push(data)
        else:
            data=r.pop()
            u.push(data)   
    res=""         
    while (not u.isempty()):
        res=u.pop()+res
    print(res)    

text_editor("hello","uurrurruur")








# reverse a string using stack

# def reverse(text):
#     s=Stack()
   
#     for i in text:
#         s.push(i)
#     res= ""    
#     while( not s.isempty()):
#         res=res+s.pop()
#     print(res)    

# reverse("hello")


# n1=Node(5)
# s=Stack()
# s.top=n1
# s.push(10)
# s.push(15)
# s.push(20)

# s.traverse()
# s.pop()
# s.traverse()
