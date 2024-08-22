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
        if name.startswith("B") or price >100:
            return
        n = Node(Car(name,price))
        if (self.isEmpty()):
            self.head = self.tail = n
        else:
            self.tail.next = n
            self.tail = n                


        pass
    # end def
#Q1-2
    #There is a given objects x. You should write statements so that x will be the first element of the list.
    def addFirst(self, X):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
#         new_node = Node(X)
#         if self.isEmpty():
#             self.head = self.tail = new_node   ''' add first'''   
#         else: 
#             new_node.next = self.head
#             self.head = new_node        
#         pass
    
    
 #################################################################   
'''  
   def addLast(self,X)
        n = Node(X)
        if (self.isEmpty()):
            self.head = self.tail = n    #add last
        else:
            self.tail.next = n
            self.tail = n
'''
#######################################################################            
    def f2_1(self, x):  #
        if self.isEmpty():
            return

        # Find the node with the maximum price
        max_node = self.head
        curr = self.head
        while curr:
            if curr.data.Price > max_node.data.Price or curr.data.Price == max_node.data.Price: # FOR LAST MAX
                max_node = curr
            curr = curr.next

        # Insert before the last element with the maximum price
        new_node = Node(x)
        if self.head == max_node:
            new_node.next = self.head
            self.head = new_node
        else:
            curr = self.head
            while curr and curr.next != max_node:
                curr = curr.next
            new_node.next = max_node
            curr.next = new_node
            
#############################################################
        def f2_1(self, x):
        if self.isEmpty():
            return

        # Find the node with the min price
        max_node = self.head
        curr = self.head
        while curr:
            if curr.data.Price < max_node.data.Price or curr.data.Price == max_node.data.Price: # FOR LAST MIN
                max_node = curr
            curr = curr.next

        # Insert before the last element with the mininum price
        new_node = Node(x)
        if self.head == max_node:
            new_node.next = self.head
            self.head = new_node
        else:
            curr = self.head
            while curr and curr.next != max_node:
                curr = curr.next
            new_node.next = max_node
            curr.next = new_node




        pass
    # end def
#Q1-3
    def delete(self, price =0):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        if self.head is None: #def f3(self) – Suppose the list contains at least 3 elements. Delete the first node having price=5. 
            return
        if self.check(self.head.data.Price):
            self.head = self.head.next
            return
        current = self.head
        prev = None
        while current is not None:
            if self.check(current.data.Price):
                prev.next = current.next
                return
            prev = current
            current = current.next
    def check(self,x):
        if x == 5 : return True
        pass 
    #end def
    
####################################################################    
    def delete_first_prime(self): #Suppose the list contains at least 3 elements. Delete the first (last) node having price is a prime number (statify abc condition)
        if self.head is None:
            return
        if self.check(self.head.data.Price):
            self.head = self.head.next
            return
        current = self.head
        prev = None
        while current is not None:
            if self.check(current.data.Price):
                prev.next = current.next
                return
            prev = current
            current = current.next
    def check(self, number):
        if number < 2:
            return False
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        return True
    
        pass
    
 ########################################   
    def delete_last_prime(self):
        if self.head is None:
        return
        curr = self.head
        prev = None
        last_node = None
        while curr.next:
            if self.check(curr.next.data.Price):#sửa điều kiện theo yêu cầu đề bài
                prev = curr
                last_node = curr.next
            curr = curr.next
        if last_node is not None:
            prev.next = last_node.next
            last_node.next = None
    def check(self, number):
        if number < 2:
            return False
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        return True
    
    
  #############################################################  
        def is_prime(self, num):    #Suppose the list contains at least 3 elements. Delete all node having price is a prime number (statify abc condition)
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def f3_2(self):
        # Check if the list contains at least 3 elements
        if self.head is None or self.head.next is None or self.head.next.next is None:
            print("The list must contain at least 3 elements.")
            return
        
        # If the head node contains a prime price
        while self.head and self.is_prime(self.head.data.Price):
            self.head = self.head.next
        
        # Traverse the list and delete nodes with a prime price
        curr = self.head
        while curr and curr.next:
            if self.is_prime(curr.next.data.Price):
                curr.next = curr.next.next
            else:
                curr = curr.next
###########################################################################
# Q1-4
    def sort(self):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========



        
         pass
    #end def    