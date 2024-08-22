import math
from Employee import *
from Node import *
class MyList:
    def __init__(self):
        self.head = None
        self.tail = None
    def isEmpty(self):
        return self.head ==None
    def traverse(self):
        pt = self.head
        while pt.next:
            print(pt.data, end = " ")
            pt = pt.next
        print(pt.data)        
    def clear(self):
        self.head = None    
#Q1-1
    def f1(self, name="", age="", salary=-1):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART 1 ========
        if name[0] == "X" or age < 15 or salary > 200: #sửa điều kiện theo yêu cầu đề bài
            return
        new_node = Node(Employee(name, age,salary))
        if self.isEmpty():
            self.head = self.tail = new_node
        else: 
            new_node.next = self.head
            self.head = new_node            
        pass        
    # end def
#Q1-2          
    def f2(self, A):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART 2 ========
        
        
        pass        
    # end def
#Q1-3
    def f3(self):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART 3 ========
        
        
        pass 
    #end def
# Q1-4
    def f4(self):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART 4 ========
        
        
        pass
    #end def
    