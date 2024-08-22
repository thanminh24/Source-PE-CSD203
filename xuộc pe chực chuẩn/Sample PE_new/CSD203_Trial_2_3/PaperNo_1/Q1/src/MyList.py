from Car import *
from Node import *
class MyList:
    def __init__(self):
        self.head = None
        self.tail = None
    def isEmpty(self):
        return self.head ==None
    def traverse(self):
        pt = self.head
        while pt:
            print(pt.data, end = " ")
            pt = pt.next
        print("")        
    def clear(self):
        self.head = None
#Q1-1
    def addLast(self, name="", price=-1):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        if name[0]=='B' or price >100:
            return 
        new_Node=Node(Car(name,price))
        if self.isEmpty():
            self.head=self.tail=new_Node
        else:
            self.tail.next=new_Node
            self.tail=new_Node


        pass
    # end def
#Q1-2    
    def addFirst(self, name="", price=-1):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        new_Node=Node(Car(name,price))
        if self.isEmpty():
            self.head=self.tail=new_Node
        else:
            new_Node.next=self.head
            self.head=new_Node


        pass
    # end def
#Q1-3
    def delete(self, price =5):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        if self.isEmpty():
            return
        
        current=self.head
        if current.data.Price==price:
            self.head=current.next
            
        while  current.next is not None:
            if current.next.data.Price ==price:
                current.next=current.next.next
                return 
            current=current.next
        
        

    #end def
# Q1-4
    def sort(self):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        if self.isEmpty() or self.head == self.tail:
            return 
        else:
            i=self.head
            while i.next:
                j=i.next
                while j:
                    if i.data.Price>j.data.Price:
                        i.data,j.data=j.data,i.data
                    j=j.next
                i=i.next

    #end def    