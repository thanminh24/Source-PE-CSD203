import math
from Student import *
from Node import *

class MyList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def isEmpty(self):
        return self.head == None
    
    def traverse(self):
        pt = self.head
        while pt:
            print(pt.data, end=" ")
            pt = pt.next
        print("")
    
    def clear(self):
        self.head = None
    
    # Q1-1
    def addFirst(self, name="", age=-1):
        if name.startswith("X") or age < 10:
            return
        else:
            new_node = Node(Student(name, age))
            new_node.next = self.head
            self.head = new_node
            if not self.tail:
                self.tail = new_node
                
    '''def addLast(self, name="", age=-1):
        if xName.startswith('B') or xAge < 17:
            return
        new_node = Node(Person(xName, xAge))
        if not self.head:
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node'''
    
    # Q1-2    
    def addNode(self, name="", age=-1):
        new_node = Node(Student(name, age))
        pt = self.head
        while pt:
            #if int(math.sqrt(pt.data.Age))**2 == pt.data.Age: #So chinh phuong
            if pt.data.Age % 2 == 0: #So chan
            #if pt.data.Age % 2 == 0 #So le
                new_node.next = pt.next
                pt.next = new_node
                if not new_node.next:
                    self.tail = new_node
                break
            pt = pt.next
    #Chèn vào sau số chẵn đầu tiên

    '''def addNode(self, name="", age=-1):
        new_node = Node(Student(name, age))
        even = None
        pt = self.head
        while pt:
            if pt.data.Age % 2 == 0: #Chẵn
                even = pt
            pt = pt.next
        if not even:
            self.addFirst(name, age)
        else:
            new_node.next = even.next
            even.next = new_node
            if even == self.tail:
                self.tail = new_node'''
      

    #Chèn vào sau số chẵn cuối cùng
    '''def addNode(self, name="", age=-1):
        new_node = Node(Student(name, age))
        even = None
        pt = self.head
        while pt:
            if pt.data.Age % 2 == 0:
                even = pt
            pt = pt.next
        if not even:
            self.addFirst(name, age)
        else:
            new_node.next = even.next
            even.next = new_node
            if even == self.tail:
                self.tail = new_node'''
    
#Chèn vào sau 1 số
    '''def addNode(self, name="", age=-1):
        new_node = Node(Student(name, age))
        
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            count = 0
            pt = self.head
            while pt:
                if pt.data.Age % 2 == 1: #Lẻ
                    count += 1
                if count == 2:                                 # Sau số đầu tiên count =1 , thứ 2 thì count = 2
                    new_node.next = pt.next
                    pt.next = new_node
                    break
                pt = pt.next
                
            if not pt.next:
                self.tail.next = new_node
                self.tail = new_node'''
                 


 

# end def
    # Q1-3
    '''def delete(self):
        if self.isEmpty() or self.head.next is None:
            return
        prev = None
        curr = self.head

        while curr:
            #if curr.data.Age in [x*x for x in range(1, int(math.sqrt(curr.data.Age))+1)]: #Điều kiện số chính phương
            if curr.data.Age in [x*x for x in range(1, int(math.sqrt(curr.data.Age))+1) if x*x % 2 == 0]: #Điểu kiện số chẵn
                if not prev:
                    self.head = curr.next
                else:
                    prev.next = curr.next
                if not curr.next:
                    self.tail = prev
                return         #Nếu đề bắt xóa hết các giá trị thì thêm # trc retur
            prev = curr
            curr = curr.next'''

             

            
    # Q1-4def sort(self):

    def sort(self):
        if self.isEmpty():
            return
        even_list = MyList()
        pt = self.head
        while pt:
            if pt.data.Age % 2 == 1:
                even_list.addFirst(pt.data.Name, pt.data.Age)
            pt = pt.next
        even_list.bubbleSort()
        pt = self.head
        pt_even = even_list.head
        while pt and pt_even:
            if pt.data.Age % 2 == 1:
                pt.data = pt_even.data
                pt_even = pt_even.next
            pt = pt.next

    def bubbleSort(self):
        if self.isEmpty() or self.head == self.tail:
            return
        end = None
        while end != self.head.next:
            pt = self.head
            while pt.next != end:
                if pt.data.Age < pt.next.data.Age:
                    temp = pt.data
                    pt.data = pt.next.data
                    pt.next.data = temp
                pt = pt.next
            end = pt