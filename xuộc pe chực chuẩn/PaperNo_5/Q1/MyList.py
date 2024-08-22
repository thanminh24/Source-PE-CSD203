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
        if name[0] == "Z" or age < 15 or salary <= 0: 
            return
        new_node = Node(Employee(name, age,salary))
        if self.isEmpty():
            self.head = self.tail = new_node
        else: 
            new_node.next = self.head
            self.head = new_node        
      
    # end def
#Q1-2          
    def f2(self, A):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART 2 ========
        if self.isEmpty() : return 
        new_node = Node(A)
        if not self.head or self.head.data.Age % 2 == 0: # sửa điều kiện theo yêu cầu đề bài
            new_node.next = self.head
            self.head = new_node
        else:
            curr = self.head
            prev = None
            while curr:
                if curr.data.Age % 2 == 0: # sửa điều kiện theo yêu cầu đề bài
                    if prev is None:
                        new_node.next = curr
                    else:
                        prev.next = new_node
                        new_node.next = curr
                    break
                prev = curr
                curr = curr.next
           
    # end def
#Q1-3
    def f3(self):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART 3 ========
        if self.head is None:
            return
        # Check if the first node's age is a square number
        if self.check(self.head.data.Age):
            self.head = self.head.next
            return
        current = self.head
        prev = None
        while current is not None:
            if self.check(current.data.Age):#sửa điều kiện theo yêu cầu đề bài
                prev.next = current.next
                return
            prev = current
            current = current.next       
        
    def check(self,x):
        if x % 2 == 0 : return True
         
    #end def
# Q1-4
    def f4(self):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART 4 ========
        totalNode = self.count()

        # Step 1: Extract employees with even ages
        lst2 = []
        cur = self.head
        for i in range(totalNode):
            if cur.data.Age % 2 == 0:  # Check if age is even
                lst2.append((cur.data.Name, cur.data.Age, cur.data.Salary))
            cur = cur.next

        # Step 2: Sort the list by Age (ascending) and Salary (descending if age is the same)
        def custom_sort(item):
            return (item[1], -item[2])  # Sort by Age ascending, Salary descending

        lst2.sort(key=custom_sort)

        # Step 3: Insert sorted data back into the nodes that have even ages
        cur = self.head
        j = 0
        for i in range(totalNode):
            if cur.data.Age % 2 == 0:  # Only replace values for even ages
                cur.data.Name = lst2[j][0]
                cur.data.Age = lst2[j][1]
                cur.data.Salary = lst2[j][2]
                j += 1
            cur = cur.next

    
    def count(self):
        cur = self.head
        count = 0
        while cur:
            count += 1
            cur = cur.next
            
        return count
        
    #end def
    