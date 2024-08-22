import math
from Customer import *
from Node import *
class MyList:
    def __init__(self):
        self.head = None
        self.tail = None
    def isEmpty(a):
        return a.head ==None
    def traverse(a):
        pt = a.head
        while pt:
            print(pt.data, end = " ")
            pt = pt.next
        print("")        
    def clear(self):
        self.head = None
#Q1-1
    def addLast(a, name="", age=-1):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART 1 ========
        if name[-1] == 'X' or age >90:#sửa điều kiện theo yêu cầu đề bài
            return
        
        n = Node(Customer(name,age))
        if (a.isEmpty()):
            a.head = a.tail = n
        else:
            a.tail.next = n
            a.tail = n
        pass
    # end def
#Q1-2    
    def addNode(self, name="", age=-1):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART 2 ========
        new_node = Node(data=Customer(name, age))

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            current = self.head
            prev = None
            count = 0
            while current:
                if current.data.Age % 2 != 0:
                    count += 1
                    if count == 2:
                        new_node.next = current
                        if prev:
                            prev.next = new_node
                        else:
                            self.head = new_node
                        break
                prev = current
                current = current.next
        pass
    # end def
#Q1-3
    def delete(self):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART 3 ========
        if self.head is None:
            return
        count = 0
        current = self.head
        prev = None
        while current is not None:
            if not self.isPerfectNumber(current.data.Age):#sửa điều kiện theo yêu cầu đề bài
                count += 1
                if count == 3: #count bằng bao nhiêu xoá thứ tự bấy nhiê
                    prev.next = current.next
                    return
            prev = current
            current = current.next

    def isPerfectNumber(self,num):
        if num <= 0:
            return False
        divisors_sum = 0
        for i in range(1, num):
            if num % i == 0:
                divisors_sum += i
        
        return divisors_sum == num
        pass
    #end def
# Q1-4
    def sort(self):
        lst2 = []
        cur = self.head
        while cur:
            if not self.is_fibonacci_number(cur.data.Age):
                lst2.append((cur.data.Name, cur.data.Age))
            cur = cur.next

        # lst2.sort(key=lambda x: x[1] )  # Sorting lst2 in ascending order based on age
        lst2.sort(key=lambda x:(x[1], -ord(x[0][0])) )
        j = 0
        cur = self.head
        while cur:
            if not self.is_fibonacci_number(cur.data.Age):
                cur.data.Name, cur.data.Age = lst2[j]
                j += 1
            cur = cur.next
        pass
    def is_fibonacci_number(self,num):
            if num < 0:
                return False
            a, b = 0, 1
            while b < num:
                a, b = b, a + b
            return b == num
    #end def    