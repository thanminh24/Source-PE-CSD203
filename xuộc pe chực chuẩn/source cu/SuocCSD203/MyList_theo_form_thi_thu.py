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
        if name[0] == 'B' or price > 100:
       #if name.startswith("B") or price > 100:
       #if name.endswith("B") or price > 100:
            return
        new_node = Node(Car(name, price))
        if not self.head:
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node              


        
    # end def
#Q1-2    
    def addFirst(self, name="", price=-1):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        new_node = Node(Car(name, price))
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
#1.
    '''def insertAfter(self, node_data, xName, xAge):
        if not self.head:
            return
        node = self.head
        while node:
            if node.data.name == node_data:
                new_node = Node(Person(xName, xAge))
                new_node.next = node.next
                node.next = new_node
                if node == self.tail:
                    self.tail = new_node
                return
            node = node.next'''
        



        
    # end def
#Q1-3
    '''def delete(self, price =0):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        if not self.head:
            return
        if self.head.data.Price == 5:
            self.head = self.head.next
            if not self.head:
                self.tail = None
            return
        curr_node = self.head
        while curr_node.next:
            if curr_node.next.data.Price == 5:
                curr_node.next = curr_node.next.next
                if not curr_node.next:
                    self.tail = curr_node
                return
            curr_node = curr_node.next'''        
    def delete(self, price=0):
        if self.isEmpty():
            return

        if self.head.data.Price == 6:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return

        current = self.head
        while current.next is not None and current.next.data.Price != 6:
            current = current.next

        if current.next is not None:
            current.next = current.next.next
        else:
            self.tail = current
        return

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
            
    #end def
# Q1-4
    def sort(self):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        if self.head is None:
            return
        swapped = True
        while swapped:
            swapped = False
            current = self.head
            while current.next is not None:
                if current.data.Price > current.next.data.Price :
                    current.data, current.next.data = current.next.data, current.data
                    swapped = True
                current = current.next

        pass
        
    #end def    