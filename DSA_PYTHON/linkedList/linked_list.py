
class Node:
    def __init__(self,value) -> None:
        self.data=value 
        self.next=None

class LinkedList:
    def __init__(self) -> None:
        # make  a empty linked list
        self.head=None
        # no of nodes in LL
        self.n=0
    def __len__(self):
        return self.n   
    def insert_head(self,value):
        # new node
        new_node=Node(value)
        # create connection
        new_node.next=self.head
        # reassign head
        self.head=new_node 
        # increment n
        self.n=self.n+1
    def __str__(self):
        curr=self.head
        result=""

        while curr != None:
            result = result + str(curr.data) + "->"
            curr=curr.next
        return result[:-2]
    def append(self,value):

        new_node=Node(value)

        if self.head == None:
            # empty
            self.head = new_node
            self.n=self.n+1
            return
        
        curr=self.head

        while curr.next !=None:
            curr=curr.next

        #u are at the last node
        curr.next=new_node       
        self.n=self.n+1

    def insert_after(self,after,value):

        new_node=Node(value)
        curr=self.head

        while curr != None:
            if curr.data == after:
                break
            curr=curr.next    
        # case -1 break -> item found --curr--not none
        if curr != None:
            new_node.next=curr.next
            curr.next=new_node
            self.n=self.n+1

        else:
            return 'Item not found'    
        #case 2 loop pura chala.item did not found -> curr == none 
    def clear(self):
        self.head=None
        self.n=0   
    def delete_head(self):
        if self.head == None:
            return "Empty Linked list"
        self.head=self.head.next
        self.n=self.n-1
    def pop(self):
        if self.head == None:
            return "Empty Linked list "
        
        curr=self.head
        # if linked list have one item 
        if curr.next== None:
            # it will be head.and delete head
            self.delete_head()
            self.n=self.n-1
            return


        while curr.next.next != None:
            curr=curr.next

        # curr--> 2nd last node
        curr.next=None
        self.n=self.n-1    
    def remove(self,value):
        if self.head == None:
            print("Empty linked list")
            return
        if self.head.data == value:
            # you want to remove the head note
            return self.delete_head()
        curr=self.head
        while curr.next != None:
            if curr.next.data == value:
                break
            curr= curr.next
        #case -1 item found 
        #case -2 item did not found
        if curr.next == None:
            print("Item did not found") 
            return
        else:
            curr.next=curr.next.next
        self.n=self.n-1    
    def search(self,item):
        curr=self.head
        pos=0
        
        while curr != None:
            pos+=1
            if curr.data == item:
                print(pos)   
                
            else:
                print("Item not found")
                return 
            curr =curr.next    
    def __getitem__(self,index):
        curr=self.head
        pos=0

        while curr != None:
            if pos == index:
                return curr.data
            curr=curr.next
            pos+=1
        return "Index Error"   
# Write a python program to find the maximum value in a linked list and relpace
# it with a given value . assume that the linked list is populeted  with whole numbers
# and there is only one maximum value in the linked list    
    def replace_max(self,value):
        temp =self.head
        max=temp
        while temp != None:
            if temp.data > max.data:
                max=temp
            temp=temp.next
        max.data= value     

#add sum odd positinal value
    def sum_odd_nodes(self):
        temp=self.head
        counter =0
        result=0
        while temp != None:
            if counter%2 != 0:
                result=result+int(temp.data)
            counter+=1
            temp=temp.next
        print(result)
# write a program to reverse a linked list containing integer data
    def reverse(self):
        prev_node=None
        curr_node=self.head

        while curr_node != None:
            next_node=curr_node.next
            curr_node.next=prev_node
            prev_node=curr_node
            curr_node=next_node
        self.head =prev_node


        

L=LinkedList()
L.insert_head(1)
L.insert_head(2)
L.insert_head(3)
L.insert_head(4)
# print(len(L))

print(L)

L.reverse()
print(L)
